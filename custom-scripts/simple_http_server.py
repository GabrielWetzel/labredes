import time
import sys
import BaseHTTPServer
import os

HOST_NAME = '0.0.0.0' # !!!REMEMBER TO CHANGE THIS!!!
PORT_NUMBER = 8000

class MyHandler(BaseHTTPServer.BaseHTTPRequestHandler):
    def do_HEAD(s):
        s.send_response(200)
        s.send_header("Content-type", "text/html")
        s.end_headers()
    def do_GET(s):
        """Respond to a GET request."""
        s.send_response(200)
        s.send_header("Content-type", "text/html")
        s.end_headers()
        s.wfile.write("<html><head><title>STATS</title></head>")

        datahora = os.popen('date').read()
        s.wfile.write("<p>Data e Hora: %s</p>" % datahora)

        with open("/proc/uptime") as file:
	  s.wfile.write("<p>Uptime : %s s </p>" % file.read().split(" ")[0])

        #with open("/proc/stat") as file:
	#  s.wfile.write("<p>Stat : %s </p>" % file.read())
	with open("/proc/meminfo") as file:
          mem = file.read().split("\n")
	  s.wfile.write("<p> %s </p>" % mem[1] + mem[2])
        with open("/proc/cpuinfo") as file:
          cpuinfo = file.read().split("\n")
	  s.wfile.write("<p> %s </p>" % cpuinfo[4])
          s.wfile.write("<p> %s </p>" % cpuinfo[6])
	with open("/proc/version") as file:
          s.wfile.write("<p> Version : %s </p>" % file.read())

	data = os.popen("iostat").read().split(" ")
	while "" in data:
          data.remove("")
	us = int(data[13])
	sy = int(data[14])
	total = us + sy
	s.wfile.write("<p>Cpu Usage (iostat) : %s %%"% total)

        data = os.popen("ps").read()
        s.wfile.write("<p> %s </p>" % data.replace("\n","</br>"))
	
          	
        s.wfile.write("</body></html>")
	


if __name__ == '__main__':
    server_class = BaseHTTPServer.HTTPServer
    httpd = server_class((HOST_NAME, PORT_NUMBER), MyHandler)
    print time.asctime(), "Server Starts - %s:%s" % (HOST_NAME, PORT_NUMBER)
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    httpd.server_close()
    print time.asctime(), "Server Stops - %s:%s" % (HOST_NAME, PORT_NUMBER)

