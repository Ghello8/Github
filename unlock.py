import uiautomator2
d=uiautomator2.connect_usb()
def unlock():
    d.swipe(0.474, 0.841,0.474, 0.363)
    d.click(0.212, 0.534)
    d.click(0.762, 0.723)
    d.click(0.763, 0.628)
    d.click(0.225, 0.729)