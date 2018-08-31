"""Q.1- Print the current day using Datetime module."""

import datetime as dt
x = dt.date.today()
print("Present day is : ",x.strftime("%A"))

"""Q.2- Open your browser and play a video using webbrowser module in python."""

import webbrowser
youtube = input('Enter Video to play:')
webbrowser.open_new_tab('https://www.youtube.com/search?btnG=1&q=%s' % youtube)

"""Q.3- Write a program to rename all the files in a directory and convert them into .jpg file format."""


import os
os.chdir('C:\\Users\\HP\\Desktop\\New folder')
i=1
for file in os.listdir():
    src=file
    dst="Dog"+str(i)+".jpg"
    os.rename(src,dst)
    i+=1
