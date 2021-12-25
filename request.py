from requests import get, utils
response=get('http://www.cbr.ru/scripts/XML_daily.asp')
print(type(response))
print(dir(response))
encodings=utils.get_encoding_from_headers(response.headers)
content=response.content.decode(encodings=encodings)
print(content)
print(response.text)
