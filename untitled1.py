from flask import Flask, request, render_template, redirect, url_for
import os
from werkzeug.utils import secure_filename
from flask_uploads import UploadSet,IMAGES,configure_uploads
from flask_wtf.file import FileField,FileAllowed,FileRequired

app = Flask(__name__)
basepath=os.path.join(os.getcwd(),'static/uploads')
app.config['UPLOADED_PHOTOS_DEST']=basepath
photos=UploadSet('photos',IMAGES)
configure_uploads(app,photos)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        f = request.files['file']
        basepath = os.path.abspath(os.path.dirname(__file__))
        upload_path = os.path.join(basepath, 'static/uploads')
        name=os.path.join(upload_path,secure_filename(f.filename))
        f.save(name)
        return redirect(url_for('index'))
    return render_template('index.html')

# def FileYZ(Flask)

@app.route('/upload', methods=['GET', 'POST'])
def upload():
    print(basepath)
    if request.method == 'POST':
        f = photos.save(request.files['file'])

        return redirect(url_for('upload'))
    return render_template('upload.html')


if __name__ == '__main__':
    app.run(debug=True)
