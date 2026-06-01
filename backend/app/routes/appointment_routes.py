"""Appointment routes"""

from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity, get_jwt
from app import db
from app.models import Appointment, Patient, Doctor, User
from datetime import datetime

bp = Blueprint('appointment', __name__, url_prefix='/api/appointments')

@bp.route('', methods=['GET'])
@jwt_required()
def get_appointments():
    """Get user appointments"""
    try:
        user_id = get_jwt_identity()
        claims = get_jwt()
        role = claims.get('role')
        
        if role == 'patient':
            patient = Patient.query.filter_by(user_id=user_id).first()
            appointments = Appointment.query.filter_by(patient_id=patient.id)\
                .order_by(Appointment.appointment_date).all()
        elif role == 'doctor':
            doctor = Doctor.query.filter_by(user_id=user_id).first()
            appointments = Appointment.query.filter_by(doctor_id=doctor.id)\
                .order_by(Appointment.appointment_date).all()
        else:
            appointments = Appointment.query.all()
        
        return jsonify({
            'appointments': [a.to_dict() for a in appointments]
        }), 200
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@bp.route('', methods=['POST'])
@jwt_required()
def book_appointment():
    """Book appointment"""
    try:
        user_id = get_jwt_identity()
        claims = get_jwt()
        
        if claims.get('role') != 'patient':
            return jsonify({'error': 'Only patients can book appointments'}), 403
        
        patient = Patient.query.filter_by(user_id=user_id).first()
        if not patient:
            return jsonify({'error': 'Patient not found'}), 404
        
        data = request.get_json()
        
        if not data.get('doctor_id') or not data.get('appointment_date'):
            return jsonify({'error': 'Missing required fields'}), 400
        
        doctor = Doctor.query.get(data['doctor_id'])
        if not doctor:
            return jsonify({'error': 'Doctor not found'}), 404
        
        appointment = Appointment(
            patient_id=patient.id,
            doctor_id=doctor.id,
            appointment_date=datetime.fromisoformat(data['appointment_date']),
            consultation_type=data.get('consultation_type', 'In-Person'),
            reason_for_visit=data.get('reason_for_visit'),
            status='Pending'
        )
        
        db.session.add(appointment)
        db.session.commit()
        
        return jsonify({
            'message': 'Appointment booked successfully',
            'appointment': appointment.to_dict()
        }), 201
    
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500


@bp.route('/<int:appointment_id>', methods=['PUT'])
@jwt_required()
def update_appointment(appointment_id):
    """Update appointment"""
    try:
        appointment = Appointment.query.get(appointment_id)
        
        if not appointment:
            return jsonify({'error': 'Appointment not found'}), 404
        
        data = request.get_json()
        
        if 'status' in data:
            appointment.status = data['status']
        if 'notes' in data:
            appointment.notes = data['notes']
        
        db.session.commit()
        
        return jsonify({
            'message': 'Appointment updated',
            'appointment': appointment.to_dict()
        }), 200
    
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500
