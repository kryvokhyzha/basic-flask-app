from flask import render_template

from app import app
from app.errors import *


@app.route('/')
def index():
    """
        Rendering index.html template
    """
    return render_template('index.html')
