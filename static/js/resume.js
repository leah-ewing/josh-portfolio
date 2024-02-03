'use strict';

// "Resume" page scripts:

const resumeDisplayWindow = document.getElementById("resume-display-window")

const resumeWorkExperienceLink = document.getElementById("resume-work-experience-profile-link")
const resumeEducationLink = document.getElementById("resume-education-profile-link")
const resumeSkillsLink = document.getElementById("resume-skills-profile-link")

const resumeWorkExperience = document.getElementById("resume-work-experience-profile")
const resumeEducation = document.getElementById("resume-education-profile")
const resumeSkills = document.getElementById("resume-skills-profile")

resumeWorkExperienceLink.addEventListener("click", function(evt) {
    evt.preventDefault()
    resumeDisplayWindow.innerHTML = resumeWorkExperience.innerHTML
})

resumeEducationLink.addEventListener("click", function(evt) {
    evt.preventDefault()
    resumeDisplayWindow.innerHTML = resumeEducation.innerHTML
})

resumeSkillsLink.addEventListener("click", function(evt) {
    evt.preventDefault()
    resumeDisplayWindow.innerHTML = resumeSkills.innerHTML
})