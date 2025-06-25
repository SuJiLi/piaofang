# -*- encoding=utf8 -*-
from airtest.core.api import *
from airtest.report.report import simple_report
import sys
sys.path.append(r"D:\PiaoFang_Test\core_gameplay")
from common import check_image1,check_image2,check_zhujiemian


dev = connect_device("Android:///Q2NVB21806000861")
os.path.dirname(os.path.abspath(__file__))
log_dir = r"D:\PiaoFang_Test\core_gameplay\guanli_log"
os.makedirs(log_dir, exist_ok=True)  # 确保目录存在
set_logdir(log_dir)  # 强制指定日志位置
check_image1(r"tpl1744879931926.png")
touch((237,2318))
sleep(5)
if not exists(Template(r"tpl1744880034806.png",threshold=0.85)):
    touch((237,2318))
sleep(5)
touch(Template(r"tpl1750390887437.png", record_pos=(-0.277, 0.21), resolution=(1080, 2400)))
check_zhujiemian()
check_image1(r"tpl1744880096403.png")

sleep(5)
touch(Template(r"tpl1744880153332.png", record_pos=(-0.448, -0.842), resolution=(1080, 2220)))
check_zhujiemian()
touch(Template(r"tpl1750390913684.png", record_pos=(-0.277, 0.348), resolution=(1080, 2400)))
check_image1(r"tpl1744880233465.png")
sleep(5)
touch(Template(r"tpl1744880427131.png", record_pos=(-0.267, 0.904), resolution=(1080, 2220)))
check_image1(r"tpl1744880445876.png")
sleep(5)
touch(Template(r"tpl1744880613862.png", record_pos=(-0.415, -0.515), resolution=(1080, 2220)))
sleep(5)
touch(Template(r"tpl1744880636894.png", record_pos=(-0.452, -0.839), resolution=(1080, 2220)))
check_zhujiemian()
touch(Template(r"tpl1750390929706.png", record_pos=(-0.278, 0.482), resolution=(1080, 2400)))
check_image1(r"tpl1744880685747.png")
sleep(5)
touch(Template(r"tpl1744880720436.png", record_pos=(-0.442, -0.838), resolution=(1080, 2220)))
check_zhujiemian()
touch(Template(r"tpl1750390949790.png", record_pos=(-0.279, 0.879), resolution=(1080, 2400)))
check_image1(r"tpl1744881133257.png")
touch(Template(r"tpl1744881150994.png", record_pos=(-0.448, -0.843), resolution=(1080, 2220)))
check_zhujiemian()
if exists(Template(r"tpl1744881341689.png")):
    touch(Template(r"tpl1744881341689.png", record_pos=(-0.279, 0.811), resolution=(1080, 2220)))
    check_image1(r"tpl1744881364694.png")
    touch(Template(r"tpl1744881412045.png", record_pos=(-0.456, -0.845), resolution=(1080, 2220)))
check_zhujiemian()
touch(Template(r"tpl1745912768129.png", record_pos=(-0.276, 0.959), resolution=(1080, 2220)))
simple_report(
    filepath=__file__,
    logpath=log_dir,
    output=os.path.join(log_dir, "report.html")
)





