import PyPDF2
import zipfile
import os

def extract_images_from_pdf(pdf_path, md_file_path):
  """Extracts images from a PDF and creates a Markdown file with image links.

  Args:
    pdf_path: Path to the PDF file.
    md_file_path: Path to the output Markdown file.
  """

  with open(pdf_path, 'rb') as pdf_file:
    pdf_reader = PyPDF2.PdfReader(pdf_file)

    with open(md_file_path, 'w') as md_file:
      for page_num in range(len(pdf_reader.pages)):
        page = pdf_reader.pages[page_num]
        for image in page.images:
          image_data = image.data
          image_ext = "png"
          image_filename = f"image_{page_num}_{image.name}.{image_ext}"
          # Write the image to a file
          with open(image_filename, 'wb') as image_file:
            image_file.write(image_data)
          # Write the Markdown image link to the MD file
          md_file.write(f"![{image_filename}]({image_filename})\n")

# Example usage:
pdf_file = "aws.pdf"
md_file = "extracted_images.md"
extract_images_from_pdf(pdf_file, md_file)