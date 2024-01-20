const chartImageWithProvidedData = async (url, manager_id) => {
    try {
        const response = await fetch(url, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },body: JSON.stringify({ manager_id: manager_id})});

        if (!response.ok) {
        throw new Error(`HTTP error! Status: ${response.status}`);
        }

        const data = await response.json();
        return data.plot
    } catch (error) {
        alert('Wykryto błąd');
        console.log(error);
    }
}
export default chartImageWithProvidedData