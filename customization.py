import qrcode
import qrcode.constants

def customization(url, fill_color, background_color):
    qr = qrcode.QRCode(version=1,
                       error_correction=qrcode.constants.ERROR_CORRECT_L,
                       box_size=20,
                       border=2)
    
    qr.add_data(url)
    qr.make(fit=True)
   
    img = qr.make_image(fill_color=fill_color, back_color=background_color)
    img.save("save_code.png") 