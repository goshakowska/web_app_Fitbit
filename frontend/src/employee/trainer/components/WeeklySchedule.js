import React from 'react';
import { Link } from 'react-router-dom';
import './WeeklySchedule.css';

const WeeklySchedule = ({ schedule }) => {
    return (
        <table className="schedule-table">
            <thead>
                <tr>
                    <th></th>
                    {schedule[0].days.map((day, index) => (
                        <th key={index}>{day}</th>
                    ))}
                </tr>
            </thead>
            <tbody>
                {schedule.map((hour, index) => (
                    <tr key={index}>
                        <td>{hour.hour}</td>
                        {hour.slots.map((slot, index) => (
                            <td key={index}>
                                {slot.type === 'empty' && (
                                    <span className="empty-slot">
                                        {slot.available ? 'Available' : ''}
                                    </span>
                                )}
                                {slot.type === 'lesson' && (
                                    <Link to={`/lesson/${slot.lessonId}`}>
                                        {slot.lessonType === 'group' ? 'Group Lesson' : 'Private Session'} - {slot.lessonName}
                                    </Link>
                                )}
                            </td>
                        ))}
                    </tr>
                ))}
            </tbody>
        </table>
    );
};

export default WeeklySchedule;