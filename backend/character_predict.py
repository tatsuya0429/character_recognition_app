import cv2
import numpy as np
import base64
import joblib

def predict(image):
  clf = joblib.load('digits.pkl')
  header, encoded = image.split(',', 1)
  img_bin = base64.b64decode(encoded)
  img = np.frombuffer(img_bin, dtype=np.uint8)
  img = cv2.imdecode(img, cv2.IMREAD_GRAYSCALE)
  img = cv2.resize(img, (8, 8))
  img = 15 - img
  img = img.reshape((-1, 64))
  res = clf.predict(img)
  print(res[0])
  return res[0]