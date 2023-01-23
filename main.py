import requests

from api_key import API_KEY as key
from translate import Translator


response = requests.get(f'https://favqs.com/api/qotd', headers={'Authorization': f'Token token={key}'})
quote = response.json()
phrase = quote["quote"]["body"]

print(phrase)



translator = Translator(to_lang='en')
translation = translator.translate("Hola mundo")
print(translation)



