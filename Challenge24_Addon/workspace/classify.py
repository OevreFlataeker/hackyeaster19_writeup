#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#from array import array
import tensorflow as tf
import sys
import os
import cv2
import csv
import numpy as np
from numpy import array
from PIL import Image
# Disable tensorflow compilation warnings
os.environ['TF_CPP_MIN_LOG_LEVEL']='2'

def load_image_into_numpy_array(image):
  (im_width, im_height) = image.size
  return np.array(image.getdata()).reshape(
      (1,im_height, im_width, 3)).astype(np.uint8)

def classify_image(sess, image):    
        print("Working on images/verification/{0}".format(image))
        image_data = Image.open("images/verification/"+image)
        image_data = image_data.convert("RGB")
        image = array(image_data).reshape(1,300,300,3)
#        image_np_expanded = load_image_into_numpy_array(image_data)        
        detection_graph = sess.graph
        softmax_tensor = detection_graph.get_tensor_by_name('image_tensor:0')		
        boxes = detection_graph.get_tensor_by_name('detection_boxes:0')
        scores = detection_graph.get_tensor_by_name('detection_scores:0')
        classes = detection_graph.get_tensor_by_name('detection_classes:0')
        num_detections = detection_graph.get_tensor_by_name('num_detections:0')		
        (boxes, scores, classes, num_detections) = sess.run([boxes, scores, classes, num_detections],feed_dict={softmax_tensor:image})
#        print(classes)
#        print(scores)
#        print(num_detections)
        egg = 0
        for idx in range (int(num_detections[0])):
                 if scores[0][idx]>0.9 and classes[0][idx]==1:
                       egg+=1
        print("Found {0} eggs".format(egg))
def main():
    with tf.gfile.GFile("inference_graph/frozen_inference_graph.pb", 'rb') as f:
        graph_def = tf.GraphDef()
        graph_def.ParseFromString(f.read())
        _ = tf.import_graph_def(graph_def, name='')
        with tf.Session() as sess:
           test_data_folder = 'images/verification'    
           #get fieldnames from DictReader object and store in list
           for r,d,f in os.walk(test_data_folder):
              for file in f:          
                 if '.png' in file:
                    print("Classifying ", file)
                    classify_image(sess,file)
    

if __name__ == '__main__':
    main()
