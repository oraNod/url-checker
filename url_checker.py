from typing import List, Tuple
import requests
from urllib.parse import urljoin
import sys
from datetime import datetime
import glob
import os

# Configuration
HOST: str = "https://docs.ansible.com"
REDIRECTS_DIR: str = "./redirect_test"
OUTPUT_FILE: str = f"url_report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"

def check_url(url: str) -> Tuple[int | str, str]:
    try:
        response: requests.Response = requests.head(url, allow_redirects=False)
        status: int = response.status_code
        redirect_url: str = response.headers.get('Location', '') if status in [301, 302] else ''
        if redirect_url and not redirect_url.startswith(('http://', 'https://')):
            redirect_url = urljoin(url, redirect_url)
        return status, redirect_url
    except requests.RequestException as e:
        return str(e), ''

def main() -> None:
    txt_files: List[str] = glob.glob(os.path.join(REDIRECTS_DIR, "*.txt"))
    if not txt_files:
        print(f"Error: No .txt files found in {REDIRECTS_DIR}")
        sys.exit(1)

    results: List[str] = []
    for txt_file in txt_files:
        with open(txt_file) as f:
            pages: List[str] = [line.strip() for line in f if line.strip()]

        for page in pages:
            url: str = urljoin(HOST, page)
            status, redirect = check_url(url)
            result: str = f"URL: {url}\nStatus: {status}"
            if redirect:
                result += f"\nRedirects to: {redirect}"
            results.append(result + "\n")

    with open(OUTPUT_FILE, 'w') as f:
        f.write("\n".join(results))
    print(f"Report generated: {OUTPUT_FILE}")

if __name__ == "__main__":
    main()