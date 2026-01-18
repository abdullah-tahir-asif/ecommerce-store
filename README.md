# Tahir Studio

A full-stack e-commerce store built using Python Flask, Bootstrap, and n8n automation. It features real-time data synchronization with Airtable and automated email notifications.

## Features

* Automated user signup via n8n webhooks
* Real-time data storage in Airtable database
* Automated welcome emails upon registration
* Integrated Add to Cart and Checkout system
* "Buy Now" functionality with instant order logging

## Technologies Used

* Python
* Flask
* Bootstrap (Frontend)
* Inline Customized CSS
* n8n (Workflow Automation)
* Airtable (Database)

## How to Run

1. Install Flask and Requests:
   `pip install flask requests`
2. Run `python app.py`
3. Open `http://127.0.0.1:5000/`

## Workflow Details

* **Signup:** Bootstrap Form → n8n Webhook → Airtable + Email Trigger
* **Checkout:** Buy Now Button → n8n Webhook → Airtable Order Log

##Author

*Abdullah Tahir
*Sofware Engineering student
