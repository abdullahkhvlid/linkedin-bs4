
# 📝 Quotes Web Scraper using BeautifulSoup

This Python script demonstrates how to use **BeautifulSoup** and **requests** to scrape real-world content from the website [quotes.toscrape.com](http://quotes.toscrape.com). It extracts data like page titles, paragraph text, anchor links, quotes, authors, tags, and more using powerful HTML traversal techniques.

---

## 🚀 Features

✔️ Fetches and parses live HTML content using `requests` and `BeautifulSoup`
✔️ Extracts:

* Page `<title>`
* All paragraph `<p>` tags
* All anchor `<a>` tags
* Unique, cleaned absolute links (excluding `#`)
* Quotes with corresponding authors and tags
* Tags by CSS classes and `id` (demo)
* Email addresses using `mailto:` (if present)

✔️ Demonstrates advanced traversal:

* `.children`, `.contents`, `.strings`, `.stripped_strings`
* `.parent`, `.parents`
* `.next_sibling`, `.previous_sibling`
* `.select()` for CSS selector queries

---

## 📂 Project Structure

```
.
├── main.py        # The main Python script
├── README.md      # This file
```

---

## 🔧 Requirements

* Python 3.6+
* `requests` library
* `beautifulsoup4`

### Install with pip:

```bash
pip install requests beautifulsoup4
```

---

## ⚙️ How It Works

1. **Sends a GET request** to `http://quotes.toscrape.com`
2. **Parses the HTML** using the built-in `html.parser`
3. **Traverses the DOM** to extract:

   * Page title using `soup.title.string`
   * Paragraphs with `soup.find_all("p")`
   * Anchor links with `soup.find_all("a")`
   * Unique full URLs using `set()` and URL correction
   * Quotes, authors, and tags using class filters
   * Elements via CSS selectors `.select(".tag")`
   * Nested text and HTML using `.children`, `.contents`, `.stripped_strings`
   * Email links with `"mailto"` prefix
   * Parent/child/sibling elements for structural understanding

---

## 📌 Sample Output

```
Page Title: Quotes to Scrape
All Paragraph Texts:
- “The world as we have created it...”
All Unique Links:
http://quotes.toscrape.com/login
http://quotes.toscrape.com/page/2/
Quotes with Authors and Tags:
Quote: “The world as we have created it...”
Author: Albert Einstein
Tags: change, deep-thoughts, thinking
Tags Using CSS Selector '.tag':
- change
- deep-thoughts
Sample Quote Children:
<class 'bs4.element.Tag'> <span class="text">“The world...”</span>
Stripped Strings from Quote:
“The world as we have created it...”
Albert Einstein
change
deep-thoughts
...
```

---

## 🛑 Legal Note

This scraper targets a public test site (`quotes.toscrape.com`) that was intentionally created for scraping practice.
**Always** check a website’s `robots.txt` and terms of service before scraping any live/real data from production websites.

---

## 📬 Contact

Made with ❤️ by [Abdullah Muhammad Khalid](mailto:contact.abdullahkhalid@gmail.com)

---

Would you like me to turn this into a `README.md` file and structure the project folder too?
