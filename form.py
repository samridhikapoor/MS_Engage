import os
import secrets
from PIL import Image
from flask import render_template, url_for, flash, redirect, request


from flask import Flask
app = Flask(__name__)

    


@app.route('/')
def description():
    return render_template('test.html')


if __name__ == '__main__':
    app.run(debug=True, port=8000)