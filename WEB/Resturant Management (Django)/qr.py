import qrcode


url_website = ""
image = qrcode.make(url_website)
image.save("qr.png")

