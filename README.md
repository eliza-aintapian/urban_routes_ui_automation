# 🧪 QA-USA Python Automation Project

## 📋 Overview
This project demonstrates **end-to-end test automation** for a web application using **Python + Selenium + Pytest**.  
It was created as part of my QA Engineering work to simulate real-world regression and smoke testing workflows.

The test suite covers user-facing functionality including:
- Navigation and UI validation  
- Login and registration  
- Form submissions and edge cases  
- Search, ordering, and confirmation flows  

All tests are built following **modular, maintainable best practices**, with clear structure and reusable page object methods.

---

## ⚙️ Tools & Technologies
- **Python** — core language  
- **Selenium WebDriver** — browser automation  
- **Pytest** — testing framework and reporting  
- **Git & GitHub** — version control and collaboration  
- **CI/CD with GitHub Actions** — automated test runs on each push  
- **Jira / TestRail (referenced)** — for test case documentation and defect tracking  

---

## 🧠 Test Design & Coverage
Test coverage focuses on both **functional** and **negative** testing scenarios:

| Category | Description |
|-----------|--------------|
| Functional | Validates primary user flows such as login, navigation, and submission |
| Boundary | Tests data limits (field lengths, special characters, numeric edges) |
| Regression | Ensures stability after new code deployments |
| API | (In progress) API-level tests using Postman for backend validation |
| Exploratory | Manual sessions to identify UI/UX inconsistencies |

Example:  
- Login field validation (empty input, special chars, incorrect creds)  
- Navigation element rendering on Chrome/Firefox  
- Form submission with incomplete data  

---

## 🧩 Project Structure
