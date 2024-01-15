// import { React, useState, useEffect } from 'react'
// // import clients from "./ClientList.json"
// import { styled } from '@mui/material/styles';
// import TableCell, { tableCellClasses } from '@mui/material/TableCell';
// import ArrowForwardIcon from '@mui/icons-material/ArrowForward';
// import Table from '@mui/material/Table';
// import TableBody from '@mui/material/TableBody';
// import TableContainer from '@mui/material/TableContainer';
// import TableHead from '@mui/material/TableHead';
// import TableRow from '@mui/material/TableRow';
// import Paper from '@mui/material/Paper';
// // import { Link } from 'react-router-dom';
// import { createTheme, ThemeProvider } from '@mui/material/styles';
// import { Link } from 'react-router-dom';
// // import {useHistory} from 'react-router-dom';


// function ClientList(props) {

//   const [clients, setClients] = useState([]);

//   const getClients = async (event) =>
//   {
//     try {
//         const response = await fetch('http://localhost:8000/portier/list_clients/', {
//           method: 'POST',
//           headers: {
//             'Content-Type': 'application/json',
//           },body: JSON.stringify()});

//         if (!response.ok) {
//           throw new Error(`HTTP error! Status: ${response.status}`);
//         }

//         const data = await response.json();
//         console.log(data.clients);

//         setClients(data.clients);

//       } catch (error) {
//         console.error('Error:', error);
//       };
// }

// useEffect(() => {getClients()}, []);


//     let theme = createTheme({

//       });

//       theme = createTheme(theme, {
//         // Custom colors created with augmentColor go here
//         palette: {
//           babyblue: theme.palette.augmentColor({
//             color: {
//               main: '#B5E2FA',
//             },
//             name: 'baby-blue',
//           }),
//           ivory: theme.palette.augmentColor({
//             color: {
//               main: '#F9F7F3',
//             },
//             name: 'ivory',
//           }),
//           tangerine: theme.palette.augmentColor({
//             color: {
//               main: '#F7A072',
//             },
//             name: 'tangerine',
//           }),
//           monotonousgrey: theme.palette.augmentColor({
//             color: {
//               main: '#D9D9D9',
//             },
//             name: '#monotonous-grey',
//           }),
//           vanilla: theme.palette.augmentColor({
//             color: {
//               main: '#EDDEA4',
//             },
//             name: 'vanilla',
//           }),
//           bottlegreen: theme.palette.augmentColor({
//             color: {
//               main: '#155E63',
//             },
//             name: 'bottle-green',
//           }),
//           darkgreen: theme.palette.augmentColor({
//             color: {
//               main: '#002F35',
//             },
//             name: 'dark-green',
//           }),

//         },
//       });

//     const StyledTableCell = styled(TableCell)(({ theme }) => ({
//         [`&.${tableCellClasses.head}`]: {
//           backgroundColor: theme.palette.tangerine.main,
//           color: theme.palette.darkgreen.main,
//           fontSize: 24,
//           fontFamily: 'Inknut Antiqua',
//         },
//         [`&.${tableCellClasses.body}`]: {
//           fontSize: 16,
//           fontFamily: 'Inknut Antiqua',
//         },
//       }));

//       const StyledTableRow = styled(TableRow)(({ theme }) => ({
//         '&:nth-of-type(odd)': {
//           backgroundColor: theme.palette.vanilla.main,
//         },
//         // hide last border
//         '&:last-child td, &:last-child th': {
//           border: 5,
//         },
//       }));

//     const filteredData = clients.filter((el) => {
//       // If no input, return the original
//       if (props.input === '') {
//           return el;
//       }

//       // Check if input is a number (for id or phone_number)
//       if (!isNaN(props.input)) {
//           return String(el.id).includes(props.input) ||
//                  String(el.phone_number).includes(props.input);
//       }

//       // Return the item which contains the user input in surname or name
//       return el.surname.toLowerCase().includes(props.input.toLowerCase()) ||
//              el.name.toLowerCase().includes(props.input.toLowerCase());
//   });

//     return (
//         <ThemeProvider theme={theme}>
//         <TableContainer component={Paper}>
//             <Table sx={{ minWidth: 500 }} aria-label="customized table">
//                 <TableHead>
//                     <StyledTableRow className='title-row'>
//                     <StyledTableCell>Id</StyledTableCell>
//                     <StyledTableCell align="right">Numer telefonu</StyledTableCell>
//                     <StyledTableCell align="right">Nazwisko</StyledTableCell>
//                     <StyledTableCell align="right">Imię</StyledTableCell>
//                     <StyledTableCell align="right">Status karty</StyledTableCell>
//                     <StyledTableCell align="right">Zobacz więcej informacji</StyledTableCell>
//                     </StyledTableRow>
//                 </TableHead>
//                 <TableBody>
//                     {filteredData.map((client) => (
//                         <TableRow key={client.id}>
//                             <StyledTableCell>{client.id}</StyledTableCell>
//                             <StyledTableCell align="right">{client.phone_number}</StyledTableCell>
//                             <StyledTableCell align="right">{client.surname}</StyledTableCell>
//                             <StyledTableCell align="right">{client.name}</StyledTableCell>
//                             <StyledTableCell align="right">{client.status ? 'Aktywny' : 'Nieaktywny'}</StyledTableCell>
//                             <StyledTableCell align="right"><Link className="link-button" to='/portier/clientinfo' state={{client}}>
//                                 <ArrowForwardIcon/></Link></StyledTableCell>
//                         </TableRow>
//                     ))}
//                 </TableBody>
//             </Table>
//     </TableContainer>
//     </ThemeProvider>
//     )
// }

