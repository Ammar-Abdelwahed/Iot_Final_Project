#!/usr/bin/env python
# coding: utf-8

# In[1]:


import picamera
from firebase_admin import credentials, initialize_app, storage
import os

# Create an instance of the PiCamera class
camera = picamera.PiCamera()

# Capture an image
camera.capture('/home/pi/Desktop/image.jpg')

cred = credentials.Certificate("home/pi/assignment-b6cec-firebase-adminsdk-scrag-753d1b4e7c.json")
initialize_app(cred, {'storageBucket': 'assignment-b6cec.appspot.com'})

fileName = '/home/pi/Desktop/image.jpg'
bucket = storage.bucket()
blob = bucket.blob(fileName)
blob.upload_from_filename(fileName)
blob.make_public()


# In[ ]:




