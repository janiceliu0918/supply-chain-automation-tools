# 📦 Supply Chain Operations & Data Automation Toolkit

## 📌 Executive Summary
A comprehensive suite of automation tools developed to bridge the gap between traditional logistics operations and data-driven efficiency. This toolkit is designed to eliminate operational bottlenecks, standardize cross-functional communication, and ensure 100% data integrity in high-volume supply chain and customs environments.

---

## 🚀 Core Modules

### 1. B2B Customs Invoice ETL Pipeline (`candata_import`)
An automated data processing pipeline built to ingest unstructured, multi-format commercial invoices and transform them into system-ready formats for customs clearance.
* **Tech Stack:** Python, Pandas, Openpyxl
* **Business Impact:** * Reduced manual data entry time by **90%**.
  * Eliminated critical formatting errors (e.g., scientific notation on tracking numbers), ensuring zero delays in CBSA release submissions.

### 2. Dynamic Vessel ETA Tracking Generator (`eta_tracking`)
A routing tool that instantly generates direct, carrier-specific tracking URLs from raw container or Bill of Lading (BL) numbers.
* **Tech Stack:** Python, Pandas
* **Supported Carriers:** COSCO, ONE, CMA CGM, OOCL, Evergreen
* **Business Impact:** * Bypassed the need for manual navigation through fragmented 3PL websites.
  * Accelerated exception management and improved proactive visibility for inbound shipments.

### 3. Logistics Communications Automation (`autohotkey`)
A workflow optimization script designed to automate repetitive Outlook email drafting, reply workflows, and inbox navigation for logistics coordinators.
* **Tech Stack:** AutoHotkey (AHK), Outlook COM Automation
* **Business Impact:** * Achieved a **~70% reduction** in manual email writing time.
  * Standardized critical communications (Arrival Notices, ETA updates) across internal teams and external stakeholders.

---

## 🧠 Strategic Value
This repository demonstrates a core philosophy: **leveraging lightweight code to solve heavy operational pain points.** By combining Python for data transformation with AHK for workflow execution, this toolkit provides a scalable blueprint for reducing manual overhead, mitigating compliance risks, and empowering Supply Chain Planners to focus on strategic KPI optimization.
