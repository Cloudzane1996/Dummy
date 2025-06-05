
"""Thread Archiver: Save Twitter threads via ThreadReaderApp

Usage:
    python thread_archiver.py https://twitter.com/username/status/1234567890
Requires:
    requests, beautifulsoup4
Note:
    ThreadReaderApp must have the thread unrolled publicly or you must be logged in.
"""

import sys
import requests
from bs4 import BeautifulSoup
from datetime import datetime
import os

def save_thread(url):
    if 'threadreaderapp.com' not in url:
        url = f"https://threadreaderapp.com/thread/{url.split('/')[-1]}.html"
    r = requests.get(url, timeout=30)
    if r.status_code != 200:
        print(f"Failed to fetch thread: {r.status_code}")
        return
    soup = BeautifulSoup(r.text, 'html.parser')
    title = soup.find('h1').get_text(strip=True)
    body = soup.find('div', {'class': 'threadreader_body'}).get_text('
', strip=True)
    now = datetime.now().strftime('%Y%m%d_%H%M')
    filename = f"thread_{title[:50].replace(' ', '_')}_{now}.txt"
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(title + '\n\n' + body)
    print(f"Saved to {filename}")

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python thread_archiver.py <thread URL>")
        sys.exit(1)
    save_thread(sys.argv[1])
