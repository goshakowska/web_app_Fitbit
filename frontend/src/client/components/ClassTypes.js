import React from "react";
import { useNavigate } from "react-router-dom";

function ClassTypes () {
    let navigate = useNavigate();

    const handleGroupClasses = () => {
        navigate('/grupowe_sklep', {
        });
      };

    const handleIndividualClasses = () => {
        navigate('/indywidualne_sklep', {
        });
      };

    return (
        <div>
        <div className="layout smallHeader">
            <div>Jakie zajęcia zamierzasz wykupić?</div>
            <button className="button-style-header text-style" onClick={handleGroupClasses}>
                Zajęcia grupowe
            </button>
            <button className="button-style-header text-style" onClick={handleIndividualClasses}>
                Zajęcia indywidualne
            </button>
        </div></div>
    )

}
export default ClassTypes