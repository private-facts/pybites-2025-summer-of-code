
import xmltodict
import httpx
NOT_FOUND = 404
def main(url = None):
    """ Make a set of URLs.

        # With async: grab a URL from
        # follow link
            # if failed, add the URL to  broken_links
            # if OK
        # crawl every URL in the sitemap?
    """

    url = 'https://pybit.es/sitemap_index.xml'

    try:
        # Send a GET request with the Accept header set to application/xml
        response = httpx.get(url, headers={"Accept": "application/xml"})
        data_dict = xmltodict.parse(response.text)
        table_of_contents = data_dict['sitemapindex']['sitemap']
        first_url = table_of_contents[0]['loc']
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
        # get it working for one link
        article = links[1] # or another N depending if it's an interesting article
        print(article)
        # 1. scrape link (newspaper3k or bs4) finding all relevant links (not sidebar/navbar stuff)
        # 2. use httpx.head like above to see if dead or alive (if not enough links process various articles)
        # 3. time sequence solution, speed it up with httpx and/or aiohttp (and/or concurrent.futures == stdlib)
        # and time it again, what is perf gain?
        

    except httpx.RequestError as exc:
        print(f"An error occurred while requesting {exc.request.url!r}: {exc}")
    except httpx.HTTPStatusError as exc:
        print(f"Error response {exc.response.status_code} while requesting {exc.request.url!r}: {exc}")
        
if __name__ == "__main__":
    main()
