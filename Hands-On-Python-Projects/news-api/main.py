import requests

def get_news(query, api_key):
    url = f"https://newsapi.org/v2/everything?q={query}&sortBy=publishedAt&apiKey={api_key}"
    response = requests.get(url)
    data = response.json()
    return data["articles"]

def main():
    query = input("What type of news are you interested in today? ")
    api_key = "YOUR_API_KEY_HERE"
    articles = get_news(query, api_key)
    for index, article in enumerate(articles):
        print(index + 1, article["title"], article["url"])
        print("\n****************************************\n")

if __name__ == "__main__":
    main()