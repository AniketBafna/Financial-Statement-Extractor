import streamlit as st
import pdfplumber
import json
import re
import pandas as pd
import io

# Function to extract text from PDF
def extract_text_from_pdf(pdf_path):
    text_data = []
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            text_data.append(page.extract_text())
    return "\n".join(text_data) if text_data else ""

# Function to extract tables using pdfplumber
def extract_tables_from_pdf(pdf_path):
    extracted_tables = []
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            for table in page.extract_tables():
                df = pd.DataFrame(table)  # Convert table to DataFrame
                extracted_tables.append(df.to_dict(orient='split'))  # Convert table to structured JSON
    return extracted_tables

# Function to clean extracted text
def clean_text(text):
    text = re.sub(r'\n+', '\n', text)  # Remove multiple newlines
    text = re.sub(r'\s+', ' ', text)  # Replace multiple spaces with a single space
    return text.strip()

# Function to parse financial data using regex
def parse_financial_data(text):
    financial_data = {
        "Standalone_Financial_Results": {},
        "Consolidated_Financial_Results": {}
    }

    # Regular expressions to extract financial information
    quarter_pattern = re.compile(r'Quarter ended (\d{1,2} \w+ \d{4})')
    revenue_pattern = re.compile(r'Revenue from operations[\s:]*([\d,\.]+)')
    profit_pattern = re.compile(r'Profit/loss for the period/year[\s:]*([\d,\.]+)')

    matches = quarter_pattern.findall(text)
    for match in matches:
        quarter = match
        revenue_match = revenue_pattern.search(text)
        profit_match = profit_pattern.search(text)

        revenue = float(revenue_match.group(1).replace(',', '')) if revenue_match else None
        profit = float(profit_match.group(1).replace(',', '')) if profit_match else None

        financial_data["Standalone_Financial_Results"][quarter] = {
            "Revenue": revenue,
            "Profit/Loss": profit
        }

    return financial_data

# Function to convert extracted data to JSON format
def convert_to_json(financial_data, tables):
    final_data = {
        "Financial_Statements": financial_data,
        "Extracted_Tables": tables
    }
    return json.dumps(final_data, indent=4)

# Streamlit UI
st.set_page_config(page_title="Financial Statement Extractor", layout="wide")
st.title("📄 Financial Statement Extractor")
st.write("Upload a financial PDF file to extract structured JSON data.")

# File uploader
uploaded_file = st.file_uploader("Upload a PDF file", type="pdf")

if uploaded_file:
    with st.spinner("Processing..."):
        # Save uploaded file
        pdf_path = "uploaded_file.pdf"
        with open(pdf_path, "wb") as f:
            f.write(uploaded_file.read())

        # Extract data
        extracted_text = extract_text_from_pdf(pdf_path)
        cleaned_text = clean_text(extracted_text)
        extracted_tables = extract_tables_from_pdf(pdf_path)
        financial_data = parse_financial_data(cleaned_text)

        # Convert to JSON
        json_output = convert_to_json(financial_data, extracted_tables)

        # Save the JSON as "data (13).json"
        json_filename = "data (13).json"
        with open(json_filename, "w", encoding="utf-8") as json_file:
            json.dump(json_output, json_file, indent=4)

        # Display extracted JSON in Streamlit
        st.subheader("Extracted Financial Data")
        st.json(json_output)

        # Provide download link
        st.subheader("Download JSON Output")
        json_bytes = io.BytesIO(json_output.encode())
        st.download_button(label="Download JSON", data=json_bytes, file_name=json_filename, mime="application/json")
