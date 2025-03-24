from gtts import gTTS
import base64
import io


def generate_report(company, analyzed_articles):
    """
    Generates a complete sentiment and topic comparison report, including
    final summaries and Hindi TTS audio.

    Parameters:
        company (str): The name of the company.
        analyzed_articles (list): List of articles with sentiment and topic data.

    Returns:
        dict: Structured report with sentiment distribution, topic overlap,
              comparative insights, English and Hindi summaries, and audio.
    """
    sentiments = {"Positive": 0, "Negative": 0, "Neutral": 0}
    all_topics = []

    for article in analyzed_articles:
        sentiments[article["Sentiment"]] += 1
        all_topics.append(set(article.get("Topics", [])))

    en_summary = (
        f"Recent news for {company} includes "
        f"{sentiments['Positive']} positive, "
        f"{sentiments['Negative']} negative, and "
        f"{sentiments['Neutral']} neutral articles."
    )

    hi_summary = (
        f"{company} की नवीनतम खबरें "
        f"{sentiments['Positive']} सकारात्मक, "
        f"{sentiments['Negative']} नकारात्मक और "
        f"{sentiments['Neutral']} न्यूट्रल रिपोर्टें शामिल हैं।"
    )

    coverage_diff = []
    for i in range(len(analyzed_articles) - 1):
        a1 = analyzed_articles[i]
        a2 = analyzed_articles[i + 1]
        comp = {
            "Comparison": f"{a1['Title'][:60]}... vs {a2['Title'][:60]}...",
            "Impact": (
                f"Article {i + 1} discusses {', '.join(a1['Topics'])}, "
                f"while Article {i + 2} focuses on {', '.join(a2['Topics'])}."
            )
        }
        coverage_diff.append(comp)

    topic_union = set().union(*all_topics)
    topic_intersection = set.intersection(*all_topics) if all_topics else set()

    unique_topics = []
    for i, topics in enumerate(all_topics):
        unique = topics - topic_intersection
        unique_topics.append({f"Unique Topics in Article {i + 1}": list(unique)})

    tts = gTTS(hi_summary, lang="hi")
    fp = io.BytesIO()
    tts.write_to_fp(fp)
    audio_base64 = base64.b64encode(fp.getvalue()).decode()

    return {
        "Company": company,
        "Articles": analyzed_articles,
        "Comparative Sentiment Score": {
            "Sentiment Distribution": sentiments,
            "Coverage Differences": coverage_diff,
            "Topic Overlap": {
                "Common Topics": list(topic_intersection),
                "Unique Topics": unique_topics
            }
        },
        "Final Sentiment Analysis (English)": en_summary,
        "Final Sentiment Analysis (Hindi)": hi_summary,
        "Audio": audio_base64
    }
