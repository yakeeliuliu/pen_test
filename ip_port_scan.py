import socket
import threading
import subprocess
import time


def ping_call():
    # fnull = open(os.devnull, 'w')
    starttime = time.strftime('%Y/%m/%d/-%H:%M:%S', time.localtime())
    log = open('ip_log.txt', 'w+')
    log.write(starttime)
    ipaddr = '192.168.2.'
    for i in (1, 2, 13, 28):
        ping_cmd = 'ping ' + ipaddr + str(i) + ' -n 1'
        subprocess.call(ping_cmd, shell=True, stdout=log)
    log.close()


def skt_connect(host, port):
    scantime = time.strftime('%Y/%m/%d/-%H:%M:%S', time.localtime())
    port_log.write(scantime, ' ', host)
    global thread_lock, skt
    try:
        thread_lock = threading.Lock()
        # 创建socket
        skt = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        skt.connect((host, port))
        # 发送消息
        msg = b'ViolentPython\r\n'
        skt.send(msg)
        # 接受服务端返回值并打印
        res = skt.recv(100)
        thread_lock.acquire()
        print('[+]{}/tcp is open.'.format(port), file=port_log)
        print(res.decode('utf-8'), file=port_log)
        # print(str(res))
        # 关闭会话链接
        skt.close()
    except Exception as e:
        thread_lock.acquire()
        print(e)
        print('[-]{}/tcp is closed.'.format(port), file=port_log)
    finally:
        thread_lock.release()
        skt.close()


def port_scan(host):
    ports = [80, 22, 443, 21, 5900]
    for port in ports:
        print('Now is scanning {}/tcp on {}.'.format(host, port))
        skt_connect(host, port)


def main():
    ping_call()
    log2 = open('ip_log.txt', 'r')
    global port_log
    port_log = open('port_log.txt', 'w+')
    for line in log2:
        if "TTL" in line:
            ip_list = line.split(' ')
            host = ip_list[1]
            port_scan(host)
    log2.close()
    port_log.close()


if __name__ == '__main__':
    main()
