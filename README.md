# Paradise Lost

A website for managing armies for tabletop board gaming.

[Paradise Lost - Live Website](https://avarice-txt.herokuapp.com/)

![Stars - Badge](https://badgen.net/github/stars/Ryael/avarice) ![Watchers - Badge](https://badgen.net/github/watchers/Ryael/avarice) ![Issues - Badge](https://badgen.net/github/issues/Ryael/avarice)

Paradise Lost is a community-based platform to allow users to build and edit their armies, find people nearby to play with should they want to opt into displaying their location, and make friends!

This is my fouth milestone project as part of Code Institute's Diploma in <strong>Software Development (E-commerce Applications)</strong>.

This project was suggested to me by my very close friend and fellow full stack developer, Simon W. He initially pitched this idea with me working on the front-end and him creating the back-end using Crystal, which is a programming language with Ruby-like syntax and C-like speed. I agreed to this but wanted to use this idea for my profolio project 4 due to it being something I'm interested in and it fitting the assessment criteria in terms of scope. As such, the back-end will be made of Python, specifically, Django, whereas the front-end consists of the usual trifecta of HTML, CSS, and JavaScript.

Inspired by Battle Scribe, which utilises an app approach and is available on both Google Play and Apple store (link to both). Unfortunately, many tabletop players have grown frustrated with there being close to no development in past few years and this has become a bit of an open niche and this will be my humble attempt to create a website that fills this niche and provides a hopefully useful service to any aspiring commanders.

For the intents and purpose of this project, Simon W. will be referred to as the client as he was the one that pitched the idea and it will be my goal to facilitate and actualise his vision.

[Self Note: Expand below into one quick paragraph but go into detail on these in a features section]

## Table of Contents

1. [Paradise Lost]
2. [Planning Phase]
    - [Strategy]
      - [Site Aims]
      - [Oppurtunities] - Feature & Viability Map
    - [Scope]
    - [Structure]
      - [Target Audience](#target-audience)
      - [User Stories]
      - [Dropped User Stories]
    - [Wireframe & Database]
    - [Design]
      - [Theme/Images]
      - [Color Scheme]
      - [Typography]
        - Font 1
        - Font 2
4. [Agile Development Process] - Trello Kanban Board & Link. Links to agile.md (Covers sprints and Epics, User Stories, and etc) A sprint will be a day.
5. [Features]
  - Landing Page
  - Logo
  - Favicon
  - Army
    - Create
    - Edit
    - Delete
    - Use Preset/Predefined
  - __Find-an-Enemy__ - Find-A-Friend (Potential alternatives: Begin Conquest, Locate Adversary?): Use a spaceship or military vehichle Font Awesome icon
  - Find commanders near you (Location based)
  - __Form Alliance__ - Add friend
  - __Open Communications__ - Direct Message
  - __Commanders?__ - Term for users? Any alternatives?
  - Sign in/Sign Out
  - Modals
  - Navbar
  - Hero Images
  - Instructions
  - Main Page Content
  - Error Pages
  - Footer
  - Members Only Page (What appears when user isn't logged in)
6.  [Code](#code)
    - [Commits](#commits)
    - [Folder Structure](#folder-structure)
    - [Constants](#constants)
    - [Helper Functions](#helper-functions)
    - [Game Loop](#game-loop)
    - [Classes](#classes)
    - [Map Design](#map-design)
    - [YAML](#yaml)
    - [Data Model](#data-model)
7. [Testing] (Link to Testing.MD)
  - Validation
    - [Python Validation](#python-validation)
    - [JS, HTML, CSS Validation]
  - Testing (Manual and User Stories)
  - Bugs
8. [Future Updates](#future-updates)
9. [Deployment](#deployment) (link to Deployment.md)
10. [Technologies Used](#technologies-used)
    - [Languages](#languages)
    - [Python Libraries](#python-libraries)
    - [Frameworks & Tools](#frameworks--tools)
11. [Credits](#credits)
12. [Acknowledgements](#acknowledgements)

