from flask import Flask, request, send_file
from PIL import Image
import io
from reportlab.pdfgen import canvas
from pdf2image import convert_from_path
import os

app = Flask(__name__)

@app.route('/')
def index():
    return send_file('templates/index.html')

@app.route('/convert', methods=['POST'])
def convert():
    file = request.files['file']
    convert_to = request.form['convertTo']
    file_ext = os.path.splitext(file.filename)[1].lower()

    if file_ext in ['.png', '.jpg', '.jpeg']:
        image = Image.open(file)
        buffer = io.BytesIO()
        if convert_to == 'pdf':
            c = canvas.Canvas(buffer)
            c.drawImage(io.BytesIO(image.tobytes()), 0, 0, width=image.width, height=image.height)
            c.save()
        else:
            if convert_to == 'jpeg':
                image = image.convert('RGB')
            image.save(buffer, format=convert_to.upper())
    elif file_ext == '.pdf' and convert_to == 'png':
        images = convert_from_path(file)
        buffer = io.BytesIO()
        images[0].save(buffer, format='PNG')
    else:
        return 'Conversion not supported', 400

    buffer.seek(0)
    return send_file(buffer, as_attachment=True, attachment_filename=f'converted_file.{convert_to}', mimetype=f'image/{convert_to}')

if __name__ == '__main__':
    app.run(debug=True)
