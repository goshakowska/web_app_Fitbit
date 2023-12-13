import { React, useState } from 'react'
import data from "./ClientList.json"

function ClientList(props) {
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
    // return (
    //     <ul>
    //         {filteredData.map((client) => (
    //             <li key={client.id}>{client.id}, {client.name}, {client.surname}, {client.pass},</li>
    //         ))}
    //     </ul>
    // )

    return (
        <table>
            <thead>
                <tr>
                    <th>Id</th>
                    <th>Name</th>
                    <th>Surname</th>
                    <th>Pass</th>
                </tr>
            </thead>
            <tbody>
                {filteredData.map((client) => (
                    <tr key={client.id}>
                        <td>{client.id}</td>
                        <td>{client.name}</td>
                        <td>{client.surname}</td>
                        <td>{client.pass}</td>
                    </tr>
                ))}
            </tbody>
        </table>
    )
}

export default ClientList