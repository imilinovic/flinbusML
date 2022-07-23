import sys, os

sys.path.extend([f'./{name}' for name in os.listdir(".") if os.path.isdir(name)])

import my_detect

from flask import Flask, request 
import base64
import json

import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt
  
app = Flask(__name__) #creating the Flask class object   
 
@app.route('/yolo',methods = ['POST'])  
def getAllClasses():
    print(request.form)  
    img_base64 = request.get_json()  
    img = base64.b64decode(img_base64['img'])

    with open('tmp/in.jpg', 'wb') as f:
            f.write(img)
    
    my_detect.run(weights='weights/best.pt', source='tmp/in.jpg')

    with open('tmp/out.jpg', 'rb') as f:
        x = base64.b64encode(f.read())
    
    x = x.decode('utf-8')

    return json.dumps({'img': x})

@app.route('/match',methods = ['POST'])  
def match():
    data = request.get_json()  
    img1 = base64.b64decode(data['img1'])
    img2 = base64.b64decode(data['img2'])

    img1 = np.asarray(bytearray(img1), dtype="uint8")
    img2 = np.asarray(bytearray(img2), dtype="uint8")

    img1 = cv.imdecode(img1,cv.IMREAD_GRAYSCALE)
    img2 = cv.imdecode(img2,cv.IMREAD_GRAYSCALE)

    orb = cv.ORB_create()
    # find the keypoints and descriptors with ORB
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # create BFMatcher object
    bf = cv.BFMatcher(cv.NORM_HAMMING, crossCheck=True)
    # Match descriptors.
    matches = bf.match(des1,des2)
    # Sort them in the order of their distance.

    filtered = []

    for match in matches:
        if match.distance < 35:
                filtered.append(match)

    if(len(filtered) > 10):
        res = True
    else:
        res = False

    return json.dumps({'res': res})

if __name__ =='__main__':  
    app.run(debug = True)  