#!/usr/bin/env python
import time
import signal
import os,sys
import datetime
import math

chars = [
    "〇",
    "一",
    "二",
    "三",
    "四",
    "五",
    "六",
    "七",
    "八",
    "九",
    "十"
]
months = [
    "睦月",
    "如月",
    "弥生",
    "卯月",
    "皐月",
    "水無月",
    "文月",
    "葉月",
    "長月",
    "神無月",
    "霜月",
    "師走"
]
hours = [
    "正子", #0
    "初丑", #1
    "正丑", #2
    "初寅", #3
    "正寅", #4
    "初卯", #5
    "正卯", #6
    "初辰", #7
    "正辰", #8
    "初巳", #9
    "正巳", #10
    "初午", #11
    "正午", #12
    "初未", #13
    "正未", #14
    "初申", #15
    "正申", #16
    "初酉", #17
    "正酉", #18
    "初戌", #19
    "正戌", #20
    "初亥", #21
    "正亥", #22
    "初子" #23
]

def toggle():
    t = ((t + 1) % 2)

def bigtokanji(num):
    s = list()
    while num!=0:
        i = num%10
        num /= 10
        num = int(num)
        s.append(chars[i])
    s.reverse()
    return "".join(s)

def monthtokanji(num):
    return months[num-1]

def tokanji(num):
    s = list()
    num_ = math.floor(num / 10)
    if num_ != 0:
        if num_ != 1:
            s.append(chars[num_])
        s.append(chars[10])
    s.append(chars[num%10])
    return "".join(s)

def hourtokanji(num):
    return hours[int(num)]

def showdate():
    now = datetime.datetime.now()
    y = bigtokanji(now.year)
    m = monthtokanji(now.month)
    d = tokanji(now.day)
    print(" ".join([(y+"年").rjust(4, "　"),m.rjust(3, "　"),(d+"日").rjust(4,"　")]))

def showtime():
    now = datetime.datetime.now()
    h = hourtokanji(now.hour)
    m = tokanji(now.minute)
    s = bigtokanji(now.second)
    print(" ".join([h,(m+"分").rjust(3, "　"),(s+"秒").rjust(2, "　")]))

t = 0;
def toggle(signum, stack):
    global t
    t = (t+1)%2
    if t == 0:
        showtime()
    else:
        showdate()
    sys.stdout.flush()

signal.signal(signal.SIGUSR1, toggle)

while True:
    if t == 0:
        showtime()
    else:
        showdate()
    sys.stdout.flush()
    time.sleep(1)

