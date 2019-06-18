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


for i in range(0,6):
    try:
        d(resourceId="com.miui.home:id/icon_icon", description=u"今日头条极速版").click(timeout=0.01)
        break
    except:
        d.swipe(0.969, 0.541,0.474, 0.563)
time.sleep(1)
d.swipe(0.474, 0.341,0.474, 0.563)
time.sleep(1)
d.click(0.547, 0.427)
for i in range(1,100):
    try:
        d(resourceId="com.ss.android.article.lite:id/rm").click(timeout=0.01)
        d.press("back")
        d.swipe(0.474, 0.341,0.474, 0.563)
        time.sleep(1)
        d.click(0.547, 0.427)
    except:
        d.swipe(0.500, 0.700,0.500, 0.100)

'''
for i in range(1,500):
    d.swipe(0.500, 0.600,0.500, 0.300)
    time.sleep(4)
    print(i)


#搜索
for i in range(0,7):
    d.click(0.331, 0.074)
    d(resourceId="com.ss.android.article.lite:id/nf").click()
    time.sleep(1)
    d.press("back")
'''

'''
d(resourceId="com.miui.home:id/icon_icon", description=u"今日头条极速版").click()
d(resourceId="com.ss.android.article.lite:id/a47").click()
#d(resourceId="com.ss.android.article.lite:id/ve").click()
#d(resourceId="com.ss.android.article.lite:id/ab8").click()
d.press("back")
d.press("back")
d.press("back")
d.press("back")
'''