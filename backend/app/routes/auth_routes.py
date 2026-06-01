"""Authentication routes"""

from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
from app import db
from app.models import User, Patient, Doctor
from datetime import datetime, timedelta
import re

bp = Blueprint('auth', __name__, url_prefix='/api/auth')

def validate_mobile(mobile):
    """Validate Indian mobile number"""
    return re.match(r'^[6-9]\d{9}$', mobile) is not None

def validate_password(password):
    """Validate password strength"""
    return len(password) >= 8

@bp.route('/register', methods=['POST'])
def register():
    """User registration"""
    try:
        data = request.get_json()
        
        # Validate input
        if not data or not all(k in data for k in ['full_name', 'mobile_number', 'password', 'role']):
            return jsonify({'error': 'Missing required fields'}), 400
        
        full_name = data['full_name'].strip()
        mobile_number = data['mobile_number'].strip()
        password = data['password']
        role = data.get('role', 'patient')
        email = data.get('email', '').strip() or None
        
        # Validate inputs
        if not full_name or len(full_name) < 2:
            return jsonify({'error': 'Invalid full name'}), 400
        
        if not validate_mobile(mobile_number):
            return jsonify({'error': 'Invalid mobile number'}), 400
        
        if not validate_password(password):
            return jsonify({'error': 'Password must be at least 8 characters'}), 400
        
        if role not in ['patient', 'doctor', 'admin']:
            return jsonify({'error': 'Invalid role'}), 400
        
        # Check if user already exists
        if User.query.filter_by(mobile_number=mobile_number).first():
            return jsonify({'error': 'Mobile number already registered'}), 409
        
        # Create new user
        user = User(
            full_name=full_name,
            mobile_number=mobile_number,
            email=email,
            role=role,
            is_verified=False,
            is_active=True
        )
        user.set_password(password)
        db.session.add(user)
        db.session.flush()
        
        # Create patient profile if role is patient
        if role == 'patient':
            patient = Patient(user_id=user.id)
            db.session.add(patient)
        
        db.session.commit()
        
        return jsonify({
            'message': 'User registered successfully',
            'user': user.to_dict()
        }), 201
    
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500


@bp.route('/login', methods=['POST'])
def login():
    """User login"""
    try:
        data = request.get_json()
        
        if not data or not all(k in data for k in ['mobile_number', 'password']):
            return jsonify({'error': 'Missing credentials'}), 400
        
        mobile_number = data['mobile_number'].strip()
        password = data['password']
        
        # Find user
        user = User.query.filter_by(mobile_number=mobile_number).first()
        
        if not user or not user.verify_password(password):
            return jsonify({'error': 'Invalid credentials'}), 401
        
        if not user.is_active:
            return jsonify({'error': 'Account is inactive'}), 403
        
        # Create JWT token
        access_token = create_access_token(
            identity=user.id,
            additional_claims={'role': user.role, 'mobile': user.mobile_number},
            expires_delta=timedelta(hours=24)
        )
        
        return jsonify({
            'message': 'Login successful',
            'access_token': access_token,
            'user': user.to_dict()
        }), 200
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@bp.route('/logout', methods=['POST'])
@jwt_required()
def logout():
    """User logout"""
    return jsonify({'message': 'Logged out successfully'}), 200


@bp.route('/forgot-password', methods=['POST'])
def forgot_password():
    """Request password reset"""
    try:
        data = request.get_json()
        
        if not data or 'mobile_number' not in data:
            return jsonify({'error': 'Mobile number required'}), 400
        
        mobile_number = data['mobile_number'].strip()
        user = User.query.filter_by(mobile_number=mobile_number).first()
        
        if not user:
            return jsonify({'error': 'User not found'}), 404
        
        # TODO: Send SMS with reset link
        return jsonify({'message': 'Password reset link sent to your mobile'}), 200
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@bp.route('/profile', methods=['GET'])
@jwt_required()
def get_profile():
    """Get current user profile"""
    try:
        user_id = get_jwt_identity()
        user = User.query.get(user_id)
        
        if not user:
            return jsonify({'error': 'User not found'}), 404
        
        return jsonify({'user': user.to_dict()}), 200
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@bp.route('/profile', methods=['PUT'])
@jwt_required()
def update_profile():
    """Update user profile"""
    try:
        user_id = get_jwt_identity()
        user = User.query.get(user_id)
        
        if not user:
            return jsonify({'error': 'User not found'}), 404
        
        data = request.get_json()
        
        if 'full_name' in data:
            user.full_name = data['full_name'].strip()
        if 'email' in data:
            user.email = data['email'].strip() or None
        
        db.session.commit()
        
        return jsonify({
            'message': 'Profile updated successfully',
            'user': user.to_dict()
        }), 200
    
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500
