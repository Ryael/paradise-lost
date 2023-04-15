# Paradise Lost

A website for managing armies for tabletop board gaming.

[Paradise Lost - Live Website](https://paradise-lost-app.herokuapp.com/)

![Stars - Badge](https://badgen.net/github/stars/Ryael/paradise-lost) ![Watchers - Badge](https://badgen.net/github/watchers/Ryael/paradise-lost) ![Issues - Badge](https://badgen.net/github/issues/Ryael/avarice)

Paradise Lost is a community-based platform to allow users to build and edit their armies, find people nearby to play with should they want to opt into displaying their location, and make friends!

This is my fouth milestone project as part of Code Institute's Diploma in <strong>Software Development (E-commerce Applications)</strong>.

This project was suggested to me by my very close friend and fellow full stack developer, Simon W. He initially pitched this idea with me working on the front-end and him creating the back-end using Crystal, which is a programming language with Ruby-like syntax and C-like speed. I agreed to this but wanted to use this idea for my profolio project 4 due to it being something I'm interested in and it fitting the assessment criteria in terms of scope. As such, the backend will be using Python and the Django web framework, whereas the front-end consists of the usual trifecta of HTML, CSS, and JavaScript.

Inspired by [Battle Scribe](https://www.battlescribe.net/), which utilises an application approach and is available on Windows, Apple Story, and Google Play. Unfortunately, many tabletop players have grown frustrated with there being close to no development in past few years and this has become a bit of an open niche and this will be my humble attempt to create a website that fills this niche and provides a hopefully useful service to any aspiring commanders.

For the intents and purpose of this project, Simon W. will be referred to as the client as he was the one that pitched the idea and it will be my goal to facilitate and actualise his vision.

## Table of Contents

1. [Paradise Lost]
2. [Planning Phase]
    - [Strategy]
      - [Site Aims]
      - [Oppurtunities] - Feature & Viability Map
    - [Scope]
3. [User Experience]
    - [Target Audience](#target-audience)
    - [User Stories]
    - [Dropped User Stories]
4. [User Interface]
    - [Wireframe & Database]
    - [Design]
      - [Theme/Images]
      - [Color Scheme]
      - [Typography]
        - Font 1
        - Font 2
5. [Agile Development Process] - Trello Kanban Board & Link. Links to agile.md (Covers sprints and Epics, User Stories, and etc) A sprint will be a day.
6. [Features]
    - Landing Page
    - Logo
    - Favicon
    - Army
      - Create
      - Edit
      - Delete
      - Use Preset/Predefined
    - Sign in/Sign Out
    - Modals
    - Navbar
    - Hero Images
    - Instructions
    - Main Page Content
    - Error Pages
    - Footer
    - Dashboard
7.  [Code](#code)
    - [Commits](#commits)
    - [Folder Structure](#folder-structure)
    - [Constants](#constants)
    - [Helper Functions](#helper-functions)
    - [Game Loop](#game-loop)
    - [Classes](#classes)
    - [Map Design](#map-design)
    - [YAML](#yaml)
    - [Data Model](#data-model)
8. [Testing] (Link to Testing.MD)
    - Validation
      - [Python Validation](#python-validation)
      - [JS, HTML, CSS Validation]
    - Testing (Manual and User Stories)
    - Bugs
9. [Future Updates](#future-updates)
10. [Deployment](#deployment) (link to Deployment.md)
11. [Technologies Used](#technologies-used)
    - [Languages](#languages)
    - [Python Libraries](#python-libraries)
    - [Frameworks & Tools](#frameworks--tools)
12. [Credits](#credits)
13. [Acknowledgements](#acknowledgements)

## Planning Phase

### Strategy

#### Site Aims

Building an army for a tabletop war game is no small feat. Hobbyists have to buy unit models of a specific faction, assemble, paint, and organise them. If they then want to play against another person, they then have to transport them while making sure they don't get damaged.

Admist all that, very game has its own ruleset. Oftentimes, most games have multiple. Put simply, there's more than one way to enjoy any particular game and this has led to the creation of various rulesets that cater to different demographics of players.

Keeping track of rulesets is tricky because one each tends to be in-depth and is usually accompanied by some thick rulebooks. As such, it can be difficult to remember which unit belongs to which army for which ruleset, and so on. Many players have taken to note-taking in journals and the like, but that is one more thing to remember to bring whenever they need to travel for games.

This application aims to streamline the process of players having to bring their physical notes everywhere. Instead, they can quickly and readily access their army rosters from the comfort of their mobile phones or computers.

Here they can create their army rosters, view them at their leisure, modify them as required, and even delete them should become unnecessary. Wherever you go, your army information is always with you.

#### Opportunities

The following was an extensive list of features that were brainstormed between Simon W. and I during the conceptualistion of the website. A feasibility chart was deemed important so as to prioritise the scope of the intended strategy.

| Opportunity             | Importance  | Feasibility   |
|------------------------ |------------ |-------------  |
| User Account Management      | 5           | 5             |
| Friend System           | 1           | 2             |
| Landing Page            | 5           | 5             |
| User Login, Logout, Register              | 5           | 5             |
| About Page              | 5           | 5             |
| User Profile            | 1           | 1             |
| Army Roster Management  | 5           | 4             |
| Roster Sharing          | 1           | 3             |
| Killteam 2018 Ruleset   | 5           | 3             |
| Error Pages             | 5           | 5             |
| **Total**               | **38**      | **33**        |

Feasibility is based on time and my current level of ability using languages.

### Scope

As there is an imbalance of 5 points in the above score, 38 vs 35), there will have to be trade-offs made due to the tight schedule of this project.

The above table has been further categorised in order to establish a clear vision of the MVP required while satisifying the above requirements.

- UX **Must's**:
  - User can login, logout, and register.
  - User can create an army roster.
  - User can edit an army roster.
  - User can view their army rosters.
  - User can delete their army rosters.

- UX **Should's**:
  - User can use the forgot your password functionality.
  - User can otherwise reset their password.
  - Landing page.
  - About page.
  - Killteam Ruleset.
  - Error pages.

- UX **Should Not's**:
  - User profile.
  - Friend system.
  - Roster sharing.
  - User can change their e-mail.

## User Experience

### Target Audience

  - People who are looking to keep track of their rosters for table-top war gaming.
  - People who are looking to replace their physical rosters notes with digital storage.
  - Fans of tabletop games.
  - Fans of sci-fi concepts.

### User Stories

#### Unregistered Users

  1. As an unregistered user, I want to quickly understand the purpose of this website so that I can see if I want to continue spending my time on this website and register.

  2. As an unregistered user, I want to easily navigate the menu without getting lost so that I know this website is worth my time and won't lead to any frustrations.

  3. As an unregistered user, I want to quickly and easily learn more about the website and its purpose if I am unable to infer its purpose from the visuals and text alone, so that I can decide if registering for this website would be beneficial to me.

  4. As an unregistered user, I want to be able to register for an account so that I can start building my army rosters.

#### Registered Users

  5. As a registered user, I want to be able to change my password should I forget so that I have ease of mind in knowing that I won't be locked out of my account.

  6. As a registered user, I want to be able to manage my account by changing my password so that I can avoid any security breaches or implement a stronger password.

  7. As a registered user, I want to be made aware of my of account management actions so that I know they have been successful.

  8. As a registered user, I want to be able to access a user dashboard so that I have a base of operations for this website that's readily available.

  9. As a registered user, I want to be able to create my roster so that I can view it later.

  10. As a registered user, I want to be able to view my roster so that I can decide if it needs to have any changes made to it.

  11. As a registered user, I want to be able to update my roster so that I can make sure it's always up to date.

  12. As a registered user, I want to be able to delete my roster so that any old or unnecessary rosters don't use any unnecessary space.

#### Admins

  13. As an admin, I want to be able to log into an admin interace so that I can view, add, update, or delete information pertaining to the army rosters.

  14. As an admin, I want to be able to access the users for the website so that I can make any adjustments to their accounts such as changing their password or email, should they request it.

  15. As an admin, I want to be able to view a list of the user so that I know how many active users there are.

#### Site User

  16. As a site user, I want to be engaged by the user interface so that I know I will enjoy spending time building my rosters as I navigate the same menus repeatedly.

  17. As a site user, I want to be shown responses from the websites upon i
