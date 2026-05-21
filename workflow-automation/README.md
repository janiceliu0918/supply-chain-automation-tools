# Logistics Workflow & Communications Automation Suite 

### 📌 Overview
This repository contains a suite of automation tools designed to reduce manual workload, improve efficiency, and standardize repetitive processes in supply chain and customs operations. 

It tackles two major operational bottlenecks: **manual Outlook email drafting** and **repetitive web navigation for container ETA tracking**.

---

### ⚙️ Core Modules & Features

**1. Outlook Email Automation (AutoHotkey)**
- Generate booking / arrival notification emails automatically
- Reply-all with standardized ETA updates
- Quick "well received" email responses
- Keyboard navigation shortcuts in Outlook

**2. Dynamic ETA Tracking Link Generator (Python)**
- Instantly generates direct tracking URLs based on carrier names and container numbers.
- Bypasses the need for manual navigation through 3PL or carrier websites.

---

### 🚀 Business Impact
- **Time Savings:** Reduced manual email writing time by ~70% and eliminated repetitive web searches, saving hours of administrative work weekly.
- **Improved Responsiveness:** Accelerated response speed in high-volume logistics operations, enabling faster exception management.
- **Process Standardization:** Ensured 100% consistent communication templates and tracking procedures across internal workflows.

---

### ⌨️ Usage & Hotkeys

**Email Automation (Run `outlook_email_automation.ahk`):**
- `Shift + W` → Move up
- `Shift + S` → Move down
- `Alt + N` → New booking email
- `Alt + E` → ETA reply template
- `Alt + W` → "Well received" quick reply

**Tracking Tool (Run `tracking_tool.py`):**
- Input carrier name and container/BL number to output the direct tracking URL.

---

### 🛠️ Tech Stack
- **Languages/Tools:** Python, AutoHotkey (AHK)
- **Integration:** Outlook COM Automation, Web Browser Routing
- **Formatting:** HTML Email Templates

---

### 📂 Project Structure
- `outlook_email_automation.ahk` → Main email automation script
- `tracking_tool.py` → Dynamic tracking URL generator script

---

### ⚠️ Notes
The AHK email script is designed specifically for the Microsoft Outlook desktop client on a Windows environment.
