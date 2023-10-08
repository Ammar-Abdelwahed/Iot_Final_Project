#!/usr/bin/env python
# coding: utf-8

# In[1]:


import cv2
import numpy as np
import math
import time


# In[2]:


def canny(img):
    gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    kernel = 5
    blur = cv2.GaussianBlur(gray,(kernel, kernel),0)
    canny = cv2.Canny(gray, 30, 100)
    return canny


# In[3]:


def region_of_interest(canny):
    height = canny.shape[0]
    width = canny.shape[1]
    mask = np.zeros_like(canny)

    poly = np.array([[
        (0, height),
        (0, 200),
        (450, 200),
        (600, height),
    ]], np.int32)

    cv2.fillPoly(mask, poly, 255)
    masked_image = cv2.bitwise_and(canny, mask)
    return masked_image


# In[4]:


def display_lines(img,lines):
    line_image = np.zeros_like(img)
    if lines is not None:
        for line in lines:
            for x1, y1, x2, y2 in line:
                cv2.line(line_image,(x1,y1),(x2,y2),(255,0,0),10)
    return line_image


# In[5]:


def calculate_central_line(image, lines):
    if lines is None:
        return None
    central_line = [0, 0, 0, 0]
    for line in lines:
        if line is not None:
            for point in line:
                central_line = [int((a + b) / 2) for a, b in zip(central_line, point)]
    return central_line


# In[6]:


def display_central_line(image, line):
    if lines is None:
        return None
    line_image = np.zeros_like(image)
    cv2.line(line_image, (line[0], line[1]), (line[2], line[3]), (255,0,0), 10)
    return line_image


# In[7]:


def make_points(image, line):
    slope, intercept = line
    y1 = int(image.shape[0])
    y2 = int(y1*1/4)
    x1 = int((y1 - intercept)/slope)
    x2 = int((y2 - intercept)/slope)
    return [[x1, y1, x2, y2]]


# In[8]:


def average_slope_intercept(image, lines):
    left_fit    = []
    right_fit   = []
    if lines is None:
        return None
    for line in lines:
        for x1, y1, x2, y2 in line:
            fit = np.polyfit((x1,x2), (y1,y2), 1)
            slope = fit[0]
            intercept = fit[1]
            if slope < 0:
                left_fit.append((slope, intercept))
            else:
                right_fit.append((slope, intercept))
    # add more weight to longer lines
    left_fit_average  = np.average(left_fit, axis=0)
    right_fit_average = np.average(right_fit, axis=0)
    time.sleep(0.2)
    print('left {}'.format(np.rad2deg(np.arctan(left_fit_average[0]))))
    print('right {}'.format(np.rad2deg(np.arctan(right_fit_average[0]))))
    left_line  = make_points(image, left_fit_average)
    right_line = make_points(image, right_fit_average)
    averaged_lines = [left_line, right_line]
    return averaged_lines


# In[9]:


def compute_steering_angle(frame, lane_lines):
    if len(lane_lines) == 0:
        return -90

    height, width, _ = frame.shape
    if len(lane_lines) == 1:
        x1, _, x2, _ = lane_lines[0][0]
        x_offset = x2 - x1
    else:
        _, _, left_x2, _ = lane_lines[0][0]
        _, _, right_x2, _ = lane_lines[1][0]
        camera_mid_offset_percent = 0.02
        mid = int(width / 2 * (1 + camera_mid_offset_percent))
        x_offset = (left_x2 + right_x2) / 2 - mid

    y_offset = int(height / 2)

    angle_to_mid_radian = math.atan(x_offset / y_offset)
    angle_to_mid_deg = int(angle_to_mid_radian * 180.0 / math.pi)
    steering_angle = angle_to_mid_deg + 90

    return steering_angle


# In[ ]:


cap = cv2.VideoCapture(0)
while(cap.isOpened()):
    ret, frame = cap.read()
    canny_image = canny(frame)
    cropped_canny = region_of_interest(canny_image)
    lines = cv2.HoughLinesP(cropped_canny, 1, np.pi/180, 20, np.array([]), minLineLength=20,maxLineGap=5)
    averaged_lines = average_slope_intercept(frame, lines)
    angle = compute_steering_angle(image, averaged_lines)
    line_image = display_lines(frame, averaged_lines)
    combo_image = cv2.addWeighted(frame, 0.8, line_image, 1, 1)
    cv2.imshow("result", resized)
    print(angle)
    if cv2.waitKey(1) == 27:
        break
cap.release()
cv2.destroyAllWindows()


# In[ ]:




