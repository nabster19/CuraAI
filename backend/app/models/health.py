"""Health Records and Tracking Models"""

from app import db
from datetime import datetime, date

class HealthRecord(db.Model):
    __tablename__ = 'health_records'
    
    id = db.Column(db.Integer, primary_key=True)
    patient_id = db.Column(db.Integer, db.ForeignKey('patients.id'), nullable=False)
    height_cm = db.Column(db.Numeric(5, 2))
    weight_kg = db.Column(db.Numeric(5, 2))
    blood_pressure_systolic = db.Column(db.Integer)
    blood_pressure_diastolic = db.Column(db.Integer)
    blood_sugar_fasting = db.Column(db.Integer)
    blood_sugar_random = db.Column(db.Integer)
    cholesterol_total = db.Column(db.Integer)
    cholesterol_ldl = db.Column(db.Integer)
    cholesterol_hdl = db.Column(db.Integer)
    triglycerides = db.Column(db.Integer)
    heart_rate = db.Column(db.Integer)
    oxygen_saturation = db.Column(db.Numeric(3, 1))
    bmi = db.Column(db.Numeric(5, 2))
    existing_diseases = db.Column(db.Text)
    allergies = db.Column(db.Text)
    current_medications = db.Column(db.Text)
    notes = db.Column(db.Text)
    record_date = db.Column(db.DateTime, default=datetime.utcnow)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    def to_dict(self):
        return {
            'id': self.id,
            'patient_id': self.patient_id,
            'height_cm': float(self.height_cm) if self.height_cm else None,
            'weight_kg': float(self.weight_kg) if self.weight_kg else None,
            'blood_pressure': f"{self.blood_pressure_systolic}/{self.blood_pressure_diastolic}" if self.blood_pressure_systolic else None,
            'blood_sugar_fasting': self.blood_sugar_fasting,
            'cholesterol_total': self.cholesterol_total,
            'heart_rate': self.heart_rate,
            'oxygen_saturation': float(self.oxygen_saturation) if self.oxygen_saturation else None,
            'bmi': float(self.bmi) if self.bmi else None,
            'existing_diseases': self.existing_diseases,
            'allergies': self.allergies,
            'current_medications': self.current_medications,
            'record_date': self.record_date.isoformat() if self.record_date else None
        }


class HealthTracking(db.Model):
    __tablename__ = 'health_tracking'
    
    id = db.Column(db.Integer, primary_key=True)
    patient_id = db.Column(db.Integer, db.ForeignKey('patients.id'), nullable=False)
    tracking_date = db.Column(db.Date, nullable=False)
    blood_pressure_systolic = db.Column(db.Integer)
    blood_pressure_diastolic = db.Column(db.Integer)
    weight_kg = db.Column(db.Numeric(5, 2))
    blood_sugar = db.Column(db.Numeric(5, 1))
    cholesterol = db.Column(db.Integer)
    water_intake_ml = db.Column(db.Integer)
    heart_rate = db.Column(db.Integer)
    steps_count = db.Column(db.Integer)
    sleep_hours = db.Column(db.Numeric(3, 1))
    exercise_minutes = db.Column(db.Integer)
    mood = db.Column(db.String(50))
    notes = db.Column(db.Text)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    def to_dict(self):
        return {
            'id': self.id,
            'patient_id': self.patient_id,
            'tracking_date': str(self.tracking_date),
            'weight_kg': float(self.weight_kg) if self.weight_kg else None,
            'blood_sugar': float(self.blood_sugar) if self.blood_sugar else None,
            'heart_rate': self.heart_rate,
            'mood': self.mood,
            'created_at': self.created_at.isoformat() if self.created_at else None
        }
