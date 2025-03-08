import pymupdf  # PyMuPDF
from pathlib import Path

def split_pdf_by_toc(pdf_path, level=1):
    if not Path(pdf_path).exists():
        print(f"File not found: {pdf_path}")
        return
    pdf = pymupdf.open(pdf_path)
    toc = pdf.get_toc()
    
    if not toc:
        print('No table of contents found in the PDF file')
        return
    
    # Create output directory
    output_dir = Path(f"divided_{Path(pdf_path).name.replace('.pdf', '')}")
    output_dir.mkdir(parents=True, exist_ok=True)
    
    # Get level 1 TOC entries
    ranges = []
    titles = []
    for entry in toc:
        if entry[0] == level:  # Level 1 entries
            ranges.append(entry[2])  # Page number
            titles.append(entry[1])  # Title
    
    # Process each section
    for i in range(len(ranges)):
        start_page = ranges[i] - 1  # PyMuPDF uses 0-based indexing
        end_page = ranges[i+1] - 1 if i+1 < len(ranges) else pdf.page_count - 1
        
        # Create a new PDF with the selected pages
        new_pdf = pymupdf.open()
        new_pdf.insert_pdf(pdf, from_page=start_page, to_page=end_page)
        
        # Create a safe filename from the title
        safe_title = "".join([c if c.isalnum() or c in [' ', '_', '-'] else '_' for c in titles[i]])
        output_path = output_dir / f"{i+1:02d}_{safe_title}.pdf"
        
        # Save the new PDF
        new_pdf.save(str(output_path))
        new_pdf.close()
        print(f"Created: {output_path}")
    
    pdf.close()
    print(f"Split complete. Files saved to {output_dir}")