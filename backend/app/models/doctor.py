"""Doctor Model"""

from app import db
from datetime import datetime

class Doctor(db.Model):
    __tablename__ = 'doctors'
    
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), unique=True, nullable=False)
    specialization = db.Column(db.String(100), nullable=False)
    license_number = db.Column(db.String(100), unique=True, nullable=False)
    hospital_name = db.Column(db.String(255))
    experience_years = db.Column(db.Integer)
    qualifications = db.Column(db.Text)
    bio = db.Column(db.Text)
    consultation_fee = db.Column(db.Numeric(10, 2))
    availability_start = db.Column(db.Time)
    availability_end = db.Column(db.Time)
    rating = db.Column(db.Numeric(3, 2), default=0.00)
    total_ratings = db.Column(db.Integer, default=0)
    profile_photo_url = db.Column(db.String(500))
    is_verified = db.Column(db.Boolean, default=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    # Relationships
    prescriptions = db.relationship('Prescription', backref='doctor', cascade='all, delete-orphan')
    appointments = db.relationship('Appointment', backref='doctor', cascade='all, delete-orphan')
    messages = db.relationship('Message', backref='doctor', cascade='all, delete-orphan')
    
    def to_dict(self):
        return {
            'id': self.id,
            'user_id': self.user_id,
            'name': self.user.full_name if self.user else None,
            'specialization': self.specialization,
            'hospital_name': self.hospital_name,
            'experience_years': self.experience_years,
            'consultation_fee': float(self.consultation_fee) if self.consultation_fee else None,
            'rating': float(self.rating) if self.rating else 0,
            'is_verified': self.is_verified,
            'created_at': self.created_at.isoformat() if self.created_at else None
        }
