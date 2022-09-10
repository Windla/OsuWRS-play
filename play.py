# coding = uft-8
import time
import win32api
import win32con
import glob  # 文件计数
import os  # 获取工作路径


# 配置文件读取
with open("config.ini", 'r') as f:
    Path = f.read()  # osu 路径
    f.close()
osuPath = Path + "\\osu!.exe"  # osu!.exe 路径
bgPath = Path + "\\Data\\bg"  # bg文件夹 路径
bgPathN = os.getcwd() + "\\bg"  # bg待替换文件夹 路径
bgTempPath = Path + "\\Data\\bg_temp\\"

# 获取待替换文件数量p
bgNum = len(glob.glob(bgPathN + "\\*.jpg"))
print("获取到的待替换图片数量为", bgNum, "张")
# 获取bg文件夹下的文件名
# 文件名 = 通过系统获取文件名(转为str(获取路径(通配符路径))).不带后缀
bgName = os.path.basename(str(glob.glob(bgPath + "\\*.jpg"))).split('.')[0]
print("获取到的原季节背景文件名:\n", bgName)

# 对于bg文件夹是否有.jpg文件进行判断 | bg文件夹是否存在
if bgNum != 0:
    # 将bg复制到同一目录下
    os.system('_copy.bat')

    '''
    # osu!获取焦点
    # os.system("taskkill /F /IM osu!.exe")
    time.sleep(5)
    win32api.ShellExecute(0, 'open', osuPath, '', '', 1)
    '''

    time.sleep(5)
    print("Start")
    while True:
        for i in range(1, bgNum + 1):
            os.system('_unlock.bat')
            # os.rename(bgPathN + i + ".jpg", bgPath + bgName + ".jpg")
            os.remove(bgPath + "\\" + bgName + ".jpg")
            os.rename(bgTempPath + "bg (" + str(i) + ")" + ".jpg", bgPath + "\\" + bgName + ".jpg")
            os.system('_lock.bat')
            print("替换成功", i, "/", bgNum)

            # 按键模拟部分 | 需要 osu! 与 OBS 配合
            # P*3
            for t in range(3):
                win32api.keybd_event(80, 0, 0, 0)
                time.sleep(0.02)
                win32api.keybd_event(80, 0, win32con.KEYEVENTF_KEYUP, 0)
                time.sleep(0.02)
            time.sleep(0.25)
            # ESC
            win32api.keybd_event(0x1B, win32api.MapVirtualKey(0x1B, 0), 0, 0)
            time.sleep(0.02)
            win32api.keybd_event(0x1B, win32api.MapVirtualKey(0x1B, 0), win32con.KEYEVENTF_KEYUP, 0)

            time.sleep(1)
            # OBS恢复 Num1
            win32api.keybd_event(0x61, win32api.MapVirtualKey(0x61, 0), 0, 0)
            time.sleep(0.02)
            win32api.keybd_event(0x61, win32api.MapVirtualKey(0x61, 0), win32con.KEYEVENTF_KEYUP, 0)
            time.sleep(1)
            # OBS暂停 Num0
            win32api.keybd_event(0x60, win32api.MapVirtualKey(0x60, 0), 0, 0)
            time.sleep(0.02)
            win32api.keybd_event(0x60, win32api.MapVirtualKey(0x60, 0), win32con.KEYEVENTF_KEYUP, 0)
        break  # 删除这行就会循环
        # os.system('_copy.bat')

    # OBS暂停 Num0 | 防止过长的录制
    win32api.keybd_event(0x60, win32api.MapVirtualKey(0x60, 0), 0, 0)
    time.sleep(0.02)
    win32api.keybd_event(0x60, win32api.MapVirtualKey(0x60, 0), win32con.KEYEVENTF_KEYUP, 0)

else:
    print("\nError: Plz check 'bg'\n"
          "请检查你的'bg'文件夹是否存在且该文件夹下是否有.jpg文件; 另外,不支持.png文件")
