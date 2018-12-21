from urllib import parse

url = parse.urlparse('https://www.youtube.com/results?search_query=헤이즈+첫눈에')
print(url)
query = parse.parse_qs(url.query)
print(query)
encoded = parse.urlencode(query, doseq=True)

print(encoded)
# print(parse.urlencode("헤이즈+첫눈에", doseq=True))