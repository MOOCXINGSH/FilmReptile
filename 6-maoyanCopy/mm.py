# -*- encoding=utf8 -*-
__author__ = "Administrator"

from airtest.core.api import *
from airtest.cli.parser import cli_setup

if not cli_setup():
    auto_setup(__file__, logdir=True, devices=[
            "Android://127.0.0.1:5037/7083743d",
    ])


# script content
print("start...")


# generate html report
# from airtest.report.report import simple_report
# simple_report(__file__, logpath=True)
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
while True:
    poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)
    poco("com.sankuai.moviepro:id/tv_information").click()
    poco(text="国产").click()
    poco(text="战狼2").click()
    snapshot(msg="当前界面.")
    swipe(Template(r"tpl1558373249036.png", record_pos=(-0.007, 0.788), resolution=(1080, 2160)), vector=[-0.4682, -0.8504])
    snapshot(msg="当前界面.")
    swipe(Template(r"tpl1558373496381.png", record_pos=(-0.013, 0.691), resolution=(1080, 2160)), vector=[-0.4731, -0.7548])
    touch(Template(r"tpl1558373882687.png", record_pos=(0.36, 0.59), resolution=(1080, 2160)))
    touch(Template(r"tpl1558373949241.png", record_pos=(-0.447, -0.274), resolution=(1080, 2160)))
    snapshot(msg="当前界面.")
    touch(Template(r"tpl1558378280045.png", record_pos=(-0.457, -0.889), resolution=(1080, 2160)))
    touch(Template(r"tpl1558378280045.png", record_pos=(-0.457, -0.889), resolution=(1080, 2160)))
    touch(Template(r"tpl1558378280045.png", record_pos=(-0.457, -0.889), resolution=(1080, 2160)))


