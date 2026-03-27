import requests  # Connects to News API and collects articles

# Personal API and Base_URL
API_KEY = ""
BASE_URL = "https://newsapi.org/v2/everything"  # NewsAPI endpoint

# Keywords List. This can be altered and changed to preference
keywords = [
    "crude oil", "oil", "WTI", "Brent", "OPEC", "Saudi", "Russia",
    "EIA", "API", "inventory", "refinery", "gasoline", "diesel",
    "natural gas", "pipeline", "production cut", "output cut",
    "Middle East", "geopolitics", "supply disruption", "sanction"
]

# Keyword Checking Function


def keyword_found(text):
    # makes everything lowercase to avoid missing articles due to caps sensitivity
    text = text.lower()
    for keyword in keywords:
        if keyword.lower() in text:
            return True  # as soon as a keyword of mine is found, function returns true and stops checking
    return False


# Set Parameters for NewsAPI
parameters = {
    # Most important line IMO. This specifies the news captured
    "q": "crude oil OR WTI OR Brent OR OPEC OR natural gas OR EIA OR API OR refinery OR Saudi OR Russia OR LNG",
    "language": "en",       # To make sure we get news in English
    "pageSize": 100,        # Max articles per request
    "apiKey": API_KEY
}

# Send Request to NewsAPI
result = requests.get(BASE_URL, params=parameters)

# Process the Articles
data = result.json()
articles = data["articles"]
print("Total articles fetched:", len(articles))

# Filter for articles containing keywords
matched_articles = []

for article in articles:
    # "" is imporant to make sure we get a string instead of a 'None' response
    title = str(article.get("title") or "")
    description = str(article.get("description") or "")
    content = title + " " + description

    if keyword_found(content):
        matched_articles.append(article)

print("Articles matching keywords:", len(matched_articles))

# Print Matching Articles
count = 1
for article in matched_articles:
    title = article.get("title", "No title available.")
    description = article.get("description", "No description available.")
    url = article.get("url", "No URL available.")

    # \n is used for readability, by providing space after each article
    print("\n[" + str(count) + "] " + title)
    print(description)
    print(url)
    count = count + 1
