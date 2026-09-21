# Go to terminal and write command pip install 
# Copy Below code

import qrcode

url= input("Enter Your url: ")
file_path=" "                    # Enter your file path to store QR code png

qr=qrcode.QRCode()
qr.add_data(url)

img=qr.make_image()
img.save(file_path)

print("QR code is generated")