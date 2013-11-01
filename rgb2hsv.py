#!/usr/bin/env python
# coding: utf-8

import os
import numpy
import cv2

def average(total, num):
    return total / num

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
mean_b = average(b_value.sum(), the_number_of_pixel)
mean_g = average(g_value.sum(), the_number_of_pixel)
mean_r = average(r_value.sum(), the_number_of_pixel)
mean_h = average(h_value.sum(), the_number_of_pixel)
mean_s = average(s_value.sum(), the_number_of_pixel)
mean_v = average(v_value.sum(), the_number_of_pixel)

print "R = " + str(mean_r), "G = " + str(mean_g), "B = " + str(mean_b)
print "H = " + str(mean_h), "S = " + str(mean_s), "V = " + str(mean_v)
