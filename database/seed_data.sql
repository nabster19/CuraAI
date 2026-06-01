-- CuraAI Seed Data
-- Sample data for testing and development

USE curaai;

-- ============================================
-- INSERT SAMPLE USERS
-- ============================================

-- Admin User
INSERT INTO users (full_name, mobile_number, password_hash, email, role, is_active, is_verified) VALUES
('Admin User', '9999999999', '$2b$12$abcdefghijklmnopqrstuvwxyz', 'admin@curaai.com', 'admin', TRUE, TRUE);

-- Patient Users
INSERT INTO users (full_name, mobile_number, password_hash, email, role, is_active, is_verified) VALUES
('Raj Kumar', '9876543210', '$2b$12$abcdefghijklmnopqrstuvwxyz', 'raj@example.com', 'patient', TRUE, TRUE),
('Priya Singh', '9876543211', '$2b$12$abcdefghijklmnopqrstuvwxyz', 'priya@example.com', 'patient', TRUE, TRUE),
('Amit Patel', '9876543212', '$2b$12$abcdefghijklmnopqrstuvwxyz', 'amit@example.com', 'patient', TRUE, TRUE),
('Neha Sharma', '9876543213', '$2b$12$abcdefghijklmnopqrstuvwxyz', 'neha@example.com', 'patient', TRUE, TRUE);

-- Doctor Users
INSERT INTO users (full_name, mobile_number, password_hash, email, role, is_active, is_verified) VALUES
('Dr. Rohit Verma', '9000000001', '$2b$12$abcdefghijklmnopqrstuvwxyz', 'dr.rohit@curaai.com', 'doctor', TRUE, TRUE),
('Dr. Anjali Gupta', '9000000002', '$2b$12$abcdefghijklmnopqrstuvwxyz', 'dr.anjali@curaai.com', 'doctor', TRUE, TRUE),
('Dr. Vikram Singh', '9000000003', '$2b$12$abcdefghijklmnopqrstuvwxyz', 'dr.vikram@curaai.com', 'doctor', TRUE, TRUE),
('Dr. Priya Nair', '9000000004', '$2b$12$abcdefghijklmnopqrstuvwxyz', 'dr.priya@curaai.com', 'doctor', TRUE, TRUE),
('Dr. Arjun Mishra', '9000000005', '$2b$12$abcdefghijklmnopqrstuvwxyz', 'dr.arjun@curaai.com', 'doctor', TRUE, TRUE),
('Dr. Sneha Das', '9000000006', '$2b$12$abcdefghijklmnopqrstuvwxyz', 'dr.sneha@curaai.com', 'doctor', TRUE, TRUE);

-- ============================================
-- INSERT PATIENT DETAILS
-- ============================================
INSERT INTO patients (user_id, age, gender, blood_type, emergency_contact, emergency_contact_name, city, state) VALUES
(2, 35, 'Male', 'O+', '9876543299', 'Rajesh Kumar', 'Mumbai', 'Maharashtra'),
(3, 28, 'Female', 'B+', '9876543298', 'Meera Singh', 'Delhi', 'Delhi'),
(4, 42, 'Male', 'A+', '9876543297', 'Ramesh Patel', 'Ahmedabad', 'Gujarat'),
(5, 31, 'Female', 'O-', '9876543296', 'Sharma Family', 'Bangalore', 'Karnataka');

-- ============================================
-- INSERT DOCTOR DETAILS
-- ============================================
INSERT INTO doctors (user_id, specialization, license_number, hospital_name, experience_years, consultation_fee, rating, is_verified) VALUES
(6, 'Cardiologist', 'MCI123456', 'Apollo Hospital', 15, 500.00, 4.8, TRUE),
(7, 'Neurologist', 'MCI123457', 'Max Healthcare', 12, 450.00, 4.7, TRUE),
(8, 'General Physician', 'MCI123458', 'Fortis Hospital', 10, 300.00, 4.6, TRUE),
(9, 'Dermatologist', 'MCI123459', 'Apollo Hospital', 8, 400.00, 4.9, TRUE),
(10, 'Orthopedic', 'MCI123460', 'Lilavati Hospital', 18, 550.00, 4.85, TRUE),
(11, 'Diabetologist', 'MCI123461', 'Max Healthcare', 14, 450.00, 4.75, TRUE);

-- ============================================
-- INSERT HEALTH RECORDS
-- ============================================
INSERT INTO health_records (patient_id, height_cm, weight_kg, blood_pressure_systolic, blood_pressure_diastolic, blood_sugar_fasting, cholesterol_total, heart_rate, oxygen_saturation, bmi, existing_diseases, allergies, current_medications) VALUES
(1, 175.5, 85.0, 130, 85, 110, 210, 72, 98.5, 27.6, 'Hypertension', 'Penicillin', 'Aspirin 100mg'),
(2, 162.0, 58.0, 120, 80, 95, 180, 68, 99.0, 22.1, 'None', 'Shellfish', 'None'),
(3, 180.0, 92.0, 140, 90, 125, 240, 78, 97.5, 28.4, 'Diabetes', 'None', 'Metformin 500mg'),
(4, 168.0, 62.0, 118, 78, 100, 195, 70, 98.8, 22.0, 'None', 'Dust allergens', 'Antihistamine');

