# File Converter

A simple file conversion web application that allows users to convert files between various formats. Currently supports converting images to PDF, PNG, JPEG, and vice versa. Built using Flask, Python, and various libraries for file handling and conversion.

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

