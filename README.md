# Ford Tax Systems AI Copilot

## Overview

This project simulates an enterprise **Tax Systems Monitoring Platform** similar to architectures used in large organizations such as Ford.

The application demonstrates how AI agents and analytics dashboards can support finance and tax teams in monitoring transactions, validating invoices, detecting system issues, and understanding tax system workflows.

The project is designed as a learning prototype inspired by enterprise tax platforms such as **Vertex O Series**, **Tax Data Hub**, and middleware integrations used in modern financial systems.

---

## Live Demo

Try the application:

Streamlit App
https://your-streamlit-link.streamlit.app

---

## Key Features

### Transaction Monitoring

Displays financial transaction data and visualizations to monitor system activity.

### Invoice vs Purchase Order Validation

Automatically detects invoice anomalies where invoice amounts exceed approved purchase orders.

### Integration Monitoring

Simulates enterprise system monitoring across systems such as ERP, Tax Engines, and Reporting Platforms.

### AI Tax Systems Copilot

An AI assistant that answers common questions about enterprise tax systems.

Example questions:

* What is tax determination?
* What is Vertex?
* How does tax reporting work?

---

## System Architecture

```
Transactional Systems
(ERP / Billing Platforms)
        ↓
Integration Layer
(Middleware / ETL)
        ↓
Tax Determination Engine
(Vertex Simulation)
        ↓
Tax Reporting Platform
(Tax Data Hub Simulation)
        ↓
AI Copilot Monitoring Layer
- Transaction Monitoring
- Invoice Validation
- Integration Health
- AI Assistant
```

---

## Project Structure

```
ford-tax-ai-copilot
│
├── agents
│   ├── finance_agent.py
│   ├── monitoring_agent.py
│   ├── tax_agent.py
│   └── ai_assistant.py
│
├── dashboard
│   └── dashboard.py
│
├── data
│   ├── transactions.csv
│   └── invoices.csv
│
├── requirements.txt
└── README.md
```

---

## Technologies Used

* Python
* Streamlit
* Pandas
* Scikit-learn
* AI Agent Design Patterns

---

## Running the Project Locally

Clone the repository:

git clone https://github.com/srikrishnaprofessional-gif/ford-tax-ai-copilot.git

Navigate into the project folder:

cd ford-tax-ai-copilot

Install dependencies:

pip install -r requirements.txt

Run the application:

streamlit run dashboard/dashboard.py

---

## Example Use Cases

Enterprise organizations rely on tax engines and financial systems to manage global tax compliance. This prototype demonstrates how AI tools can help analysts:

* Monitor transaction flows
* Validate financial governance controls
* Detect anomalies in invoice data
* Monitor system integrations
* Explain enterprise tax architecture

---

## Author

Srikrishna Ganapathy
Program & Delivery Professional – AI, Finance Systems, and Enterprise Transformation

LinkedIn
https://www.linkedin.com/in/sri-krishna-r-g-63715358

GitHub
https://github.com/srikrishnaprofessional-gif
