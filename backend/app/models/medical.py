"""Medical Records and Appointment Models"""

from app import db
from datetime import datetime, date

class Prescription(db.Model):
    __tablename__ = 'prescriptions'
    
    id = db.Column(db.Integer, primary_key=True)
    patient_id = db.Column(db.Integer, db.ForeignKey('patients.id'), nullable=False)
    doctor_id = db.Column(db.Integer, db.ForeignKey('doctors.id'))
    prescription_file_url = db.Column(db.String(500))
    extracted_medicines = db.Column(db.Text)
    extracted_diagnosis = db.Column(db.Text)
    upload_date = db.Column(db.DateTime, default=datetime.utcnow)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    def to_dict(self):
        return {
            'id': self.id,
            'patient_id': self.patient_id,
            'doctor_id': self.doctor_id,
            'prescription_file_url': self.prescription_file_url,
            'extracted_medicines': self.extracted_medicines,
            'upload_date': self.upload_date.isoformat() if self.upload_date else None
        }


class Report(db.Model):
    __tablename__ = 'reports'
    
    id = db.Column(db.Integer, primary_key=True)
    patient_id = db.Column(db.Integer, db.ForeignKey('patients.id'), nullable=False)
    report_type = db.Column(db.String(100), default='Other')
    report_file_url = db.Column(db.String(500))
    extracted_text = db.Column(db.Text)
    ai_summary = db.Column(db.Text)
    report_date = db.Column(db.Date)
    upload_date = db.Column(db.DateTime, default=datetime.utcnow)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    def to_dict(self):
        return {
            'id': self.id,
            'patient_id': self.patient_id,
            'report_type': self.report_type,
            'report_file_url': self.report_file_url,
            'ai_summary': self.ai_summary,
            'upload_date': self.upload_date.isoformat() if self.upload_date else None
        }


class Appointment(db.Model):
    __tablename__ = 'appointments'
    
    id = db.Column(db.Integer, primary_key=True)
    patient_id = db.Column(db.Integer, db.ForeignKey('patients.id'), nullable=False)
    doctor_id = db.Column(db.Integer, db.ForeignKey('doctors.id'), nullable=False)
    appointment_date = db.Column(db.DateTime, nullable=False)
    consultation_type = db.Column(db.String(20), default='In-Person')
    status = db.Column(db.String(20), default='Pending')
    notes = db.Column(db.Text)
    reason_for_visit = db.Column(db.Text)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    def to_dict(self):
        return {
            'id': self.id,
            'patient_id': self.patient_id,
            'doctor_id': self.doctor_id,
            'appointment_date': self.appointment_date.isoformat() if self.appointment_date else None,
            'consultation_type': self.consultation_type,
            'status': self.status,
            'reason_for_visit': self.reason_for_visit,
            'created_at': self.created_at.isoformat() if self.created_at else None
        }


class Message(db.Model):
    __tablename__ = 'messages'
    
    id = db.Column(db.Integer, primary_key=True)
    patient_id = db.Column(db.Integer, db.ForeignKey('patients.id'), nullable=False)
    doctor_id = db.Column(db.Integer, db.ForeignKey('doctors.id'), nullable=False)
    sender_type = db.Column(db.String(20), nullable=False)
    message_text = db.Column(db.Text, nullable=False)
    is_read = db.Column(db.Boolean, default=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    def to_dict(self):
        return {
            'id': self.id,
            'patient_id': self.patient_id,
            'doctor_id': self.doctor_id,
            'sender_type': self.sender_type,
            'message_text': self.message_text,
            'is_read': self.is_read,
            'created_at': self.created_at.isoformat() if self.created_at else None
        }
