import requests
from bs4 import BeautifulSoup
from googlesearch import search


def fetch_articles(company_name):
    """
    Fetches up to 10 news articles related to a given company name.

    Parameters:
        company_name (str): The name of the company to search articles for.

    Returns:
        list: A list of dictionaries containing 'title', 'url', and 'content'
              for each valid article.
    """
    query = f"{company_name} latest news"
    urls = list(search(query, num_results=20))

    articles = []
    for url in urls:
        try:
            response = requests.get(url, timeout=5)
            soup = BeautifulSoup(response.content, 'html.parser')

            title = soup.title.string.strip() if soup.title else None
            paragraphs = soup.find_all('p')
            content = ' '.join(p.get_text() for p in paragraphs[:10]).strip()

            if not title or len(content) < 50:
                continue

            blocked_keywords = ["access denied", "not allowed", "error", "reference"]
            if any(keyword in title.lower() for keyword in blocked_keywords):
                continue

            articles.append({
                "title": title,
                "url": url,
                "content": content
            })

            if len(articles) >= 10:
                break

        except Exception:
            continue

    return articles
