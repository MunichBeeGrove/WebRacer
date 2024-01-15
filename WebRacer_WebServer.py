import http.server
import socketserver
import RunRace

PORT = 8000

class MyHttpRequestHandler(http.server.SimpleHTTPRequestHandler):
    initialized = False
    NUMBER_OF_RACERS = 6
    standing = list()
    not_finished = True
    
    def initialize(self):
        MyHttpRequestHandler.standing = list()
        MyHttpRequestHandler.not_finished = True
        for _ in range (MyHttpRequestHandler.NUMBER_OF_RACERS):
            MyHttpRequestHandler.standing.append(1)
        MyHttpRequestHandler.initialized = True
    
    
    def do_GET(self):
        
        if MyHttpRequestHandler.initialized == False:
            self.initialize()
            
        if self.path == '/':
            self.initialize()
            self.path = './StarterPage.html'
        elif self.path == '/MinimalisticRefresh.html':
            #next step in the race
            print("Before " + str(MyHttpRequestHandler.standing))
            self.not_finished = RunRace.next_step(MyHttpRequestHandler.standing, MyHttpRequestHandler.not_finished)
            print("Serving Minimalistic")
            print (MyHttpRequestHandler.standing)
        return http.server.SimpleHTTPRequestHandler.do_GET(self)
    

        
Handler = MyHttpRequestHandler

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("serving at port", PORT)
    httpd.serve_forever()
