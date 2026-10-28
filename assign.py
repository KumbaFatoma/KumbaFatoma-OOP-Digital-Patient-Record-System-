from datetime import datetime, timedelta
import re

# ==========================
# DOCTOR CLASS
# ==========================

class Doctor:
    total_doctors = 0

    def __init__(self, doctor_id, name, department, speciality):
        self.doctor_id = doctor_id
        self.name = name
        self.department = department
        self.speciality = speciality

        Doctor.total_doctors += 1

    def display_details(self):
        print("\nDoctor Details")
        print(f"Doctor ID   : {self.doctor_id}")
        print(f"Name        : {self.name}")
        print(f"Department  : {self.department}")
        print(f"Speciality  : {self.speciality}")

    @classmethod
    def get_total_doctors(cls):
        print(f"\nTotal Doctors: {cls.total_doctors}")

    @classmethod
    def hospital_message(cls):
        print(
            "\nDoctors are available Monday-Friday "
            "from 9:00 AM to 5:00 PM."
        )


# ==========================
# PATIENT CLASS
# ==========================

class Patient:
    total_patients = 0

    def __init__(self, patient_id, name, age, blood_group):
        self.patient_id = patient_id
        self.name = name
        self.age = age
        self.blood_group = blood_group

        self.doctor = None
        self.appointment = None

        Patient.total_patients += 1

    def assign_doctor(self, doctor):
        self.doctor = doctor

    def schedule_appointment(self, appointment):
        self.appointment = appointment

    # ==========================
    # CANCEL APPOINTMENT
    # ==========================

    def cancel_appointment(self):
        if self.appointment:
            print(
                f"\nAppointment on {self.appointment[0]}"
                f" at {self.appointment[1]} cancelled."
            )

            self.appointment = None

        else:
            print("\nNo appointment exists.")

    # ==========================
    # RESCHEDULE APPOINTMENT
    # ==========================

    def reschedule_appointment(self, appointment):
        self.appointment = appointment

        print("\nAppointment rescheduled successfully.")
        print(f"Date : {appointment[0]}")
        print(f"Time : {appointment[1]}")

    # ==========================
    # DISPLAY PATIENT INFORMATION
    # ==========================

    def display_info(self):
        print("\n===================================")
        print("PATIENT PROFILE")
        print("===================================")

        print(f"Patient ID   : {self.patient_id}")
        print(f"Name         : {self.name}")
        print(f"Age          : {self.age}")

        print(
            f"Blood Group  : "
            f"{self.blood_group[0]}{self.blood_group[1]}"
        )

        if self.doctor:
            print(f"Doctor       : {self.doctor.name}")
            print(f"Department   : {self.doctor.department}")

        if self.appointment:
            print(
                f"Appointment  : "
                f"{self.appointment[0]} at {self.appointment[1]}"
            )
        else:
            print("Appointment  : None")

    # ==========================
    # SAVE PATIENT RECORDS TO FILE
    # ==========================

    def save_records_to_file(self):
        filename = f"{self.patient_id}_records.txt"

        try:
            with open(filename, "w", encoding="utf-8") as file:

                file.write("DIGITAL PATIENT RECORD SYSTEM\n")
                file.write("===================================\n")
                file.write("PATIENT PROFILE\n")
                file.write("===================================\n")

                file.write(f"Patient ID   : {self.patient_id}\n")
                file.write(f"Name         : {self.name}\n")
                file.write(f"Age          : {self.age}\n")

                file.write(
                    f"Blood Group  : "
                    f"{self.blood_group[0]}{self.blood_group[1]}\n"
                )

                if self.doctor:
                    file.write(f"Doctor       : {self.doctor.name}\n")
                    file.write(
                        f"Department   : {self.doctor.department}\n"
                    )
                    file.write(
                        f"Speciality   : {self.doctor.speciality}\n"
                    )
                else:
                    file.write("Doctor       : Not assigned\n")

                if self.appointment:
                    file.write(
                        f"Appointment Date : {self.appointment[0]}\n"
                    )
                    file.write(
                        f"Appointment Time : {self.appointment[1]}\n"
                    )
                else:
                    file.write("Appointment  : None\n")

            print("\nYour records have been saved successfully!")
            print(f"File name: {filename}")
            print("Location: Current working directory.")

        except OSError as error:
            print("\nUnable to save your records.")
            print(f"Error: {error}")

    # ==========================
    # TOTAL PATIENTS
    # ==========================

    @classmethod
    def get_total_patients(cls):
        print(f"\nTotal Patients: {cls.total_patients}")

    # ==========================
    # PATIENT POLICY
    # ==========================

    @classmethod
    def patient_policy(cls):
        print("\nPatient records are stored securely.")
        print("The system follows DPG principles.")


