import sys, os

sys.path.extend([f'./{name}' for name in os.listdir(".") if os.path.isdir(name)])

import detect

from flask import Flask, request 
import base64
import json

  
app = Flask(__name__) #creating the Flask class object   
 
@app.route('/',methods = ['POST'])  
def getAllClasses():
    print(request.form)  
    img_base64 = request.get_json()  
    img = base64.b64decode(img_base64['img'])

    with open('tmp/in.jpg', 'wb') as f:
            f.write(img)
    
    detect.run(weights='weights/best.pt', source='tmp/in.jpg')

    with open('tmp/out.jpg', 'rb') as f:
        x = base64.b64encode(f.read())
    
    x = x.decode('utf-8')

    return json.dumps({'img': x})

if __name__ =='__main__':  
    app.run(debug = True)  