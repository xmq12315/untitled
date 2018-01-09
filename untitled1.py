from flask import Flask, request, render_template, redirect, url_for
import os
from werkzeug.utils import secure_filename

app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('index.html')


@app.route('/upload', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        f = request.files['file']
        basepath = os.path.abspath(os.path.dirname(__file__))
        upload_path = os.path.join(basepath, 'static/uploads')
        f.save(upload_path, secure_filename(f.filemame))
        return redirect(url_for('hello_world'))
    return render_template('index.html')


if __name__ == '__main__':
    app.run()