# ==========================
# PATIENT RECORD SYSTEM
# ==========================

class PatientRecordSystem:

    patient_counter = 1000

    def __init__(self):
        self.patients = {}
        self.booked_slots = set()

        self.doctors = {
            1: Doctor(
                "D101",
                "Dr. Augusta Abu",
                "Cardiology",
                "Heart Disease"
            ),

            2: Doctor(
                "D102",
                "Dr. Michaella Smith",
                "Paediatrics",
                "Child Healthcare"
            ),

            3: Doctor(
                "D103",
                "Dr. Kemliana Sellu",
                "Dermatology",
                "Skin Conditions"
            ),

            4: Doctor(
                "D104",
                "Dr. David Koroma",
                "Orthopaedics",
                "Bone and Joint Care"
            ),

            5: Doctor(
                "D105",
                "Dr. Kumba Kamara",
                "General Medicine",
                "Routine Checkup and General Consultation"
            )
        }

    # ==========================
    # GENERATE PATIENT ID
    # ==========================

    @classmethod
    def generate_patient_id(cls):
        cls.patient_counter += 1
        return f"P{cls.patient_counter}"

    # ==========================
    # DISPLAY SYSTEM INFORMATION
    # ==========================

    @classmethod
    def display_system_info(cls):
        print("\nDIGITAL PATIENT RECORD SYSTEM")
        print(
            "Provides appointment management "
            "and patient tracking."
        )

    # ==========================
    # SHOW AVAILABLE DOCTORS
    # ==========================

    def show_doctors(self):
        print("\nAVAILABLE DOCTORS")

        for key, doctor in self.doctors.items():
            print("\n--------------------------------")
            print(f"{key}. {doctor.name}")
            print(f"Department : {doctor.department}")
            print(f"Speciality : {doctor.speciality}")

    # ==========================
    # ASSIGN APPOINTMENT
    # ==========================

    def assign_appointment(self):
        appointment_date = datetime.now() + timedelta(days=1)

        # Skip weekends
        while appointment_date.weekday() >= 5:
            appointment_date += timedelta(days=1)

        appointment_time = datetime.strptime("09:00", "%H:%M")

        slot = (
            appointment_date.strftime("%d/%m/%Y"),
            appointment_time.strftime("%H:%M")
        )

        while slot in self.booked_slots:
            appointment_time += timedelta(minutes=30)

            if appointment_time.hour >= 17:
                appointment_date += timedelta(days=1)

                while appointment_date.weekday() >= 5:
                    appointment_date += timedelta(days=1)

                appointment_time = datetime.strptime("09:00", "%H:%M")

            slot = (
                appointment_date.strftime("%d/%m/%Y"),
                appointment_time.strftime("%H:%M")
            )

        self.booked_slots.add(slot)

        print("\nDoctor Assigned Appointment")
        print(f"Date : {slot[0]}")
        print(f"Time : {slot[1]}")

        return slot

    # ==========================
    # RESCHEDULE APPOINTMENT
    # ==========================

    def reschedule_by_doctor(self, patient):
        print("\nReschedule request received.")

        new_date = datetime.now() + timedelta(days=3)

        while new_date.weekday() >= 5:
            new_date += timedelta(days=1)

        new_slot = (
            new_date.strftime("%d/%m/%Y"),
            "10:00"
        )

        while new_slot in self.booked_slots:
            new_date += timedelta(days=1)

            while new_date.weekday() >= 5:
                new_date += timedelta(days=1)

            new_slot = (
                new_date.strftime("%d/%m/%Y"),
                "10:00"
            )

        self.booked_slots.add(new_slot)

        patient.reschedule_appointment(new_slot)

    # ==========================
    # REGISTER PATIENT
    # ==========================

    def register_patient(self):
        print("\nNEW PATIENT REGISTRATION")

        # Validate name
        while True:
            name = input("Enter Name: ").strip()

            if name and re.fullmatch(r"[A-Za-z .'-]+", name):
                break

            print("Enter a valid name using letters and spaces.")

        # Validate age
        while True:
            age = input("Enter Age: ").strip()

            if age.isdigit() and int(age) > 0:
                age = int(age)
                break

            print("Age must be a positive number.")

        # Validate blood type
        blood_type = input(
            "Enter Blood Type (A/B/AB/O): "
        ).strip().upper()

        while blood_type not in ("A", "B", "AB", "O"):
            print("Invalid blood type.")
            blood_type = input(
                "Enter Blood Type (A/B/AB/O): "
            ).strip().upper()

        # Validate RH factor
        rh = input("Enter RH Factor (+/-): ").strip()

        while rh not in ("+", "-"):
            print("RH factor must be + or -.")
            rh = input("Enter RH Factor (+/-): ").strip()

        blood_group = (blood_type, rh)

        patient_id = self.generate_patient_id()

        patient = Patient(
            patient_id,
            name,
            age,
            blood_group
        )

        # Select doctor
        self.show_doctors()

        while True:
            choice = input("\nSelect Doctor: ").strip()

            if choice.isdigit() and int(choice) in self.doctors:
                doctor = self.doctors[int(choice)]
                patient.assign_doctor(doctor)
                break

            print("Invalid doctor choice.")

        # Assign appointment
        appointment = self.assign_appointment()
        patient.schedule_appointment(appointment)

        # Store patient in dictionary
        self.patients[patient.patient_id] = patient

        print("\nRegistration Successful!")
        print(f"Patient ID: {patient.patient_id}")
        print("Please keep your Patient ID for future login.")

    # ==========================
    # PATIENT LOGIN DASHBOARD
    # ==========================

    def login_patient(self):
        patient_id = input("\nEnter Patient ID: ").strip()

        if patient_id not in self.patients:
            print("\nPatient not found.")
            print(
                "Note: This version stores records in memory "
                "while the program is running."
            )
            return

        patient = self.patients[patient_id]

        while True:
            print("\n================================")
            print(f"Welcome {patient.name}")
            print("PATIENT DASHBOARD")
            print("================================")

            print("1. View Profile")
            print("2. View Appointment")
            print("3. Request Reschedule")
            print("4. Cancel Appointment")
            print("5. Save My Records to File")
            print("0. Logout")

            choice = input("\nChoose Option: ").strip()

            if choice == "1":
                patient.display_info()

            elif choice == "2":
                if patient.appointment:
                    print("\nAPPOINTMENT DETAILS")
                    print(f"Date : {patient.appointment[0]}")
                    print(f"Time : {patient.appointment[1]}")
                else:
                    print("\nNo appointment found.")

            elif choice == "3":
                self.reschedule_by_doctor(patient)

            elif choice == "4":
                patient.cancel_appointment()

            elif choice == "5":
                patient.save_records_to_file()

            elif choice == "0":
                print("\nYou have logged out successfully.")
                break

            else:
                print("\nInvalid option. Please try again.")

    # ==========================
    # MAIN MENU
    # ==========================

    def run(self):
        while True:
            print("\n====================================")
            print(" DIGITAL PATIENT RECORD SYSTEM")
            print("====================================")
            print("1. Register Patient")
            print("2. Patient Login")
            print("3. View Doctors")
            print("4. Total Patients")
            print("5. Total Doctors")
            print("6. Patient Policy")
            print("7. Hospital Information")
            print("8. Exit")
            print("====================================")

            option = input("Select Option: ").strip()

            if option == "1":
                self.register_patient()

            elif option == "2":
                self.login_patient()

            elif option == "3":
                self.show_doctors()

            elif option == "4":
                Patient.get_total_patients()

            elif option == "5":
                Doctor.get_total_doctors()

            elif option == "6":
                Patient.patient_policy()

            elif option == "7":
                Doctor.hospital_message()

            elif option == "8":
                print(
                    "\nThank you for using the "
                    "Digital Patient Record System."
                )
                break

            else:
                print("\nInvalid option. Please try again.")


# ==========================
# RUN THE PROGRAM
# ==========================

if __name__ == "__main__":
    system = PatientRecordSystem()
    system.run()