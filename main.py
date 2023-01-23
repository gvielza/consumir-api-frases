import requests

api_key = "39e8a1f0052f8a49c98db69baac9e216"

response = requests.get(f'https://favqs.com/api/qotd', headers={'Authorization': f'Token token={api_key}'})
quote = response.json()
print(quote)
