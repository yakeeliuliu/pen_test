import os
import subprocess
import time


def ping_call():
    start_time = time.time()
    fnull = open(os.devnull, 'w')
    log = open('1.txt', 'w')
    for i in range(1, 5):
        ipaddr = '192.168.2.' + str(i)
        ping_cmd = 'ping ' + ipaddr + ' -n 2'
        subprocess.call(ping_cmd, shell=True, stdout=log, stderr=fnull)
        current_time = time.strftime('%Y%m%d-%H:%M:%S', time.localtime())
        log.write(str(current_time))
        print('now is pinging {}'.format(ipaddr))
    fnull.close()


ping_call()
