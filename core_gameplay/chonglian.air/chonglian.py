# -*- encoding=utf8 -*-
__author__ = "Administrator"

from airtest.core.api import *

dev = connect_device("Android:///Q2NVB21806000861")

touch(Template(r"tpl1749109060222.png", threshold=0.3, record_pos=(0.276, -0.902), resolution=(1080, 2240)))
sleep(5)
touch(Template(r"tpl1749109092661.png", threshold=0.3, record_pos=(0.181, 0.639), resolution=(1080, 2240)))
pic=wait(Template(r"tpl1750323713818.png", threshold=0.5, record_pos=(-0.006, 0.531), resolution=(1080, 2400)))
if pic:
    sleep(5)
    touch((531,1805))
sleep(50)
if wait(Template(r"tpl1749109161160.png")):
    print("已重启")
    







