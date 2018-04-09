from urllib.parse import urlparse

# Get domain name (example.com)
def get_domain_name(url):
    try:
        results = get_sub_domain(url).split('.')
        return results[-2] + '.' + results[-1]
    except Exception as e:
        print("Error: " + e)
        return ''

def get_sub_domain(url):
    try:
        return urlparse(url).netloc
    except Exception as e:
        print("Error: " + e)
        return ''

print(get_domain_name('https://www.amazon.co.uk/'))
