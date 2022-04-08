from socket import socket

def main():
    # 1、创建套接字对象默认使用TCP和Ipv4协议
    client = socket()
    client.connect(('192.168.50.1', 6789))
    print(client.recv(1024).decode('utf-8'))
    client.close()

if __name__ == '__main__':
    main()