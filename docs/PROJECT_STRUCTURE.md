# CuraAI Project Structure

## Directory Layout

```
CuraAI/
├── frontend/                          # React.js Frontend
│   ├── public/
│   │   └── index.html
│   ├── src/
│   │   ├── components/                # Reusable React components
│   │   │   ├── ProtectedRoute.jsx
│   │   │   ├── Sidebar.jsx
│   │   │   ├── HealthCard.jsx
│   │   │   └── ...
│   │   ├── pages/                     # Page components
│   │   │   ├── HomePage.jsx
│   │   │   ├── LoginPage.jsx
│   │   │   ├── RegisterPage.jsx
│   │   │   ├── DashboardPage.jsx
│   │   │   └── ...
│   │   ├── services/                  # API services
│   │   │   ├── api.js                 # Axios instance
│   │   │   └── index.js               # Service exports
│   │   ├── store/                     # Zustand stores
│   │   │   └── authStore.js
│   │   ├── App.jsx                    # Main app component
│   │   ├── main.jsx                   # Entry point
│   │   └── index.css                  # Tailwind CSS
│   ├── package.json
│   ├── vite.config.js
│   ├── tailwind.config.js
│   └── postcss.config.js
│
├── backend/                           # Flask Backend
│   ├── app/
│   │   ├── models/                    # SQLAlchemy models
│   │   │   ├── user.py                # User model
│   │   │   ├── patient.py             # Patient model
│   │   │   ├── doctor.py              # Doctor model
│   │   │   ├── health.py              # Health records
│   │   │   ├── ai_models.py           # AI prediction models
│   │   │   ├── medical.py             # Medical records
│   │   │   ├── logs.py                # Logs and notifications
│   │   │   └── __init__.py
│   │   │
│   │   ├── routes/                    # API route handlers
│   │   │   ├── auth_routes.py         # Authentication routes
│   │   │   ├── patient_routes.py      # Patient routes
│   │   │   ├── doctor_routes.py       # Doctor routes
│   │   │   ├── appointment_routes.py  # Appointment routes
│   │   │   ├── ai_routes.py           # AI prediction routes
│   │   │   ├── admin_routes.py        # Admin routes
│   │   │   └── __init__.py
│   │   │
│   │   ├── services/                  # Business logic
│   │   │   ├── ai_service.py          # AI/ML service
│   │   │   ├── email_service.py       # Email service
│   │   │   ├── sms_service.py         # SMS notifications
│   │   │   ├── ocr_service.py         # OCR processing
│   │   │   └── __init__.py
│   │   │
│   │   ├── utils/                     # Utility functions
│   │   │   ├── decorators.py
│   │   │   ├── validators.py
│   │   │   └── helpers.py
│   │   │
│   │   ├── ml_models/                 # Machine learning models
│   │   │   ├── disease_predictor.pkl
│   │   │   └── drug_recommender.pkl
│   │   │
│   │   └── __init__.py                # Flask app factory
│   │
│   ├── config.py                      # Configuration
│   ├── run.py                         # Application entry point
│   ├── requirements.txt               # Python dependencies
│   ├── .env.example                   # Environment template
│   └── .env                           # Environment variables (git ignored)
│
├── database/                          # Database files
│   ├── schema.sql                     # Database schema
│   └── seed_data.sql                  # Sample test data
│
├── docs/                              # Documentation
│   ├── SETUP.md                       # Setup instructions
│   ├── API_DOCUMENTATION.md           # API reference
│   ├── DEPLOYMENT.md                  # Deployment guide
│   └── PROJECT_STRUCTURE.md           # This file
│
├── .gitignore                         # Git ignore file
├── README.md                          # Project README
├── LICENSE                            # MIT License
└── docker-compose.yml                 # Docker orchestration
```

## Key Components

### Frontend Structure

**Components:**
- `ProtectedRoute` - Route protection with role-based access
- `Sidebar` - Navigation sidebar with menu items
- `HealthCard` - Reusable health metrics card
- `Header` - Navigation header
- `Modal` - Reusable modal component

**Pages:**
- `HomePage` - Landing page with features
- `LoginPage` - User login
- `RegisterPage` - User registration
- `DashboardPage` - Main dashboard
- `ProfilePage` - User profile management
- `HealthRecordsPage` - Health records view/edit
- `AppointmentsPage` - Appointment booking and management
- `DoctorListPage` - Browse doctors
- `AdminPage` - Admin dashboard

