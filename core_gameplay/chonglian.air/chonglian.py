# -*- encoding=utf8 -*-
__author__ = "Administrator"

from airtest.core.api import *

dev = connect_device("Android:///Q2NVB21806000861")

touch((839,137))
sleep(5)
touch(Template(r"tpl1750904016357.png", threshold=0.5, record_pos=(0.177, 0.708), resolution=(1080, 2400)))
pic=wait(Template(r"tpl1750843426933.png", record_pos=(-0.012, -0.592), resolution=(1080, 2400)))

if pic:
    sleep(20)
    touch((531,1805))
sleep(50)

    







