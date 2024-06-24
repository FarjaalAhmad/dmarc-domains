import re
import bs4
import json
import argparse
import requests as req
from typing import Optional

DMARC_URL = "https://dmarc.live/info/"
DMARC_API = "https://dmarc.live/api/related/{}/100000"

def fetch_dmarc_data(domain: str) -> None:
    response: req.Response = req.get(f"{DMARC_URL}{domain}")
    html_content: str = response.text
    
    soup: bs4.BeautifulSoup = bs4.BeautifulSoup(html_content, 'html.parser')
    
    script_tag: Optional[bs4.element.Tag] = soup.find('script', string=lambda t: t and 'var live =' in t)
    
    if script_tag:
        match: Optional[re.Match] = re.search(r"dmarc_hash:'([^']+)'", script_tag.string)
        
        if match:
            dmarc_hash: str = match.group(1)
            api_response: req.Response = req.get(DMARC_API.format(dmarc_hash))
            domains_json: dict = api_response.json()
            
            for domain in domains_json.get("domains", []):
                print(domain)

def main() -> None:
    parser: argparse.ArgumentParser = argparse.ArgumentParser(description='Fetch domains with the same DMARC record.')
    parser.add_argument('-d', '--domain', required=True, help='Specify the domain to check.')
    args: argparse.Namespace = parser.parse_args()

    fetch_dmarc_data(args.domain)

main()
