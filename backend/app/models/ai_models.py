"""AI Predictions and Recommendations Models"""

from app import db
from datetime import datetime

class Symptom(db.Model):
    __tablename__ = 'symptoms'
    
    id = db.Column(db.Integer, primary_key=True)
    patient_id = db.Column(db.Integer, db.ForeignKey('patients.id'), nullable=False)
    symptom_text = db.Column(db.Text, nullable=False)
    severity = db.Column(db.String(20), default='Mild')
    duration_days = db.Column(db.Integer)
    symptom_date = db.Column(db.DateTime, default=datetime.utcnow)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    # Relationships
    disease_predictions = db.relationship('DiseasePrediction', backref='symptom', cascade='all, delete-orphan')
    
    def to_dict(self):
        return {
            'id': self.id,
            'patient_id': self.patient_id,
            'symptom_text': self.symptom_text,
            'severity': self.severity,
            'duration_days': self.duration_days,
            'symptom_date': self.symptom_date.isoformat() if self.symptom_date else None
        }


class DiseasePrediction(db.Model):
    __tablename__ = 'disease_predictions'
    
    id = db.Column(db.Integer, primary_key=True)
    patient_id = db.Column(db.Integer, db.ForeignKey('patients.id'), nullable=False)
    symptom_id = db.Column(db.Integer, db.ForeignKey('symptoms.id'))
    predicted_disease = db.Column(db.String(255), nullable=False)
    confidence_percentage = db.Column(db.Numeric(5, 2))
    severity_level = db.Column(db.String(20), default='Mild')
    precautions = db.Column(db.Text)
    requires_doctor_visit = db.Column(db.Boolean, default=True)
    is_rare_disease = db.Column(db.Boolean, default=False)
    prediction_date = db.Column(db.DateTime, default=datetime.utcnow)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    # Relationships
    drug_recommendations = db.relationship('DrugRecommendation', backref='disease_prediction', cascade='all, delete-orphan')
    
    def to_dict(self):
        return {
            'id': self.id,
            'patient_id': self.patient_id,
            'predicted_disease': self.predicted_disease,
            'confidence_percentage': float(self.confidence_percentage) if self.confidence_percentage else 0,
            'severity_level': self.severity_level,
            'precautions': self.precautions,
            'requires_doctor_visit': self.requires_doctor_visit,
            'is_rare_disease': self.is_rare_disease,
            'prediction_date': self.prediction_date.isoformat() if self.prediction_date else None
        }


class DrugRecommendation(db.Model):
    __tablename__ = 'drug_recommendations'
    
    id = db.Column(db.Integer, primary_key=True)
    patient_id = db.Column(db.Integer, db.ForeignKey('patients.id'), nullable=False)
    disease_prediction_id = db.Column(db.Integer, db.ForeignKey('disease_predictions.id'))
    medicine_name = db.Column(db.String(255), nullable=False)
    dosage = db.Column(db.String(100))
    frequency = db.Column(db.String(100))
    duration_days = db.Column(db.Integer)
    side_effects = db.Column(db.Text)
    food_restrictions = db.Column(db.Text)
    alternative_medicines = db.Column(db.Text)
    warning_message = db.Column(db.Text, default='This recommendation is AI-generated and should be verified by a licensed doctor.')
    recommendation_date = db.Column(db.DateTime, default=datetime.utcnow)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    def to_dict(self):
        return {
            'id': self.id,
            'patient_id': self.patient_id,
            'medicine_name': self.medicine_name,
            'dosage': self.dosage,
            'frequency': self.frequency,
            'duration_days': self.duration_days,
            'side_effects': self.side_effects,
            'food_restrictions': self.food_restrictions,
            'warning_message': self.warning_message,
            'recommendation_date': self.recommendation_date.isoformat() if self.recommendation_date else None
        }
