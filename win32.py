import win32api
import win32con

s=str(win32api.GetCursorPos())
print(s)
win32api.MessageBox(win32con.NULL, 'Python 你好！', '你好', win32con.MB_OK)  