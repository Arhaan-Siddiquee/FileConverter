# File Converter

A simple file conversion web application that allows users to convert files between various formats. Currently supports converting images to PDF, PNG, JPEG, and vice versa. Built using Flask, Python, and various libraries for file handling and conversion.

<img src="https://eu-central.storage.cloudconvert.com/tasks/489659f1-3216-48fd-8325-c13a8e9a31eb/converter.webp?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=cloudconvert-production%2F20240829%2Ffra%2Fs3%2Faws4_request&X-Amz-Date=20240829T181257Z&X-Amz-Expires=86400&X-Amz-Signature=9a7e295cbc1200da7b4941fdf53c2f48199432c8212d5a302ef45915c40a35bc&X-Amz-SignedHeaders=host&response-content-disposition=inline%3B%20filename%3D%22converter.webp%22&response-content-type=image%2Fwebp&x-id=GetObject" alt="Alt text" style="width: desired-width; height: desired-height;">


## Features

- **Convert Images**: Convert PNG, JPEG, and JPG files to PDF.
- **Convert PDFs**: Convert PDF files to PNG.
- **File Upload**: Easy file selection and conversion through a web interface.
- **User-Friendly Interface**: Clean and responsive design with a modern dark theme.

## Technologies Used

- **Flask**: Web framework for building the web application.
- **PIL (Pillow)**: Python Imaging Library for image processing.
- **ReportLab**: Library for generating PDFs.
- **pdf2image**: Converts PDF files to images.
- **HTML/CSS**: For building the front-end interface.

## Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/yourusername/file-converter.git
   cd file-converter
2. **Set Up a Virtual Environment:**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
4. **Run the Application**:
   ```bash
   python app.py


## Project Structure

- **app.py**: The main Flask application file.
- **PIL (Pillow)**: Python Imaging Library for image processing.
- **ReportLab**: Library for generating PDFs.
- **pdf2image**: Converts PDF files to images.
- **HTML/CSS**: For building the front-end interface.
