OCR-Based Health Monitoring System with Risk Analysis Using SVM

Overview

This project aims to develop an OCR-based health monitoring system that extracts vital medical information from health reports and performs risk analysis using Support Vector Machine (SVM). The system processes scanned medical documents using Optical Character Recognition (OCR) and applies machine learning techniques to assess potential health risks.

Features

OCR Processing: Extracts text from medical reports using EasyOCR.

Data Preprocessing: Cleans and structures extracted data for analysis.

Machine Learning with SVM: Classifies patients into different risk levels (low, medium, high).

Visualization & Reports: Generates insights for healthcare professionals.

Scalability: Can be integrated with hospital management systems.

Technologies Used

Programming Language: Python

Libraries: OpenCV, EasyOCR, Pandas, NumPy, Scikit-learn, Matplotlib, Seaborn

Machine Learning Model: Support Vector Machine (SVM)

Installation

Prerequisites

Ensure you have Python installed along with the required dependencies:

pip install opencv-python easyocr numpy pandas scikit-learn matplotlib seaborn

Clone the Repository

git clone https://github.com/your-username/ocr-health-risk-analysis.git
cd ocr-health-risk-analysis

Usage

1. Run OCR to Extract Data

from ocr_module import extract_text
text = extract_text('medical_report.jpg')
print(text)

2. Process Extracted Data

from data_processing import clean_data
processed_data = clean_data(text)

3. Perform Risk Analysis Using SVM

from risk_analysis import predict_risk
risk_level = predict_risk(processed_data)
print(f"Predicted Health Risk Level: {risk_level}")

Disclaimer

This system primarily utilizes CPU processing, which may impact performance for large-scale data extraction and analysis. Using GPU acceleration can significantly enhance OCR processing speed, machine learning model training, and overall system efficiency. For optimal results, a GPU-powered setup is recommended.
