"""Patient routes"""

from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity, get_jwt
from app import db
from app.models import Patient, HealthRecord, HealthTracking, Symptom
from datetime import datetime, date
import json

bp = Blueprint('patient', __name__, url_prefix='/api/patient')

@bp.before_request
@jwt_required()
def check_patient_role():
    """Verify user is a patient"""
    claims = get_jwt()
    if claims.get('role') not in ['patient', 'admin']:
        return {'error': 'Unauthorized'}, 403


@bp.route('/profile', methods=['GET'])
def get_patient_profile():
    """Get patient profile"""
    try:
        user_id = get_jwt_identity()
        patient = Patient.query.filter_by(user_id=user_id).first()
        
        if not patient:
            return jsonify({'error': 'Patient profile not found'}), 404
        
        return jsonify({'patient': patient.to_dict()}), 200
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@bp.route('/profile', methods=['PUT'])
def update_patient_profile():
    """Update patient profile"""
    try:
        user_id = get_jwt_identity()
        patient = Patient.query.filter_by(user_id=user_id).first()
        
        if not patient:
            return jsonify({'error': 'Patient profile not found'}), 404
        
        data = request.get_json()
        
        # Update fields
        allowed_fields = ['age', 'gender', 'blood_type', 'emergency_contact', 
                         'emergency_contact_name', 'address', 'city', 'state', 'pincode']
        
        for field in allowed_fields:
            if field in data:
                setattr(patient, field, data[field])
        
        db.session.commit()
        
        return jsonify({
            'message': 'Patient profile updated',
            'patient': patient.to_dict()
        }), 200
    
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500


@bp.route('/health-records', methods=['GET'])
def get_health_records():
    """Get patient health records"""
    try:
        user_id = get_jwt_identity()
        patient = Patient.query.filter_by(user_id=user_id).first()
        
        if not patient:
            return jsonify({'error': 'Patient not found'}), 404
        
        records = HealthRecord.query.filter_by(patient_id=patient.id)\
            .order_by(HealthRecord.record_date.desc()).all()
        
        return jsonify({
            'records': [r.to_dict() for r in records]
        }), 200
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@bp.route('/health-records', methods=['POST'])
def add_health_record():
    """Add health record"""
    try:
        user_id = get_jwt_identity()
        patient = Patient.query.filter_by(user_id=user_id).first()
        
        if not patient:
            return jsonify({'error': 'Patient not found'}), 404
        
        data = request.get_json()
        
        record = HealthRecord(
            patient_id=patient.id,
            height_cm=data.get('height_cm'),
            weight_kg=data.get('weight_kg'),
            blood_pressure_systolic=data.get('blood_pressure_systolic'),
            blood_pressure_diastolic=data.get('blood_pressure_diastolic'),
            blood_sugar_fasting=data.get('blood_sugar_fasting'),
            cholesterol_total=data.get('cholesterol_total'),
            heart_rate=data.get('heart_rate'),
            oxygen_saturation=data.get('oxygen_saturation'),
            existing_diseases=data.get('existing_diseases'),
            allergies=data.get('allergies'),
            current_medications=data.get('current_medications'),
            notes=data.get('notes')
        )
        
        db.session.add(record)
        db.session.commit()
        
        return jsonify({
            'message': 'Health record added',
            'record': record.to_dict()
        }), 201
    
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500


@bp.route('/symptoms', methods=['POST'])
def add_symptom():
    """Add symptom"""
    try:
        user_id = get_jwt_identity()
        patient = Patient.query.filter_by(user_id=user_id).first()
        
        if not patient:
            return jsonify({'error': 'Patient not found'}), 404
        
        data = request.get_json()
        
        if not data.get('symptom_text'):
            return jsonify({'error': 'Symptom text required'}), 400
        
        symptom = Symptom(
            patient_id=patient.id,
            symptom_text=data['symptom_text'],
            severity=data.get('severity', 'Mild'),
            duration_days=data.get('duration_days')
        )
        
        db.session.add(symptom)
        db.session.commit()
        
        return jsonify({
            'message': 'Symptom recorded',
            'symptom': symptom.to_dict()
        }), 201
    
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500


@bp.route('/health-tracking', methods=['POST'])
def add_health_tracking():
    """Add daily health tracking"""
    try:
        user_id = get_jwt_identity()
        patient = Patient.query.filter_by(user_id=user_id).first()
        
        if not patient:
            return jsonify({'error': 'Patient not found'}), 404
        
        data = request.get_json()
        tracking_date = data.get('tracking_date', str(date.today()))
        
        tracking = HealthTracking(
            patient_id=patient.id,
            tracking_date=datetime.strptime(tracking_date, '%Y-%m-%d').date(),
            blood_pressure_systolic=data.get('blood_pressure_systolic'),
            blood_pressure_diastolic=data.get('blood_pressure_diastolic'),
            weight_kg=data.get('weight_kg'),
            blood_sugar=data.get('blood_sugar'),
            cholesterol=data.get('cholesterol'),
            water_intake_ml=data.get('water_intake_ml'),
            heart_rate=data.get('heart_rate'),
            sleep_hours=data.get('sleep_hours'),
            exercise_minutes=data.get('exercise_minutes'),
            mood=data.get('mood'),
            notes=data.get('notes')
        )
        
        db.session.add(tracking)
        db.session.commit()
        
        return jsonify({
            'message': 'Health data tracked',
            'tracking': tracking.to_dict()
        }), 201
    
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500
