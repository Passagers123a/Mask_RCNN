# -*- coding: utf-8 -*-
"""
Created on Tue Mar 26 11:23:42 2019

@author: Lavinia
"""
import os,shutil
import sys
import numpy as np

input_file = "F:\\python\\leaf\\lable\\testing_files"  #文件路径
img_json = ".json"
img_pic = "pic"
#def arrange_file(input_file,img_type):
#创建.json文件夹
file_json = os.path.join(input_file,img_json)
file_pic = os.path.join(input_file,img_pic)  
file_mask = os.path.join(input_file,"cv2_mask") 
file_lableme = os.path.join(input_file,"lableme_json") 
if not os.path.isdir(file_json):
    os.makedirs(file_json)
#如果dst所指的目录不存在，而src是一个文件，
#所以程序默认会认为dst是指的一个没有扩展名的文件，而不是一个文件夹。就会生成一个批次文件夹              
if not os.path.isdir(file_pic):
    os.makedirs(file_pic)       
if not os.path.isdir(file_mask):
    os.makedirs(file_mask)       
if not os.path.isdir(file_lableme):
    os.makedirs(file_lableme)  
    
for files in os.listdir(input_file):
   file_path = os.path.join(input_file, files)
   if(os.path.isdir(file_path)):
       for file in os.listdir(file_path):
            if file =='label.png':
                full_path = os.path.join(files, file)
                despath = os.path.join(file_mask) #,files   
                shutil.copy(full_path, despath)
                os.rename(os.path.join(file_mask,file),
                          os.path.join(file_mask,str(files)+".png"))
                shutil.move(file_path, file_lableme) 
                break;
   else:
        name = os.path.basename(files)  # 获取文件名
        dirname = os.path.dirname(files)  # 获取文件目录
        filename1 = os.path.splitext(files)[1]  # 读取文件后缀名
        filename0 = os.path.splitext(files)[0]  #读取文件名
        if filename1=='.jpg' or filename1=='.JPG' :
            full_path = os.path.join(input_file, files)
            despath = os.path.join(file_pic) #.jpg为你的文件类型，即后缀名，读者自行修改, filename0+'.jpg'
            shutil.move(full_path, despath)   
        elif filename1 == '.json' :
            full_path = os.path.join(input_file, files)
            despath = os.path.join(file_json) #,files   
            shutil.move(full_path, despath)

    
                
        
        
        
        
        
        
        
        
        