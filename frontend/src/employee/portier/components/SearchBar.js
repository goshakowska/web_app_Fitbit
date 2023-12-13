import { React, useState } from 'react';
import TextField from '@mui/material/TextField/TextField';
import ClientList from "./ClientList";
// import "./App.css";

function SearchBar() {
  const [inputText, setInputText] = useState("");
  let inputHandler = (e) => {
    //convert input text to lower case
    console.log("Value of yourVariable:", e.target.value);
    // var lowerCase = e.target.value.toLowerCase();
    // setInputText(lowerCase);
    setInputText(e.target.value);
  };

  return (
    <div className="main">
      <h1>Wyszukiwarka klientów</h1>
      <div className="search">
        <TextField
          id="outlined-basic"
          onChange={inputHandler}
          variant="outlined"
          fullWidth
          label="Search"
        />
      </div>
      <ClientList input={inputText} />
    </div>
  );
}

export default SearchBar;