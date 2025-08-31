

import httpx

def get_page(url = None):
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
        print(first_url)

        # Raise an exception for bad status codes (4xx or 5xx)
        response.raise_for_status()

        # Check if the Content-Type header indicates XML
        if "application/xml" in response.headers.get("Content-Type", ""):
            # Access the XML content as text
            xml_content = response.text
            print("Received XML content:")
            print(xml_content)
        else:
            print("Response content is not XML.")
            print(response.text)

    except httpx.RequestError as exc:
        print(f"An error occurred while requesting {exc.request.url!r}: {exc}")
    except httpx.HTTPStatusError as exc:
        print(f"Error response {exc.response.status_code} while requesting {exc.request.url!r}: {exc}")
        
if __name__ == "__main__":
    main()
