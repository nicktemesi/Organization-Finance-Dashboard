

// this  validates user credentials
const validUsername = 'nick';
const validPassword = 'password123';

document.getElementById('login-form').addEventListener('submit', function(e) {
  e.preventDefault();  // Prevent the form from submitting

  const username = document.getElementById('username').value;
  const password = document.getElementById('password').value;

  // Check if the credentials match
  if (username === validUsername && password === validPassword) {
    // Store the login status in sessionStorage
    sessionStorage.setItem('loggedIn', 'true');

    // Redirect to the dashboard page after successful login
    window.location.href = 'dashboard.html';
  } else {
    // Display error message if credentials are incorrect
    document.getElementById('error-message').textContent = 'Invalid username or password.';
  }
});