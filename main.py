"""
Created by Brian langay
Git user = brian-Lab-0
brianlangay0@gmail.com
at 12-12-2024
"""

#Requred libraries
from http.server import BaseHTTPRequestHandler, HTTPServer
import urllib.parse
from langchain_ollama import OllamaLLM


    """_Model initialization_
    Initialize the Ollama model
    eg model = OllamaLLM(model="minicpm-v")
    choose the model from your installed models 
    model = OllamaLLM(model="llama3")

    """


class RequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        # Parse the prompt from the URL
        parsed_path = urllib.parse.urlparse(self.path)
        prompt = urllib.parse.unquote(parsed_path.path.strip('/'))

        if prompt:
            try:
                # Invoke the Ollama model with the dynamic prompt
                result = model.invoke(input=prompt)

                # Send the model's response back to the client
                self.send_response(200)
                self.send_header('Content-type', 'text/plain')
                self.end_headers()
                self.wfile.write(result.strip().encode('utf-8'))

            except Exception as e:
                # Handle any errors by sending a 500 response
                self.send_response(500)
                self.send_header('Content-type', 'text/plain')
                self.end_headers()
                self.wfile.write(f"Error: {str(e)}".encode('utf-8'))
        else:
            # Handle cases where no prompt is provided
            self.send_response(400)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(b"Bad Request: No prompt provided")

def run(server_class=HTTPServer, handler_class=RequestHandler, port=8089):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f'Starting httpd server on port {port}...')
    httpd.serve_forever()

if __name__ == '__main__':
    run()
