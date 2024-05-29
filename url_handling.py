import validators
import sys

def is_valid_url(url):
    return validators.url(url)

url = input("Enter the URL you would like to make into a QR code: ")
if not is_valid_url(url):
    print("The URL is not valid.")
    sys.exit()
