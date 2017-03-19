#/user/bin/python
#encoding:utf_8
import csv
import os
import time

#控制类
class Controller(object):
    def __init__(self,count):
        self.counter=count
        self.alldata=[('timestamp','cpuvalue')]

    #单次测试过程
    def testprocess(self):
        result=os.popen('adb shell dumpsys cpuinfo|grep com.qihoo.browser')
        for line in result.readlines():
            cpuvalue=line.split('%')[0]
        currenttime=self.getCurrentTime()
        self.alldata.append((currenttime,cpuvalue))

    #多次执行测试过程
    def run(self):
        while self.counter>0:
            self.testprocess()
            self.counter=self.counter-1
            time.sleep(5)
    #获取当前时间戳
    def getCurrentTime(self):
        currentTime=time.strftime('%yY-%m-%d %H:%M:%S',time.localtime())
        return currentTime

    #def collectAllData(self):
    #数据存储
    def saveDatatoCSV(self):
        csvfile=file('cpuvalue.csv','wb')
        writer=csv.writer(csvfile)
        writer.writerows(self.alldata)
        csvfile.close()

if __name__=='__main__':
    controller=Controller(10)
    controller.run()
    controller.saveDatatoCSV()
















