# Financial Statement Extractor App

## Overview

This Streamlit app extracts standalone and consolidated financial statements from PDF files and converts them into structured JSON format.

## Features

- Upload a PDF file containing financial statements
- Extracts both **text** and **tables** using pdfplumber
- Cleans and processes extracted text using **regex-based parsing**
- Structures the extracted data into JSON format
- Displays the extracted JSON output in Streamlit
- Allows users to **download the JSON output**

## Requirements

Ensure you have the following dependencies installed:

"pip install streamlit pdfplumber pandas"


## How to Run

1. Clone the repository (if applicable) or save the script locally.
2. Navigate to the directory where the script is saved.
3. Run the following command:

"streamlit run app.py"

4. Upload a PDF file and view the extracted results.

## File Structure

```
project-directory/
│-- app.py (Main Streamlit App)
│-- sample_pdfs/ (Optional: Store test PDF files)
│-- requirements.txt (Dependencies)
│-- README.md (This file)
```

## Inference

- The app processes the uploaded PDF to extract text and tables.
- Extracted text is **cleaned** and **parsed using regex** for financial data.
- Extracted tables are structured into JSON format.
- JSON output includes **financial results** and **tables as structured data**.
- Users can **download** the structured JSON for further analysis.

## Challenges & Considerations

- **Variability in PDFs**: Formatting inconsistencies may affect extraction accuracy.
- **OCR Requirement**: If PDFs are scanned images, OCR tools like Tesseract might be needed.
- **Complex Table Structures**: Some financial tables might require advanced parsing techniques.
- **Regex Limitations**: Financial data extraction depends on predictable text patterns.

## Next Steps (Enhancements)

- Implement **OCR for scanned PDFs**.
- Improve **data structuring using advanced NLP models**.
- Enhance **table extraction for better formatting**.
- Deploy the app on **Streamlit Cloud for easy access**.
