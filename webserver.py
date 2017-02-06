from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
import read_restaurants, insert_rest, delete
import cgi
import re

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
                    output += "<li><h2>"+restaurant.name+ "</h2></li>"
                    output += "<a href='/restaurants/"+str(restaurant.id) +"/edit' style='color:blue'>Edit</a><br>" \
                               "<a href='/restaurants/"+str(restaurant.id)+"/delete' style='color:red'>Delete</a><br><br>"
                output += "</ul>"
                output += "<br><a href='restaurants/new'>Make new Restaurant</a>"
                output += "</body></html>"

                self.wfile.write(output)
                print output
                return

            if self.path.endswith('/restaurants/new'):
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                output = "<html><body>"
                output += '<form method="POST" enctype="multipart/form-data" action="/restaurants/new">' \
                         '<h1>Make a new restaurant</h1>' \
                         '<input name="restaurant" type="text">' \
                         '<input type="submit" value="Submit">' \
                         '</form>'
                output += "</body></html>"

                self.wfile.write(output)
                print output
                return

            if self.path.endswith('/edit'):
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                id = re.findall(r'\d+', self.path)[0]
                print "ID: %s"%str(id)
                output = "<html><body>"
                output += '<form method="POST" enctype="multipart/form-data" action="/restaurants/edit">' \
                          '<h1>Edit Restaurant</h1>' \
                          '<input name="restaurant1" type="text">' \
                          '<input name="id" type="hidden" value="'+str(id)+'">'\
                          '<input type="submit" value="Submit">' \
                          '</form>'
                output += "</body></html>"

                self.wfile.write(output)
                print output
                return

            if self.path.endswith('/delete'):
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                id = re.findall(r'\d+', self.path)[0]
                restaurant = read_restaurants.getRestaurant(int(id))
                output = "<html><body>"
                output += '<form method="POST" enctype="multipart/form-data" action="/restaurants/delete">' \
                          '<h1>Are you sure you want to delete '+restaurant.name+'?</h1>' \
                          '<input name="del_id" type="hidden" value="' + str(id) + '">' \
                          '<input type="submit" value="Yes">' \
                          '</form>'
                output += "</body></html>"

                self.wfile.write(output)
                print output
                return







        except IOError:
            self.send_error(404, "File not found %s"%self.path)

    def do_POST(self):
        try:
            print self.path
            if self.path.endswith('/new'):
                ctype, pdict = cgi.parse_header(self.headers.getheader('content-type'))
                if ctype == 'multipart/form-data':
                    fields = cgi.parse_multipart(self.rfile, pdict)
                    restName = fields.get('restaurant')
                    print "Restaurant: %s" %restName
                    insert_rest.insertRestaurant(restName[0])

            if self.path.endswith('/edit'):
                ctype, pdict = cgi.parse_header(self.headers.getheader('content-type'))
                if ctype == 'multipart/form-data':
                    fields = cgi.parse_multipart(self.rfile, pdict)
                    name = fields.get('restaurant1')
                    id = fields.get('id')
                    print "Name: %s" % name
                    print "Id: %s" % id
                    read_restaurants.modifyRestaurant(int(id[0]), name[0])

            if self.path.endswith('/delete'):

                ctype, pdict = cgi.parse_header(self.headers.getheader('content-type'))
                if ctype == 'multipart/form-data':
                    fields = cgi.parse_multipart(self.rfile, pdict)
                    del_id = fields.get('del_id')
                    print "Delete ID: %s" % del_id
                    delete.deleteRestaurant(int(del_id[0]))

            self.send_response(301)
            self.send_header('Content-type', 'text/html')
            self.send_header('Location', '/restaurants')
            self.end_headers()




        except:
            pass


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
