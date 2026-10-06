from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.parse import urlparse, parse_qs

from Controller.StudentManagement import StudentManagement
from Config import APP_CONFIG

student_management = StudentManagement()


class Application(BaseHTTPRequestHandler):
    """Handle HTTP requests for the student management system."""

    def send_html(self, content, status=200):
        content = content.encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", "text/html; charset=utf-8")
        self.send_header("Content-Length", str(len(content)))
        self.end_headers()
        self.wfile.write(content)

    def send_static_file(self, path):
        try:
            with open(path, "rb") as file:
                content = file.read()

            self.send_response(200)

            if path.endswith(".css"):
                self.send_header("Content-Type", "text/css")
            elif path.endswith(".jpg"):
                self.send_header("Content-Type", "image/jpeg")
            elif path.endswith(".png"):
                self.send_header("Content-Type", "image/png")

            self.send_header("Content-Length", str(len(content)))
            self.end_headers()
            self.wfile.write(content)

        except FileNotFoundError:
            self.send_html("File Not Found", 404)

    def do_GET(self):
        parsed_url = urlparse(self.path)
        path = parsed_url.path
        query = parse_qs(parsed_url.query)

        if path.startswith("/Public/"):
            file_path = path.lstrip("/")
            self.send_static_file(file_path)
            return

        content = student_management.handle_get(path, query)
        self.send_html(content)

    def do_POST(self):
        content_length = int(self.headers.get("Content-Length", 0))
        body = self.rfile.read(content_length).decode("utf-8")
        data = parse_qs(body)
        path = urlparse(self.path).path

        content = student_management.handle_post(path, data)
        self.send_html(content)


server = HTTPServer((APP_CONFIG["host"], APP_CONFIG["port"]), Application)

print("=================================")
print("Student Management System")
print("Server running at:")
print(f"http://{APP_CONFIG['host']}:{APP_CONFIG['port']}")
print("=================================")

try:
    server.serve_forever()
except KeyboardInterrupt:
    print("\nServer stopped.")
    student_management.close_database()
    server.server_close()