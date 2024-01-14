import React from "react";

const WelcomePrompt = ({ userName}) => {
    return (
        <div className="welcome-prompt">
            <h1>Welcome {userName}</h1>
        </div>
    )
}

export default WelcomePrompt;