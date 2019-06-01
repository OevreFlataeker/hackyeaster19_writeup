Install TF on Linux/Windows
* IMPORTANT *

Whenever you "git pull" e.g. the “object_detection” repo you HAVE to recreate the protobuf definitions! See: https://tensorflow-object-detection-api-tutorial.readthedocs.io/en/latest/install.html –> “Protobuf Installation/Compilation”

or just:

Windows:

# From within TensorFlow/models/research/
for /f %i in ('dir /b object_detection\protos\*.proto') do protoc object_detection\protos\%i --python_out=.

Linux:

cd /tmp/workspace/models/research
protoc object_detection/protos/*.proto --python_out .


Assumption: All action happens in /tmp/workspace

0) Install CUDA on Linux.

Use the deb package from the NVIDIA Download page to do so.

https://developer.nvidia.com/cuda-downloads?target_os=Linux&target_arch=x86_64&target_distro=Ubuntu&target_version=1604&target_type=deblocal

You can use the latest and greatest for your overall installation. Follow the setup instructions on the NVIDIA Homepage:

`sudo dpkg -i cuda-repo-ubuntu1604-10-1-local-10.1.168-418.67_1.0-1_amd64.deb`
`sudo apt-key add /var/cuda-repo-<version>/7fa2af80.pub`
`sudo apt-get update`
`sudo apt-get install cuda`
Then we will side-by-side install CUDA 10.0, because TF does not support 10.1 yet.

Delete the sym-link /usr/local/cuda.

Then download the v10.0 of CUA but use type “runfile (local)”. Run it and install to /usr/local/cuda-10.0

Do NOT choose to install the driver. CUDA 10.0 can also use the driver of CUDA 10.1! When finished install CUDNN package for the corresponding CUDA version as well (separate download). CUDNN is just a include and lib file that can be copied into /usr/local/cuda-10.0/include and /usr/local/cuda-10.0/lib64 respectively.

1) Install anaconda

2) Generate a new env:

conda create --name tf_cu10" (or similar)
3) Install requirements

conda install tensorflow-gpu pandas matplotlib pillow

(Replace tensorflow-gpu with tensorflow if you need to train on CPU! conda SHOULD take care of all relevant 3rd party libs like the compatible cuda-10.0. This means that even if you installed CUDA 10.0 side-by-side above, conda will probably install (most) of it again)

4) Download Tensorflow model repo:

https://github.com/tensorflow/models/archive/master.zip, unzip and rename directory from “models-master” to “models” and copy to /tmp/workspace

5) mkdir /tmp/workspace/training

6) Compile protobufs

 cd /tmp/workspace/models/research
 protoc object_detection/protos/*.proto --python_out .

 /*
 Windows: 
 You might need to download the binary from https://github.com/protocolbuffers/protobuf/releases/download/v3.8.0/protoc-3.8.0-win64.zip if it was not properly supplied by conda!
 Call is different on Windows due to "*" operator!
 # From within TensorFlow/models/research/
 for /f %i in ('dir /b object_detection\protos\*.proto') do protoc object_detection\protos\%i --python_out=.
 */

7) Let's try the training with RCNN resnet101-Kitti! Others surely work as well but no guarantee everything runs smoothly here-after! Some models are outdated and not 100% compatible with the lastest tf version!
(Update: faster_rcnn_resnet101_kitti_2018_01_28 is actually much to slow for our use case. Please better download ssd_mobilenetv2_coco... from the model zoo page below!)

Download the following model from:

8) https://github.com/tensorflow/models/blob/master/research/object_detection/g3doc/detection_model_zoo.md

 faster_rcnn_resnet101_kitti_2018_01_28.tar.gz (http://download.tensorflow.org/models/object_detection/faster_rcnn_resnet101_kitti_2018_01_28.tar.gz)
 unpack as /tmp/workspace/pre-trained-model 
 
9) Create a conda activate script to set pythonpath, etc.

 /*
 Windows:
 Just "set PYTHONPATH=...." or look for a persistent solution yourself (bat file, whatever...)
 */
 vi ~/.conda/envs/tf_cu10/etc/conda/activate.d/activate.sh (You might need to create the path structure first!)
 # Adapt all paths accordingly!
