from flask import Flask, render_template, request
import boto3
import os

app = Flask(__name__)
rekognition = boto3.client('rekognition', region_name='us-east-1')

UPLOAD_FOLDER = 'static/uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    file = request.files['image']
    filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
    file.save(filepath)

    with open(filepath, 'rb') as img_file:
        response = rekognition.detect_labels(
            Image={'Bytes': img_file.read()},
            MaxLabels=10
        )

    labels = [label['Name'] for label in response['Labels']]
    return render_template('result.html', filename=file.filename, labels=labels)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

