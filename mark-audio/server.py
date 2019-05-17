'''http服务器'''
import os  # Python的标准库中的os模块包含普遍的操作系统功能
import re  # 引入正则表达式对象
from urllib.parse import unquote # 用于对URL进行编解码
from http.server import HTTPServer, BaseHTTPRequestHandler  # 导入HTTP处理相关的模块
import mark
import json


# 自定义处理程序，用于处理HTTP请求
class TestHTTPHandler(BaseHTTPRequestHandler):
    # 处理GET请求
    def do_GET(self):
        #获得url地址
        url_path=self.path
        #定义返回值
        result=-1
        if url_path== "/favicon.ico":
            return
        else:
            #匹配/?sentence=
            pattern="/api?sentence="
            try:
                result=url_path.index(pattern)
            except Exception as e:
                print(e)

            if result!=0:
                #失败
                self.protocal_version = 'HTTP/1.1'  # 设置协议版本
                self.send_response(404)  # 设置响应状态码
                self.send_header("Welcome", "Contect")  # 设置响应头
                self.end_headers()
            else:
                #成功
                #获取字符串
                sentence=unquote(url_path[11:])
                zhuyin_list=mark.zhuyin(sentence)
                self.protocal_version = 'HTTP/1.1'  # 设置协议版本
                self.send_response(200)  # 设置响应状态码
                self.send_header("Welcome", "Contect")  # 设置响应头
                self.end_headers()
                #设置输出流编码
                self.wfile.write(json.dumps(zhuyin_list).encode('utf-8'))


# 启动服务函数
def start_server(port):
    try:
        http_server = HTTPServer(('127.0.0.1', int(port)), TestHTTPHandler)
        print("server start!")
        http_server.serve_forever()  # 设置一直监听并接收请求
    except KeyboardInterrupt:
        print("server shutdown")
        http_server.socket.close()

if __name__ == '__main__':
    start_server(8000)
