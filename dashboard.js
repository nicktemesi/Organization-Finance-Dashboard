

// Check if the user is logged in
if (sessionStorage.getItem('loggedIn') !== 'true') {
    // If not logged in, redirect to the login page
    window.location.href = 'login.html';
  }
  
  // Logout functionality
  document.getElementById('logout').addEventListener('click', function() {
    // Remove the login status from sessionStorage
    sessionStorage.removeItem('loggedIn');
  
    // Redirect to the login page after logout
    window.location.href = 'login.html';
  });