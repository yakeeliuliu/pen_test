import optparse
import socket


def connscan(tgthost, tgtport):
    try:
        connskt = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        connskt.connect((tgthost, tgtport))
        connskt.send('ViolentPython\r\n')
        result = connskt.recv(100)
        print('{} /tcp open'.format(tgtport))
        print('[+] ' + str(result))
        connskt.close()
    except:
        print('[-] {}/tcp closed'.format(tgtport))


def portScan(tgthost, tgtport):
    global tgtip
    try:
        tgtip = socket.gethostbyname(tgthost)
    except:
        print('cannot resolve {}, unknown host'.format(tgthost))

    try:
        tgtname = socket.gethostbyaddr(tgtip)
        print('scan result for {}.'.format(tgtname))
    except:
        print('scan result for {}.'.format(tgtip))

    print('scanning port {}'.format(tgtport))
    connscan(tgthost, tgtport)


def main():
    parser = optparse.OptionParser('[*] Usage : ./portscanner.py -H <target host> -p <target port>')
    parser.add_option('-H', dest='tgthost', type='string', help='specify a target')
    parser.add_option('-P', dest='tgtport', type='string', help='specify a port number')
    (options, args) = parser.parse_args()
    tgthost = options.tgthost
    tgtport = options.tgtport
    if (tgthost is None) | (tgtport is None):
        print(parser.usage)
        exit(0)
    portScan(tgthost, tgtport)


if __name__ == '__main__':
    main()
