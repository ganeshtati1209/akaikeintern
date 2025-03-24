from collection_data import fetch_articles
from sentiment_analysis import analyze_sentiment
from summary_report import generate_report


def generate_full_report(company):
    """
    Generates the complete sentiment analysis report for a given company.

    Parameters:
        company (str): The name of the company to analyze.

    Returns:
        dict: A structured report including article data, sentiment analysis,
              comparative analysis, and summary in English and Hindi.
    """
    articles = fetch_articles(company)
    analyzed = [analyze_sentiment(article) for article in articles]
    report = generate_report(company, analyzed)
    return report
