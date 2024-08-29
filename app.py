from flask import Flask, request, send_file
from PIL import Image
import io
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from pdf2image import convert_from_path
import os
import tempfile

app = Flask(__name__)

@app.route('/')
def index():
    return send_file('templates/index.html')

@app.route('/convert', methods=['POST'])
def convert():
    try:
        file = request.files['file']
        convert_to = request.form['convertTo']
        file_ext = os.path.splitext(file.filename)[1].lower()
        buffer = io.BytesIO()

        if file_ext in ['.png', '.jpg', '.jpeg']:
            image = Image.open(file)
            
            if convert_to == 'pdf':
                # Create a temporary file to save the image
                with tempfile.NamedTemporaryFile(delete=False, suffix='.png') as temp_image_file:
                    image.save(temp_image_file, format='PNG')
                    temp_image_file_path = temp_image_file.name
                
                # Convert the temporary PNG file to PDF
                with tempfile.NamedTemporaryFile(delete=False, suffix='.pdf') as temp_pdf_file:
                    c = canvas.Canvas(temp_pdf_file.name, pagesize=letter)
                    c.drawImage(temp_image_file_path, 0, 0, width=letter[0], height=letter[1])
                    c.save()
                    temp_pdf_file.seek(0)
                    buffer.write(temp_pdf_file.read())
                    
                # Clean up the temporary files
                os.remove(temp_image_file_path)
            else:
                if convert_to == 'jpeg':
                    image = image.convert('RGB')
                image.save(buffer, format=convert_to.upper())
                
        elif file_ext == '.pdf' and convert_to == 'png':
            images = convert_from_path(file)
            images[0].save(buffer, format='PNG')
        else:
            return 'Conversion not supported or invalid file type', 400

        buffer.seek(0)
        return send_file(buffer, as_attachment=True, download_name=f'converted_file.{convert_to}', mimetype=f'image/{convert_to}')
    
    except Exception as e:
        app.logger.error(f"Conversion error: {e}")
        return f"An error occurred during conversion: {e}", 500

if __name__ == '__main__':
    app.run(debug=True)
