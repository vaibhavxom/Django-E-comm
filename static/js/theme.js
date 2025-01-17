// script.js

// Get the toggle button and theme label
const changeTheme = document.getElementById('mode');
const themeLabel = document.getElementById('theme');

// Check localStorage for saved mode
const mode = window.localStorage.getItem('mode');
if (mode === 'dark') {
    document.body.classList.add('dark');
    themeLabel.innerHTML = "Light Theme"; // Update label
    changeTheme.checked = true; // Set toggle to checked
} else {
    document.body.classList.remove('dark');
    themeLabel.innerHTML = "Dark Theme"; // Update label
    changeTheme.checked = false; // Set toggle to unchecked
}

// Add event listener for the toggle button
changeTheme.addEventListener('change', () => {
    if (changeTheme.checked) {
        document.body.classList.add('dark');
        themeLabel.innerHTML = "Light Theme"; // Update label
        window.localStorage.setItem('mode', 'dark'); // Save mode to localStorage
    } else {
        document.body.classList.remove('dark');
        themeLabel.innerHTML = "Dark Theme"; // Update label
        window.localStorage.setItem('mode', 'light'); // Save mode to localStorage
    }
});