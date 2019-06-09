from flask import Response
@app.route("/")
def hello():
    xml = '<Response><Say>Hello world.</Say></Response>'
    return Response(xml, mimetype='text/xml')