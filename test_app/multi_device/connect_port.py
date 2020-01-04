import subprocess
from time import ctime

def appium_start(host,port):
    '''启动appium server'''
    #eg:"start /b appium -a 127.0.0.1 -p 4723 -bp 4724"
    bootstrap_port=str(port+1)
    cmd='start /b appium -a {} -p {} -bp {}'.format(host,port,bootstrap_port)
    print('%s at %s' % (cmd, ctime()))
    subprocess.Popen(cmd,shell=True,stdout=open('./'+'4723'+'.log','a'),stderr=subprocess.STDOUT)

if __name__ == '__main__':
    host = '127.0.0.1'
    port=4723
    appium_start(host,port)