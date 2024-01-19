import { React, useState } from 'react';
import TextField from '@mui/material/TextField/TextField';
import ClientList from "./ClientList";
import "../styles/SearchBar.css";
import { createTheme, ThemeProvider } from '@mui/material/styles';
import AccountCircle from '@mui/icons-material/AccountCircle';
import InputAdornment from '@mui/material/InputAdornment';
import { InputLabelProps } from '@mui/material';
function SearchBar() {

  let theme = createTheme({
  });

  theme = createTheme(theme, {
    palette: {
      babyblue: theme.palette.augmentColor({
        color: {
          main: '#B5E2FA',
        },
        name: 'baby-blue',
      }),
      ivory: theme.palette.augmentColor({
        color: {
          main: '#F9F7F3',
        },
        name: 'ivory',
      }),
      tangerine: theme.palette.augmentColor({
        color: {
          main: '#F7A072',
        },
        name: 'tangerine',
      }),
      monotonousgrey: theme.palette.augmentColor({
        color: {
          main: '#D9D9D9',
        },
        name: '#monotonous-grey',
      }),
      vanilla: theme.palette.augmentColor({
        color: {
          main: '#EDDEA4',
        },
        name: 'vanilla',
      }),
      bottlegreen: theme.palette.augmentColor({
        color: {
          main: '#155E63',
        },
        name: 'bottle-green',
      }),
      darkgreen: theme.palette.augmentColor({
        color: {
          main: '#002F35',
        },
        name: 'dark-green',
      }),

    },
  });
  const [inputText, setInputText] = useState("");
  let inputHandler = (e) => {
    console.log("Value of yourVariable:", e.target.value);
    setInputText(e.target.value);
  };

  return (

    <div className="main">
      <ThemeProvider theme={theme}>
      <h1 className="title">Wyszukiwarka klientów</h1>
      <div className="search">

        <TextField
          id="filled-basic"
          backgroundColor="ivory"
          onChange={inputHandler}
          variant="outlined"
          fullWidth
          label="Search client"
          InputLabelProps={{style: {fontSize: 20, fontFamily: 'Inknut Antiqua'}}}
          color="vanilla"
          focused
          InputProps={{
            startAdornment: (
              <InputAdornment position="start">
                <AccountCircle color="vanilla" />
              </InputAdornment>
            ),
          }}
        />
      </div>
      <ClientList input={inputText} />
      </ThemeProvider>
    </div>
  );
}

export default SearchBar;