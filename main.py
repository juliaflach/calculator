#!/usr/bin/env python3
#
from flask import Flask
from routes import index, get_result

## Flask app
app = Flask(__name__)

app.add_url_rule('/', view_func=index)
app.add_url_rule('/', view_func=get_result, methods = ['POST'])

if __name__ == "__main__":
    app.run(host='0.0.0.0', port='8080')
