import React from 'react';
import { FiHeart, FiActivity, FiDroplet, FiTrendingUp } from 'react-icons/fi';

const HealthCard = ({ icon: Icon, title, value, unit, trend, color }) => {
  return (
    <div className={`bg-white rounded-lg shadow p-6 border-l-4 ${color}`}>
      <div className="flex justify-between items-start">
        <div>
          <p className="text-gray-600 text-sm font-medium">{title}</p>
          <p className="text-3xl font-bold text-gray-900 mt-2">
            {value}
            <span className="text-lg text-gray-500 ml-2">{unit}</span>
          </p>
          {trend && (
            <p className={`text-sm mt-2 ${trend > 0 ? 'text-green-600' : 'text-red-600'}`}>
              <FiTrendingUp className="inline mr-1" />
              {trend > 0 ? '+' : ''}{trend}% from last week
            </p>
          )}
        </div>
        <div className={`p-3 rounded-lg ${color.replace('border', 'bg').replace('4', '100')}`}>
          <Icon size={24} className={`text-${color.split('-')[1]}-600`} />
        </div>
      </div>
    </div>
  );
};

export default HealthCard;
