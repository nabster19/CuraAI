import React, { useState, useEffect } from 'react';
import { patientService } from '../services';
import Sidebar from '../components/Sidebar';
import HealthCard from '../components/HealthCard';
import { FiPlus } from 'react-icons/fi';

const DashboardPage = () => {
  const [sidebarOpen, setSidebarOpen] = useState(false);
  const [healthData, setHealthData] = useState(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    fetchHealthData();
  }, []);

  const fetchHealthData = async () => {
    try {
      const response = await patientService.getHealthRecords();
      if (response.data.records.length > 0) {
        setHealthData(response.data.records[0]);
      }
    } catch (error) {
      console.error('Error fetching health data:', error);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="flex bg-gray-50 min-h-screen">
      <Sidebar isOpen={sidebarOpen} setIsOpen={setSidebarOpen} />

      <main className="flex-1 p-4 md:p-8 md:ml-0">
        <div className="mt-12 md:mt-0">
          <h1 className="text-3xl font-bold text-gray-900 mb-2">Welcome to CuraAI</h1>
          <p className="text-gray-600 mb-8">Your Personal Health Management Dashboard</p>

          {/* Health Cards Grid */}
          <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6 mb-8">
            <HealthCard
              title="Weight"
              value={healthData?.weight_kg || '-'}
              unit="kg"
              trend={2.5}
              color="border-blue-500"
            />
            <HealthCard
              title="Blood Pressure"
              value={healthData?.blood_pressure || '-'}
              unit="mmHg"
              trend={-1.2}
              color="border-red-500"
            />
            <HealthCard
              title="Heart Rate"
              value={healthData?.heart_rate || '-'}
              unit="bpm"
              trend={0}
              color="border-green-500"
            />
            <HealthCard
              title="BMI"
              value={healthData?.bmi || '-'}
              unit="kg/m²"
              trend={1.5}
              color="border-orange-500"
            />
          </div>

          {/* Quick Actions */}
          <div className="bg-white rounded-lg shadow p-6">
            <h2 className="text-2xl font-bold text-gray-900 mb-4">Quick Actions</h2>
            <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
              <button className="flex items-center justify-center space-x-2 bg-primary-600 hover:bg-primary-700 text-white py-3 px-6 rounded-lg transition">
                <FiPlus size={20} />
                <span>Add Health Record</span>
              </button>
              <button className="flex items-center justify-center space-x-2 bg-primary-600 hover:bg-primary-700 text-white py-3 px-6 rounded-lg transition">
                <FiPlus size={20} />
                <span>Track Symptoms</span>
              </button>
            </div>
          </div>
        </div>
      </main>
    </div>
  );
};

export default DashboardPage;
