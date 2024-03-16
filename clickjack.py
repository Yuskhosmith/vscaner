import requests

HEADERS = {
    'X-Frame-Options': "X-Frame-Options tells the browser whether you want to allow your site to be framed or not. By preventing a browser from framing your site you can defend against attacks like clickjacking. Recommended value \"X-Frame-Options: SAMEORIGIN\".",
    'Content-Security-Policy': "Content Security Policy (CSP) is an added layer of security that helps to detect and mitigate certain types of attacks, including Cross Site Scripting (XSS) and data injection attacks. These attacks are used for everything from data theft to site defacement to distribution of malware.",
    'X-XSS-Protection': "X-XSS-Protection is a header that stops pages from loading when they detect reflected cross-site scripting (XSS) attacks.",
    'X-Content-Type-Options': "The X-Content-Type-Options response HTTP header is a marker used by the server to indicate that the MIME types advertised in the Content-Type headers should not be changed and be followed.",
    'Referrer-Policy': "The Referrer-Policy HTTP header controls how much referrer information (sent via the Referer header) should be included with requests.",
    'Feature-Policy': "Feature Policy is a web platform feature which allows developers to selectively enable and disable use of various browser features and APIs. The policy is sent via a HTTP response header sent by the server.",
    'Permissions-Policy': 'The Permissions-Policy HTTP header replaces the existing Feature-Policy header for controlling delegation of permissions and powerful features. It allows a website to control which features and APIs can be used in the browser.'
}

def check_clickjacking(url):
    # Send a GET request to the URL and retrieve the response headers
    response = requests.get(url)
    headers = response.headers

    # Check if the 'X-Frame-Options' header is present in the response
    for (header, description) in HEADERS.items():
        if header in headers:
            print(f'{header} is enabled for URL: {url}')
        else:
            print(f'{header} is disabled for URL: {url}')
            print(description)
    # if 'X-Frame-Options' in headers:
    #     print(f'Clickjacking protection is enabled for URL: {url}')
    # else:
    #     print(f'Clickjacking protection is disabled for URL: {url}')
