"""Patient Model"""

from app import db
from datetime import datetime

class Patient(db.Model):
    __tablename__ = 'patients'
    
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), unique=True, nullable=False)
    age = db.Column(db.Integer)
    gender = db.Column(db.String(20))
    blood_type = db.Column(db.String(5))
    emergency_contact = db.Column(db.String(20))
    emergency_contact_name = db.Column(db.String(255))
    address = db.Column(db.Text)
    city = db.Column(db.String(100))
    state = db.Column(db.String(100))
    pincode = db.Column(db.String(10))
    profile_photo_url = db.Column(db.String(500))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    # Relationships
    health_records = db.relationship('HealthRecord', backref='patient', cascade='all, delete-orphan')
    symptoms = db.relationship('Symptom', backref='patient', cascade='all, delete-orphan')
    disease_predictions = db.relationship('DiseasePrediction', backref='patient', cascade='all, delete-orphan')
    drug_recommendations = db.relationship('DrugRecommendation', backref='patient', cascade='all, delete-orphan')
    prescriptions = db.relationship('Prescription', backref='patient', cascade='all, delete-orphan')
    reports = db.relationship('Report', backref='patient', cascade='all, delete-orphan')
    appointments = db.relationship('Appointment', backref='patient', cascade='all, delete-orphan')
    messages = db.relationship('Message', backref='patient', cascade='all, delete-orphan')
    health_tracking = db.relationship('HealthTracking', backref='patient', cascade='all, delete-orphan')
    
    def to_dict(self):
        return {
            'id': self.id,
            'user_id': self.user_id,
            'age': self.age,
            'gender': self.gender,
            'blood_type': self.blood_type,
            'emergency_contact': self.emergency_contact,
            'city': self.city,
            'state': self.state,
            'created_at': self.created_at.isoformat() if self.created_at else None
        }
