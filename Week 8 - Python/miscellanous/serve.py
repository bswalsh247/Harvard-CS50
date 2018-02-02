from http.server import BaseHTTPRequestHandler, HTTPServer

# HTTPRequestHandler class
class HTTPServer_RequestHandler(BaseHTTPRequestHandler):

    # GET
    def do_GET(self):
        # send response status code
        self.send_response(200)

        # send headers
        self.send_header('Content-type','text/html')
        self.end_headers()

        # determine message to send to client
        if self.path == "/":
            message = "Hello, world!"
        else:
            name = self.path[1:]
            message = "Hello, {}!".format(name)

        # write message to socket connection that my server has with the browser, the internet connection we have
        self.wfile.write(bytes(message, "utf8"))
        return

# We’ll write our own do_GET function for the server that is called when a GET request 
# is received. We’ll always send back the response code 200, send a header, and write a 
# message back.

# And all of these functions and features we’d learn about from reading Python 
# documentation online.

# Here we configure the server
def run():
  print('starting server...')

  # set up server
  port = 8080
  server_address = ('127.0.0.1', port)
  httpd = HTTPServer(server_address, HTTPServer_RequestHandler)

  # run server
  print('running server on port {}...'.format(port))
  httpd.serve_forever()


run()

# We specify the port that we want to listen to messages from, the address 
# of the server (127.0.0.1 is always our own computer, create an HTTPServer 
# that’s built-into Python, but giving it our own HTTPServer_RequestHandler. 
# And finally we run it with the serve_forever function.




