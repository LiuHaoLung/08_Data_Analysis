import pandas

url = 'https://en.wikipedia.org/wiki/Python_(programming_language)'
d = pandas.read_html(url)
print(d)

d = pandas.read_html(url)[1]
print(d)
