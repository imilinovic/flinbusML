import base64
import requests

with open("/home/leon3428/Pictures/test1.jpg", "rb") as img_file:
    img1 = base64.b64encode(img_file.read())
img1 = img1.decode('utf-8')

with open("/home/leon3428/Pictures/test2.jpg", "rb") as img_file:
    img2 = base64.b64encode(img_file.read())
img2 = img2.decode('utf-8')


url = 'http://127.0.0.1:5000/match'
myobj = {'img1': img1, 'img2': img2}

x = requests.post(url, json = myobj)

print(x.text)