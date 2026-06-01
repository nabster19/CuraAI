#!/bin/bash
# CuraAI Setup Script

echo "🏥 CuraAI - Healthcare Platform Setup"
echo "====================================="
echo ""

# Check prerequisites
echo "Checking prerequisites..."

command -v python3 &> /dev/null || { echo "❌ Python 3 not found"; exit 1; }
command -v node &> /dev/null || { echo "❌ Node.js not found"; exit 1; }
command -v mysql &> /dev/null || { echo "❌ MySQL not found"; exit 1; }

echo "✓ All prerequisites found"
echo ""

# Backend setup
echo "Setting up backend..."
cd backend
python3 -m venv venv
source venv/bin/activate 2>/dev/null || . venv/Scripts/activate 2>/dev/null
pip install -r requirements.txt
cp .env.example .env
echo "✓ Backend setup complete"
echo ""

# Frontend setup
echo "Setting up frontend..."
cd ../frontend
npm install
echo "✓ Frontend setup complete"
echo ""

echo "====================================="
echo "✓ Setup complete!"
echo ""
echo "Next steps:"
echo "1. Configure database/MySQL"
echo "2. Edit backend/.env with database credentials"
echo "3. Run 'npm run dev' in frontend/ for development"
echo "4. Run 'python run.py' in backend/ for API server"
echo ""
