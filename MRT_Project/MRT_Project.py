import tkinter   
import random
import csv


blue_line=['後山埤站','市政府站','國父紀念館站','忠孝敦化站','忠孝復興站','忠孝新生站','西門站','龍山寺站','府中站']

red_line=['淡水站','北投站','劍潭站','圓山站','中山站','東門站','大安站','大安森林公園站','信義安和站','台北101站']
two_line=['後山埤站','市政府站','國父紀念館站','忠孝敦化站','忠孝復興站','忠孝新生站','西門站','龍山寺站','府中站','淡水站','北投站','劍潭站','圓山站','中山站','東門站','大安站','大安森林公園站','信義安和站','台北101站']


    
def redline():
    lab2["text"] = random.choice(red_line)
    lab5['text']=' '
    for row in list_data2:
        if row[0] == lab2["text"]:
           lab3["text"] = '從北車去該站的票價(現金/悠遊卡)：' + str(row[2]) +'/' + str(row[1]) + '元 \n 從北車去該地要花' + str(row[3]) + '分鐘 \n 從該地回動物園站要花' + str(row[4]) + '分鐘 \n 到動物園的票價(現金/悠遊卡)：' + str(row[5]) +'元' 
    for row in list_data4:
        if row[0] == lab2["text"]:
          lab4['text'] = lab2["text"]+"的景點和美食:"
          lab5["text"] = "推薦:" + str(row[1:5])+'\n'+lab5["text"]
         

    
def blueline():
    lab2["text"] = random.choice(blue_line)
    lab5['text']=' '
    for row in list_data1:
        if row[0] == lab2["text"]:
            lab3["text"] = '從北車去該站的票價(現金/悠遊卡)：' + str(row[2]) +'/' + str(row[1]) + '元 \n 從北車去該地要花' + str(row[3]) + '分鐘 \n 從該地回動物園站要花' + str(row[4]) + '分鐘 \n 到動物園的票價(現金/悠遊卡)：' + str(row[5]) +'元' 
    for row in list_data4:
        if row[0] == lab2["text"]:
          lab4['text'] = lab2["text"]+"的景點和美食:"
          lab5["text"] = "推薦:" + str(row[1:5])+'\n'+lab5["text"]
        
    
def twoline():
    lab2["text"] = random.choice(two_line)
    lab5['text']=' '
    for row in list_data3:
        if row[0] == lab2["text"]:
            lab3["text"] = '從北車去該站的票價(現金/悠遊卡)：' + str(row[2]) +'/' + str(row[1]) + '元 \n 從北車去該地要花' + str(row[3]) + '分鐘 \n 從該地回動物園站要花' + str(row[4]) + '分鐘 \n 到動物園的票價(現金/悠遊卡)：' + str(row[5]) +'元' 
    for row in list_data4:
        if row[0] == lab2["text"]:
          lab4['text'] = lab2["text"]+"的景點和美食:"
          lab5["text"] = "推薦:" + str(row[1:5])+'\n'+lab5["text"]
          

with open('捷運吃玩 - 藍線票價.csv','r', encoding="utf-8") as csvFile:
      cr = csv.reader(csvFile)     
      list_data1 = list(cr)    
with open('捷運吃玩 - 紅線票價.csv','r', encoding="utf-8") as csvFile:
      cr = csv.reader(csvFile)     
      list_data2 = list(cr)
with open('捷運吃玩 - 兩線票價.csv','r', encoding="utf-8") as csvFile:
      cr = csv.reader(csvFile)     
      list_data3 = list(cr)
with open('捷運吃玩 - 藍紅線.csv','r', encoding="utf-8") as csvFile:
      cr = csv.reader(csvFile)     
      list_data4 = list(cr) 

    

win=tkinter.Tk()  
win.title('今天要去哪裡玩?')   
win.geometry('800x500') 


lab1=tkinter.Label(win, text="按下按鈕決定要去哪裡玩", font=('標楷體',14),padx=45,pady=15)
lab2=tkinter.Label(win,padx=1,pady=1)
lab3=tkinter.Label(win,text='',padx=25,pady=10)
lab4=tkinter.Label(win,text='',padx=1,pady=5)
lab5=tkinter.Label(win,text='',padx=50,pady=5) 

btn1=tkinter.Button(win,text='紅線',command=redline,padx=5,pady=5)
btn2=tkinter.Button(win,text='藍線',command=blueline,padx=5,pady=5)
btn3=tkinter.Button(win,text='隨機選',command=twoline,padx=5,pady=5)


lab1.pack(side='top')
btn1.pack(side='top')
btn2.pack(side='top')
btn3.pack(side='top')
lab2.pack(side='top')
lab3.pack(side='top')
lab4.pack(side='top')
lab5.pack(side='top')



win.mainloop()     