#!/bin/sh
ORIGINAL_LD_LIBRARY_PATH=$LD_LIBRARY_PATH
ORIGINAL_PATH=$PATH
ORIGINAL_PYTHONPATH=$PYTHONPATH
export LD_LIBRARY_PATH=/usr/local/cuda-10.0/lib64:/usr/local/cuda-10.0/extras/CUPTI/lib64:/lib/nccl/cuda-10:$LD_LIBRARY_PATH
export PATH=/usr/local/cuda-10.0/bin:$PATH
export PYTHONPATH=/tmp/workspace/models/research/object_detection:/tmp/workspace/models/research/slim
echo Configured LD_LIBRARY_PATH and PATH to /usr/local/cuda-10/ and PYTHONPATH to TF object_detection folders
vi ~/.conda/envs/tf_cu10/etc/conda/deactivate.d/deactivate.sh (You might need to create the path structure first!)
# Adapt all paths accordingly!

#!/bin/sh
 
export LD_LIBRARY_PATH=$ORIGINAL_LD_LIBRARY_PATH
unset ORIGINAL_LD_LIBRARY_PATH
export PATH=$ORIGINAL_PATH
unset ORIGINAL_PATH
export PYTHONPATH=$ORIGINAL_PYTHONPATH
unset ORIGINAL_PYTHONPATH
echo Reset LD_LIBRARY_PATH, PATH and PYTHONPATH to original path

10) Build “Object detection” stuff

cd /tmp/workspace/models/research
python setup.py build     <-- MANDATORY!!!
python setup.py install   <-- MANDATORY!!! Also on Windows an "install" has to be done! Otherwise all subsequent calls fail!

11) Download Training tools:

wget https://raw.githubusercontent.com/douglasrizzo/detection_util_scripts/master/generate_csv.py
wget https://raw.githubusercontent.com/datitran/raccoon_dataset/master/generate_tfrecord.py

12) Create this diff file (ONLY VALID FOR THESE TRAINING IMAGES THAT HAVE MORE THAN 1 LABEL AND ARE OF TYPE PNG!! Adapt accordingly to your image setup)

32c32
<     if row_label == 'raccoon':
---
>     if row_label == 'egg':
33a34,51
>     elif row_label == 'badge':
>         return 2
>     elif row_label == 'lock':
>         return 3
>     elif row_label == 'rubik':dir
>         return 4
>     elif row_label == 'bunny':
>         return 5
>     elif row_label == 'ball':
>         return 6
>     elif row_label == 'dog':
>         return 7
>     elif row_label == 'handheld':
>         return 8
>     elif row_label == 'piggy':
>         return 9
>     elif row_label == 'eggw':
>         return 10
34a53
>         print("Undefined row_label!", row_label)
52c71
<     image_format = b'jpg'
---
>     image_format = b'png'
A

