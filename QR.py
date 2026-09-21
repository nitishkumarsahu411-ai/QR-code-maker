import qrcode

url= input("Enter Your url: ")
file_path="C:\\Users\\HP\\Videos\\figma\\Linkdin qr code"

qr=qrcode.QRCode()
qr.add_data(url)

img=qr.make_image()
img.save(file_path)

print("QR code is generated")