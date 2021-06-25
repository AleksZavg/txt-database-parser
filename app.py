from flask import Flask, render_template
from pages import *

from loader import app


@app.route('/')
def index():
    return "This is index page"

if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)

