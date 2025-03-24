# 📰 Company News Sentiment Analyzer with Hindi TTS

This is a full-stack application that analyzes recent news coverage for a given company. It scrapes the top 10 news articles, performs sentiment analysis using Hugging Face transformers, extracts key topics, generates a comparative analysis, and produces a Hindi audio summary using gTTS.

---

## 🚀 Features

- Scrapes 10 recent news articles using BeautifulSoup (non-JavaScript)
- Sentiment classification: Positive / Negative / Neutral
- Extracts key topics using YAKE
- Comparative sentiment analysis across articles
- Text summary in both English and Hindi
- Hindi audio output using TTS
- Streamlit web UI
- FastAPI backend for processing
- Ready for deployment on Hugging Face Spaces

---

## 📁 Project Structure

```
.
├── app.py                  # FastAPI backend OR main Streamlit file on HF
├── streamlit_UI.py         # Streamlit frontend (renamed to app.py for Spaces)
├── api.py                  # Core integration logic
├── collection_data.py      # Scraper for 10 articles
├── sentiment_analysis.py   # HuggingFace + keyword extraction
├── summary_report.py       # Summary, comparison, Hindi TTS
├── requirements.txt        # Python dependencies
├── .env                    # Optional secrets file
├── README.md               # Project instructions
```

---

## ⚙️ Setup Instructions (Local)

1. **Clone the repository:**

```bash
git clone https://huggingface.co/spaces/Ganeshtati/news_analysis
cd news_analysis
```

2. **Create a virtual environment:**

```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

3. **Install dependencies:**

```bash
pip install -r requirements.txt
```

4. **Start the backend:**

```bash
uvicorn app:app --reload
```

5. **Run the frontend:**

Open a new terminal:

```bash
streamlit run streamlit_UI.py
```

---

## 🧪 Example Output

**Input:**
```json
{
  "company": "Tesla"
}
```

**Output:**
- List of article titles, summaries, sentiment, and topics
- Comparative sentiment insights (positive vs. negative angles)
- Common and unique topics
- Final sentiment summary in English and Hindi
- Audio output in Hindi

---

## 🧠 Dependencies

```text
streamlit
fastapi
uvicorn
transformers
gtts
requests
beautifulsoup4
googlesearch-python
python-dotenv
yake
```

---

## 🌐 Hugging Face Deployment Guide

### 1. Create a new Space
- Go to: https://huggingface.co/spaces
- Click **Create new Space**
- Choose SDK: **Streamlit**
- Name your space and make it public/private

### 2. Clone the HF repo

```bash
git clone https://huggingface.co/spaces/your-username/news-sentiment-analyzer
cd news-sentiment-analyzer
```

### 3. Copy your code and rename frontend:

```bash
cp ../your-local-project/* .
mv streamlit_UI.py app.py
```

### 4. Commit and push

```bash
git add .
git commit -m "Deploy to Hugging Face Spaces"
git push
```

HF will auto-build and host your app. The live app URL will be:

```
https://huggingface.co/spaces/your-username/news-sentiment-analyzer
```

---

## 🙌 Credits

- [Hugging Face Transformers](https://huggingface.co/models)
- [gTTS](https://pypi.org/project/gTTS/)
- [Streamlit](https://streamlit.io/)
- [FastAPI](https://fastapi.tiangolo.com/)
- [YAKE Keyword Extractor](https://github.com/LIAAD/yake)

---
