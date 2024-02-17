import requests

def check_clickjacking(url):
    # Send a GET request to the URL and retrieve the response headers
    response = requests.get(url)
    headers = response.headers

    # Check if the 'X-Frame-Options' header is present in the response
    if 'X-Frame-Options' in headers:
        print(f'Clickjacking protection is enabled for URL: {url}')
    else:
        print(f'Clickjacking protection is disabled for URL: {url}')
