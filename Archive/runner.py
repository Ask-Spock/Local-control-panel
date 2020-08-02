#This Modulue developed in order to runn on all file in a folder 


import os



for filename in os.listdir('.'):
    if(filename.lower().endswith('.html')):
        print(filename)