import React, { useState } from 'react';
import '../styles/RegisterTrainingPopup.css';
function RegisterTrainingPopup() {
    const [isVisible, setIsVisible] = useState(false);
    const [isVisibleAdditional, setIsVisibleAdditional] = useState(false);
    const [isVisibleLastAdditional, setisVisibleLastAdditional] = useState(false);
    const closePopup = () => setIsVisible(false);

    return (
        <div onClick={closePopup}>
            <button className='client-info' onClick={(e) => {e.stopPropagation(); setIsVisible(!isVisible);}}>Zarejestruj trening</button>
            {isVisible && (
                <div>
                    <h5 className="info">Trening rozpoczęty</h5>
                <button className='client-info' onClick={(f) => {f.stopPropagation(); setIsVisibleAdditional(!isVisibleAdditional);}}>Przydziel szafkę</button>
                <button className='client-info' onClick={closePopup}>Nie przydzielaj</button>
                {isVisibleAdditional && (
                    <div>
                        <h5 className="info">Przydzielono szafkę nr. 1.</h5>
                        <button className='client-info' onClick={closePopup}>Zamknij</button>
                    </div>
                )}

                </div>
            )}
        </div>
    );
}

export default RegisterTrainingPopup;