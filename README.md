# DMARC Domains

## Overview
dmarc-domains.py is a Python script designed to retrieve a list of domains that share the same DMARC (Domain-based Message Authentication, Reporting, and Conformance) record as a specified domain. This tool leverages the automation to fetch data from the `www.dmarc.live` using Requests and Beautiful Soup for parsing the HTML content to extract the domain names.

## Features
- Fetches and prints a list of domains with the same DMARC record for the input domain.

## Requirements
To run this script, you will need Python 3.7 or newer. The following Python packages are also required:
- `bs4`
- `requests`

You can use the following command for easy installation of depencencies.
- `pip3 install bs4 requests`

## Usage

To use the DMARC Domain Fetcher, run the script from the command line with the `-d/--domain` argument followed by the domain name you wish to query. Here is an example command:

`python dmarc-domains.py -d yahoo.com`


### Output
The script will print a list of domains that share the same DMARC record for the specified domain. If no domains are found, it will output nothing.

## Note
This script is intended for educational and ethical use only. Ensure you have permission to scrape the website and are compliant with their terms of service and any legal requirements.

## Contributing
Contributions to the DMARC Domain Fetcher are welcome. Please open an issue or pull request to suggest improvements or add new features.

## License
This script is released under the MIT License. See the LICENSE file for details.

#### P.S.: The idea was taken from @Tedixx's tool, but it was using browser which consumes very much resources. So, I wrote efficient code without using much resources.
