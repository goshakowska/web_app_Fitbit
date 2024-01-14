import { React } from 'react'
import data from "./ClientList.json"
import { styled } from '@mui/material/styles';
import TableCell, { tableCellClasses } from '@mui/material/TableCell';
import ArrowForwardIcon from '@mui/icons-material/ArrowForward';
import Table from '@mui/material/Table';
import TableBody from '@mui/material/TableBody';
import TableContainer from '@mui/material/TableContainer';
import TableHead from '@mui/material/TableHead';
import TableRow from '@mui/material/TableRow';
import Paper from '@mui/material/Paper';
// import { Link } from 'react-router-dom';
import { createTheme, ThemeProvider } from '@mui/material/styles';
import { Link } from 'react-router-dom';
// import {useHistory} from 'react-router-dom';


function ClientList(props) {

    // const renderLink = (id) => {
    //     return (
    //         <Link to={`/client-info-sum-up/${id}`}>
    //             <ArrowForwardIcon/>
    //         </Link>
    //     )
    // }
    // const navigation = useNavigate();
    // function handleClick() {
    //     navigation.navigate('/portier/clientinfo', {props: props.id});
    // }
    let theme = createTheme({
        // Theme customization goes here as usual, including tonalOffset and/or
        // contrastThreshold as the augmentColor() function relies on these
      });

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

    //create a new array by filtering the original array
    const filteredData = data.filter((el) => {
        //if no input the return the original
        if (props.input === '') {
            return el;
        }
        if (!isNaN(props.input)) {
            return String(el.id).includes(props.input)
        }
        //return the item which contains the user input
        else {
            return el.surname.toLowerCase().includes(props.input.toLowerCase())
        }
    })


    return (
        <ThemeProvider theme={theme}>
        <TableContainer component={Paper}>
            <Table sx={{ minWidth: 500 }} aria-label="customized table">
                <TableHead>
                    <StyledTableRow className='title-row'>
                    <StyledTableCell>Id</StyledTableCell>
                    <StyledTableCell align="right">Surname</StyledTableCell>
                    <StyledTableCell align="right">Name</StyledTableCell>
                    <StyledTableCell align="right">Fitness Card</StyledTableCell>
                    <StyledTableCell align="right">See more info</StyledTableCell>
                    </StyledTableRow>
                </TableHead>
                <TableBody>
                    {filteredData.map((client) => (
                        <TableRow key={client.id}>
                            <StyledTableCell>{client.id}</StyledTableCell>
                            <StyledTableCell align="right">{client.surname}</StyledTableCell>
                            <StyledTableCell align="right">{client.name}</StyledTableCell>
                            <StyledTableCell align="right">{client.cardStatus ? 'Aktywny' : 'Nieaktywny'}</StyledTableCell>
                            <StyledTableCell align="right"><Link className="link-button" to='/portier/clientinfo' state={{client}}>
                                <ArrowForwardIcon/></Link></StyledTableCell>
                        </TableRow>
                    ))}
                </TableBody>
            </Table>
    </TableContainer>
    </ThemeProvider>
    )
}

export default ClientList