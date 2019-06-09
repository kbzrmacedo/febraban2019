from flask import Response
from flask import Flask
myapp = Flask(__name__)

@myapp.route("/")
def hello():
    xml = '<Response><Say>Hello world.</Say></Response>'
    return Response(xml, mimetype='text/xml')

if __name__ == '__main__':
    app.run()
