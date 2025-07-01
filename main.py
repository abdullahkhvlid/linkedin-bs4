import requests
from bs4 import BeautifulSoup
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

url = "https://linkedin.com"
r = requests.get(url)
htmlContent = r.content

soup = BeautifulSoup(htmlContent, "html.parser")

title = soup.title
paras = soup.find_all("p")
anchor = soup.find_all("a")

for link in anchor:
    print(link.get("href"))

links = set()
for l in anchor:
    href = l.get("href")
    if href and (href != "#"):
        if href.startswith("http"):
            whole_link = href
        else:
            whole_link = "https://linkedin.com" + href
        links.add(whole_link)
    print(whole_link)

sample = soup.find(id="_rht_toaster")
print(sample.children)
print(sample.contents)

for item in sample.strings:
    print(item)

for item in sample.stripped_strings:
    print(item)

print(sample.parent)

for i in sample.parents:
    print(i)
    print(i.name)

print(sample.next_sibling)
print(sample.next_sibling.next_sibling)

elem = soup.select(".class name")

for a in soup.find_all("a"):
    email = a.get("href")
    if email and email.startswith("mailto"):
        print(email)
    else:
        print("No email found in this link")

s = soup.select(".x")
print(s)
s = soup.select("#hello")
print(s)
