import requests
from bs4 import BeautifulSoup
import json

def count_words(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    text = soup.get_text()

    words = text.split()
    word_counts = {}
    for word in words:
        word_counts[word] = word_counts.get(word, 0) + 1

    result = [{word : count} for word, count in word_counts.items()]
    return json.dumps(result)

# Example usage
url = 'https://en.wikipedia.org/wiki/The_Kerala_Story'
output = count_words(url)
print(output)