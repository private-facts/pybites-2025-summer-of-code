import xmltodict
from time import time
import json
from bs4 import BeautifulSoup
import httpx

NOT_FOUND = 404
TTL = 60 * 60
VALID_CODES = {403}
RESULT_FILE_NAME = "checked_links.json"


def is_live_link(link: str) -> bool:
    try:
        resp = httpx.request("head", link, follow_redirects=True)
        ok = (200 <= resp.status_code < 300) or resp.status_code in VALID_CODES
        return ok
    except Exception:
        return False


def needs_testing(href, tested_links):
    if href not in tested_links:
        return True
    _, tstamp = tested_links[href]
    if int(time()) - tstamp >= TTL:
        return True
    return False


def save_results(path_name, test_results):
    with open(path_name, "w") as file:
        json.dump(test_results, file)


def main(url=None):
    """Make a set of URLs.

    # With async: grab a URL from
    # follow link
        # if failed, add the URL to  broken_links
        # if OK
    # crawl every URL in the sitemap?
    """

    url = "https://pybit.es/sitemap_index.xml"
    tested_links = {}
    try:
        # Send a GET request with the Accept header set to application/xml
        response = httpx.get(url, headers={"Accept": "application/xml"})
        data_dict = xmltodict.parse(response.text)
        table_of_contents = data_dict["sitemapindex"]["sitemap"]
        first_url = table_of_contents[0]["loc"]
        # print(first_url)
        # TODO: this is only checking the first URL in the sitemap index
        # Need to loop through all URLs in the sitemap index
        # and check each one for broken links
        # Send a GET request with the Accept header set to application/xml
        response = httpx.get(first_url, headers={"Accept": "application/xml"})
        data_dict = xmltodict.parse(response.text)
        links = [link["loc"] for link in data_dict["urlset"]["url"]]
        """
        for link in links:
            # Check each link to see if working or broken
            print(f"Checking link: {link}")
            response = httpx.head(link)
            if response.status_code == NOT_FOUND:
                print(f"--Oh Noo: Broken link: {link}")
        """
        # get it working for one link
        articles = links[:10]  # just ten for now
        for article in articles:
            print("checking", article)  # each pybites article
            response = httpx.get(article)
            soup = BeautifulSoup(response.text, "html.parser")
            html = soup.find("div", class_="entry-content")
            links = html.find_all("a")

            for li in links:
                href = li.get("href")
                if href is None or not needs_testing(href, tested_links):
                    continue

                link_status = is_live_link(href)
                tested_links[href] = (link_status, int(time()))
                if not link_status :
                    print(href, link_status)

        save_results(path_name=RESULT_FILE_NAME, test_results=tested_links)

    except httpx.RequestError as exc:
        print(f"An error occurred while requesting {exc.request.url!r}: {exc}")
    except httpx.HTTPStatusError as exc:
        print(
            f"Error response {exc.response.status_code} while requesting {exc.request.url!r}: {exc}"
        )


if __name__ == "__main__":
    main()

# TODO Next: read the file of checked links so we don't repeat recent checks...
# TODO 3. time sequence solution, speed it up with httpx and/or aiohttp (and/or concurrent.futures == stdlib)
# TODO and time it again, what is perf gain?
