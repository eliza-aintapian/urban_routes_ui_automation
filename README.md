# 🧪 Urban Routes – Python Test Automation Project

## 📋 Overview
This project automates **end-to-end testing** for the Urban Routes web application — a training app for practicing functional and regression testing.  
The goal is to validate key user journeys such as selecting locations, choosing a ride plan, adding payment details, and placing an order.  

The test suite is written in **Python**, using **Selenium WebDriver** and **Pytest**, following modular **Page Object Model (POM)** principles to keep tests maintainable and reusable.

---

## ⚙️ Tools & Technologies
- **Python** – programming language  
- **Selenium WebDriver** – browser automation  
- **Pytest** – test framework and reporting  
- **Git & GitHub** – version control  
- **ChromeDriver** – browser driver for local runs  
- *(Optionally)* **GitHub Actions** – CI/CD test automation  

---

## 🧠 Test Coverage

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

## 🧩 Project Structure
