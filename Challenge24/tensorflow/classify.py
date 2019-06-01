#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 26 07:16:04 2018

@author: raghav prabhu
Re-modified TensorFlow classification file according to our need.
"""
from array import array
import tensorflow as tf
import sys
import os
import cv2
import csv
import numpy as np
from utils import label_map_util
from matplotlib import pyplot as plt
from utils import visualization_utils as vis_util
import requests

from PIL import Image
# Disable tensorflow compilation warnings
os.environ['TF_CPP_MIN_LOG_LEVEL']='2'

label_map = label_map_util.load_labelmap("D:\\Tensorflow/workspace/training_demo/annotations/eggs.pbtxt")
categories = label_map_util.convert_label_map_to_categories(label_map, max_num_classes=1, use_display_name=True)
category_index = label_map_util.create_category_index(categories)


def load_image_into_numpy_array(image):
  (im_width, im_height) = image.size
  return np.array(image.getdata()).reshape(
      (im_height, im_width, 3)).astype(np.uint8)

'''// convert OpenCV tensor to TensorFlow tensor
def matToTensor(image: Mat): Tensor = {
  val imageRGB = new Mat
  cvtColor(image, imageRGB, COLOR_BGR2RGB) // convert channels from OpenCV GBR to RGB
  val imgBuffer = imageRGB.createBuffer[ByteBuffer]
  val shape = Shape(1, image.size.height, image.size.width(), image.channels)
  Tensor.fromBuffer(UINT8, shape, imgBuffer.capacity, imgBuffer)
}'''		

'''
Classify images from test folder and predict dog breeds along with score.
'''
def classify_image(sess, fullpath):
    # Loads label file, strips off carriage return
    #label_lines = [line.rstrip() for line
    #               in tf.gfile.GFile("trained_model/retrained_labels.txt")]
   
    # Unpersists graph from file
    #with tf.gfile.FastGFile("trained-inference-graphs\output_inference_graph_v1.pb\\frozen_inference_graph.pb", 'rb') as f:
    # Read the image_data
        #print("Working on ", fullpath)
        #image_data = tf.gfile.GFile("images\\test\\"+image, 'rb').read()
        #image = Image.open("d:\\tensorflow\\workspace\\training_demo\\images\\test_new\\"+img)


        image = Image.open(fullpath)
        #image_np_expanded = np.expand_dims(image_data, axis=0)
        image_np = load_image_into_numpy_array(image) 
        image_np_expanded = np.expand_dims(image_np, axis=0)		
        #print("expanded image...")
        detection_graph = sess.graph
        softmax_tensor = detection_graph.get_tensor_by_name('image_tensor:0')		
        boxes = detection_graph.get_tensor_by_name('detection_boxes:0')
        scores = detection_graph.get_tensor_by_name('detection_scores:0')
        classes = detection_graph.get_tensor_by_name('detection_classes:0')
        num_detections = detection_graph.get_tensor_by_name('num_detections:0')		
        (boxes, scores, classes, num_detections) = sess.run([boxes, scores, classes, num_detections],feed_dict={softmax_tensor:image_np_expanded})
        #print(classes)
        #print(num_detections)
        
		#print(scores)
		# Count scores > 0.1
        cnt = 0
        idx = 0

        for score in scores[0]:            
            if score>0.1:
               cnt+=1
			  
            idx+=1
        #print("Hits: ", cnt)
        
        #vis_util.visualize_boxes_and_labels_on_image_array(image_np,np.squeeze(boxes), np.squeeze(classes).astype(np.int32), np.squeeze(scores), category_index, use_normalized_coordinates=True,line_thickness=2, min_score_thresh=0.01)
        #cv2.imshow(img,image_np)
        #cv2.imwrite(fullpath+"_proc.jpg",image_np)
        return(cnt)
		# Feed the image_data as input to the graph and get first prediction
        
'''
        predictions = sess.run(softmax_tensor, {'DecodeJpeg/contents:0': image_data})

		# Sort to show labels of first prediction in order of confidence
        top_k = predictions[0].argsort()[-len(predictions[0]):][::-1]
        records = []
        row_dict = {}
        head, tail = os.path.split(file)
        row_dict['id'] = tail.split('.')[0]

        for node_id in top_k:			
			# Some breed names are mismatching with breed name in csv header names.
			
           score = predictions[0][node_id]			
           print(score)
        records.append(row_dict.copy())
	'''		
    #f.close()    
#26: 22 eggs
#27: 23 eggs
#28: 23 eggs
#29: 32 eggs
#30: 31 eggs
def main():
    #with tf.gfile.GFile("pre-trained-model\\frozen_inference_graph.pb", 'rb') as f:
    #with tf.gfile.GFile("D:\\Tensorflow\\workspace\\training_demo\\trained-inference-graphs\\output_inference_graph_v8.pb\\frozen_inference_graph.pb", 'rb') as f:
    with tf.gfile.GFile(
                "D:\\Tensorflow\\workspace\\training_demo\\trained-inference-graphs\\final_egg.pb\\frozen_inference_graph.pb",
                'rb') as f:
    #with tf.gfile.GFile(
     #       "D:\\retrained_graph.pb",
      #      'rb') as f:
        graph_def = tf.GraphDef()
        graph_def.ParseFromString(f.read())
        _ = tf.import_graph_def(graph_def, name='')
        with tf.Session() as sess:
           '''test_data_folder = 'D:\\Tensorflow\\workspace\\training_demo\\images\\test_new'
           #get fieldnames from DictReader object and store in list
           for r,d,f in os.walk(test_data_folder):
              for file in f:          
                 if '.jpg' in file:
                    print("Classifying ", file)
                    classify_image(sess,file)
            '''
            # Play the game
           #proxies = {
           #    'http': 'http://127.0.0.1:8080',
           #    'https': 'http://127.0.0.1:8080',
           #}
           proxies = None
           mainpage_req = requests.get('http://whale.hacking-lab.com:3555/', proxies=proxies)

           max_correct = 0
           correct = 0
           # Hot start
           classify_image(sess,"start.jpg")
           i = 0
           while True:
               i=i+1
           #for i in range(1, 200):
               p_res = requests.get('http://whale.hacking-lab.com:3555/picture', cookies=mainpage_req.cookies,
                                    proxies=proxies, stream=True)
               le_image = p_res.content # The image
               afile = open(str(i)+".jpg","wb")
               afile.write(le_image)
               afile.close()
               cnt = classify_image(sess,str(i)+".jpg")
               payload = {'s': cnt}
               r = requests.post('http://whale.hacking-lab.com:3555/verify', data=payload, proxies=proxies,
                                 cookies=mainpage_req.cookies)
               print(r.text)
               if ("Wrong solution" in r.text):
                   correct = 0
                   print("Max correct: ", max_correct)
                   #afile = open(str(i) + "_wrong.jpg", "wb")
                   #afile.write(le_image)
                   #afile.close()
               else:
                   correct+=1
                   if correct > max_correct:
                       max_correct = correct
               os.remove(str(i)+".jpg")
if __name__ == '__main__':
    main()
