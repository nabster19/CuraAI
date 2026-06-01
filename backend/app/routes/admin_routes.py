"""Admin routes"""

from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity, get_jwt
from app import db
from app.models import User, Patient, Doctor, Appointment, Notification

bp = Blueprint('admin', __name__, url_prefix='/api/admin')

@bp.before_request
@jwt_required()
def check_admin():
    """Verify user is admin"""
    claims = get_jwt()
    if claims.get('role') != 'admin':
        return {'error': 'Admin access required'}, 403


@bp.route('/users', methods=['GET'])
def get_users():
    """Get all users"""
    try:
        users = User.query.all()
        return jsonify({
            'users': [u.to_dict() for u in users]
        }), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@bp.route('/doctors', methods=['GET'])
def get_doctors():
    """Get all doctors"""
    try:
        doctors = Doctor.query.all()
        return jsonify({
            'doctors': [d.to_dict() for d in doctors]
        }), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@bp.route('/appointments', methods=['GET'])
def get_appointments():
    """Get all appointments"""
    try:
        appointments = Appointment.query.all()
        return jsonify({
            'appointments': [a.to_dict() for a in appointments]
        }), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@bp.route('/stats', methods=['GET'])
def get_stats():
    """Get platform statistics"""
    try:
        stats = {
            'total_users': User.query.count(),
            'total_patients': Patient.query.count(),
            'total_doctors': Doctor.query.count(),
            'total_appointments': Appointment.query.count(),
            'pending_appointments': Appointment.query.filter_by(status='Pending').count()
        }
        return jsonify(stats), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500
