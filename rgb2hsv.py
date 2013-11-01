#!/usr/bin/env python
# coding: utf-8
import os
import numpy
import cv2

imagename = "img/red_square.jpg"

# 画像読み込み
imagedata = cv2.imread(imagename)
imageheight, imagewidth = imagedata.shape[:2]
    
the_number_of_pixel = imageheight * imagewidth

# RGB の値
r_value = imagedata[:,:,2]
g_value = imagedata[:,:,1]
b_value = imagedata[:,:,0]

# GRBからHSVに変換
hsvdata = cv2.cvtColor(imagedata, cv2.COLOR_BGR2HSV)

# HSV の値
h_value = hsvdata[:,:,0]
s_value = hsvdata[:,:,1]
v_value = hsvdata[:,:,2]

# 各値の平均値
mean_b = numpy.mean(b_value)
mean_g = numpy.mean(g_value)
mean_r = numpy.mean(r_value)
mean_h = numpy.mean(h_value)
mean_s = numpy.mean(s_value)
mean_v = numpy.mean(v_value)

print "R = " + str(mean_r), "G = " + str(mean_g), "B = " + str(mean_b)
print "H = " + str(mean_h), "S = " + str(mean_s), "V = " + str(mean_v)
