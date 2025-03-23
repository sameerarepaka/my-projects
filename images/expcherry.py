# import cherrypy
# class MyApp:
#     # @cherrypy.expose
#     def text(self):
#         return "This is a plain text response!"
#     # @cherrypy.expose
#     def html(self):
#         return """
#     <!DOCTYPE html>
#     <html>
#     <head>
#         <title>CherryPy HTML</title>
#     </head>
#     <body>
#         <h1>Hello!!! This is a CherryPy Experiment</h1>
#         <p>This is a HTML page served by cherrypy.</p>
#     </body>
#     <html>
# """
#     @cherrypy.expose
#     def external_html(self):
#         return open('externl_page.html').read()
# if __name__=='__main__':
#     cherrypy.config.update({"server.socket_host":"127.0.0.1",
#         "server.socket_port":8086})
       
#     cherrypy.quickstart(MyApp())

import cherrypy
import os

class MyApp:
    @cherrypy.expose
    def index(self):
        return "This is a plain text response!"

    @cherrypy.expose
    def external_html(self):
        # Set the Content-Type for HTML
        cherrypy.response.headers['Content-Type'] = 'text/html'
        try:
            # Ensure the file path is correct
            file_path = os.path.join(os.path.dirname(__file__), 'external_page.html')
            with open(file_path, 'r') as f:
                return f.read()
        except FileNotFoundError:
            return "Error: external_page.html not found."

    @cherrypy.expose
    def expcherry(self):
        # Set the Content-Type for HTML
        cherrypy.response.headers['Content-Type'] = 'text/html'
        return """
        <html>
            <head>
                <title>CherryPy HTML Page.</title>
            </head>
            <body>
                <h1>Hello! Welcome to CherryPy Experiment Module!</h1>
                <p>This is an HTML page served by CherryPy.</p>
            </body>
        </html>
        """

if __name__ == '__main__':
    # Start the CherryPy application
    cherrypy.config.update({"server.socket_host":"0.0.0.0",
         "server.socket_port":8093})
       
    cherrypy.quickstart(MyApp())
