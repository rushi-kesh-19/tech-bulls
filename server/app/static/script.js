import axios from "axios";


document.getElementById("loginForm").addEventListener("submit", async function (event) {
    event.preventDefault(); // Prevent default form submission

    // Get form values
    const username = document.getElementById("username").value;
    const password = document.getElementById("password").value;

    try {
        // Call the Flask API using Axios
        const response = await axios.post("/login", {
            username: username,
            password: password,
        });

        // Handle success
        if (response.status === 200) {
            alert("Login successful!");
            console.log(response.data);
            // Redirect to the home page or dashboard
            window.location.href = "/";
        }
    } catch (error) {
        // Handle error
        if (error.response) {
            // Server responded with a status other than 2xx
            alert("Login failed: " + error.response.data.message);
        } else {
            // Other errors (e.g., network error)
            console.error("Error during login:", error);
            alert("An error occurred. Please try again.");
        }
    }
});
