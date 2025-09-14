import os
import sys
import PyPDF2
import fitz  # PyMuPDF

def extract_text(pdf_path):
    """
    Extract text from a PDF file using PyPDF2
    """
    try:
        text = ""
        with open(pdf_path, 'rb') as file:
            reader = PyPDF2.PdfReader(file)
            num_pages = len(reader.pages)
            print(f"Total pages: {num_pages}")
            
            for page_num in range(num_pages):
                page = reader.pages[page_num]
                text += page.extract_text()
                print(f"Extracted text from page {page_num + 1}")
        
        # Save the extracted text to a file
        output_file = os.path.splitext(pdf_path)[0] + "_text.txt"
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(text)
        
        print(f"Text extracted successfully and saved to {output_file}")
        return True
    except Exception as e:
        print(f"Error extracting text: {e}")
        return False

def extract_images(pdf_path):
    """
    Extract images from a PDF file using PyMuPDF (fitz)
    """
    try:
        # Open the PDF
        pdf_document = fitz.open(pdf_path)
        output_dir = os.path.splitext(pdf_path)[0] + "_images"
        
        # Create output directory if it doesn't exist
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)
        
        # Counter for extracted images
        image_count = 0
        
        # Iterate through each page
        for page_num in range(len(pdf_document)):
            page = pdf_document[page_num]
            image_list = page.get_images(full=True)
            
            print(f"Found {len(image_list)} images on page {page_num + 1}")
            
            # Extract each image
            for img_index, img in enumerate(image_list):
                xref = img[0]  # Get the XREF of the image
                base_image = pdf_document.extract_image(xref)
                image_bytes = base_image["image"]
                image_ext = base_image["ext"]
                
                # Save the image
                image_filename = f"{output_dir}/image_p{page_num + 1}_{img_index}.{image_ext}"
                with open(image_filename, "wb") as img_file:
                    img_file.write(image_bytes)
                    image_count += 1
        
        pdf_document.close()
        print(f"Successfully extracted {image_count} images to {output_dir}")
        return True
    except Exception as e:
        print(f"Error extracting images: {e}")
        return False

def merge_pdfs(pdf_paths, output_path):
    """
    Merge multiple PDF files into one
    """
    try:
        merger = PyPDF2.PdfMerger()
        
        # Add each PDF to the merger
        for pdf in pdf_paths:
            merger.append(pdf)
        
        # Write the merged PDF to the output file
        merger.write(output_path)
        merger.close()
        
        print(f"PDFs merged successfully into {output_path}")
        return True
    except Exception as e:
        print(f"Error merging PDFs: {e}")
        return False

def split_pdf(pdf_path, output_dir=None):
    """
    Split a PDF into separate files, one for each page
    """
    try:
        # If no output directory is specified, create one based on the PDF name
        if output_dir is None:
            output_dir = os.path.splitext(pdf_path)[0] + "_split"
        
        # Create output directory if it doesn't exist
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)
        
        # Open the PDF file
        with open(pdf_path, 'rb') as file:
            reader = PyPDF2.PdfReader(file)
            num_pages = len(reader.pages)
            
            # Extract each page and save as a separate PDF
            for page_num in range(num_pages):
                writer = PyPDF2.PdfWriter()
                writer.add_page(reader.pages[page_num])
                
                output_filename = f"{output_dir}/page_{page_num + 1}.pdf"
                with open(output_filename, 'wb') as output_file:
                    writer.write(output_file)
                
                print(f"Page {page_num + 1} saved as {output_filename}")
        
        print(f"PDF split successfully into {num_pages} files in {output_dir}")
        return True
    except Exception as e:
        print(f"Error splitting PDF: {e}")
        return False

def get_pdf_file():
    """
    Get a PDF file path from user input and validate it
    """
    while True:
        pdf_path = input("Enter the path to the PDF file: ").strip()
        
        # Check if the file exists and is a PDF
        if not os.path.exists(pdf_path):
            print("File does not exist. Please enter a valid path.")
        elif not pdf_path.lower().endswith('.pdf'):
            print("File is not a PDF. Please enter a valid PDF file.")
        else:
            return pdf_path

def get_multiple_pdf_files():
    """
    Get multiple PDF file paths from user input
    """
    pdf_paths = []
    
    while True:
        pdf_path = input("Enter the path to a PDF file (or 'done' when finished): ").strip()
        
        if pdf_path.lower() == 'done':
            if len(pdf_paths) < 2:
                print("You need to provide at least 2 PDF files for merging.")
            else:
                break
        elif not os.path.exists(pdf_path):
            print("File does not exist. Please enter a valid path.")
        elif not pdf_path.lower().endswith('.pdf'):
            print("File is not a PDF. Please enter a valid PDF file.")
        else:
            pdf_paths.append(pdf_path)
            print(f"Added {pdf_path} to the list. Total PDFs: {len(pdf_paths)}")
    
    return pdf_paths

def main():
    while True:
        print("\n===== PDF Utility Application =====")
        print("1. Extract text from a PDF")
        print("2. Extract images from a PDF")
        print("3. Merge multiple PDFs into one")
        print("4. Split a PDF into separate files")
        print("5. Exit")
        
        choice = input("\nEnter your choice (1-5): ").strip()
        
        if choice == '1':
            # Extract text
            pdf_path = get_pdf_file()
            extract_text(pdf_path)
        
        elif choice == '2':
            # Extract images
            pdf_path = get_pdf_file()
            extract_images(pdf_path)
        
        elif choice == '3':
            # Merge PDFs
            pdf_paths = get_multiple_pdf_files()
            output_path = input("Enter the output PDF file path: ").strip()
            if not output_path.lower().endswith('.pdf'):
                output_path += '.pdf'
            merge_pdfs(pdf_paths, output_path)
        
        elif choice == '4':
            # Split PDF
            pdf_path = get_pdf_file()
            split_pdf(pdf_path)
        
        elif choice == '5':
            # Exit
            print("Thank you for using the PDF Utility Application. Goodbye!")
            sys.exit(0)
        
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")
        
        input("\nPress Enter to continue...")

if __name__ == "__main__":
    main()