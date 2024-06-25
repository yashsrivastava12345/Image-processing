import base64 
with open("New Folder/1.jpeg", "rb") as image2string: 
	converted_string = base64.b64encode(image2string.read())

import qrcode
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=2,
    border=8,
)
qr.add_data("My Data")
qr.make()
img = qr.make_image(fill_color="black", back_color="white")
img.save("qrcode.png")
"""import base64 
with open("New Folder/1.jpeg", "rb") as image2string: 
	converted_string = base64.b64encode(image2string.read())

import qrcode
qr = qrcode.QRCode(version=1, box_size=10, border=5)
data = converted_string.decode('utf-8')
qr.add_data(data)
print(converted_string.decode('utf-8'))
qr.make(fit=True)
img = qr.make_image(fill_color="black", back_color="white")
img.save("qrcode.png")"""
"""with open('encode.bin', "wb") as file: 
	file.write(converted_string)

file = open('encode.bin', 'rb') 
byte = file.read() 
file.close() 

decodeit = open('hello_level.jpeg', 'wb') 
decodeit.write(base64.b64decode((byte))) 
decodeit.close() """
