# 🧠 Form Automation with Selenium

This is a Python automation project that uses Selenium to automatically fill out a local HTML form with validated user input. It includes input validation using regular expressions, modularized code for better structure, and a simple local form interface.

## 🚀 Features

- Automatically fills HTML forms using Selenium
- Input validation for name, email, and message
- Clean and modular Python code
- Localhost-ready HTML form
- Useful for learning Selenium, automation, and input validation

## 📁 Project Structure

form-automation-selenium/ ├── automation.py          # Handles the Selenium automation logic ├── form.html              # The local HTML form ├── form_inputs.py         # Gets and stores user input ├── input_validation.py    # Validates name, email, and message ├── run.py                 # Main runner script ├── requirements.txt       # Required Python packages └── README.md              # Project documentation

## ⚙️ Requirements

- Python 3.8+
- Google Chrome
- ChromeDriver installed and added to PATH

Install the required packages:

`bash
pip install -r requirements.txt

🧪 How to Run

1. Make sure your ChromeDriver version matches your installed Chrome browser.


2. Run a local server to host the form.html. For example:



python -m http.server

Then open the form in your browser at localhost

3. Execute the automation script:



python run.py

🧹 Input Validation

The form inputs are validated based on the following rules:

Name: Only English letters and spaces (no numbers or symbols)

Email: Must be in valid email format (example@gmail.com)

Message: anything is allowed


📦 Packages Used

selenium

re (built-in)

time (built-in)


🪪 License

This project is licensed under the MIT License.

Feel free to contribute or fork the project if you find it useful!
