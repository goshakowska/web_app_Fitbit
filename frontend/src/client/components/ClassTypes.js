import React from "react";
import { useNavigate } from "react-router-dom";

function ClassTypes () {
    // shows decision site for client - if he wants to buy group or individual classes
    let navigate = useNavigate();

    const handleGroupClasses = () => {
        // redirect to group classes shop
        navigate('/grupowe_sklep', {
        });
      };

    const handleIndividualClasses = () => {
        // redirect to individual classes shop
        navigate('/indywidualne_sklep', {
        });
      };

    return (
        <div>
        <div className="layout2 smallHeader">
            <div>Jakie zajęcia zamierzasz wykupić?</div>
            <button className="buttonDecisionSite text-style" onClick={handleGroupClasses}>
                Zajęcia grupowe
            </button>
            <button className="buttonDecisionSite text-style" onClick={handleIndividualClasses}>
                Zajęcia indywidualne
            </button>
        </div></div>
    )

}
export default ClassTypes