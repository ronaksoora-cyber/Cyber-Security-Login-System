# 🛡️ Smart Cyber Security Login System with Fake URL Detection

![Python](https://img.shields.io/badge/Python-3.x-blue)




![Tkinter](https://img.shields.io/badge/GUI-Tkinter-green)




![SQLite](https://img.shields.io/badge/Database-SQLite3-orange)




![Status](https://img.shields.io/badge/Status-Complete-brightgreen)

## Overview

A Python-based desktop application that combines **secure user authentication** with an intelligent **Fake URL Detection engine**. 



##  Features

-  **Secure Login System** — SHA-256 cryptographic password hashing
-  **Password Strength Analyzer** — Real-time 4-parameter evaluation
-  **Strong Password Generator** — One-click secure password creation
-  **Show/Hide Password** — Toggle password visibility
-  **Fake URL Detection** — Rule-based phishing URL analyzer
-  **Threat Classification** — Color-coded Safe/Suspicious/Dangerous
-  **URL History Log** — Session-wise scanned URL records
-  **Real-time Clock** — Live timestamp on dashboard



##  Technologies Used

 Technology                 |                 Purpose 

 Python 3.x                 |          Core programming language 
 Tkinter                    |           GUI development 
 SQLite3                    |           Local database storage 
 hashlib (SHA-256)          |             Password hashing 
 time                       |              Real-time clock 


##  Repository Structure

Cyber-Security-Login-System/

 main.py                  # Complete project source code
 1_SHA256_Hashing.py      # SHA-256 cryptographic hashing
 2_Password_Strength.py   # Password strength analyzer
 3_SQLite_Database.py     # Database security implementation
 4_Tkinter_GUI.py         # GUI development with Tkinter
 5_URL_Detection.py       # Fake URL detection engine
 README.md                # Project documentation



##  How to Run

**1. Clone the repository:**

git clone https://github.com/ronaksoora-cyber/Cyber-Security-Login-System.git

**2. Install required library:**

pip install pillow

**3. Run the project:**

python main.py



##  How URL Detection Works

 Indicator                                                |           Score  

 '@' symbol in URL                                        |            +20 
 HTTP instead of HTTPS                                    |            +20 
 Hyphens in domain                                        |            +10 
 URL length > 30 chars                                    |            +10 
 Suspicious keywords (login, verify, bank, free, bonus)   |          +10 each 





Fake Score             |               Verdict 

 0 - 39                |               Safe 
 40 - 69               |             Suspicious 
 70 - 100              |             Dangerous 


 
