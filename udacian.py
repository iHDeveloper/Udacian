from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.parse import parse_qs

form = '''<!DOCTYPE html>
<title>Udacian</title>
<form method="POST">
    <label>Name:
        <input name="name">
    </label>
    <br>
    <label>City:
        <input name="city">
    </label>
    <br>
    <label>Enrollment:
        <input name="enrollment">
    </label>
    <br>
    <label>Nanodegree:
        <input name="nanodegree">
    </label>
    <br>
    <label>Status:
        <input name="status">
    </label>
    <br>
    <button type="submit">Press it!</button>
</form>
<pre>
{}
</pre>
'''

memory = []

class HTTPHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html; charset=utf-8')
        self.end_headers()
        self.wfile.write(form.format("\n".join(memory)).encode())
    def do_POST(self):
        length = int(self.headers.get('Content-length', 0))
        body = self.rfile.read(length).decode()
        params = parse_qs(body)
        name = params["name"][0]
        city = params["city"][0]
        enrollment = params["enrollment"][0].split(" ")
        enrollment = tuple(enrollment)
        nanodegree = params["nanodegree"][0]
        status = params["status"][0]
        udacian = Udacian(name, city, enrollment, nanodegree, status)
        memory.append(udacian.__str__())
        self.send_response(301)
        self.send_header('Location', '/')
        self.end_headers()



class Udacian: 
    def __init__(self, name, city, enrollment, nanodegree, status):
        self.name = name
        self.city = city
        self.enrollment = enrollment
        self.nanodegree = nanodegree
        self.status = status
    def __str__(self):
        return "{} is enrolled in {} studying {} in {} {} with {}, he/she is {}".format(
            self.name,
            self.city,
            self.nanodegree,
            self.enrollment[0],
            self.enrollment[1],
            self.enrollment[2],
            self.status
        )
        
if __name__ == '__main__':
    server_address = ('', 8000)
    httpd = HTTPServer(server_address, HTTPHandler)
    httpd.serve_forever()

# enrollment = ( 'Sat', 'am', 'Ms. Lujuain' )
# udacian = Udacian('Mohammed', 'Riyadh', enrollment, 'FSND', 'on tracking')

