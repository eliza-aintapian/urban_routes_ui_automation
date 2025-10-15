# Urban Routes – Python Test Automation Project

## Overview
This project automates **end-to-end testing** for the Urban Routes web application — a training app for practicing functional and regression testing.  
The goal is to validate key user journeys such as selecting locations, choosing a ride plan, adding payment details, and placing an order.  

The test suite is written in **Python**, using **Selenium WebDriver** and **Pytest**, following modular **Page Object Model (POM)** principles to keep tests maintainable and reusable.

---

## Tools & Technologies
- **Python** – programming language  
- **Selenium WebDriver** – browser automation  
- **Pytest** – test framework and reporting  
- **Git & GitHub** – version control  
- **ChromeDriver** – browser driver for local runs  
- *(Optionally)* **GitHub Actions** – CI/CD test automation  

---

## Test Coverage

| Feature | Description |
|----------|--------------|
| Route setup | Selects pickup and destination points |
| Plan selection | Chooses “Supportive” plan and validates it |
| Phone input | Enters phone number and confirmation code |
| Payment | Adds card number and code |
| Driver message | Adds a note for the driver |
| Add-ons | Orders blankets/handkerchiefs and ice cream |
| Order flow | Confirms order and validates “Car search” modal |

Each test uses clean, modular functions from `pages.py` and relies on test data constants from `data.py`.

---

## Project Structure
QA-USA-Python_Automation/
│
├── data.py # Test data and constants (URLs, input data)
├── helpers.py # Utility functions (URL check, phone code retrieval)
├── pages.py # Page Object Model with reusable UI element locators and methods
├── main.py # Test suite with Pytest test cases
├── requirements.txt # Dependencies
└── README.md # Project documentation

---

## How to Run the Tests Locally

**1. Clone the repository**
git clone https://github.com/eliza-aintapian/QA-USA-Python_Automation.git
cd QA-USA-Python_Automation
2. Create & activate a virtual environment
python -m venv venv
source venv/bin/activate     # Mac/Linux
venv\Scripts\activate        # Windows
3. Install dependencies
pip install -r requirements.txt
4. Run all tests
pytest -v
You can also run individual tests by specifying the file or test name:

pytest -v main.py::TestUrbanRoutes::test_fill_card

Example Test Flow
Test: test_order_2_ice_creams()

Opens the Urban Routes page.

Sets pickup and destination locations.

Selects the “Supportive” plan.

Adds two ice creams via the counter button.

Verifies the counter shows 2.

This test checks the correct increment of item counters and ensures UI responsiveness.

Key Concepts Demonstrated
Page Object Model (POM) for maintainability

Reusable locators and methods

Assertions for validation of test results

Modular structure for scalability

Good QA practices: setup/teardown, data isolation, and readable reports

Security & Privacy Notice
All test data in this project (addresses, phone numbers, card numbers) are mock values created for educational purposes.
No real user information or production systems are accessed.

## Author
**Eliza Aintapian**  
QA Engineer | Manual + Automation | API | Web | Mobile Testing  
📧 eliza.aintapian@gmail.com  
🔗 [LinkedIn](https://www.linkedin.com/in/eliza-aintapian/)
