from flask import Flask, render_template, request
import boto3
import os
app = Flask(__name__)
@app.route('/')
def home():
    return render_template('index.html')
@app.route('/upload', methods=['POST'])
def upload():
    if 'file' not in request.files:
        return "No file part"
    file = request.files['file']
    if file.filename == '':
        return "No selected file"
    # Save uploaded image to /static/uploads/ folder
    filepath = os.path.join('static/uploads', file.filename)
    file.save(filepath)
    # Read image bytes for AWS Rekognition
    with open(filepath, 'rb') as image_file:
        image_bytes = image_file.read()
    client = boto3.client('rekognition', region_name='us-east-1')  #Or your region
    response = client.detect_labels(Image={'Bytes': image_bytes}, MaxLabels=10)
    labels = response['Labels']
    return render_template('result.html', labels=labels, image_path=filepath)
if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0')
