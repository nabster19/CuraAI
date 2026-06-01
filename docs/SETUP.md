# CuraAI - Setup Guide

## Prerequisites

Before you start, make sure you have the following installed:

- **Node.js** (v16 or higher)
- **Python** (v3.8 or higher)
- **MySQL** (v8.0 or higher)
- **Git**

## Backend Setup

### 1. Install Python Dependencies

```bash
cd backend
python -m venv venv

# On Windows
venv\Scripts\activate

# On macOS/Linux
source venv/bin/activate

pip install -r requirements.txt
```

### 2. Configure Environment

```bash
cp .env.example .env
```

Edit `.env` with your configuration:

```env
FLASK_ENV=development
DATABASE_URL=mysql+pymysql://root:password@localhost/curaai
JWT_SECRET_KEY=your-super-secret-key
TWILIO_ACCOUNT_SID=your_twilio_sid
TWILIO_AUTH_TOKEN=your_twilio_token
TWILIO_PHONE_NUMBER=+1234567890
```

### 3. Setup Database

```bash
mysql -u root -p < ../database/schema.sql
mysql -u root -p < ../database/seed_data.sql
```

### 4. Run Flask Server

```bash
python run.py
```

Server will start at `http://localhost:5000`

## Frontend Setup

### 1. Install Node Dependencies

```bash
cd frontend
npm install
```

### 2. Start Development Server

```bash
npm run dev
```

Frontend will start at `http://localhost:3000`

## Database Setup

### Using MySQL CLI

```bash
# Login to MySQL
mysql -u root -p

# Run schema
source database/schema.sql;

# Run seed data
source database/seed_data.sql;
```

### Verify Installation

```bash
mysql -u root -p curaai
SHOW TABLES;
```

You should see all tables created.

## Testing the Application

### Test Data

Default test accounts created:

**Patient**
- Mobile: 9876543210
- Password: (set during registration)

**Doctor**
- Mobile: 9000000001
- Password: (set during registration)

**Admin**
- Mobile: 9999999999
- Password: (set during registration)

### API Testing

Use Postman or cURL:

```bash
# Register
curl -X POST http://localhost:5000/api/auth/register \
  -H "Content-Type: application/json" \
  -d '{
    "full_name": "John Doe",
    "mobile_number": "9876543210",
    "password": "password123",
    "role": "patient"
  }'

# Login
curl -X POST http://localhost:5000/api/auth/login \
  -H "Content-Type: application/json" \
  -d '{
    "mobile_number": "9876543210",
    "password": "password123"
  }'
```

## Troubleshooting

### Database Connection Error

```
Error: Access denied for user 'root'@'localhost'
```

**Solution:** Check MySQL credentials in `.env`

### Port Already in Use

```
Error: Address already in use
```

**Solution:** Change port in configuration

```bash
# Flask
API_PORT=5001

# React
npm run dev -- --port 3001
```

### Module Not Found

```
ModuleNotFoundError: No module named 'flask'
```

**Solution:** Install dependencies

```bash
pip install -r requirements.txt
```

## Next Steps

1. Read [API_DOCUMENTATION.md](./API_DOCUMENTATION.md) for API endpoints
2. Read [DEPLOYMENT.md](./DEPLOYMENT.md) for production deployment
3. Customize the application as needed

## Support

For issues, check:
- Backend logs: `logs/curaai.log`
- Browser console for frontend errors
- MySQL error logs
