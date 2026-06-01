import React from 'react';
import { FaHeartbeat, FaShieldAlt, FaBrain, FaUsers } from 'react-icons/fa';
import { useNavigate } from 'react-router-dom';

const HomePage = () => {
  const navigate = useNavigate();

  return (
    <div className="bg-white">
      {/* Navigation */}
      <nav className="bg-primary-900 text-white p-4 shadow-lg">
        <div className="max-w-7xl mx-auto flex justify-between items-center">
          <h1 className="text-2xl font-bold">CuraAI</h1>
          <div className="space-x-4">
            <button
              onClick={() => navigate('/login')}
              className="px-4 py-2 bg-white text-primary-900 rounded font-bold hover:bg-gray-100"
            >
              Login
            </button>
            <button
              onClick={() => navigate('/register')}
              className="px-4 py-2 bg-primary-500 text-white rounded font-bold hover:bg-primary-600"
            >
              Register
            </button>
          </div>
        </div>
      </nav>

      {/* Hero Section */}
      <section className="bg-gradient-to-r from-primary-600 to-primary-800 text-white py-20 px-4">
        <div className="max-w-4xl mx-auto text-center">
          <h2 className="text-5xl font-bold mb-4">AI-Powered Healthcare Platform</h2>
          <p className="text-xl mb-8">Secure medical records, AI disease predictions, and seamless doctor connectivity</p>
          <div className="space-x-4">
            <button
              onClick={() => navigate('/register')}
              className="px-8 py-3 bg-white text-primary-900 rounded-lg font-bold hover:bg-gray-100"
            >
              Get Started
            </button>
            <button className="px-8 py-3 bg-primary-500 text-white rounded-lg font-bold hover:bg-primary-600">
              Learn More
            </button>
          </div>
        </div>
      </section>

      {/* Features Section */}
      <section className="py-16 px-4">
        <div className="max-w-6xl mx-auto">
          <h3 className="text-4xl font-bold text-center mb-12">Our Features</h3>
          <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-8">
            {[
              { icon: FaHeartbeat, title: 'Health Tracking', desc: 'Monitor your health metrics daily' },
              { icon: FaBrain, title: 'AI Predictions', desc: 'Get disease predictions from symptoms' },
              { icon: FaShieldAlt, title: 'Secure Records', desc: 'Your data is encrypted and safe' },
              { icon: FaUsers, title: 'Doctor Network', desc: 'Connect with verified specialists' },
            ].map((feature, idx) => (
              <div key={idx} className="bg-gray-50 p-8 rounded-lg text-center">
                <feature.icon size={40} className="text-primary-600 mx-auto mb-4" />
                <h4 className="text-xl font-bold mb-2">{feature.title}</h4>
                <p className="text-gray-600">{feature.desc}</p>
              </div>
            ))}
          </div>
        </div>
      </section>

      {/* Footer */}
      <footer className="bg-gray-900 text-white py-8 text-center">
        <p>&copy; 2026 CuraAI. All rights reserved.</p>
      </footer>
    </div>
  );
};

export default HomePage;