/* Alternative: Just differentiate between 1 (our egg) and everything else (“0”)

def class_text_to_int(row_label):
    if row_label == "egg":  # 'ship':
        return 1
    else:
    	return 0
		
13) Generate TF records

python3 generate_csv.py xml images/train/ train.csv
python3 generate_csv.py xml images/test/ test.csv
FULL PATHNAMES MANDATORY!

python generate_tfrecord.py --csv_input=/tmp/workspace/train.csv --output_path=/tmp/workspace/train.tfrecord --image_dir=/tmp/workspace/images/train/
python generate_tfrecord.py --csv_input=/tmp/workspace/test.csv --output_path=/tmp/workspace/test.tfrecord --image_dir=/tmp/workspace/images/test/
You should have now:

-rw-rw-r-- 1 daubsi daubsi      2955 May 29 09:07 generate_csv.py
-rw-rw-r-- 1 daubsi daubsi      3856 May 29 10:18 generate_tfrecord.py
-rw-rw-r-- 1 daubsi daubsi       671 May 29 10:21 generate_tfrecord.py.diff
drwxrwxr-x 4 daubsi daubsi     98304 May 29 09:15 images
drwxrwxr-x 6 daubsi daubsi      4096 May 29 09:22 models
drwxr-xr-x 3 daubsi daubsi      4096 Feb  1  2018 pre-trained-model
-rw-rw-r-- 1 daubsi daubsi     20746 May 29 09:21 test.csv
-rw-rw-r-- 1 daubsi daubsi  15985366 May 29 10:22 test.tfrecord
-rw-rw-r-- 1 daubsi daubsi    104172 May 29 09:21 train.csv
-rw-rw-r-- 1 daubsi daubsi  84519078 May 29 10:18 train.tfrecord
 
* Step 13 has to be repeated everytime you add/change the pictures *

14) Generate a file “label.pbtxt” in /tmp/workspace:

item {
        id: 1
        name: 'egg'
}
 
item {
        id: 2
        name: 'badge'
}
 
item {
        id: 3
        name: 'lock'
}
 
item {
        id: 4
        name: 'rubik'
}
 
item {
        id: 5
        name: 'bunny'
}
 
item {
        id: 6
        name: 'ball'
}
 
item {
        id: 7
        name: 'dog'
}
 
item {
        id: 8
        name: 'handheld'
}
 
item {
        id: 9
        name: 'piggy'
}
 
item {
        id: 10
        name: 'eggw'
}
14) Change the pipeline.config in directory “pre-trained-model”:

num_classes: X → 10 (Or just 1 or 2 depending on the approach during tfrecord generation!)

In section “train_config”, keyword “fine_tune_checkpoint” change value to “/tmp/workspace/pre-trained-model/model.ckpt” (This path defined where the pre-trained-model resides that should be loaded. We will specify a training folder on the command line later on. For the initial run we will initialize from the pre-trained-model our model, then later-on if we CTRL+C and restart the training TF will load the last checkpoint from the "training" folder not from the "pre-trained-model" folder!

Value “num_steps” - set to e.g. 100000 or leave at default (depends on model used!)

Section:

train_input_reader {
  label_map_path: "/tmp/workspace/label.pbtxt"
  tf_record_input_reader {
    input_path: "/tmp/workspace/train.tfrecord"
  }
}
eval_config {
  num_examples: 500
  metrics_set: "coco_metrics"	
  use_moving_averages: false
}
eval_input_reader {
  label_map_path: "/tmp/workspace/label.pbtxt"
  tf_record_input_reader {
    input_path: "/tmp/workspace/test.tfrecord"
  }
}
Section: “Learning rate” Check whether there is a “step: 0” somewhere and change to “step: 1”, otherwise a ValueError will be thrown when training starts. This is because there were some changes since when the model was released and tensorflow updates.

Example:

learning_rate {
        manual_step_learning_rate {
          initial_learning_rate: 9.99999974738e-05
          schedule {
            step: 0 <--- Change this one to 1!
            learning_rate: 9.99999974738e-05
          }
          schedule {
            step: 500000
            learning_rate: 9.99999974738e-06
          }
          schedule {
            step: 700000
            learning_rate: 9.99999997475e-07
          }
        }
      }
15) Install pycocotools

pip install pycocotools
/* Windows: –> This call fails on Windows! Incompatibility Makefile↔Visual Studio! https://github.com/cocodataset/cocoapi/issues/169 Do this here (Windows only!)

conda install git
pip3 install "git+https://github.com/philferriere/cocoapi.git#egg=pycocotools&subdirectory=PythonAPI"
*/

16) Change model_main.py to log more info:

cd /tmp/workspace
In file

models/research/object_detection/model_main.py 
insert this line around line 58 (after the imports and define stuff)

tf.logging.set_verbosity(tf.logging.INFO)

17) Train! Do it!

python models/research/object_detection/model_main.py --pipeline_config_path=pre-trained-model/pipeline.config --model_dir=training --num_train_steps=100000

18) Open 2nd Terminal

conda activate tf_cu10
tensorboard --host 127.0.0.1 --logdir=/tmp/workspace/training
Point browser to 127.0.0.1:6006

18) Create inference graph when done

I trained for about 23.000 steps and had very good results already with this model. Before we can use the graph for anything we need to “freeze” it. This can be done using this command

python models/research/object_detection/export_inference_graph.py --input_type image_tensor --pipeline_config_path pre-trained-model/pipeline.config --trained_checkpoint_prefix training/model.ckpt-23542 --output_directory inference_graph

Replace model.ckpt-23542 with the biggest number in your training folder!

19) Check with classify.py We can classify an image via this adhoc program

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
It will take all the pictures from the images/verification folder.

20) Get the flag

The script player.py plays the game and shows how to use it for getting the flag in challenge 24 of HE19.
It expects the frozen model in "inference_graph/frozen_inference_graph.pb"

 
Add-On:

These two files can be used to download new images and make a verification set from them (by courtesy of Evandrix! Thanks mate!)

00-download.py:

