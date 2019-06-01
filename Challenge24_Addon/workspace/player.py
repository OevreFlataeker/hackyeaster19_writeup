#!/usr/bin/env python
#-*- coding: utf-8 -*-
import time
import re
import os
import errno
import sys
sys.dont_write_bytecode = True
import json
import hashlib
import requests
requests.packages.urllib3.disable_warnings()
from PIL import Image
import tensorflow as tf
from numpy import array

cookie_sid = None

def mkdirp(path):
	try: os.makedirs(path)
	except OSError as exc:
		if exc.errno == errno.EEXIST and os.path.isdir(path): pass
		else: raise
		
def cookie_sid_(sess=requests.Session()):
	global cookie_sid
	resp = sess.get("http://whale.hacking-lab.com:3555")
	hdr_cookie = resp.headers["Set-Cookie"]
	m = re.match(r"^sessionId=(eyJhbGciOiJIUzI1Ni[A-Za-z0-9-_\.]+);",hdr_cookie)
	if m: cookie_sid = m.group(1)

def cleanup(prefix):
	filename = "%s.jpg"%prefix
	if os.path.isfile(filename): os.remove(filename)

	for x in range(3):
		for y in range(3):
			filename = "%s-%d-%d.png"%(prefix,x,y)
			if os.path.isfile(filename): os.remove(filename)

# @ https://www.peterbe.com/plog/best-practice-with-retries-with-requests
if __name__ == "__main__":
	with requests.Session() as sess:
		while cookie_sid is None: cookie_sid_(sess)
		prefix = os.path.splitext(os.path.basename(__file__))[0]
		idx,rd,rd_max,solved = 0,0,0,{}
		with tf.gfile.GFile("frozen_inference_graph_ssd_inceptionv2_coco", 'rb') as f:
			graph_def = tf.GraphDef()
			graph_def.ParseFromString(f.read())
			_ = tf.import_graph_def(graph_def, name='')
			with tf.Session() as tf_sess:
				
				while True:
					while True:
						gstart = time.time()
						img_orig = []
						try:
							resp = sess.get("http://whale.hacking-lab.com:3555/picture",headers={"Cookie":"sessionId=%s"%cookie_sid},stream=True)
							if resp.status_code == 400: cookie_sid_(sess)
							resp.raise_for_status()
							filename = "%s.jpg"%prefix
							if os.path.isfile(filename): os.remove(filename)
							with open(filename,"wb") as f:
								for chunk in resp.iter_content(chunk_size=1024):
									if chunk:
										f.write(chunk)
										img_orig.append(chunk)
							break
						except: pass
					gend = time.time()
					print("Get new image took: ", gend-gstart)
					if not os.path.isfile(filename): continue
					#img_orig = "".join(img_orig)
					#print("=>",filename)
					jpg_filename = filename
					img_in = Image.open(filename).convert("RGBA")
					for x in range(3):
						for y in range(3):
							filename = "%s-%d-%d.png"%(prefix,x,y)
							if os.path.isfile(filename): os.remove(filename)
					dim,border = 300,10
					for x in range(3):
						for y in range(3):
							sx,sy = x*(dim+border),y*(dim+border)
							ex,ey = sx+dim,sy+dim
							img_out = img_in.crop((sx,sy,ex,ey))
							filename = "%s-%d-%d.png"%(prefix,x,y)
							img_out.save(filename)
							#print("=>",filename)
					N = 0
					egg = 0
					for x in range(3):
						for y in range(3):
							filename = "%s-%d-%d.png"%(prefix,x,y)							
							start = time.time()
							image_data = Image.open(filename)
							image_data = image_data.convert("RGB")
							image = array(image_data).reshape(1,300,300,3)
							detection_graph = tf_sess.graph
							softmax_tensor = detection_graph.get_tensor_by_name('image_tensor:0')
							boxes = detection_graph.get_tensor_by_name('detection_boxes:0')
							scores = detection_graph.get_tensor_by_name('detection_scores:0')
							classes = detection_graph.get_tensor_by_name('detection_classes:0')
							num_detections = detection_graph.get_tensor_by_name('num_detections:0')
							(boxes, scores, classes, num_detections) = tf_sess.run([boxes, scores, classes, num_detections],feed_dict={softmax_tensor:image})
							end = time.time()
							print(end-start)
							#print(num_detections[0])
							#print(classes[0])
							#print(scores[0])
							for elem in range (int(num_detections[0])):
								if scores[0][elem]>0.9 and classes[0][elem]==1:
									egg+=1
							
							# print "(%d,%d) = %d"%(x,y,len(detections))
							#N += len(detections)
					#print("Found {0} eggs".format(egg))
					resp_txt = None
					while resp_txt is None:
						pbstart = time.time()
						try:
							resp = sess.post("http://whale.hacking-lab.com:3555/verify",
							headers={"Cookie":"sessionId=%s"%cookie_sid,"Content-Type":"application/x-www-form-urlencoded; charset=UTF-8"},data={"s":egg})
							resp_txt = resp.text
						except: resp_txt = None
						pbend = time.time()
						print("Postback time: " , pbend-pbstart)
						#print(resp_txt)
					if resp_txt == "Wrong solution, hobo..." or resp_txt == "Waaay to slow...":
						rd,solved = 0,{}
						# if img_orig:
						# 	basedir = "val"
						# 	mkdirp(basedir)
						# 	filename = "%s.jpg"%hashlib.sha1(img_orig).hexdigest()
						#	filepath = os.path.join(basedir,filename)
						# 	with open(filepath,"wb") as f: f.write(img_orig)
						# 	print "=>",filepath
					else:
						m = re.match(r"^Great success. Round (\d+) solved.",resp_txt)
						if m:
							rd = int(m.group(1))
							rd_max = max(rd_max,rd)
							solved[rd] = {"ans":N,"img":img_orig}
						elif m is None:
							assert resp_txt == "he19-s7Jj-mO4C-rP13-ySsJ"
							if resp_txt.startswith("he19-"):
								print("flag =",resp_txt)
								basedir = "solved"
							mkdirp(basedir)
							for k,v in iter(solved.items()):
								filename = "%02d=%d.jpg"%(k,v["ans"])
								filepath = os.path.join(basedir,filename)
								with open(filepath,"wb") as f: f.write(v["img"])
								print("=>",filepath)
							cleanup(prefix)
							sys.exit()
					print("i=%d max(rd)=%d rd=%d #=%d resp:%s"%(idx,rd_max,rd,egg,resp_txt))
					
					cleanup(prefix)
					idx += 1

