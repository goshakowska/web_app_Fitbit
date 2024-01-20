const chartImage = async (url) => {
    try {
        const response = await fetch(url, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        });

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

export default chartImage