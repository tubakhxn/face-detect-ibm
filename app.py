from flask import Flask, render_template, request, redirect, url_for
import os
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'static/uploads/'
app.config['ALLOWED_EXTENSIONS'] = {'png', 'jpg', 'jpeg'}

if not os.path.exists(app.config['UPLOAD_FOLDER']):
    os.makedirs(app.config['UPLOAD_FOLDER'])

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        description = request.form.get('description', '')
        file = request.files.get('screenshot')
        filename = None
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        # Save description and filename to a simple list (in-memory)
        uploads = []
        if os.path.exists('uploads.txt'):
            with open('uploads.txt', 'r') as f:
                for line in f:
                    uploads.append(line.strip().split('|'))
        if filename:
            uploads.append([filename, description])
            with open('uploads.txt', 'a') as f:
                f.write(f"{filename}|{description}\n")
        return render_template('index.html', uploads=uploads)
    else:
        uploads = []
        if os.path.exists('uploads.txt'):
            with open('uploads.txt', 'r') as f:
                for line in f:
                    uploads.append(line.strip().split('|'))
        return render_template('index.html', uploads=uploads)

if __name__ == '__main__':
    app.run(debug=True)
