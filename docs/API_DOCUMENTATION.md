# CuraAI API Documentation

## Base URL

```
http://localhost:5000/api
```

## Authentication

All endpoints (except auth) require JWT token in header:

```
Authorization: Bearer <your_jwt_token>
```

## Authentication Endpoints

### Register User

```
POST /auth/register
```

**Request Body:**
```json
{
  "full_name": "John Doe",
  "mobile_number": "9876543210",
  "password": "password123",
  "role": "patient",
  "email": "john@example.com"
}
```

**Response:**
```json
{
  "message": "User registered successfully",
  "user": {
    "id": 1,
    "full_name": "John Doe",
    "mobile_number": "9876543210",
    "role": "patient",
    "created_at": "2026-06-01T10:00:00"
  }
}
```

### Login

```
POST /auth/login
```

**Request Body:**
```json
{
  "mobile_number": "9876543210",
  "password": "password123"
}
```

**Response:**
```json
{
  "message": "Login successful",
  "access_token": "eyJhbGciOiJIUzI1NiIs...",
  "user": {
    "id": 1,
    "full_name": "John Doe",
    "role": "patient"
  }
}
```

### Logout

```
POST /auth/logout
```

**Response:**
```json
{
  "message": "Logged out successfully"
}
```

### Get Profile

```
GET /auth/profile
```

**Response:**
```json
{
  "user": {
    "id": 1,
    "full_name": "John Doe",
    "mobile_number": "9876543210",
    "email": "john@example.com",
    "role": "patient"
  }
}
```

### Update Profile

```
PUT /auth/profile
```

**Request Body:**
```json
{
  "full_name": "John Doe Updated",
  "email": "newemail@example.com"
}
```

## Patient Endpoints

### Get Patient Profile

```
GET /patient/profile
```

**Response:**
```json
{
  "patient": {
    "id": 1,
    "user_id": 1,
    "age": 35,
    "gender": "Male",
    "blood_type": "O+",
    "city": "Mumbai",
    "state": "Maharashtra"
  }
}
```

### Update Patient Profile

```
PUT /patient/profile
```

**Request Body:**
```json
{
  "age": 36,
  "gender": "Male",
  "blood_type": "O+",
  "emergency_contact": "9876543299",
  "city": "Mumbai",
  "state": "Maharashtra"
}
```

### Get Health Records

```
GET /patient/health-records
```

**Response:**
```json
{
  "records": [
    {
      "id": 1,
      "patient_id": 1,
      "height_cm": 175.5,
      "weight_kg": 85.0,
      "blood_pressure": "130/85",
      "blood_sugar_fasting": 110,
      "cholesterol_total": 210,
      "bmi": 27.6,
      "existing_diseases": "Hypertension",
      "allergies": "Penicillin",
      "current_medications": "Aspirin 100mg"
    }
  ]
}
```

### Add Health Record

```
POST /patient/health-records
```

**Request Body:**
```json
{
  "height_cm": 175.5,
  "weight_kg": 85.0,
  "blood_pressure_systolic": 130,
  "blood_pressure_diastolic": 85,
  "blood_sugar_fasting": 110,
  "cholesterol_total": 210,
  "heart_rate": 72,
  "oxygen_saturation": 98.5,
  "existing_diseases": "Hypertension",
  "allergies": "Penicillin",
  "current_medications": "Aspirin 100mg"
}
```

### Add Health Tracking

```
POST /patient/health-tracking
```

**Request Body:**
```json
{
  "tracking_date": "2026-06-01",
  "weight_kg": 85.2,
  "blood_sugar": 115,
  "heart_rate": 74,
  "water_intake_ml": 2000,
  "sleep_hours": 7.5,
  "exercise_minutes": 30,
  "mood": "Good"
}
```

### Add Symptom

```
POST /patient/symptoms
```

**Request Body:**
```json
{
  "symptom_text": "Sharp chest pain while climbing stairs",
  "severity": "Severe",
  "duration_days": 3
}
```

## AI Endpoints

### Predict Disease

```
POST /ai/predict-disease
```

**Request Body:**
```json
{
  "symptom_text": "Sharp chest pain while climbing stairs, shortness of breath",
  "severity": "Severe",
  "duration_days": 3
}
```

