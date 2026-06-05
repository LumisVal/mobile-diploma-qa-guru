📱 Mobile Automation Project







📖 About Project

This project contains automated mobile UI tests for the Wikipedia Android application.

The framework is implemented using Python, Pytest and Appium following the Page Object Model (POM) pattern.

The project demonstrates
Mobile UI Test Automation
Page Object Architecture
Allure Reporting
Allure TestOps Integration
Jenkins CI/CD
BrowserStack Cloud Execution
Real Android Device Testing
🎯 Tested Application
Wikipedia Android

Wikipedia is a free online encyclopedia available through a native Android application.

Official website:

https://www.wikipedia.org/

🛠 Technology Stack
Test Automation
🐍 Python
🧪 Pytest
📱 Appium
Reporting
📊 Allure Report
📝 Allure TestOps
CI/CD
⚙️ Jenkins
Cloud Testing
☁️ BrowserStack
Version Control
🐙 GitHub
✅ Implemented Test Cases
TC-01 Skip onboarding

Verify successful onboarding completion and navigation to the main screen.

TC-02 Search article

Verify article search functionality using a valid query.

TC-03 Open article

Verify opening an article from search results.

TC-04 Open Saved tab

Verify navigation to the Saved section.

TC-05 Open More tab

Verify navigation to the More section.

📂 Project Structure
```text
mobile-diploma-qa-guru
│
├── config
│   ├── context.py
│   └── settings.py
│
├── docs
│   └── screenshots
│
├── pages
│   ├── main_page.py
│   ├── onboarding_page.py
│   └── search_page.py
│
├── tests
│   ├── test_onboarding.py
│   ├── test_search.py
│   ├── test_navigation.py
│   └── test_more.py
│
├── utils
│   └── attachments.py
│
├── .env.bstack
├── .env.credentials
├── .env.local_emulator
├── .env.local_real
│
├── conftest.py
├── pytest.ini
├── requirements.txt
│
├── allure-results
├── allure-report
│
└── README.md
```
Project Structure




🚀 Running Tests
Install dependencies
pip install -r requirements.txt
Run tests
pytest .
Generate Allure results
pytest --alluredir=allure-results
Open Allure Report
allure serve allure-results
⚙️ Jenkins Integration

The project is integrated with Jenkins for automated execution.

Jenkins capabilities
Remote execution
Build history
Allure integration
Continuous Integration workflow
Jenkins Job




📊 Allure Report

Allure Report provides detailed information about test execution.

Features
Test statuses
Execution statistics
Attachments
Execution history
Detailed test information
Allure Overview




Test Details




📝 Allure TestOps

Manual test cases are maintained in Allure TestOps.

Implemented Manual Test Cases
TC-01 Skip onboarding
TC-02 Search article
TC-03 Open article
TC-04 Open Saved tab
TC-05 Open More tab
Test Cases




☁️ BrowserStack Integration

BrowserStack is used to execute tests on real Android devices.

Execution Environment
Device: Google Pixel 8
Platform: Android 14
Framework: Appium + Pytest
BrowserStack Sessions




🎯 Test Coverage

The project covers the following functionality:

Onboarding flow
Search functionality
Article opening
Navigation
Saved section
More section
📈 CI/CD Pipeline
GitHub
   ↓
Jenkins
   ↓
Pytest
   ↓
Appium
   ↓
BrowserStack
   ↓
Allure Report
   ↓
Allure TestOps

## 👨‍💻 Author

> **Leonid Chaliy**  
> QA Automation Engineer  
>
> 🐙 GitHub: https://github.com/LumisVal  
> 📱 Mobile Automation • 🌐 UI Automation • 🔌 API Testing

📌 Diploma Project

This repository was developed as part of the QA Automation Engineer diploma project and demonstrates practical skills in:

Mobile Test Automation
Python Test Framework Development
Page Object Pattern
CI/CD Integration
Reporting & Analytics
Test Management
Real Device Testing