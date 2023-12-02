import React, { useState, useEffect } from "react";

function App() {
  const [text, setText] = useState([]);

  useEffect(() => {
    fetch(' http://localhost:8000/').then(res => res.json()).then(data => {
        setText(data.message);
      });
    }, []);


  return (
    <div className="font-bold text-6xl justify-center p-6">
      Hello World :) Status django {text}
    </div>
  );
}

export default App;
