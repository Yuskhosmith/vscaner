import clickjack

def main():
    # Specify the URLs you want to scan for clickjacking vulnerabilities
    urls = ['http://www.example.com', 'http://www.google.com']

    for url in urls:
        print(f"Scanning vulnerability for URL: {url}")
        clickjack.check_clickjacking(url)

if __name__ == "__main__":
    main()