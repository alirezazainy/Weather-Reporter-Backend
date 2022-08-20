from requests_html import HTMLSession, HTML, BaseParser
import requests
import urllib3
# Parsing Tool

# For Bypassing ssl errors must write this code below
requests.packages.urllib3.disable_warnings()
requests.packages.urllib3.util.ssl_.DEFAULT_CIPHERS += 'HIGH:!DH:!aNULL'
try:
    requests.packages.urllib3.contrib.pyopenssl.DEFAULT_SSL_CIPHER_LIST += 'HIGH:!DH:!aNULL'
except AttributeError:
    pass


def parse():
    """
    The html parser for get irimo.ir weather details
    Returns a string it have weather details of 32 state of iran 
    """
    session = HTMLSession()
    page = session.get("https://irimo.ir/far/index.php", verify=True)
    divs = page.html.find("div.fr.detail", clean=True, first=True).text
    div = divs.split("آخرین")[0]
    return div


# it's shit part of this program and my brain has going down
