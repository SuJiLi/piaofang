# -*- encoding=utf8 -*-
__author__ = "B27"

from airtest.core.api import *
from airtest.report.report import simple_report
import sys
sys.path.append(r"D:\PiaoFang_Test\core_gameplay")
from common import check_image1,check_image2,check_zhujiemian

dev = connect_device("Android:///Q2NVB21806000861")
os.path.dirname(os.path.abspath(__file__))

log_dir = r"D:\PiaoFang_Test\core_gameplay\yiren_log"
os.makedirs(log_dir, exist_ok=True)  # 确保目录存在
set_logdir(log_dir)  # 强制指定日志位置

sleep(10)
touch((397,2318))
sleep(5)
touch(Template(r"tpl1750392066293.png", threshold=0.6, record_pos=(-0.241, -0.321), resolution=(1080, 2400)))
sleep(5)
touch(Template(r"tpl1744716428373.png", record_pos=(0.344, -0.333), resolution=(1080, 2220)))
sleep(5)
if exists(Template(r"tpl1745830267535.png")):
    touch((952,1359))
    
sleep(5)
if not exists(Template(r"tpl1744716461316.png")):
    touch(Template(r"tpl1744774004071.png", threshold=0.8, record_pos=(-0.396, -0.183), resolution=(1080, 2220)))
touch(Template(r"tpl1744716461316.png", record_pos=(-0.005, 0.187), resolution=(1080, 2220)))
sleep(5)
touch(Template(r"tpl1744716797234.png", record_pos=(-0.304, 0.597), resolution=(1080, 2220)))
sleep(5)
if exists(Template(r"tpl1744774506106.png", threshold=0.9)):
        touch(Template(r"tpl1744774531636.png", record_pos=(-0.428, -0.343), resolution=(1080, 2220)))
        sleep(5)
        touch(Template(r"tpl1744774555695.png", record_pos=(-0.447, -0.843), resolution=(1080, 2220)))
elif exists(Template(r"tpl1744716821809.png",threshold=0.9)):   
        print("有资源")
        touch(Template(r"tpl1744716839504.png", record_pos=(-0.001, 0.887), resolution=(1080, 2220)))
        sleep(5)
        touch(Template(r"tpl1744716858898.png", record_pos=(-0.449, -0.843), resolution=(1080, 2220)))
else:
    touch(Template(r"tpl1745304632687.png", record_pos=(-0.448, -0.842), resolution=(1080, 2220)))
sleep(10)
if exists(Template(r"tpl1745829848051.png")):
        touch(Template(r"tpl1745829871553.png", record_pos=(-0.423, -0.661), resolution=(1080, 2220)))
touch(Template(r"tpl1750903727472.png", record_pos=(-0.421, -0.74), resolution=(1080, 2400)))

check_zhujiemian()
simple_report(
    filepath=__file__,
    logpath=log_dir,
    output=os.path.join(log_dir, "report.html")
)

















