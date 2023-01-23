import requests

from api_key import API_KEY as key
from translate import Translator


response = requests.get(f'https://favqs.com/api/qotd', headers={'Authorization': f'Token token={key}'})
quote = response.json()
phrase = quote["quote"]["body"]
autor = quote["quote"]["author"]

print(phrase)



translator = Translator(to_lang='es')
translation = translator.translate(phrase)
print(translation)
print(autor)



