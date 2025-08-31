# Pybites 2025 Challenge

## First, have fun

This is a friendly, open challenge—no PRs or grading. Just build something cool and show it off in the Pybites community! 🧠✨

## Scraping challenge

This Community Code Challenge invites you to build a powerful Blog Scraper using our very own https://pybit.es blog.

🧪 The Challenge

Your mission:

✅ Create your own repo or Gist: 

✅ Write a scraper that crawls pybit.es
    ```python
    import httpx
    r = httpx.get('https://https://pybit.es/sitemap_index.xml
    print(r.t)
    ```

✅ Extract blog metadata ....
and 
find dead links (Please use the sitemaps in the link above)
- find a link
- try it
- If fails, write it down

✅ Export results in CSV/JSON (and maybe even PDF!)

✅ Share your project in the community thread

Because its feed (https://pybit.es/feed/) only holds the last 10 articles, you want to use the sitemaps listed here -> https://pybit.es/sitemap_index.xml

This is your chance to:

✅ Level up your web scraping skills on a real-world site

✅ Detect dead links across hundreds of blog posts

✅ Extract and analyze metadata from developer-written content

✅ Output and/or visualize the data

Build something that’s useful, insightful, and fun to work on 💡

🧩 What You’ll Build

A tool that:

Scrapes all articles from the PyBites blog

Extracts post metadata like title, URL, date, author, and tags

Checks all internal and external links for broken URLs (status 400+)

Outputs structured data in CSV or JSON format

Highlights which articles contain dead links 🛠️

🏆 Bonus Features (Stretch Goals)

Looking for extra challenge? Try implementing:

📄 A PDF summary of article titles and publish dates

👥 Author stats: how many posts each one has written

🔖 Tag analysis: find the top 5 most-used tags

🗂️ Archive view: group posts by year or month

🧪 A CLI interface: filter posts by author, tag, date, or count (--since 2020, --limit 10, etc.)

⚡ Speed boost: use threading or asyncio to make link-checking or scraping faster

🛠 Suggested Tools & Technologies

Use any stack you like! But here are some great tools to explore:

requests + BeautifulSoup or Newspaper3k — classic Python scraping libraries

aiohttp or concurrent.futures — speed up link checking

WeasyPrint, pdfkit, or reportlab — for PDF generation

argparse, Typer, or click — to build a user-friendly CLI

🧠 Learning Goals

Practice real-world HTML scraping

Learn how to parse and clean data from messy layouts

Build a tool that checks for broken links at scale

Create reports that offer insights on a real blog archive

(Optional) Explore PDF creation and CLI tooling





## Milestones:

✅ Create your own repo or Gist
 
✅ Write a scraper that crawls pybit.es

✅ Extract blog metadata and find dead links (Please use the sitemaps in the link above)

✅ Export results in CSV/JSON (and maybe even PDF!)

✅ Share your project in the community thread

## Ensemble ?

### Collaboration tools:

- Mobtimer: https://mobti.me/pybites-ensemble

### Contributor headers


Co-authored-by: Blaise Pabon <blaise@gmail.com>
Co-authored-by: CodeConnoisseur74 <info@focusbit.io>