**Response:**
```json
{
  "message": "Disease prediction completed",
  "symptom": {
    "id": 1,
    "symptom_text": "Sharp chest pain...",
    "severity": "Severe"
  },
  "predictions": [
    {
      "id": 1,
      "predicted_disease": "Coronary Artery Disease",
      "confidence_percentage": 85.5,
      "severity_level": "Severe",
      "requires_doctor_visit": true
    }
  ]
}
```

### Recommend Drugs

```
POST /ai/recommend-drugs
```

**Request Body:**
```json
{
  "disease": "Coronary Artery Disease"
}
```

**Response:**
```json
{
  "recommendations": [
    {
      "id": 1,
      "medicine_name": "Aspirin",
      "dosage": "100 mg",
      "frequency": "Once daily",
      "side_effects": "Stomach upset, bleeding",
      "warning_message": "This recommendation is AI-generated..."
    }
  ]
}
```

### Recommend Doctors

```
POST /ai/recommend-doctors
```

**Request Body:**
```json
{
  "disease": "Coronary Artery Disease"
}
```

**Response:**
```json
{
  "doctors": [
    {
      "specialization": "Cardiologist",
      "recommendation": "See a Cardiologist for Coronary Artery Disease"
    }
  ]
}
```

## Doctor Endpoints

### List Doctors

```
GET /doctor/list?specialization=Cardiologist
```

**Response:**
```json
{
  "doctors": [
    {
      "id": 1,
      "user_id": 6,
      "name": "Dr. Rohit Verma",
      "specialization": "Cardiologist",
      "hospital_name": "Apollo Hospital",
      "experience_years": 15,
      "consultation_fee": 500,
      "rating": 4.8
    }
  ]
}
```

### Get Doctor Details

```
GET /doctor/{doctor_id}
```

**Response:**
```json
{
  "doctor": {
    "id": 1,
    "name": "Dr. Rohit Verma",
    "specialization": "Cardiologist",
    "hospital_name": "Apollo Hospital",
    "experience_years": 15,
    "consultation_fee": 500,
    "rating": 4.8,
    "contact_info": {
      "mobile": "9000000001",
      "email": "dr.rohit@curaai.com"
    }
  }
}
```

### Get Specializations

```
GET /doctor/specializations
```

**Response:**
```json
{
  "specializations": [
    "Cardiologist",
    "Neurologist",
    "General Physician",
    "Dermatologist",
    "Orthopedic",
    "Diabetologist"
  ]
}
```

## Appointment Endpoints

### Get Appointments

```
GET /appointments
```

**Response:**
```json
{
  "appointments": [
    {
      "id": 1,
      "patient_id": 1,
      "doctor_id": 1,
      "appointment_date": "2026-06-15T10:00:00",
      "consultation_type": "In-Person",
      "status": "Confirmed",
      "reason_for_visit": "Chest pain evaluation"
    }
  ]
}
```

### Book Appointment

```
POST /appointments
```

**Request Body:**
```json
{
  "doctor_id": 1,
  "appointment_date": "2026-06-15T10:00:00",
  "consultation_type": "In-Person",
  "reason_for_visit": "Chest pain evaluation"
}
```

### Update Appointment

```
PUT /appointments/{appointment_id}
```

**Request Body:**
```json
{
  "status": "Completed",
  "notes": "Patient recovered well"
}
```

## Admin Endpoints

### Get All Users

```
GET /admin/users
```

### Get All Doctors

```
GET /admin/doctors
```

### Get All Appointments

```
GET /admin/appointments
```

### Get Platform Statistics

```
GET /admin/stats
```

**Response:**
```json
{
  "total_users": 100,
  "total_patients": 80,
  "total_doctors": 6,
  "total_appointments": 45,
  "pending_appointments": 5
}
```

## Error Responses

### 400 - Bad Request

```json
{
  "error": "Bad request",
  "message": "Missing required fields"
}
```

### 401 - Unauthorized

```json
{
  "error": "Unauthorized",
  "message": "Invalid credentials"
}
```

### 403 - Forbidden

```json
{
  "error": "Forbidden",
  "message": "Access denied"
}
```

### 404 - Not Found

```json
{
  "error": "Not found",
  "message": "Resource not found"
}
```

### 500 - Server Error

```json
{
  "error": "Internal server error",
  "message": "An unexpected error occurred"
}
```