**Services:**
- `authService` - Authentication operations
- `patientService` - Patient operations
- `doctorService` - Doctor operations
- `appointmentService` - Appointment management
- `aiService` - AI predictions
- `adminService` - Admin operations

**Store:**
- `authStore` - Authentication state management

### Backend Structure

**Models:**
- `User` - User accounts
- `Patient` - Patient profiles
- `Doctor` - Doctor profiles
- `HealthRecord` - Health metrics
- `HealthTracking` - Daily tracking
- `Symptom` - Patient symptoms
- `DiseasePrediction` - AI predictions
- `DrugRecommendation` - Drug suggestions
- `Prescription` - Doctor prescriptions
- `Report` - Medical reports
- `Appointment` - Appointment records
- `Message` - Doctor-patient messages
- `Notification` - SMS notifications
- `AdminLog` - Admin activity logs

**Routes:**
- `/api/auth/*` - Authentication
- `/api/patient/*` - Patient operations
- `/api/doctor/*` - Doctor operations
- `/api/appointments/*` - Appointments
- `/api/ai/*` - AI predictions
- `/api/admin/*` - Admin operations

**Services:**
- `ai_service` - Disease prediction and drug recommendations
- `email_service` - Email notifications
- `sms_service` - SMS via Twilio
- `ocr_service` - Document scanning and extraction

## Database Schema

**Core Tables:**
- `users` - User accounts and authentication
- `patients` - Patient profiles
- `doctors` - Doctor profiles
- `health_records` - Patient health metrics
- `health_tracking` - Daily health tracking

**Medical Tables:**
- `symptoms` - Patient symptoms
- `disease_predictions` - AI disease predictions
- `drug_recommendations` - AI drug suggestions
- `prescriptions` - Doctor prescriptions
- `reports` - Medical reports

**Scheduling & Communication:**
- `appointments` - Doctor appointments
- `messages` - Doctor-patient messages
- `notifications` - SMS notifications

**Admin Tables:**
- `admin_logs` - Admin activity logs

## Technology Stack

**Frontend:**
- React.js (UI framework)
- Vite (Build tool)
- Tailwind CSS (Styling)
- Zustand (State management)
- Chart.js (Data visualization)
- React Router (Navigation)

**Backend:**
- Flask (Web framework)
- SQLAlchemy (ORM)
- PyMySQL (MySQL driver)
- Scikit-learn (ML library)
- Pandas (Data processing)
- Tesseract OCR (Document scanning)
- Twilio (SMS service)

**Database:**
- MySQL 8.0

**DevOps:**
- Docker
- Docker Compose
- Nginx
- Gunicorn

## API Flow

1. **Authentication Flow:**
   - User registers with mobile number and password
   - Password hashed with bcrypt
   - User logs in and receives JWT token
   - Token stored in localStorage
   - Token sent with each API request

2. **Health Record Flow:**
   - Patient submits health metrics
   - Data validated and stored in database
   - History maintained with timestamps
   - Frontend displays charts and trends

3. **AI Prediction Flow:**
   - Patient enters symptoms
   - Symptoms sent to AI service
   - ML model predicts diseases
   - Predictions stored with confidence scores
   - Drug recommendations generated

4. **Appointment Flow:**
   - Patient selects doctor and time
   - Appointment created in database
   - SMS notification sent via Twilio
   - Doctor receives appointment notification
   - Appointment status tracked

## Security Implementation

1. **Password Security:**
   - Bcrypt hashing with 12 rounds
   - No passwords stored in plain text

2. **API Security:**
   - JWT token-based authentication
   - 24-hour token expiration
   - Role-based access control

3. **Data Security:**
   - SQL injection prevention via ORM
   - CORS configured
   - File upload validation
   - HTTPS for production

4. **Session Management:**
   - JWT tokens stored securely
   - Automatic logout on token expiration
   - Logout functionality

## Performance Optimization

1. **Frontend:**
   - Code splitting with React Router
   - Lazy loading of components
   - Optimized bundle size with Vite
   - Tailwind CSS purging

2. **Backend:**
   - Database connection pooling
   - Query optimization with SQLAlchemy
   - Caching mechanisms
   - Pagination for large datasets

3. **Database:**
   - Proper indexing
   - Query optimization
   - Regular backups

## Testing

- Unit tests for backend functions
- Integration tests for API endpoints
- Frontend component tests
- E2E testing with Cypress

## Deployment

Supported deployment platforms:
- Docker + Docker Compose
- AWS EC2 + RDS
- Heroku
- DigitalOcean
- Azure App Service
