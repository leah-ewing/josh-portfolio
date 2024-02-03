'use strict';

// "Nature" page scripts:

const natureDisplayWindow = document.getElementById("nature-display-window")

const natureWorkExperienceLink = document.getElementById("nature-work-experience-profile-link")
const throughHikingExperienceLink = document.getElementById("through-hiking-experience-profile-link")
const natureCertificationsLink = document.getElementById("nature-certifications-profile-link")
const natureGalleryLink = document.getElementById("nature-gallery-profile-link")

const natureWorkExperience = document.getElementById("nature-work-experience-profile")
const throughHikingExperience = document.getElementById("through-hiking-experience-profile")
const natureCertifications = document.getElementById("nature-certifications-profile")
const natureGallery = document.getElementById("nature-gallery-profile")

natureWorkExperienceLink.addEventListener("click", function(evt) {
    evt.preventDefault()
    natureDisplayWindow.innerHTML = natureWorkExperience.innerHTML
})

throughHikingExperienceLink.addEventListener("click", function(evt) {
    evt.preventDefault()
    natureDisplayWindow.innerHTML = throughHikingExperience.innerHTML
})

natureCertificationsLink.addEventListener("click", function(evt) {
    evt.preventDefault()
    natureDisplayWindow.innerHTML = natureCertifications.innerHTML
})

natureGalleryLink.addEventListener("click", function(evt) {
    evt.preventDefault()
    natureDisplayWindow.innerHTML = natureGallery.innerHTML
})