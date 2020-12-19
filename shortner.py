import pyshorteners
url = input("New URL you want to shorten: ")
shortener = pyshorteners.Shortener()
a = shortener.tinyurl.short(url)
print(a)