#!/usr/bin/env python
#-*- coding: utf-8 -*-
 
import re
import os
import errno
import sys
sys.dont_write_bytecode = True
import hashlib
import requests
requests.packages.urllib3.disable_warnings()
from util import *
 
def download(basedir,N=100):
	mkdirp(basedir)
	for i in range(N):
		sess = requests.Session()
		resp = sess.get("http://whale.hacking-lab.com:3555")
		hdr_cookie = resp.headers.get("Set-Cookie",None)
		m = re.match(r"^sessionId=(eyJhbGciOiJIUzI1Ni[A-Za-z0-9-_\.]+);",hdr_cookie)
		if m:
			cookie_sid = m.group(1)
			resp = sess.get("http://whale.hacking-lab.com:3555/picture",
				headers={"Cookie":"sessionId=%s"%cookie_sid},stream=False)
			# if resp.status_code == 400: cookie_sid_(sess)
			# resp.raise_for_status()
			content = resp.content
			filename = "%s.jpg"%hashlib.sha1(content).hexdigest()
			filepath = os.path.join(basedir,filename)
			# if os.path.isfile(filepath): os.remove(filepath)
			# for chunk in resp.iter_content(chunk_size=1024): pass
			with open(filepath,"wb") as f: f.write(content)
			print (i+1),"=>",filepath
		sess.close()
 
if __name__ == "__main__": download("0-download",int(sys.argv[1]))

01-crop:

#!/usr/bin/env python
#-*- coding: utf-8 -*-
 
import sys
sys.dont_write_bytecode = True
import io
import hashlib
from PIL import Image
from util import *
 
def crop(indir,outdir):
	DIM,BORDER = 300,10
	W = H = 3
	mkdirp(outdir)
	for item in filelist(indir,".jpg"):
		filepath = item["filepath"]
		img_in = Image.open(filepath).convert("RGBA")
		for x in range(W):
			for y in range(H):
				sx,sy = x*(DIM+BORDER),y*(DIM+BORDER)
				ex,ey = sx+DIM,sy+DIM
				img_out = img_in.crop((sx,sy,ex,ey))
				img_out_bs = io.BytesIO()
				img_out.save(img_out_bs,format="PNG") # "JPEG"
				img_out_bs = img_out_bs.getvalue()
				outfile = "%s.png"%hashlib.sha1(img_out_bs).hexdigest()
				outpath = os.path.join(outdir,outfile)
				if not os.path.isfile(outpath):
					img_out.save(outpath)
					print(item["filename"],"(%d,%d)"%(x,y),"=>",outpath)
 
if __name__ == "__main__": crop("0-download","1-crop")
util.py:

#!/usr/bin/env python
#-*- coding: utf-8 -*-
 
import os
import errno
import sys
sys.dont_write_bytecode = True
import contextlib
 
@contextlib.contextmanager
def stdout_redirect(to=os.devnull):
	fd = sys.stdout.fileno()
	def _redirect_stdout(to):
		sys.stdout.close()
		os.dup2(to.fileno(),fd)
		sys.stdout = os.fdopen(fd,"w")
	with os.fdopen(os.dup(fd),"w") as old_stdout:
		with open(to,"w") as file: _redirect_stdout(to=file)
		try: yield
		finally: _redirect_stdout(to=old_stdout)
 
@contextlib.contextmanager
def stderr_redirect(to=os.devnull):
	fd = sys.stderr.fileno()
	def _redirect_stderr(to):
		sys.stderr.close()
		os.dup2(to.fileno(),fd)
		sys.stderr = os.fdopen(fd,"w")
	with os.fdopen(os.dup(fd),"w") as old_stderr:
		with open(to,"w") as file: _redirect_stderr(to=file)
		try: yield
		finally: _redirect_stderr(to=old_stderr)
 
def mkdirp(path):
	try: os.makedirs(path)
	except OSError as exc:
		if exc.errno == errno.EEXIST and os.path.isdir(path): pass
		else: raise
 
def filelist(basedir,filter_ext):
	assert filter_ext.startswith(".")
	for root,dirs,files in os.walk(basedir):
		for filename in files:
			filename = os.path.basename(filename)
			prefix,ext = os.path.splitext(filename)
			if ext == filter_ext:
				filepath = os.path.join(root,filename)
				yield {"basedir":root,"basename":prefix,"ext":ext,"filename":filename,"filepath":filepath}