-- ============================================
-- INSERT SAMPLE SYMPTOMS
-- ============================================
INSERT INTO symptoms (patient_id, symptom_text, severity, duration_days) VALUES
(1, 'Sharp chest pain while climbing stairs, shortness of breath', 'Severe', 3),
(2, 'Frequent dizziness and blurry vision', 'Moderate', 5),
(3, 'Increased thirst and frequent urination', 'Moderate', 7),
(4, 'Itchy skin rash after eating seafood', 'Mild', 2);

-- ============================================
-- INSERT DISEASE PREDICTIONS
-- ============================================
INSERT INTO disease_predictions (patient_id, symptom_id, predicted_disease, confidence_percentage, severity_level, requires_doctor_visit) VALUES
(1, 1, 'Coronary Artery Disease', 85.5, 'Severe', TRUE),
(1, 1, 'Angina', 75.2, 'Severe', TRUE),
(2, 2, 'Vertebrobasilar Insufficiency', 68.3, 'Moderate', TRUE),
(3, 3, 'Type 2 Diabetes', 92.1, 'Moderate', TRUE),
(4, 4, 'Allergic Reaction', 88.7, 'Mild', FALSE);

-- ============================================
-- INSERT DRUG RECOMMENDATIONS
-- ============================================
INSERT INTO drug_recommendations (patient_id, disease_prediction_id, medicine_name, dosage, frequency, duration_days, side_effects, food_restrictions) VALUES
(1, 1, 'Aspirin', '100 mg', 'Once daily', 30, 'Stomach upset, bleeding', 'None'),
(1, 1, 'Atorvastatin', '40 mg', 'Once daily at night', 90, 'Muscle pain, liver issues', 'Limit grapefruit'),
(2, 3, 'Betahistine', '16 mg', 'Three times daily', 14, 'Headache, nausea', 'None'),
(3, 4, 'Metformin', '500 mg', 'Twice daily with meals', 180, 'GI upset, B12 deficiency', 'None'),
(4, 5, 'Cetirizine', '10 mg', 'Once daily', 7, 'Drowsiness, dry mouth', 'None');

-- ============================================
-- INSERT APPOINTMENTS
-- ============================================
INSERT INTO appointments (patient_id, doctor_id, appointment_date, consultation_type, status, reason_for_visit) VALUES
(1, 1, '2026-06-15 10:00:00', 'In-Person', 'Confirmed', 'Chest pain evaluation'),
(2, 2, '2026-06-18 14:30:00', 'Video', 'Pending', 'Dizziness check-up'),
(3, 6, '2026-06-20 09:00:00', 'In-Person', 'Confirmed', 'Diabetes management'),
(4, 4, '2026-06-22 11:00:00', 'In-Person', 'Pending', 'Allergic reaction consultation');

-- ============================================
-- INSERT MESSAGES
-- ============================================
INSERT INTO messages (patient_id, doctor_id, sender_type, message_text, is_read) VALUES
(1, 1, 'Patient', 'Hi Dr. Verma, I am experiencing severe chest pain. Can I book an appointment?', FALSE),
(1, 1, 'Doctor', 'Please come to the hospital immediately or call emergency services if it is severe.', TRUE),
(2, 2, 'Patient', 'Dr. Gupta, my dizziness has been ongoing for 5 days. What should I do?', FALSE);

-- ============================================
-- INSERT NOTIFICATIONS
-- ============================================
INSERT INTO notifications (user_id, notification_type, title, message, phone_number, sms_sent) VALUES
(2, 'Appointment', 'Appointment Confirmed', 'Your appointment with Dr. Rohit Verma is confirmed on 2026-06-15 at 10:00 AM', '9876543210', TRUE),
(3, 'Message', 'New Message', 'Dr. Anjali Gupta has sent you a message', '9876543211', TRUE),
(5, 'Reminder', 'Medicine Reminder', 'Remember to take your Metformin 500mg', '9876543213', TRUE);

-- ============================================
-- INSERT HEALTH TRACKING
-- ============================================
INSERT INTO health_tracking (patient_id, tracking_date, blood_pressure_systolic, blood_pressure_diastolic, weight_kg, blood_sugar, cholesterol, water_intake_ml, heart_rate, sleep_hours, exercise_minutes, mood) VALUES
(1, '2026-05-25', 135, 87, 85.2, NULL, NULL, 2000, 74, 6.5, 30, 'Okay'),
(1, '2026-05-26', 132, 84, 85.1, NULL, NULL, 2100, 72, 7.0, 45, 'Good'),
(2, '2026-05-25', 118, 78, 58.1, 95, NULL, 2500, 68, 7.5, 40, 'Good'),
(3, '2026-05-25', 138, 88, 92.2, 135, 242, 1800, 76, 6.0, 20, 'Okay');
