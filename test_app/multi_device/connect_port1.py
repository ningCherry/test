import subprocess
from time import ctime
import multiprocessing

def appium_start(host,port):
    '''启动appium server'''
    #eg:"start /b appium -a 127.0.0.1 -p 4723 -bp 4724"
    bootstrap_port=str(port+1)
    cmd='start /b appium -a {} -p {} -bp {}'.format(host,port,bootstrap_port)
    print('%s at %s' % (cmd, ctime()))
    subprocess.Popen(cmd,shell=True,stdout=open('./'+str(4723)+'.log','a'),stderr=subprocess.STDOUT)

desird_process=[]
host = '127.0.0.1'
for i in range(2):
    port=4723+2*i
    desired=multiprocessing.Process(target=appium_start,args=(host,port))
    desird_process.append(desired)

if __name__ == '__main__':
    for i in desird_process:
        i.start()
    for i in desird_process:
        i.join()