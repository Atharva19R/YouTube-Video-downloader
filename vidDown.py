# -*- coding: utf-8 -*-
"""
Created on Wed Aug 25 11:10:24 2021

@author: AR
"""
from tkinter import *
from pytube import YouTube

root = Tk()
root.geometry('500x300')
root.resizable(0,0)
root.title("AR--YT DOWNLOADER")

Label(root,text = 'YT video downloader',font = 'Sans 20 bold').pack()

link = StringVar()

Label(root,text='Paste Link Here:',font ='Sans 15 bold').place(x=160 ,y=60)
link_enter = Entry(root,width =70,textvariable = link).place(x=32,y=90)
def Downloader():     
    url =YouTube(str(link.get()))
    video = url.streams.first()
    video = url.streams.get_highest_resolution()
    video.download()
    Label(root, text = 'DOWNLOADED', font = 'arial 15').place(x= 180 , y = 210)  

Button(root,text = 'DOWNLOAD', font = 'arial 15 bold' ,bg = 'pale violet red', padx = 2, command = Downloader).place(x=180 ,y = 150)

root.mainloop()