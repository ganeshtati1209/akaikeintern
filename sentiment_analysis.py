from transformers import pipeline
import yake

classifier = pipeline("sentiment-analysis")
kw_extractor = yake.KeywordExtractor(n=1, top=5)


def analyze_sentiment(article):
    """
    Performs sentiment analysis and topic extraction on a news article.

    Parameters:
        article (dict): A dictionary containing 'title' and 'content' keys.

    Returns:
        dict: Processed article with 'Title', 'Summary', 'Sentiment', and 'Topics'.
    """
    sentiment_result = classifier(article["content"][:512])[0]
    label = sentiment_result["label"]
    sentiment = (
        "Positive" if label == "POSITIVE"
        else "Negative" if label == "NEGATIVE"
        else "Neutral"
    )

    topics = [kw[0] for kw in kw_extractor.extract_keywords(article["content"])]

    return {
        "Title": article["title"],
        "Summary": article["content"][:300],
        "Sentiment": sentiment,
        "Topics": topics
    }
