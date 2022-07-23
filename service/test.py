import base64
import requests

with open("/home/leon3428/Pictures/test.jpeg", "rb") as img_file:
    my_string = base64.b64encode(img_file.read())
my_string = my_string.decode('utf-8')

print(my_string)

url = 'http://127.0.0.1:5000/'
myobj = {'img': my_string}

x = requests.post(url, json = myobj)

print(x.text)