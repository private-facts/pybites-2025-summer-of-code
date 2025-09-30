# Pybites 2025 Challenge

## First, have fun

This is a friendly, open challenge—no PRs or grading. Just build something cool and show it off in the Pybites community! 🧠✨
This Community Code Challenge invites you to build a powerful Blog Scraper using our very own https://pybit.es blog.

## 🧪 The Scraping Challenge

Your mission:
✅ Export results in CSV/JSON (and maybe even PDF!)
✅ Share your project in the community thread

Build something that’s useful, insightful, and fun to work on 💡

### 🧠 Learning Goals

[ ]Practice real-world HTML scraping
[ ] Learn how to parse and clean data from messy layouts
[ ] Build a tool that checks for broken links at scale
[ ] Create reports that offer insights on a real blog archive
[ ] (Optional) Explore PDF creation and CLI tooling[ ]
[ ]## 🧩 What You’ll Build

### Build A tool that:

[ ] Scrapes all articles from the PyBites blog. Because its feed (https://pybit.es/feed/) only holds the last 10 articles, you want to use the sitemaps listed here -> https://pybit.es/sitemap_index.xml
[ ] Extracts post metadata like 
    - title, 
    - URL, 
    - date, 
    - author, 
    - and tags
[ ] Checks all internal and external links for broken URLs (status 400+)
[ ] Outputs structured data in CSV or JSON format
[ ] Highlights which articles contain dead links 🛠️

### 🏆 Bonus Features (Stretch Goals)

Looking for extra challenge? Try implementing:
[ ] 📄 A PDF summary of article titles and publish dates
[ ] 👥 Author stats: how many posts each one has written
[ ] 🔖 Tag analysis: find the top 5 most-used tags
[ ] 🗂️ Archive view: group posts by year or month
[ ] 🧪 A CLI interface: filter posts by author, tag, date, or count (--since 2020, --limit 10, etc.)
[ ] ⚡ Speed boost: use threading or asyncio to make link-checking or scraping faster
[ ] 🛠 Suggested Tools & Technologies

Use any stack you like! But here are some great tools to explore:

requests + BeautifulSoup or Newspaper3k — classic Python scraping libraries
aiohttp or concurrent.futures — speed up link checking
WeasyPrint, pdfkit, or reportlab — for PDF generation
argparse, Typer, or click — to build a user-friendly CLI

--- 

## Opinionated Example using Incremental Variations

### Version 0 - The Naive Exercise

✅ get the list of blog articles on pybit.es from the site map....and for each article, find dead links

- find a link
- get the headers (faster than the whole thing.)
- If fails...
    - Only looking for Error 404, since other kinds of codes other than 200 (like 301 - Permanently Moved) seemed to work.
    - Follow-up question: Are there other codes besides 404 that indicate dead links?
    - Follow-up question: Do we want to flag other codes (like 301) that work, but aren't in the 200 range in some way?

https://stackoverflow.com/a/73302844
1. parse links from one article, use bs4 or newspaper3k
2. check links for dead ones
3. process links in sequence

### Version 2 - Add asynch client to make it faster

4. experiment with httpx.AsyncClient() and/or aiohttp
- https://tonybaloney.github.io/posts/why-isnt-python-async-more-popular.html#backend-fragmentation
- https://newspaper.readthedocs.io/en/latest/
- https://www.crummy.com/software/BeautifulSoup/bs4/doc/#find-all

### Version 3 - Add threads to make it multi-processing client
- (and/or concurrent.futures == stdlib)

## Tips for Ensemble Coding sessions...

### Collaboration tools:

- Mobtimer: https://mobti.me/pybites-ensemble

### Contributor headers

Co-authored-by: Blaise Pabon <blaise@gmail.com>
Co-authored-by: CodeConnoisseur74 <info@focusbit.io>
Co-authored by: Anschel Burk <anschel.burk@gmail.com>
Co-authored-by: Kishan Patel <kishanpatel789@gmail.com>
Co-authored-by: Rana Khalil <r.ash.khalil96@gmail.com>
Co-authored-by: Bob Belderbos <bob@pybit.es>
Co-authored-by: John Safrit <eedesigner@gmail.com>