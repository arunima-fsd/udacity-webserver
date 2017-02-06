from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
import read_restaurants

class webserverHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        try:

            if self.path.endswith('/restaurants'):
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                output = ""
                output += "<html><body>"
                output += "<ul>"
                restaurants = read_restaurants.getRestaurants()
                for restaurant in restaurants:
                    output += "<li>"+restaurant.name+ "</li>"
                output += "</ul></body></html>"

                self.wfile.write(output)
                print output
                return
        except IOError:
            self.send_error(404, "File not found %s"%self.path)


def main():
    try:
        port = 8080
        server = HTTPServer(('', port), webserverHandler)
        print "The server is running on %s"%port
        #The following line continues to listen until I press
        # CTRL+C
        server.serve_forever()


    except KeyboardInterrupt:
        print "The server has stopped listening"
        server.socket.close()







if __name__ == '__main__':
    main()
