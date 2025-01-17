/*!
* Start Bootstrap - Shop Homepage v5.0.6 (https://startbootstrap.com/template/shop-homepage)
* Copyright 2013-2023 Start Bootstrap
* Licensed under MIT (https://github.com/StartBootstrap/startbootstrap-shop-homepage/blob/master/LICENSE)
*/
// This file is intentionally blank
// Use this file to add JavaScript to your project

const theme = document.getElementById('theme');
const changeTheme = document.getElementById('mode');
changeTheme.onchange = (e) => {
  if (changeTheme.checked === true) {
    console.log("Checked")
    theme.innerHTML="Light Theme"
    document.documentElement.classList.remove("dark")
    document.documentElement.classList.add("light")
    window.localStorage.setItem('mode', 'light');
  } else {
    console.log("Not Checked")
    theme.innerHTML="Dark Theme"
    document.documentElement.classList.remove("light")
    document.documentElement.classList.add("dark")
    window.localStorage.setItem('mode', 'dark');
  }
}
const mode = window.localStorage.getItem('mode');
if (mode == 'dark') {
  changeTheme.checked = true;
  document.documentElement.classList.remove("light")
  document.documentElement.classList.add("dark")
}

if (mode == 'light') {
  changeTheme.checked = false;
  document.documentElement.classList.remove("dark")
  document.documentElement.classList.add("light")
}