'use strict';

// "Music" page scripts:

const musicDisplayWindow = document.getElementById("music-display-window")

const musicEducationLink = document.getElementById("music-education-profile-link")
const musicWorkExperienceLink = document.getElementById("music-work-experience-profile-link")
const musicProductionExperienceLink = document.getElementById("music-production-experience-profile-link")
const songwritingHighlightsLink = document.getElementById("songwriting-highlights-profile-link")
const musicGigHighlightsLink = document.getElementById("music-gig-highlights-profile-link")
const musicOtherExperienceLink = document.getElementById("music-other-experience-profile-link")

const musicEducation = document.getElementById("music-education-profile")
const musicWorkExperience = document.getElementById("music-work-experience-profile")
const musicProductionExperience = document.getElementById("music-production-experience-profile")
const songwritingHighlights = document.getElementById("songwriting-highlights-profile")
const musicGigHighlights = document.getElementById("music-gig-highlights-profile")
const musicOtherExperience = document.getElementById("music-other-experience-profile")

musicEducationLink.addEventListener("click", function(evt) {
    evt.preventDefault()
    musicDisplayWindow.innerHTML = musicEducation.innerHTML
})

musicWorkExperienceLink.addEventListener("click", function(evt) {
    evt.preventDefault()
    musicDisplayWindow.innerHTML = musicWorkExperience.innerHTML
})

musicProductionExperienceLink.addEventListener("click", function(evt) {
    evt.preventDefault()
    musicDisplayWindow.innerHTML = musicProductionExperience.innerHTML
})

songwritingHighlightsLink.addEventListener("click", function(evt) {
    evt.preventDefault()
    musicDisplayWindow.innerHTML = songwritingHighlights.innerHTML
})

musicGigHighlightsLink.addEventListener("click", function(evt) {
    evt.preventDefault()
    musicDisplayWindow.innerHTML = musicGigHighlights.innerHTML
})

musicOtherExperienceLink.addEventListener("click", function(evt) {
    evt.preventDefault()
    musicDisplayWindow.innerHTML = musicOtherExperience.innerHTML
})