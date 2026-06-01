-- CuraAI Database Schema
-- MySQL Healthcare Platform Database

CREATE DATABASE IF NOT EXISTS curaai;
USE curaai;

-- ============================================
-- USERS TABLE
-- ============================================
CREATE TABLE users (
    id INT PRIMARY KEY AUTO_INCREMENT,
    full_name VARCHAR(255) NOT NULL,
    mobile_number VARCHAR(20) UNIQUE NOT NULL,
    password_hash VARCHAR(255) NOT NULL,
    email VARCHAR(255) UNIQUE,
    role ENUM('patient', 'doctor', 'admin') DEFAULT 'patient',
    is_active BOOLEAN DEFAULT TRUE,
    is_verified BOOLEAN DEFAULT FALSE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    INDEX idx_role (role),
    INDEX idx_mobile (mobile_number),
    INDEX idx_active (is_active)
);

-- ============================================
-- PATIENTS TABLE
-- ============================================
CREATE TABLE patients (
    id INT PRIMARY KEY AUTO_INCREMENT,
    user_id INT NOT NULL UNIQUE,
    age INT,
    gender ENUM('Male', 'Female', 'Other'),
    blood_type VARCHAR(5),
    emergency_contact VARCHAR(20),
    emergency_contact_name VARCHAR(255),
    address TEXT,
    city VARCHAR(100),
    state VARCHAR(100),
    pincode VARCHAR(10),
    profile_photo_url VARCHAR(500),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE,
    INDEX idx_user (user_id)
);

-- ============================================
-- DOCTORS TABLE
-- ============================================
CREATE TABLE doctors (
    id INT PRIMARY KEY AUTO_INCREMENT,
    user_id INT NOT NULL UNIQUE,
    specialization VARCHAR(100) NOT NULL,
    license_number VARCHAR(100) UNIQUE NOT NULL,
    hospital_name VARCHAR(255),
    experience_years INT,
    qualifications TEXT,
    bio TEXT,
    consultation_fee DECIMAL(10, 2),
    availability_start TIME,
    availability_end TIME,
    rating DECIMAL(3, 2) DEFAULT 0.00,
    total_ratings INT DEFAULT 0,
    profile_photo_url VARCHAR(500),
    is_verified BOOLEAN DEFAULT FALSE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE,
    INDEX idx_specialization (specialization),
    INDEX idx_user (user_id)
);

-- ============================================
-- HEALTH_RECORDS TABLE
-- ============================================
CREATE TABLE health_records (
    id INT PRIMARY KEY AUTO_INCREMENT,
    patient_id INT NOT NULL,
    height_cm DECIMAL(5, 2),
    weight_kg DECIMAL(5, 2),
    blood_pressure_systolic INT,
    blood_pressure_diastolic INT,
    blood_sugar_fasting INT,
    blood_sugar_random INT,
    cholesterol_total INT,
    cholesterol_ldl INT,
    cholesterol_hdl INT,
    triglycerides INT,
    heart_rate INT,
    oxygen_saturation DECIMAL(3, 1),
    bmi DECIMAL(5, 2),
    existing_diseases TEXT,
    allergies TEXT,
    current_medications TEXT,
    notes TEXT,
    record_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (patient_id) REFERENCES patients(id) ON DELETE CASCADE,
    INDEX idx_patient (patient_id),
    INDEX idx_date (record_date)
);

-- ============================================
-- SYMPTOMS TABLE
-- ============================================
CREATE TABLE symptoms (
    id INT PRIMARY KEY AUTO_INCREMENT,
    patient_id INT NOT NULL,
    symptom_text TEXT NOT NULL,
    severity ENUM('Mild', 'Moderate', 'Severe', 'Emergency') DEFAULT 'Mild',
    duration_days INT,
    symptom_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (patient_id) REFERENCES patients(id) ON DELETE CASCADE,
    INDEX idx_patient (patient_id),
    INDEX idx_date (symptom_date)
);

-- ============================================
-- DISEASE_PREDICTIONS TABLE
-- ============================================
CREATE TABLE disease_predictions (
    id INT PRIMARY KEY AUTO_INCREMENT,
    patient_id INT NOT NULL,
    symptom_id INT,
    predicted_disease VARCHAR(255) NOT NULL,
    confidence_percentage DECIMAL(5, 2),
    severity_level ENUM('Mild', 'Moderate', 'Severe', 'Emergency') DEFAULT 'Mild',
    precautions TEXT,
    requires_doctor_visit BOOLEAN DEFAULT TRUE,
    is_rare_disease BOOLEAN DEFAULT FALSE,
    prediction_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (patient_id) REFERENCES patients(id) ON DELETE CASCADE,
    FOREIGN KEY (symptom_id) REFERENCES symptoms(id) ON DELETE SET NULL,
    INDEX idx_patient (patient_id),
    INDEX idx_disease (predicted_disease)
);

-- ============================================
-- DRUG_RECOMMENDATIONS TABLE
-- ============================================
CREATE TABLE drug_recommendations (
    id INT PRIMARY KEY AUTO_INCREMENT,
    patient_id INT NOT NULL,
    disease_prediction_id INT,
    medicine_name VARCHAR(255) NOT NULL,
    dosage VARCHAR(100),
    frequency VARCHAR(100),
    duration_days INT,
    side_effects TEXT,
    food_restrictions TEXT,
    alternative_medicines TEXT,
    warning_message TEXT DEFAULT 'This recommendation is AI-generated and should be verified by a licensed doctor.',
    recommendation_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (patient_id) REFERENCES patients(id) ON DELETE CASCADE,
    FOREIGN KEY (disease_prediction_id) REFERENCES disease_predictions(id) ON DELETE SET NULL,
    INDEX idx_patient (patient_id)
);

