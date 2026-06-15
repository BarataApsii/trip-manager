✈️ Trip Manager








📌 Overview

Trip Manager is an internal travel booking management system designed to simplify the process of recording flight bookings, managing customer data, tracking payments, and generating professional travel documents.

It is used after completing bookings on airline websites. Once a booking is made, details are manually entered into the system to generate structured receipts and travel advisories for customers.

🎯 Purpose

Trip Manager helps travel agents or booking officers:

Organize flight booking records
Manage customer information
Track fare breakdowns and service fees
Generate receipts
Create travel advisory documents
Maintain clean financial records
⚙️ Features
👤 Customer Management
✈️ Flight Booking Records (PNR, ticket number, route, date)
💰 Cost Breakdown (Airfare, Taxes, Service Fee)
🧾 Receipt Generation
📄 Travel Advisory PDF Generation
📊 Simple Dashboard Overview
🔄 Workflow
Customer requests booking
        ↓
Booking made on airline website
        ↓
E-ticket received from airline
        ↓
Details entered into Trip Manager
        ↓
System generates:
   • Travel Advisory PDF
   • Receipt with breakdown
        ↓
Sent to customer
🧱 Tech Stack
Python
Django
PostgreSQL
Bootstrap 5
HTML, CSS, JavaScript
WeasyPrint (PDF generation)
🗂️ Project Structure
trip-manager/
│
├── config/              # Django project settings
├── core/                # Shared utilities (PDF, helpers)
├── customers/           # Customer management
├── bookings/            # Flight booking records
├── payments/            # Payment and fare breakdown
├── documents/           # PDF generation (receipt, advisory)
├── templates/           # HTML templates
├── static/              # CSS, JS, images
├── media/               # Uploaded files (tickets)
├── manage.py
└── requirements.txt
📄 Document Outputs

Trip Manager generates:

Travel Advisory
Flight details
Travel instructions
Contact information
Receipt
Booking reference
Cost breakdown
Service fee
Total payment
🚀 Future Improvements
Email delivery of PDFs
SMS notifications
Multi-user roles (admin, staff)
Advanced reporting dashboard
Cloud storage integration (OCI / AWS)
Airline API integration (optional)
⚠️ Important Note

Trip Manager is not an airline ticketing system.
It is a booking management and documentation tool used to organize travel records and generate customer receipts and travel advisories.

📷 Screenshots (Planned)

Add screenshots here later

Dashboard view
Booking entry form
Generated receipt PDF
Travel advisory PDF
👨‍💻 Developer

Apsie Tese
Built for internal travel booking operations and business automation.