// export default ClientList


import React, { useState, useEffect } from 'react';
import { styled } from '@mui/material/styles';
import TableCell, { tableCellClasses } from '@mui/material/TableCell';
import ArrowForwardIcon from '@mui/icons-material/ArrowForward';
import Table from '@mui/material/Table';
import TableBody from '@mui/material/TableBody';
import TableContainer from '@mui/material/TableContainer';
import TableHead from '@mui/material/TableHead';
import TableRow from '@mui/material/TableRow';
import Paper from '@mui/material/Paper';
import Pagination from '@mui/material/Pagination';
import TablePagination from '@mui/material/TablePagination';
import { createTheme, ThemeProvider } from '@mui/material/styles';
import { Link } from 'react-router-dom';

function ClientList(props) {
  const [clients, setClients] = useState([]);
  const [currentPage, setCurrentPage] = useState(0);
  const rowsPerPage = 10; // Number of rows to display per page

  const getClients = async () => {
    try {
      const response = await fetch('http://localhost:8000/portier/list_clients/', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(),
      });

      if (!response.ok) {
        throw new Error(`HTTP error! Status: ${response.status}`);
      }

      const data = await response.json();
      console.log(data.clients);
      setClients(data.clients);
    } catch (error) {
      console.error('Error:', error);
    }
  };

  useEffect(() => {
    getClients();
  }, []);

  useEffect(() => {
    setCurrentPage(0);
  }, [props.input]);

  let theme = createTheme({});

      theme = createTheme(theme, {
        // Custom colors created with augmentColor go here
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

    const StyledTableCell = styled(TableCell)(({ theme }) => ({
        [`&.${tableCellClasses.head}`]: {
          backgroundColor: theme.palette.tangerine.main,
          color: theme.palette.darkgreen.main,
          fontSize: 24,
          fontFamily: 'Inknut Antiqua',
        },
        [`&.${tableCellClasses.body}`]: {
          fontSize: 16,
          fontFamily: 'Inknut Antiqua',
        },
      }));

      const StyledTableRow = styled(TableRow)(({ theme }) => ({
        '&:nth-of-type(odd)': {
          backgroundColor: theme.palette.vanilla.main,
        },
        // hide last border
        '&:last-child td, &:last-child th': {
          border: 5,
        },
      }));
      const handlePageChange = (event, newPage) => {
        setCurrentPage(newPage);
      };

      const filteredData = clients.filter((el) => {
        // If no input, return the original
        if (props.input === '') {
          return el;
        }

        // Check if input is a number (for id or phone_number)
        if (!isNaN(props.input)) {
          return String(el.id).includes(props.input) || String(el.phone_number).includes(props.input);
        }

        // Return the item which contains the user input in surname or name
        return (
          el.surname.toLowerCase().includes(props.input.toLowerCase()) ||
          el.name.toLowerCase().includes(props.input.toLowerCase())
        );
      });

      const paginatedData = filteredData.slice(currentPage * rowsPerPage, (currentPage + 1) * rowsPerPage);

      return (
        <ThemeProvider theme={theme}>
          <TableContainer component={Paper}>
            <Table sx={{ minWidth: 500 }} aria-label="customized table">
              <TableHead>
                <StyledTableRow className="title-row">
                  <StyledTableCell>Id</StyledTableCell>
                  <StyledTableCell align="right">Numer telefonu</StyledTableCell>
                  <StyledTableCell align="right">Nazwisko</StyledTableCell>
                  <StyledTableCell align="right">Imię</StyledTableCell>
                  <StyledTableCell align="right">Status karty</StyledTableCell>
                  <StyledTableCell align="right">Zobacz więcej informacji</StyledTableCell>
                </StyledTableRow>
              </TableHead>
              <TableBody>
                {paginatedData.map((client) => (
                  <TableRow key={client.id}>
                    <StyledTableCell>{client.id}</StyledTableCell>
                    <StyledTableCell align="right">{client.phone_number}</StyledTableCell>
                    <StyledTableCell align="right">{client.surname}</StyledTableCell>
                    <StyledTableCell align="right">{client.name}</StyledTableCell>
                    <StyledTableCell align="right">{client.status ? 'Aktywny' : 'Nieaktywny'}</StyledTableCell>
                    <StyledTableCell align="right">
                      <Link className="link-button" to="/portier/clientinfo" state={{ client: client.id }}>
                        <ArrowForwardIcon />
                      </Link>
                    </StyledTableCell>
                  </TableRow>
                ))}
              </TableBody>
            </Table>
            <TablePagination
              rowsPerPageOptions={[]}
              component="div"
              count={filteredData.length}
              rowsPerPage={rowsPerPage}
              page={currentPage}
              onPageChange={handlePageChange}
            />
          </TableContainer>
        </ThemeProvider>
      );
    }

    export default ClientList;