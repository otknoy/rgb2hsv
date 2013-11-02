#!/usr/bin/env python
# coding: utf-8
import os
import numpy
import cv2

imagename = "img/red_square.jpg"

# 画像読み込み
imagedata = cv2.imread(imagename)

# GRBからHSVに変換
hsvdata = cv2.cvtColor(imagedata, cv2.COLOR_BGR2HSV)

# 各値の平均値
mean_b, mean_g, mean_r = [e.mean() for e in imagedata.transpose()]
mean_h, mean_s, mean_v = [e.mean() for e in hsvdata.transpose()]

print "R = " + str(mean_r), "G = " + str(mean_g), "B = " + str(mean_b)
print "H = " + str(mean_h), "S = " + str(mean_s), "V = " + str(mean_v)
