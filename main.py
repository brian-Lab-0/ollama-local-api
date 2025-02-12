"""
Created by Brian langay
Git user = brian-Lab-0
brianlangay0@gmail.com
at 12-12-2024
"""

from http.server import BaseHTTPRequestHandler, HTTPServer
import urllib.parse
from langchain_ollama import OllamaLLM

# Global variable to hold the model instance
model = None

class RequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        global model

        # Parse the prompt from the URL path (ignoring any leading/trailing '/')
        parsed_path = urllib.parse.urlparse(self.path)
        prompt = urllib.parse.unquote(parsed_path.path.strip('/'))

        if prompt:
            try:
                # Invoke the Ollama model with the dynamic prompt
                result = model.invoke(input=prompt)

                # Send the model's response back to the client
                self.send_response(200)
                self.send_header('Content-Type', 'text/plain')
                self.end_headers()
                self.wfile.write(result.strip().encode('utf-8'))
            except Exception as e:
                # Handle errors by sending a 500 response with error details
                self.send_response(500)
                self.send_header('Content-Type', 'text/plain')
                self.end_headers()
                error_message = f"Error: {str(e)}"
                self.wfile.write(error_message.encode('utf-8'))
        else:
            # Respond with a 400 error if no prompt is provided
            self.send_response(400)
            self.send_header('Content-Type', 'text/plain')
            self.end_headers()
            self.wfile.write(b"Bad Request: No prompt provided")

def run(server_class=HTTPServer, handler_class=RequestHandler, port=8089):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f"Starting HTTP server on port {port}...")
    httpd.serve_forever()

if __name__ == '__main__':
    # Prompt the user to input the model name before starting the server.
    model_name = input("Enter the model name to use (e.g., 'llama2'): ").strip()
    if not model_name:
        print("No model name provided. Exiting.")
        exit(1)

    # Instantiate the Ollama model with the selected model name.
    model = OllamaLLM(model=model_name)
    print(f"Using model: {model_name}")

    # Start the HTTP server.
    run()
