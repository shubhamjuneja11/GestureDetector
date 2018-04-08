import threading
import time
import cv2
import numpy as np
import os, sys
import tensorflow as tf
from DisplayText import DisplayText
image_path = "./a.jpeg"
thresh1=1
img=1
# Maybe I need threading here, just a reminder threading.Thread
class GestureDetector():
    def __init__(self):
        #threading.Thread.__init__(self)
        self.c = 0
        print('GestureDetection initiated')
        self.displayText = DisplayText()
    '''def run(self):
        self.RunCamera()
        '''

    def RunCamera(self):
        cap = cv2.VideoCapture(0)
        backgroundSubtractor = cv2.createBackgroundSubtractorMOG2()
        while (cap.isOpened()):
            ret, img = cap.read()
            subtractedBackgroundImage = backgroundSubtractor.apply(img)
            cv2.imshow('image', subtractedBackgroundImage)
            cv2.imwrite("a.jpeg", img)
            k = cv2.waitKey(10)
            if k == 27:
                break
            self.c+=1
            # Slow detection rate, processor can't handle for 100 after 6-7 detections, totally fucked up after that
            if(self.c%200==0):
                self.RunGraph()


    def RunGraph(self):
        image_data = tf.gfile.FastGFile(image_path, 'rb').read()
        label_lines = [line.rstrip() for line
                       in tf.gfile.GFile("./graph_files/output_labels.txt")]
        with tf.gfile.FastGFile("./graph_files/output_graph.pb", 'rb') as f:
            graph_def = tf.GraphDef()
            graph_def.ParseFromString(f.read())
            tf.import_graph_def(graph_def, name='')
        with tf.Session() as sess:
            softmax_tensor = sess.graph.get_tensor_by_name('final_result:0')
            predictions = sess.run(softmax_tensor,{'DecodeJpeg/contents:0': image_data})
            top_k = predictions[0].argsort()[-len(predictions[0]):][::-1]
            guess = label_lines[top_k[0]]
            cv2.imshow('Gesture', img)
            cv2.imshow('Thresholded', thresh1)
            self.displayText.display(" Gesture Detected - "+guess)
            print(guess)

    def StartDetection(self):
        self.RunCamera()
