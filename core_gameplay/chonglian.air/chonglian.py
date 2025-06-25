# -*- encoding=utf8 -*-
__author__ = "Administrator"

from airtest.core.api import *

dev = connect_device("Android:///Q2NVB21806000861")

touch((839,137))
sleep(5)
touch(Template(r"tpl1749109092661.png", threshold=0.3, record_pos=(0.181, 0.639), resolution=(1080, 2240)))
pic=wait(Template(r"tpl1750843426933.png", record_pos=(-0.012, -0.592), resolution=(1080, 2400)))

if pic:
    sleep(10)
    touch((531,1805))
sleep(50)

    







