import urlparse


# Method to get domain name
def get_domain_name(url):
    try:
        results = get_sub_domain_name(url).split('.')
        return results[-2] + '.' + results[-1]
    except:
        return ''


# Method to get sub domain name
def get_sub_domain_name(url):
    try:
        return urlparse.urlparse(url).netloc
    except:
        return ''

