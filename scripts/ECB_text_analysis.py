   #Step 1: Importing libraries
from collections import Counter
from pathlib import Path
import re

import spacy
from spacytextblob.spacytextblob import SpacyTextBlob
import pandas as pd
import requests
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt
from wordcloud import STOPWORDS, WordCloud



  #Step 2: Initializing NLP pipeline with spaCy and sentiment analysis
nlp = spacy.load("en_core_web_sm")
nlp.add_pipe("spacytextblob")



  # Step 3: Defining URL and creating folders for storing data and outputs
URL = "https://www.ecb.europa.eu/press/govcdec/otherdec/2026/html/ecb.gc260504~07dc9bac72.en.html"

DATA_DIR = Path("data")
OUTPUT_DIR = Path("outputs")

DATA_DIR.mkdir(exist_ok=True)
OUTPUT_DIR.mkdir(exist_ok=True)



# Step 4: Defining helper functions for cleaning, labeling sentiment, and tokenizing text

def clean_whitespace(text: str) -> str:
    """Turn repeated spaces, tabs, and newlines into single spaces."""
    return re.sub(r"\s+", " ", text).strip()

def sentiment_label(score: float) -> str:
    """Convert polarity score into label."""
    if score >= 0.1:
        return "positive"
    if score <= -0.1:
        return "negative"
    return "neutral"

def tokenize_words(text: str, stopwords: set[str]) -> list[str]:
    """Tokenize and remove stopwords."""
    tokens = re.findall(r"[A-Za-z][A-Za-z'-]+", text.lower())
    return [t for t in tokens if len(t) > 2 and t not in stopwords]



# Step 5: Fetching webpage content using HTTP request
headers = {"User-Agent": "Mozilla/5.0 (text analysis tutorial)"}
response = requests.get(URL, headers=headers, timeout=30)
response.raise_for_status()



# Step 6: Parse HTML content and locate main article section
soup = BeautifulSoup(response.text, "lxml")

section = soup.select_one("main div.section")
if section is None:
    raise RuntimeError("Could not find article section.")



# Step 7: Removing unwanted elements and extract clean paragraphs
for unwanted in section.select('script, style, a[href="#qa"], .ecb-publicationDate'):
    unwanted.decompose()

text_blocks = []
for element in section.find_all("p"):
    classes = element.get("class", [])

    if "ecb-pressContentSubtitle" in classes:
        continue

    text = clean_whitespace(element.get_text(" ", strip=True))
    if text:
        text_blocks.append(text)

full_text = "\n\n".join(text_blocks)



# Step 8: Saving extracted text to local file
text_path = DATA_DIR / "ecb_govdec_2026-05-04.txt"
text_path.write_text(full_text, encoding="utf-8")



# Step 9: Performing sentiment analysis for each paragraph
results = []
for i, para in enumerate(text_blocks, start=1):
    doc = nlp(para)
    polarity = doc._.blob.polarity

    results.append({
        "paragraph_number": i,
        "paragraph_text": para,
        "sentiment_score": round(polarity, 3),
        "sentiment_label": sentiment_label(polarity)
    })

df = pd.DataFrame(results)



# Step 10: Saving sentiment results to CSV file
sentiment_path = OUTPUT_DIR / "ecb_paragraph_sentiment.csv"
df.to_csv(sentiment_path, index=False, encoding="utf-8")

print("\nSentiment preview:")
print(df.head())



# Step 11: Generating word frequency counts for auto stopword detection
raw_tokens = re.findall(r"[A-Za-z][A-Za-z'-]+", full_text.lower())
raw_counts = Counter(raw_tokens)



# Step 12: Identifying frequent words as candidate stopwords
auto_candidates = {
    word for word, count in raw_counts.items()
    if count > 10 and len(word) <= 6
}

print("\nAuto-detected stopword candidates:")
print(sorted(auto_candidates))



# Step 13: Creating final stopword list combining default, manual, and auto-generated words
custom_stopwords = set(STOPWORDS)

custom_stopwords.update({
    "ecb", "euro", "area", "monetary", "policy",
    "inflation", "council", "financial"
})
custom_stopwords.update(auto_candidates)



# Step 14: Tokenizing text and computing top 50 frequent meaningful words
tokens = tokenize_words(full_text, custom_stopwords)
word_counts = Counter(tokens)

top_words = pd.DataFrame(word_counts.most_common(60),columns=["word", "count"])

top_words_path = OUTPUT_DIR / "ecb_top_words.csv"
top_words.to_csv(top_words_path, index=False)



# Step 15: Generating and saving word cloud visualization
wordcloud = WordCloud(
    width=1200,
    height=700,
    background_color="white",
    stopwords=custom_stopwords,
    max_words=60,
    colormap="viridis",
    random_state=42
).generate(full_text)

wordcloud_path = OUTPUT_DIR / "ecb_wordcloud.png"

plt.figure(figsize=(12, 7))
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")
plt.tight_layout()
plt.savefig(wordcloud_path, dpi=200)
plt.close()



# Step 16: Creating and saving sentiment distribution bar chart
plt.figure()
df["sentiment_label"].value_counts().plot(kind="bar")
plt.title("Sentiment Distribution")
plt.xlabel("Sentiment")
plt.ylabel("Count")
plt.tight_layout()
plt.savefig(OUTPUT_DIR / "sentiment_distribution.png")
plt.close()



# Step 17: Printing summary of outputs and average sentiment score
print("\nSaved files:")
print("Text:", text_path)
print("Sentiment CSV:", sentiment_path)
print("Top words CSV:", top_words_path)
print("Word cloud:", wordcloud_path)
print("Sentiment plot:", OUTPUT_DIR / "sentiment_distribution.png")

print("\nAverage sentiment:", round(df["sentiment_score"].mean(), 3))