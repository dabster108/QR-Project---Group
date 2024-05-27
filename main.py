import qrcode as qr
import customization
from url_handling import url

def user_view(user_input):
    if user_input == "default" or user_input == "d":
        fill_color = "black"
        background_color = "white"
    else:
        fill_color = input("Enter fill color you want which is stripes or lines: ") 
        background_color = input("Enter background color you want for the QR code: ")
        
    return fill_color, background_color

user_input = input("Do you want to use default colors for the QR code? (yes/no or d for default): ")
fill_color, background_color = user_view(user_input)
img = qr.make(url)
customization.customization(url, fill_color, background_color)

