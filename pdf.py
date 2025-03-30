import os
from PyPDF2 import PdfReader, PdfWriter

def split_pdf(input_pdf, output_dir, pages_per_section=10):
    """
    Splits a PDF into smaller PDFs with a specified number of pages per section.

    Args:
        input_pdf (str): Path to the input PDF file.
        output_dir (str): Directory to save the output PDFs.
        pages_per_section (int): Number of pages per output PDF.
    """
    # Ensure the output directory exists
    os.makedirs(output_dir, exist_ok=True)

    # Read the input PDF
    reader = PdfReader(input_pdf)
    total_pages = len(reader.pages)

    # Split the PDF into sections
    for start_page in range(0, total_pages, pages_per_section):
        writer = PdfWriter()

        # Get the range of pages for the current section
        end_page = min(start_page + pages_per_section, total_pages)
        for page_number in range(start_page, end_page):
            writer.add_page(reader.pages[page_number])

        # Save the current section to a new PDF
        output_pdf = os.path.join(output_dir, f"section_{start_page + 1}_to_{end_page}.pdf")
        with open(output_pdf, "wb") as output_file:
            writer.write(output_file)

        print(f"Saved: {output_pdf}")

# Example usage
input_pdf_path = "PDFName.pdf"  # Replace with your PDF path
output_directory = "OutputFolder"  # Replace with your desired output folder
pages_per_file = 10  # Number of pages per section

split_pdf(input_pdf_path, output_directory, pages_per_file)
