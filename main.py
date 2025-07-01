import requests
from bs4 import BeautifulSoup
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

url = "http://quotes.toscrape.com"
r = requests.get(url)
htmlContent = r.content
soup = BeautifulSoup(htmlContent, "html.parser")

print("Page Title:", soup.title.string)
print("=" * 60)

print("All Paragraph Texts:")
for p in soup.find_all("p"):
    print("-", p.get_text(strip=True))
print("=" * 60)

print("All Unique Links:")
links = set()
for a in soup.find_all("a"):
    href = a.get("href")
    if href and not href.startswith("#"):
        full = href if href.startswith("http") else url + href
        links.add(full)
for link in links:
    print(link)
print("=" * 60)

print("Quotes with Authors and Tags:")
quotes = soup.find_all("div", class_="quote")
for q in quotes:
    quote_text = q.find("span", class_="text").get_text()
    author = q.find("small", class_="author").get_text()
    tags = [tag.get_text() for tag in q.find_all("a", class_="tag")]
    print("Quote:", quote_text)
    print("Author:", author)
    print("Tags:", ", ".join(tags))
    print("-" * 60)

toaster = soup.find(id="toaster")
print("Find by ID (toaster):", toaster)

print("Tags Using CSS Selector '.tag':")
tags = soup.select(".tag")
for t in tags:
    print("-", t.get_text())
print("=" * 60)

sample_quote = soup.find("div", class_="quote")
print("Sample Quote Children:")
for child in sample_quote.children:
    print(type(child), child)
print("=" * 60)

print("Stripped Strings from Quote:")
for s in sample_quote.stripped_strings:
    print(s)
print("=" * 60)

print("Email Links:")
for a in soup.find_all("a"):
    email = a.get("href")
    if email and email.startswith("mailto:"):
        print(email)
print("=" * 60)

print("Parent of sample quote tag:", sample_quote.parent.name)
print("All parents:")
for p in sample_quote.parents:
    print("-", p.name)
print("=" * 60)

print("Next sibling of quote:", sample_quote.next_sibling)
print("Next valid sibling:", sample_quote.next_sibling.next_sibling)
