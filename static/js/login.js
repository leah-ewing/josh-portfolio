'use strict';

// Login Pop-up Scripts

const adminLoginPopupWindow = document.getElementById("login-popup-window")

const adminLoginButton = document.getElementById("admin-login-logo")
const adminLoginCloseButton = document.getElementById("close-button-login-popup-window")


adminLoginButton.addEventListener("click", function(evt) {
    evt.preventDefault()
    adminLoginPopupWindow.style.display = "block"
})

adminLoginCloseButton.addEventListener("click", function(evt) {
    evt.preventDefault()
    adminLoginPopupWindow.style.display = "none"
})