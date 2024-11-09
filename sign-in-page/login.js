
    // Wait for the DOM to load
    document.addEventListener('DOMContentLoaded', function () {
        // Select the form element
        const form = document.querySelector('form');

        // Add event listener to handle form submission
        form.addEventListener('submit', function (event) {
            event.preventDefault();  // Prevent the default form submission

            // Get the age value
            const age = document.getElementById('age').value;

            // Get the selected symptoms
            const symptoms = Array.from(document.querySelectorAll('input[name="symptom"]:checked'))
                .map(checkbox => checkbox.value);

            // Create the data object to send in the POST request
            const formData = {
                age: age,
                symptoms: symptoms
            };

            // Send the data to the backend using Fetch API
            fetch('/submit_form', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify(formData)
            })
            .then(response => response.json())
            .then(data => {
                // Handle the response from the backend
                if (data.error) {
                    alert('Error: ' + data.error);
                } else {
                    alert('Success: ' + data.message);
                }
            })
            .catch(error => {
                console.error('Error:', error);
                alert('There was an error with the form submission.');
            });
        });
    });

