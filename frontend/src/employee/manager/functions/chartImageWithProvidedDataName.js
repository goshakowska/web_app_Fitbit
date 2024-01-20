const chartImageWithProvidedDataName = async (url, manager_id, equipment_name) => {
    try {
        const response = await fetch(url, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },body: JSON.stringify({ manager_id: manager_id, equipment_name: equipment_name })});

        if (!response.ok) {
        throw new Error(`HTTP error! Status: ${response.status}`);
        }

        const data = await response.json();
        return data.plot;
    } catch (error) {
        alert('Wykryto błąd');
        console.log(error);
    }
}

export default chartImageWithProvidedDataName;