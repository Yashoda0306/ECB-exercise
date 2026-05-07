# ECB-exercise

### Analysis Summary

### 1. ECB Page Chosen
I choose following ECB Governing Council decision page: 
(https://www.ecb.europa.eu/press/press_conference/monetary-policy-statement/2026/html/ecb.is260430~f99cb123a8.en.html)
for my analysis. 

This page contains structured paragraphs which covers:
- Monetary policy decisions
- Inflation outlook
- Economic growth and risks
- Financial conditions
- Interest rates and lending
- Forward guidance and market expectations

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
- Scalability across different ECB  
- Reduction of repetitive policy-related noise  
  ##### This approach improves keyword extraction by removing both generic and ECB-specific high-frequency terms.


### 3️. Paragraph-Level Results & Sentiment Distribution
The analysis processed 48 paragraphs from the given ECB monetary policy statement press conference
- Majority of paragraphs were **Positive** which reflects institutional confidence, stability, and policy reassurance.
- Few are neutral so it follows neutral tone.  
- Mild number of paragraphs were negative which discussed: geopolitical risks, inflation pressures, economic uncertainty and market volatility.

The overall average sentiment score was 0.128 which indicates a generally stable and cautiously positive communication tone.
“Positive” reflects institutional wording, not emotional tone.  

### Key Insights
From the word frequency and word cloud analysis, the dominant themes include:
- inflation and price developments
- economic growth outlook
- energy prices and risks
- interest rates and lending conditions
- monetary policy decisions
- financial market conditions

The ECB consistently emphasizes:
- maintaining price stability
- monitoring economic and geopolitical risks
- data-dependent monetary policy decisions
- financial system resilience

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


