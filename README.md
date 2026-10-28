# Digital Patient Record System 🩺💻

An open-source, terminal-based Digital Patient Record System developed as a practical software solution for an Object-Oriented Programming (OOP) curriculum. This application models real-world healthcare administration workflows—including patient registration, medical personnel management, and automated conflict-free appointment scheduling.

---

## 🌟 Key Features & Technical Scope

* Object-Oriented Design: Implements a robust multi-class architecture featuring Doctor, Patient, and PatientRecordSystem classes with dedicated attributes, instance behaviors, and class-level tracking (@classmethod).
* Optimized Data Structures: 
  - Dictionaries: Used for rapid O(1) entity lookups by unique IDs.
  - Sets: Utilized (self.booked_slots) to dynamically track and eliminate appointment scheduling conflicts.
  - Tuples: Incorporated for immutable data pairings such as blood groups (type, rh) and appointment timestamps (date, time).
* Automated Scheduling: Automatically calculates the next available weekday morning slot while preventing double-booking across hospital schedules.
* Data Privacy & Local Storage: Centralized cloud storage is avoided; patients maintain complete control over their data through secure, localized text file exports (<Patient_ID>_records.txt).
* Digital Public Goods (DPG) Compliance: Built entirely in standard core Python without commercial software dependencies, ensuring open-source transparency, modular reusability, and inclusive terminal accessibility.

---

## 🛠️ System Architecture

1. Doctor Class: Manages healthcare provider profiles (doctor_id, name, department, speciality) and utilizes class methods to track institutional metrics.
2. Patient Class: Encapsulates individual health demographics and exposes instance methods for profile viewing, appointment updates, rescheduling, and text file exports.
3. PatientRecordSystem Class: Acts as the central command engine managing state registries, input validations (using regular expressions), and the core user interaction loop.

---

## 🌍 Digital Public Goods (DPG) Alignment

- Open-Source & Reusable: Developed using pure standard Python libraries (datetime, re) with zero proprietary dependencies.
- Inclusive & Accessible: Lightweight command-line interface runs efficiently on low-spec systems without requiring high-bandwidth internet.
- Data Sovereignty: User data is processed locally in memory with optional single-patient text file exports to respect individual privacy.
- Modular Design: Clean separation of concerns allows for easy future integration with external databases or web interfaces.

---

## 🚀 Getting Started & Installation

### Prerequisites
- Python 3.x installed on your system.

### Running the Application
1. Clone the repository:
   git clone https://github.com/KumbaFatoma/OOP-Digital-Patient-Record-System.git

2. Navigate to the project directory:
   cd OOP-Digital-Patient-Record-System

3. Run the Python application:
   python patient_record_system.py

---

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details. Designed in alignment with Digital Public Goods (DPG) standards for open-source educational use.
