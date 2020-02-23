import socket
import threading
import subprocess
import os


def ping_call():
    fnull = open(os.devnull, 'w')
    ipaddr = '192.168.2.'
    for i in (1, 2, 13, 28):
        ping_cmd = 'ping ' + ipaddr + str(i) + '-n 2'
        res = subprocess.call(ping_cmd, shell=True, stdout=fnull, stderr=fnull)
        if res:
            print('[-] {}{} is DOWN'.format(ipaddr, str(i)))
        else:
            ip = ipaddr + str(i)
            print('[+] {} is UP'.format(ip))
            port_scan(ip)


def skt_connect(host, port):
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
        print('[+]{}/tcp is open.'.format(port))
        print(res.decode('utf-8'))
        # print(str(res))
        # 关闭会话链接
        skt.close()
    except Exception as e:
        thread_lock.acquire()
        print(e)
        print('[-]{}/tcp is closed.'.format(port))
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


if __name__ == '__main__':
    main()
