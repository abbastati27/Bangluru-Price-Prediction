async function predictPrice() {
    const location = document.getElementById('location').value;
    const size = document.getElementById('size').value;
    const bath = document.getElementById('bath').value;
    const bhk = document.getElementById('bhk').value;
  
    const response = await fetch('http://localhost:5000/predict', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({ location, size, bath, bhk })
    });
  
    const data = await response.json();
    document.getElementById('result').innerText = `Predicted Price: ${data.prediction}`;
  }
  // Fetch the columns.json file
fetch('columns.json')  // Ensure the path is correct
.then(response => response.json())  // Parse the JSON response
.then(data => {
  const locationSelect = document.getElementById('location');
  
  // Check if 'data_columns' exists in the data
  if (data.data_columns && Array.isArray(data.data_columns)) {
    // Exclude the first 3 columns (total_sqft, bath, bhk)
    const locations = data.data_columns.slice(3);  // This excludes the first 3 columns
    
    locations.forEach(location => {
      // Create a new option element for each location
      const option = document.createElement('option');
      option.value = location;  // The location name itself as value
      option.text = location;   // The display name for the location
      locationSelect.appendChild(option); // Add the option to the dropdown
    });
  } else {
    console.error('No locations found in columns.json');
  }
})
.catch(error => console.error('Error fetching locations:', error));

