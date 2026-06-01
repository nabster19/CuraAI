"""Doctor routes"""

from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity, get_jwt
from app import db
from app.models import Doctor, User

bp = Blueprint('doctor', __name__, url_prefix='/api/doctor')

@bp.route('/list', methods=['GET'])
def list_doctors():
    """Get list of all doctors"""
    try:
        specialization = request.args.get('specialization')
        
        query = Doctor.query.filter_by(is_verified=True)
        
        if specialization:
            query = query.filter_by(specialization=specialization)
        
        doctors = query.all()
        
        return jsonify({
            'doctors': [d.to_dict() for d in doctors]
        }), 200
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@bp.route('/<int:doctor_id>', methods=['GET'])
def get_doctor(doctor_id):
    """Get doctor details"""
    try:
        doctor = Doctor.query.get(doctor_id)
        
        if not doctor:
            return jsonify({'error': 'Doctor not found'}), 404
        
        doctor_data = doctor.to_dict()
        doctor_data['contact_info'] = {
            'mobile': doctor.user.mobile_number if doctor.user else None,
            'email': doctor.user.email if doctor.user else None
        }
        
        return jsonify({'doctor': doctor_data}), 200
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@bp.route('/specializations', methods=['GET'])
def get_specializations():
    """Get all doctor specializations"""
    try:
        specializations = db.session.query(Doctor.specialization).distinct().all()
        specs = [s[0] for s in specializations if s[0]]
        
        return jsonify({
            'specializations': specs
        }), 200
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@bp.route('/profile', methods=['GET'])
@jwt_required()
def get_doctor_profile():
    """Get own doctor profile"""
    try:
        user_id = get_jwt_identity()
        claims = get_jwt()
        
        if claims.get('role') != 'doctor':
            return jsonify({'error': 'Not authorized'}), 403
        
        doctor = Doctor.query.filter_by(user_id=user_id).first()
        
        if not doctor:
            return jsonify({'error': 'Doctor profile not found'}), 404
        
        return jsonify({'doctor': doctor.to_dict()}), 200
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500
