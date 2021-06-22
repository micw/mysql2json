#!/usr/bin/env python3

import os
import mysql.connector
import json
import http.server as SimpleHTTPServer
import socketserver as SocketServer

def getenv(name, default_value=None):
    ret=os.getenv(name, default_value)
    if ret is None:
        print("Missing environment variable:",name)
        quit(1)
    return ret


def execute_query():
    mysql_host=getenv("MYSQL_HOST")
    mysql_port=int(getenv("MYSQL_PORT","3306"))
    mysql_user=getenv("MYSQL_USER")
    mysql_password=getenv("MYSQL_PASSWORD")
    mysql_database=getenv("MYSQL_DATABASE")
    mysql_query=getenv("MYSQL_QUERY")
    with mysql.connector.connect(
            host=mysql_host,
            port=mysql_port,
            user=mysql_user,
            password=mysql_password,
            database=mysql_database
        ) as db:
        rs=db.cursor()
        rs.execute(mysql_query)
        cols=rs.column_names
        results=[]
        for row in rs:
            for i,col in enumerate(row):
                results.append({
                    cols[i]:col
                })

        return results

class HttpHandler(SimpleHTTPServer.SimpleHTTPRequestHandler):

    def do_GET(self):
        result=json.dumps(execute_query())
        self.send_response(200)
        self.send_header("Content-type", "application/json")
        self.end_headers()
        self.wfile.write(result.encode())
        pass

def main():
    execute_query()
    http_port=int(getenv("HTTP_PORT","8000"))
    with SocketServer.TCPServer(("", http_port), HttpHandler) as httpd:
        print("serving at port", http_port)
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("stopping server")
            pass
        finally:
            httpd.server_close()


if __name__ == "__main__":
    main()
