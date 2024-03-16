import requests

def scan_headers(url):
    try:
        # Send a GET request to the target URL
        response = requests.get(url)
        
        # Extract headers from the response
        headers = response.headers
        
        # Check for security-relevant headers
        security_headers = {
            'Content-Security-Policy': 'default-src \'self\'',
            'X-Content-Type-Options': 'nosniff',
            'Strict-Transport-Security': 'max-age=31536000; includeSubDomains; preload',
            'Referrer-Policy': 'no-referrer',
            'X-Frame-Options': 'DENY'
        }
        
        # Check if each security header is present in the response
        results = {}
        for header, value in security_headers.items():
            if header in headers:
                results[header] = {'status': 'Present', 'value': headers[header]}
            else:
                results[header] = {'status': 'Missing', 'suggestion': value}
        
        return results
    except requests.RequestException as e:
        return {'error': str(e)}
