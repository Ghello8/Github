import uiautomator2
import time
d=uiautomator2.connect_usb()
d.screen_off()
d.screen_on()
d.swipe(0.474, 0.841,0.474, 0.363)

d.click(0.212, 0.534)
d.click(0.762, 0.723)
d.click(0.763, 0.628)
d.click(0.225, 0.729)
time.sleep(0.5)
d.press("home")
d.press("home")

#我不懂GITHUB怎么工作的,我再次不懂这个怎么弄


#找到app
for i in range(0,6):        
    try:
        d(resourceId="com.miui.home:id/icon_icon", description=u"腾讯新闻极速版").click(timeout=0.01)
        break
    except:
        d.swipe(0.969, 0.541,0.474, 0.563)
time.sleep(1)

#点击推荐内容
d.click(0.369, 0.36)
#阅读文章
tex_num=0
for i in range(1,100):    
    try:
        d(text=u"").click(timeout=0.01)
        time.sleep(18)
        tex_num=tex_num+1
        re_text="已阅读"+str(tex_num)+"篇文章"
        print(re_text)
        if tex_num==1:
            break
    except:
        d.swipe(0.500, 0.900,0.500, 0.200)

time.sleep(2)  
d.press("back")

#点击视频
d.click(0.375, 0.144)
#刷新
d.swipe(0.474, 0.241,0.474, 0.863)
time.sleep(2)

for i in range(1,100):
    #播放
    d(resourceId="com.tencent.news.lite:id/asw").click()
    time.sleep(10)
    #点击屏幕调处按钮
    d(resourceId="com.tencent.news.lite:id/ae7").click()
    time.sleep(1)
    #拉到最后
    d.click	(0.784, 0.46)
    time.sleep(3)
    d.swipe(0.474, 0.241,0.474, 0.863)
    time.sleep(2)
    print("已看"+str(i)+"个视频")
 


#暂停
#d(resourceId="com.tencent.news.lite:id/asw").click()


#

'''
#点击推荐内容
d.click(0.369, 0.36)
#阅读文章
tex_num=0
for i in range(1,100):    
    try:
        d(resourceId="com.tencent.news.lite:id/a29").click()
        d(resourceId="com.tencent.news.lite:id/a29").click()
        time.sleep(18)
        d.press("back")
        tex_num=tex_num+1
        re_text="已阅读"+str(tex_num)+"篇文章"
        print(re_text)
        d.swipe(0.474, 0.241,0.474, 0.863)
        time.sleep(1)
        if tex_num==20:
            break
        #点击推荐内容
        d.click(0.369, 0.36)
       
    except:
        d.swipe(0.500, 0.900,0.500, 0.200)
    
'''