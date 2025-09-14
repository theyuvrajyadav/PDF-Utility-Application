# PDF Utility Application

A Python application for working with PDF files. This utility provides several features for manipulating PDF documents.

## Features

1. **Extract Text**: Extract all text content from a PDF file and save it to a text file.
2. **Extract Images**: Extract all images from a PDF file and save them to a directory.
3. **Merge PDFs**: Combine multiple PDF files into a single PDF document.
4. **Split PDF**: Split a PDF document into separate files, one for each page.

## Requirements

- Python 3.6 or higher
- Required Python packages (install using `pip install -r requirements.txt`):
  - PyPDF2
  - PyMuPDF (fitz)
  - pdfplumber

## Installation

1. Clone or download this repository
2. Install the required packages:

```
pip install -r requirements.txt
```

## Usage

Run the application by executing the main.py file:

```
python main.py
```

Follow the on-screen menu to select the desired operation:

### 1. Extract Text from a PDF

This option extracts all text content from a PDF file and saves it to a text file with the same name as the PDF but with a "_text.txt" suffix.

### 2. Extract Images from a PDF

This option extracts all images from a PDF file and saves them to a directory named after the PDF with "_images" suffix. Images are saved with their original format.

### 3. Merge Multiple PDFs into One

This option allows you to combine multiple PDF files into a single PDF document. You'll be prompted to enter the paths of the PDF files you want to merge and the output file path.

### 4. Split a PDF into Separate Files

This option splits a PDF document into separate files, one for each page. The resulting files are saved in a directory named after the PDF with "_split" suffix.

## Example

```
===== PDF Utility Application =====
1. Extract text from a PDF
2. Extract images from a PDF
3. Merge multiple PDFs into one
4. Split a PDF into separate files
5. Exit

Enter your choice (1-5): 1
Enter the path to the PDF file: document.pdf
Total pages: 5
Extracted text from page 1
Extracted text from page 2
Extracted text from page 3
Extracted text from page 4
Extracted text from page 5
Text extracted successfully and saved to document_text.txt

Press Enter to continue...
```

## Error Handling

The application includes error handling for common issues such as:
- Invalid file paths
- Non-PDF files
- Permission errors
- Corrupted PDF files

## License

This project is open source and available for personal and commercial use.