# CuraAI Deployment Guide

## Prerequisites

- AWS Account (or any cloud provider)
- Git
- Docker (optional but recommended)

## Deployment Options

## 1. Docker Deployment (Recommended)

### Create Dockerfile for Backend

```dockerfile
FROM python:3.9-slim

WORKDIR /app

COPY backend/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY backend/ .

EXPOSE 5000

CMD ["gunicorn", "--bind", "0.0.0.0:5000", "run:app"]
```

### Create Dockerfile for Frontend

```dockerfile
FROM node:16-alpine

WORKDIR /app

COPY frontend/package*.json .
RUN npm install

COPY frontend/ .
RUN npm run build

FROM nginx:alpine
COPY --from=0 /app/dist /usr/share/nginx/html
COPY nginx.conf /etc/nginx/conf.d/default.conf

EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]
```

### Create docker-compose.yml

```yaml
version: '3.8'

services:
  mysql:
    image: mysql:8.0
    environment:
      MYSQL_ROOT_PASSWORD: root
      MYSQL_DATABASE: curaai
    ports:
      - "3306:3306"
    volumes:
      - mysql_data:/var/lib/mysql

  backend:
    build:
      context: .
      dockerfile: Dockerfile.backend
    ports:
      - "5000:5000"
    environment:
      DATABASE_URL: mysql+pymysql://root:root@mysql/curaai
      FLASK_ENV: production
      JWT_SECRET_KEY: your-secret-key
    depends_on:
      - mysql

  frontend:
    build:
      context: .
      dockerfile: Dockerfile.frontend
    ports:
      - "80:80"
    depends_on:
      - backend

volumes:
  mysql_data:
```

### Run with Docker Compose

```bash
docker-compose up -d
```

## 2. AWS EC2 Deployment

### Step 1: Launch EC2 Instance

1. Go to AWS Console
2. Launch Ubuntu 20.04 LTS instance
3. Configure security groups:
   - Port 22 (SSH)
   - Port 80 (HTTP)
   - Port 443 (HTTPS)
   - Port 3000 (Frontend dev)
   - Port 5000 (Backend)

### Step 2: SSH into Instance

```bash
ssh -i your-key.pem ubuntu@your-instance-ip
```

### Step 3: Install Dependencies

```bash
sudo apt update
sudo apt install -y python3-pip python3-venv node.js npm mysql-server nginx
```

### Step 4: Clone Repository

```bash
git clone https://github.com/nabster19/CuraAI.git
cd CuraAI
```

### Step 5: Setup Backend

```bash
cd backend
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

# Configure environment
cp .env.example .env
# Edit .env with your settings

# Install gunicorn
pip install gunicorn
```

### Step 6: Setup Frontend

```bash
cd ../frontend
npm install
npm run build
```

### Step 7: Configure Nginx

Create `/etc/nginx/sites-available/curaai`:

```nginx
server {
    listen 80;
    server_name your-domain.com;

    # Frontend
    location / {
        root /home/ubuntu/CuraAI/frontend/dist;
        try_files $uri $uri/ /index.html;
    }

    # Backend API
    location /api/ {
        proxy_pass http://localhost:5000/api/;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
    }
}
```

Enable site:

```bash
sudo ln -s /etc/nginx/sites-available/curaai /etc/nginx/sites-enabled/
sudo nginx -t
sudo systemctl restart nginx
```

### Step 8: Setup Systemd Service

Create `/etc/systemd/system/curaai-backend.service`:

```ini
[Unit]
Description=CuraAI Backend
After=network.target

[Service]
User=ubuntu
WorkingDirectory=/home/ubuntu/CuraAI/backend
ExecStart=/home/ubuntu/CuraAI/backend/venv/bin/gunicorn -w 4 -b 0.0.0.0:5000 run:app
Restart=always

[Install]
WantedBy=multi-user.target
```

Start service:

```bash
sudo systemctl enable curaai-backend
sudo systemctl start curaai-backend
```

## 3. Heroku Deployment

### Step 1: Install Heroku CLI

```bash
curl https://cli-assets.heroku.com/install.sh | sh
```

### Step 2: Login to Heroku

```bash
heroku login
```

### Step 3: Create Procfile

```
web: gunicorn run:app
```

### Step 4: Deploy Backend

```bash
cd backend
heroku create your-app-name
heroku addons:create cleardb:ignite
git push heroku main
```

### Step 5: Deploy Frontend

```bash
cd frontend
npm run build

# Deploy to Vercel or Netlify
vercel deploy
```

## 4. DigitalOcean Deployment

### Step 1: Create Droplet

1. Go to DigitalOcean console
2. Create Ubuntu 20.04 droplet
3. SSH into droplet

### Step 2: Install Docker

```bash
curl -fsSL https://get.docker.com -o get-docker.sh
sudo sh get-docker.sh
```

### Step 3: Deploy with Docker

```bash
git clone https://github.com/nabster19/CuraAI.git
cd CuraAI
docker-compose up -d
```

## SSL/TLS Certificate (Let's Encrypt)

```bash
sudo apt install certbot python3-certbot-nginx
sudo certbot certonly --nginx -d your-domain.com

# Auto-renew
sudo systemctl enable certbot.timer
```

## Environment Variables for Production

```env
FLASK_ENV=production
DATABASE_URL=mysql+pymysql://user:password@host/dbname
JWT_SECRET_KEY=very-long-random-secret-key
TWILIO_ACCOUNT_SID=your_sid
TWILIO_AUTH_TOKEN=your_token
TWILIO_PHONE_NUMBER=+1234567890
CORS_ORIGINS=https://your-domain.com
```

## Monitoring

### Setup Logging

```bash
# View backend logs
journalctl -u curaai-backend -f

# View nginx logs
sudo tail -f /var/log/nginx/error.log
```

### Setup Monitoring with New Relic

```bash
pip install newrelic
newrelic-admin generate-config your-license-key newrelic.ini
```

## Backup Strategy

### MySQL Backup

```bash
mysqldump -u root -p curaai > backup.sql

# Restore
mysql -u root -p curaai < backup.sql
```

### Automated Daily Backup

```bash
#!/bin/bash
BACKUP_DIR="/backups"
DATE=$(date +%Y%m%d_%H%M%S)
mysqldump -u root -p$DB_PASSWORD curaai > $BACKUP_DIR/curaai_$DATE.sql

# Upload to S3
aws s3 cp $BACKUP_DIR/curaai_$DATE.sql s3://your-bucket/backups/
```

## Troubleshooting

### Backend won't start

```bash
# Check service status
sudo systemctl status curaai-backend

# Check logs
journalctl -u curaai-backend -n 50
```

### Database connection error

```bash
# Test connection
mysql -u user -p -h host -D database
```

### SSL certificate issues

```bash
# Renew certificate
sudo certbot renew
```