-- ============================================
-- PRESCRIPTIONS TABLE
-- ============================================
CREATE TABLE prescriptions (
    id INT PRIMARY KEY AUTO_INCREMENT,
    patient_id INT NOT NULL,
    doctor_id INT,
    prescription_file_url VARCHAR(500),
    extracted_medicines TEXT,
    extracted_diagnosis TEXT,
    upload_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (patient_id) REFERENCES patients(id) ON DELETE CASCADE,
    FOREIGN KEY (doctor_id) REFERENCES doctors(id) ON DELETE SET NULL,
    INDEX idx_patient (patient_id)
);

-- ============================================
-- REPORTS TABLE
-- ============================================
CREATE TABLE reports (
    id INT PRIMARY KEY AUTO_INCREMENT,
    patient_id INT NOT NULL,
    report_type ENUM('Blood Report', 'X-Ray', 'CT Scan', 'MRI', 'ECG', 'Ultrasound', 'Other') DEFAULT 'Other',
    report_file_url VARCHAR(500),
    extracted_text TEXT,
    ai_summary TEXT,
    report_date DATE,
    upload_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (patient_id) REFERENCES patients(id) ON DELETE CASCADE,
    INDEX idx_patient (patient_id),
    INDEX idx_type (report_type)
);

-- ============================================
-- APPOINTMENTS TABLE
-- ============================================
CREATE TABLE appointments (
    id INT PRIMARY KEY AUTO_INCREMENT,
    patient_id INT NOT NULL,
    doctor_id INT NOT NULL,
    appointment_date DATETIME NOT NULL,
    consultation_type ENUM('In-Person', 'Video', 'Phone') DEFAULT 'In-Person',
    status ENUM('Pending', 'Confirmed', 'Completed', 'Cancelled') DEFAULT 'Pending',
    notes TEXT,
    reason_for_visit TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (patient_id) REFERENCES patients(id) ON DELETE CASCADE,
    FOREIGN KEY (doctor_id) REFERENCES doctors(id) ON DELETE CASCADE,
    INDEX idx_patient (patient_id),
    INDEX idx_doctor (doctor_id),
    INDEX idx_date (appointment_date),
    INDEX idx_status (status)
);

-- ============================================
-- MESSAGES TABLE
-- ============================================
CREATE TABLE messages (
    id INT PRIMARY KEY AUTO_INCREMENT,
    patient_id INT NOT NULL,
    doctor_id INT NOT NULL,
    sender_type ENUM('Patient', 'Doctor') NOT NULL,
    message_text TEXT NOT NULL,
    is_read BOOLEAN DEFAULT FALSE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (patient_id) REFERENCES patients(id) ON DELETE CASCADE,
    FOREIGN KEY (doctor_id) REFERENCES doctors(id) ON DELETE CASCADE,
    INDEX idx_conversation (patient_id, doctor_id),
    INDEX idx_unread (is_read)
);

-- ============================================
-- NOTIFICATIONS TABLE
-- ============================================
CREATE TABLE notifications (
    id INT PRIMARY KEY AUTO_INCREMENT,
    user_id INT NOT NULL,
    notification_type ENUM('Appointment', 'Message', 'Reminder', 'Alert', 'Report') DEFAULT 'Alert',
    title VARCHAR(255),
    message TEXT NOT NULL,
    phone_number VARCHAR(20),
    sms_sent BOOLEAN DEFAULT FALSE,
    sent_at TIMESTAMP,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE,
    INDEX idx_user (user_id),
    INDEX idx_sent (sms_sent)
);

-- ============================================
-- HEALTH_TRACKING TABLE
-- ============================================
CREATE TABLE health_tracking (
    id INT PRIMARY KEY AUTO_INCREMENT,
    patient_id INT NOT NULL,
    tracking_date DATE NOT NULL,
    blood_pressure_systolic INT,
    blood_pressure_diastolic INT,
    weight_kg DECIMAL(5, 2),
    blood_sugar DECIMAL(5, 1),
    cholesterol INT,
    water_intake_ml INT,
    heart_rate INT,
    steps_count INT,
    sleep_hours DECIMAL(3, 1),
    exercise_minutes INT,
    mood VARCHAR(50),
    notes TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (patient_id) REFERENCES patients(id) ON DELETE CASCADE,
    INDEX idx_patient (patient_id),
    INDEX idx_date (tracking_date),
    UNIQUE KEY unique_tracking (patient_id, tracking_date)
);

-- ============================================
-- ADMIN_LOGS TABLE
-- ============================================
CREATE TABLE admin_logs (
    id INT PRIMARY KEY AUTO_INCREMENT,
    admin_id INT NOT NULL,
    action VARCHAR(255) NOT NULL,
    resource_type VARCHAR(100),
    resource_id INT,
    details TEXT,
    ip_address VARCHAR(50),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (admin_id) REFERENCES users(id) ON DELETE CASCADE,
    INDEX idx_admin (admin_id),
    INDEX idx_date (created_at)
);

-- ============================================
-- INDICES FOR PERFORMANCE
-- ============================================
CREATE INDEX idx_patient_user ON patients(user_id);
CREATE INDEX idx_doctor_user ON doctors(user_id);
CREATE INDEX idx_records_patient ON health_records(patient_id);
CREATE INDEX idx_symptoms_patient ON symptoms(patient_id);
CREATE INDEX idx_predictions_patient ON disease_predictions(patient_id);
CREATE INDEX idx_recommendations_patient ON drug_recommendations(patient_id);
CREATE INDEX idx_appointments_patient ON appointments(patient_id);
CREATE INDEX idx_appointments_doctor ON appointments(doctor_id);
CREATE INDEX idx_messages_conversation ON messages(patient_id, doctor_id);
