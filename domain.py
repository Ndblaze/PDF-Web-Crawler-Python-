
import requests
from urllib.parse import urlparse

# Get domain name (example.com)
def get_domain_name(url):
    try:
        results = get_sub_domain_name(url).split('.')
        return results[-2] + '.' + results[-1]
    except:
        return ''


def get_header(url):
    r = requests.get(url)
    j = (r.headers['Content-Type'])
    (r.status_code)
    return j


# Get sub domain name (name.example.com)
def get_sub_domain_name(url):
    try:
        return urlparse(url).netloc
    except:
        return ''
