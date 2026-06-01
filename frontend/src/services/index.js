import api from './api';

// Authentication
export const authService = {
  register: (data) => api.post('/auth/register', data),
  login: (data) => api.post('/auth/login', data),
  logout: () => api.post('/auth/logout'),
  getProfile: () => api.get('/auth/profile'),
  updateProfile: (data) => api.put('/auth/profile', data),
  forgotPassword: (mobile) => api.post('/auth/forgot-password', { mobile_number: mobile }),
};

// Patient
export const patientService = {
  getProfile: () => api.get('/patient/profile'),
  updateProfile: (data) => api.put('/patient/profile', data),
  getHealthRecords: () => api.get('/patient/health-records'),
  addHealthRecord: (data) => api.post('/patient/health-records', data),
  getHealthTracking: () => api.get('/patient/health-tracking'),
  addHealthTracking: (data) => api.post('/patient/health-tracking', data),
  addSymptom: (data) => api.post('/patient/symptoms', data),
};

// Doctor
export const doctorService = {
  listDoctors: (specialization) => 
    api.get('/doctor/list', { params: { specialization } }),
  getDoctor: (id) => api.get(`/doctor/${id}`),
  getSpecializations: () => api.get('/doctor/specializations'),
  getProfile: () => api.get('/doctor/profile'),
};

// Appointments
export const appointmentService = {
  getAppointments: () => api.get('/appointments'),
  bookAppointment: (data) => api.post('/appointments', data),
  updateAppointment: (id, data) => api.put(`/appointments/${id}`, data),
};

// AI
export const aiService = {
  predictDisease: (data) => api.post('/ai/predict-disease', data),
  recommendDrugs: (data) => api.post('/ai/recommend-drugs', data),
  recommendDoctors: (data) => api.post('/ai/recommend-doctors', data),
};

// Admin
export const adminService = {
  getUsers: () => api.get('/admin/users'),
  getDoctors: () => api.get('/admin/doctors'),
  getAppointments: () => api.get('/admin/appointments'),
  getStats: () => api.get('/admin/stats'),
};
