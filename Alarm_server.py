from http.server import BaseHTTPRequestHandler, HTTPServer
from weather import get_weather
from calendar_personal import get_calendar
from ChatGPT import get_morning_motivation, get_tech_news, get_health_tip
import time

class SimpleHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        # send response, but not too much (sorry Apple ;) ) 
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(bytes("Received Request!", "utf8"))
        print("Received Request!")

        # various tasks
        weather = get_weather()
        calendar = get_calendar()

        # Run tasks
        weather
        time.sleep(2)
        calendar
        time.sleep(2)

        # Run ChatGPT script
        motivation = get_morning_motivation()
        time.sleep(2)
        print(motivation)
        tech = get_tech_news()
        time.sleep(2)
        print(tech)
        health = get_health_tip()
        time.sleep(2)
        print(health)

        return 

def run(server_class=HTTPServer, handler_class=SimpleHandler, port=8080):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f'Starting server on port {port}...')
    httpd.serve_forever()

if __name__ == '__main__':
    run()

