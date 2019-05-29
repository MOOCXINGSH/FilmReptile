# -*- encoding=utf8 -*-
__author__ = "Administrator"

from airtest.core.api import *
from airtest.cli.parser import cli_setup

if not cli_setup():
    auto_setup(__file__, logdir=True, devices=[
            "Android://127.0.0.1:5037/6cb5fe5b",
    ])
print("start...")
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)
poco(text="捉妖记")
poco("android.widget.LinearLayout").offspring("android:id/content").offspring("com.sankuai.moviepro:id/root_recycle").child("android.widget.RelativeLayout")[2].child("com.sankuai.moviepro:id/first_layout")#poco("com.sankuai.moviepro:id/tv_information").click()
#poco(text="国产").click()
while True:
    poco.swipe([0.5,0.5],[0.5,0.623])
    #poco("com.sankuai.moviepro:id/mil_container").focus([0.5,0.5]).click()
    poco("com.sankuai.moviepro:id/root_recycle").focus([0.5,0.86]).click()
    mode = True
    k=1
    m=1
    while mode==True:
        sleep(1)
        snapshot(msg="当前界面.")
        poco.swipe([0.5,0.9],[0.5,0.1])
        k=k+1
        if k==5:
            touch(Template(r"tpl1558460717253.png", record_pos=(-0.454, -0.885), resolution=(1080, 2160)))
            mode =not mode
            break
            
        if exists(Template(r"tpl1558458406606.png", record_pos=(0.371, -0.76), resolution=(1080, 2160))):
            touch(Template(r"tpl1558458423851.png", record_pos=(0.369, -0.759), resolution=(1080, 2160)))
            while mode==True:
                sleep(1)
                snapshot(msg="当前界面.")
                if exists(Template(r"tpl1558458574036.png", record_pos=(-0.441, -0.164), resolution=(1080, 2160))):
                    touch(Template(r"tpl1558458586688.png", record_pos=(-0.437, -0.164), resolution=(1080, 2160)))
                    while mode==True:
                        sleep(1)
                        snapshot(msg="当前界面.")
                        poco.swipe([0.5,0.9],[0.5,0.1])
                        m=m+1
                        if m==50:
                            touch(Template(r"tpl1558460701633.png", record_pos=(-0.452, -0.886), resolution=(1080, 2160)))
                            sleep(1)
                            touch(Template(r"tpl1558460717253.png", record_pos=(-0.454, -0.885), resolution=(1080, 2160)))
                            mode = not mode
                            break

                        if exists(Template(r"tpl1558757177899.png", record_pos=(-0.441, -0.075), resolution=(576, 1024))):

                            touch(Template(r"tpl1558757195141.png", record_pos=(-0.441, -0.073), resolution=(576, 1024)))

                            while mode==True:
                                sleep(1)
                                snapshot(msg="当前界面.")
                                poco.swipe([0.5,0.9],[0.5,0.1])
                                touch(Template(r"tpl1558460701633.png", record_pos=(-0.452, -0.886), resolution=(1080, 2160)))
                                sleep(1)
                                touch(Template(r"tpl1558460717253.png", record_pos=(-0.454, -0.885), resolution=(1080, 2160)))
                                mode = not mode




              


                        




















