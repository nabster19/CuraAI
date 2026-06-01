# CuraAI – AI Powered Smart Healthcare and Clinical Decision Support Platform

## Overview

CuraAI is a professional full-stack AI healthcare platform designed for secure medical record management, AI-powered disease prediction, drug recommendations, and seamless doctor-patient connectivity.

## Features

✅ **User Authentication** - Secure multi-role authentication (Patient, Doctor, Admin)  
✅ **Health Records Management** - Editable digital health profiles with history tracking  
✅ **Digital Health Tracking** - Track BP, weight, BMI, cholesterol with analytics graphs  
✅ **Prescription & Report Upload** - OCR-based extraction of medications and diagnoses  
✅ **Custom Symptom Input** - Natural language symptom analysis with urgency detection  
✅ **AI Disease Prediction** - ML-powered disease detection with confidence scores  
✅ **AI Drug Recommendations** - Intelligent medicine suggestions based on medical history  
✅ **Doctor Recommendation System** - Auto-suggest specialists based on symptoms  
✅ **Doctor Connect System** - Appointment booking, messaging, and consultation requests  
✅ **SMS Notifications** - Twilio integration for real-time alerts  
✅ **Admin Dashboard** - Comprehensive management of users, doctors, and analytics  
✅ **Security** - JWT authentication, bcrypt hashing, role-based access control  

## Tech Stack

### Frontend
- React.js with Hooks
- Tailwind CSS
- Chart.js for data visualization
- Axios for API calls

### Backend
- Python Flask
- SQLAlchemy ORM
- JWT for authentication

### Database
- MySQL

### AI/ML
- Scikit-learn
- Pandas
- NumPy

### Additional Services
- Tesseract OCR for document scanning
- Twilio SMS API for notifications
- bcrypt for password security

## Project Structure

```
CuraAI/
├── frontend/                 # React.js application
│   ├── public/
│   ├── src/
│   │   ├── components/
│   │   ├── pages/
│   │   ├── services/
│   │   ├── utils/
│   │   ├── styles/
│   │   └── App.js
│   ├── package.json
│   └── tailwind.config.js
├── backend/                  # Flask API server
│   ├── app/
│   │   ├── models/
│   │   ├── routes/
│   │   ├── services/
│   │   ├── utils/
│   │   ├── ml_models/
│   │   └── __init__.py
│   ├── config.py
│   ├── requirements.txt
│   ├── run.py
│   └── .env.example
├── database/                 # MySQL schema
│   ├── schema.sql
│   └── seed_data.sql
├── docs/                     # Documentation
│   ├── API_DOCUMENTATION.md
│   ├── DEPLOYMENT.md
│   └── SETUP.md
└── README.md
```

## Quick Start

### Prerequisites
- Node.js 16+
- Python 3.8+
- MySQL 8.0+
- Git

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/nabster19/CuraAI.git
   cd CuraAI
   ```

2. **Setup Backend**
   ```bash
   cd backend
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install -r requirements.txt
   cp .env.example .env
   # Configure your .env file
   python run.py
   ```

3. **Setup Frontend**
   ```bash
   cd frontend
   npm install
   npm start
   ```

4. **Setup Database**
   ```bash
   mysql -u root -p < database/schema.sql
   mysql -u root -p < database/seed_data.sql
   ```

## Database Tables

- **users** - User accounts with authentication
- **patients** - Patient profiles and health data
- **doctors** - Doctor profiles and specializations
- **health_records** - Editable health metrics
- **symptoms** - Patient symptom entries
- **disease_predictions** - AI prediction results
- **drug_recommendations** - AI drug suggestions
- **prescriptions** - Uploaded prescriptions
- **reports** - Medical reports with OCR data
- **appointments** - Booking records
- **notifications** - SMS notifications log
- **messages** - Doctor-patient communication

## API Endpoints

### Authentication
- `POST /api/auth/register` - User registration
- `POST /api/auth/login` - User login
- `POST /api/auth/logout` - User logout
- `POST /api/auth/forgot-password` - Password reset

### Patient
- `GET /api/patient/profile` - Get patient profile
- `PUT /api/patient/profile` - Update profile
- `GET /api/patient/health-records` - Get health records
- `POST /api/patient/health-records` - Add health records

### AI Services
- `POST /api/ai/predict-disease` - Predict disease from symptoms
- `POST /api/ai/recommend-drugs` - Get drug recommendations
- `POST /api/ai/recommend-doctors` - Get doctor suggestions

### Appointments
- `GET /api/appointments` - List appointments
- `POST /api/appointments` - Book appointment
- `PUT /api/appointments/:id` - Update appointment

## Configuration

Create a `.env` file in the backend directory:

```env
FLASK_ENV=development
FLASK_APP=run.py
DATABASE_URL=mysql+pymysql://root:password@localhost/curaai
JWT_SECRET_KEY=your-secret-key-here
TWILIO_ACCOUNT_SID=your-twilio-sid
TWILIO_AUTH_TOKEN=your-twilio-token
TWILIO_PHONE_NUMBER=+1234567890
```

## Security Features

- ✅ bcrypt password hashing
- ✅ JWT token-based authentication
- ✅ SQL injection prevention via ORM
- ✅ File upload validation
- ✅ Role-based access control (RBAC)
- ✅ Session management
- ✅ CORS security headers

## Deployment

See [DEPLOYMENT.md](docs/DEPLOYMENT.md) for detailed deployment instructions for:
- AWS EC2
- Heroku
- Docker
- DigitalOcean

## Contributing

1. Create a feature branch (`git checkout -b feature/AmazingFeature`)
2. Commit changes (`git commit -m 'Add AmazingFeature'`)
3. Push to branch (`git push origin feature/AmazingFeature`)
4. Open a Pull Request

## License

MIT License - see LICENSE file for details

## Support

For issues and questions, please open an issue on GitHub.

## Roadmap

- [ ] Video consultation integration
- [ ] Telemedicine features
- [ ] Advanced ML models
- [ ] Mobile app (React Native)
- [ ] Insurance integration
- [ ] Blockchain for medical records

---

**Built with ❤️ for healthcare**