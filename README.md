
# 🌐 LinkedIn Web Scraper using BeautifulSoup

This Python script demonstrates how to use **BeautifulSoup** and **requests** to scrape key HTML elements such as titles, links, paragraphs, and email addresses from a target webpage. The current example targets [LinkedIn](https://linkedin.com), but the script can be adapted to any site that permits scraping.

---

## 🚀 Features

* Fetches and parses live HTML content using `requests` and `BeautifulSoup`
* Extracts:

  * Page title
  * All `<p>` paragraph tags
  * All `<a>` anchor tags
  * Cleaned absolute links (no `#`, no duplicates)
  * Tags by `id` and `class`
  * All email addresses using `mailto`
* Demonstrates traversal:

  * `.children`, `.contents`, `.strings`, `.stripped_strings`
  * `.parent`, `.parents`
  * `.next_sibling`, `.previous_sibling`
* Uses both `soup.find()` and `soup.select()` (CSS selectors)

---

## 📂 Project Structure

```plaintext
.
├── main.py        # The main Python script
├── README.md      # Project documentation
```

---

## 🔧 Requirements

* Python 3.6+
* `requests` library
* `beautifulsoup4`

### Install dependencies:

```bash
pip install requests beautifulsoup4
```

---

## 🧪 How It Works

1. **Sends a GET request** to `https://linkedin.com`
2. **Parses the HTML** content with `html.parser`
3. **Traverses HTML** to extract:

   * Title: `soup.title`
   * All paragraphs: `soup.find_all("p")`
   * All links: `soup.find_all("a")`
4. **Filters and cleans links** using conditions and `set()`
5. **Traverses DOM** for elements with specific `id` and `class`
6. **Uses CSS Selectors** like `.select(".class")` and `.select("#id")`
7. **Detects and prints email addresses** using `mailto` links

---

## 📌 Sample Output

```bash
https://linkedin.com/jobs
https://linkedin.com/feed
mailto:example@email.com
...
<p>Hello</p>
<span>World</span>
Hello
World
<class 'bs4.element.Tag'>
...
```

---

## 🛑 Legal Note

This script is for **educational purposes only**. Always ensure that the website’s `robots.txt` allows scraping. Do not scrape content from websites like LinkedIn without proper authorization, as it violates their [terms of service](https://www.linkedin.com/legal/user-agreement).

---

## 📬 Contact

Made with ❤️ by [Abdullah Muhammad Khalid](mailto:contact.abdullahkhalid@gmail.com)


