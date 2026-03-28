# sacco-smartloan
Loan calculator
FastAPI Mini Loan Application
Overview

This is a beginner-friendly FastAPI application that allows SACCO members to request loans based on their salary. The app calculates loan eligibility, monthly repayment, interest and provides a credit score. Loan requests are approved or rejected based on SACCO rules.

Features

Approve or reject loan requests based on 1/3 salary rule and maximum loan limit (4× net salary)

Calculate monthly repayment, interest and total loan

Display loan request history

Simple credit score evaluation (Low / Medium / High Risk)

Easy-to-understand Jinja2 HTML interface

System Requirements

Python 3.10+

OS: Windows / Linux / MacOS

Tools: VS Code, PyCharm or any code editor

Installation Instructions
1. Clone the repository
2. https://github.com/LAURASOY1/sacco-smartloan
cd fastapi-loan-app
3. Create a virtual environment
python -m venv venv
# Activate environment
source venv/bin/activate    # Linux / Mac
venv\Scripts\activate       # Windows
3. Install dependencies
pip install fastapi uvicorn jinja2
4. Create templates directory

Ensure you have a folder called templates with the index.html file inside.

mkdir templates
# Add index.html inside this folder
Running the App

Start the FastAPI server:

uvicorn main:app --reload

Open your browser and navigate to:

http://127.0.0.1:8000
Usage

Fill in your name, salary, loan amount and number of months.

Click Submit.

View approval status, repayment details, credit score and loan history.

File Structure
fastapi-loan-app/
├── main.py            # FastAPI app
├── templates/
│   └── index.html     # HTML template for UI
├── README.md          # Installation & usage guide
└── requirements.txt   # Optional for dependencies
