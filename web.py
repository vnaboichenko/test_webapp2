import webapp2

class HelloWebapp2(webapp2.RequestHandler):
    def get(self):
#        import ipdb
#        ipdb.set_trace()
        if self.request.headers.environ.get('HTTP_ACCEPT') :
            self.response.write("{'message': 'Good Morning'}")
        else:
            self.response.write("<p>Hello, World</p>")

app = webapp2.WSGIApplication([
    ('/', HelloWebapp2),
], debug=True)

def main():
    from paste import httpserver
    httpserver.serve(app, host='127.0.0.1', port='8080')

if __name__ == '__main__':
    main()
