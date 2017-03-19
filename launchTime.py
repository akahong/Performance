#/user/bin/python
#encoding:utf_8
import csv
import os
import time

#app类
class APP(object):
    def __init__(self):
        self.content=''
        self.startTime=0

    #'''启动app'''
    def LaunchApp(self):
        cmd='adb shell am start -W -n com.android.browser/.BrowserActivity'
        self.content=os.popen(cmd)

    #'''停止app'''
    def StopApp(self):
        cmd = 'adb shell am force-stop com.android.browser'
        os.popen(cmd)

    #'''获取启动时间'''
    def GetLaunchedTime(self):
        for line in self.content.readlines():
            if 'ThisTime' in line:
                self.startTime=line.split(';')[1]
                break
        return self.startTime

#控制类
class Controller(object):
    def __init__(self,count):
        self.app=APP()
        self.counter=count
        self.alldata=[('timestamp','elapsedtime')]

    #单次测试过程
    def testprocess(self):
        self.app.LaunchApp()
        elapsedtime=self.app.GetLaunchedTime()
        self.app.StopApp()
        currenttime=self.getCurrentTime()
        self.alldata.append((currenttime,elapsedtime))

    #多次执行测试过程
    def run(self):
        while self.counter>0:
            self.testprocess()
            self.counter=self.counter-1
    #获取当前时间戳
    def getCurrentTime(self):
        currentTime=time.strftime('%yY-%m-%d %H:%M:%S',time.localtime())
        return currentTime

    #def collectAllData(self):
    #数据存储
    def saveDatatoCSV(self):
        csvfile=file('StartTime.csv','wb')
        writer=csv.writer(csvfile)
        writer.writerows(self.alldata)
        csvfile.close()

if __name__=='__main__':
    controller=Controller(10)
    controller.run()
    controller.saveDatatoCSV()
















