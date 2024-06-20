import React, { useState, useEffect } from 'react';

function AppointmentPage() {
  const [appointments, setAppointments] = useState([]);

  useEffect(() => {
    // Fetch appointments from API
  }, []);

  return (
    <div>
      <h1>Appointments</h1>
      <ul>
        {appointments.map((appointment) => (
          <li key={appointment.id}>
            {appointment.date}: {appointment.description}
          </li>
        ))}
      </ul>
    </div>
  );
}

export default AppointmentPage;
