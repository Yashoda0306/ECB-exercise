# ECB-exercise

### Analysis Summary

### 1. ECB Page Chosen
I choose following ECB Governing Council decision page: 
https://www.ecb.europa.eu/press/govcdec/otherdec/2026/html/ecb.gc260504~07dc9bac72.en.html 
for my analysis. 

This page contains structured paragraphs which covers:
- Monetary policy decisions  
- Inflation outlook  
- Economic conditions and risks  
- Forward guidance  

### 2️. Sentiment Package Used and Why 
I used  spaCy  with the SpacyTextBlob extension for sentiment analysis.
This approach was chosen because it provides:
-Straightforward polarity scores (-1 to +1) for each paragraph
-Seamless integration with spaCy’s NLP pipeline
-Efficient processing of structured text
-No requirement for model training 

##### In addition, I extended the analysis with help of AI by:
- implimenting **automatic stopword detection** (frequency-based)  
- Combining with **manual domain-specific stopwords**  

Which improves:
- Keyword relevance  
- Scalability across documents  
- Reduction of domain-specific noise  
  ##### This approach improves keyword extraction by removing both generic and ECB-specific high-frequency terms.


### 3️. Paragraph-Level Results & Sentiment Distribution
- Majority of paragraphs were **Neutral** so neutral tone dominates which reflects technical and policy languange. 
- Few are positive which reflects stability, resilience and policy support. 
- None of them are negative which is expected due to formal central bank communication style.  

“Positive” reflects institutional wording, not emotional tone  

### Key Insights
From the word frequency and word cloud analysis, the main perception includes:
-inflation and price stability
-monetary policy decisions
-economic outlook and risks
-financial conditions and interest rates

The ECB consistently emphasizes maintaining inflation targets, monitoring economic risks and data-dependent policy decisions.

### Sentiment Distribution
-Added sentiment distribution visualization to better summarize paragraph-level sentiment results
-Helps quickly understand the overall tone of the ECB communication
-Makes sentiment scores easier to interpret through visual representation

### 4. Outputs
After running the script, the following files are generated:

| File | Description |
|------|------------|
| `ecb_paragraph_sentiment.csv` | Sentiment per paragraph |
| `ecb_top_words.csv` | Top 60 keywords |
| `ecb_wordcloud.png` | Keyword visualization |
| `sentiment_distribution.png` | Sentiment distribution chart |


