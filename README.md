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
    - [Design Philosophy]
      - [Color Scheme]
      - [Typography]
    - [Wireframes]
    - [Database]
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
    - Navbar
    - Hero Images
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

  2. As an unregistered user, I want to easily navigate the menu without getting lost by seeing the uniformity of each page so that I know this website is worth my time and won't lead to any frustrations.

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

  17. As a site user, I want to be shown responses from the website upon interaction with it so that I know the creation, deletion, or update of my roster has been successful.

  18. As a site user, I want to experience a unique and uniform design with appealing colours so that every part of the website stimulates a positive response.

  19. As a site user, I want to be able to access the website from any screen size and still have a pleasant viewing experience so that I'm not restricted to only viewing this website on bigger screens.

  20. As a site user, I want to be able to contact the admin via e-mail, find their GitHub project repository, or even find them on other socials like LinkedIn.

#### Dropped

Certain user stories were dropped as part of the agile process. They are as follows:

  - As a registered user, I want to be able make a profile so that I can share my roster via a link.
  - As a registered user, I want to be able to private my rosters so that they don't appear on my profile.
  - As a registered user, I want to view other peoples' profiles so that I can view their rosters.
  - As a regsitered user, I want to add other people as friends so that we can make rosters and play together.
  - As a registered user, I want to delete a friend because they were very unsportsmanlike after beating me in a game.
  - As a registered user, I want to find nearby active players so that we can meet-up and play games.
  - As an admin, I want to add headings to the admin database tables so I can more quickly understand my data.
  - As an admin, I want to filter the admin database tables so that I can more easily find the data I need.

## User Interface

### Design Philosophy

The design of this website began with a simple yet clear vision: to replicate the menus present in old real-time strategy games, such as the Command & Conquer series. While navigating the many menus of the game, especially when choosing a location to start a campaign on on Earth, the player is able to choose their starting location. While they're choosing, a hologram of the Earth is playing on screen. While not exactly the same, [this video (timestamped)](https://youtu.be/j77gwvA2bQU?t=35), shows a very similar sequence.

My goal was first and foremost to replicate this sort of feeling: that the user is looking over the planet, ready to make their move. As such, I began scouring the website for a video that was not too long and looped perfectly, which is when I happened on Free Stock Videos by [Videezy](https://www.videezy.com/abstract/50298-futuristic-globe-world-earth-planet-in-cyberspace-with-binary-code). There's a great collection of high quality videos that are free to use with attribution. This video in particular was exactly what I was looking for, it's a relatively short and perfect loop that features a rotating holograph of the planet.

The colour scheme was picked from this video, which serves as the landing page for the website. The rest of the UI was built around this colour scheme and inspiration. The button style used is reminicsient of a commanding officer making difficult decisions as the reticule focuses in. While of course this website does nothing so serious or grave, this is just the feeling I wanted to evoke with my designs. The menus themselves are simple, sleek, angular, with a repeated dot background combined a semi-transparent black to yellow gradient.

The design of the UI was mostly made with a mobile-first approach but for the smallest viewports, the menus expands to 80-100% of the width to allow for easier viewing.

#### Colours

The below image was generated using [coolers.co](https://coolors.co/fd9c31-cccccc-ffffff). The orange is the colour that was picked from the landing page video, silver was often used for text, and the white was used for titles and as a form of contrast between the black and greys present throughout the site.

#### Typography

Two fonts were specifically chosen for this website:

- *Orbitron*

Orbitron was chosen due to its sleek look which feels like something out of a fururistic sci-fi movie. As it's intended for display purposes, it was used for the logo and as text headings.

- Exo*

Exo was chosen to compliment Orbitron as it also conveys a similarly futuristic yet elegant feeling. While it can also be used for headings, Exo looks much better at small text sizes, which is what it's used for in this project.

### Wireframes

The conceptualisation of the layout used in this project began with simple pen and paper sketches, which were then transformed into wireframes via Balsamiq. Everything shown here is a rough beta of the layout, some of which has changed during development.

This is the prototype of the project, which changes over the course of project development.

<details>
  <summary>Home Page</summary>
  <img src="docs/wireframes/main.png" alt="Wireframe of the Home Page">
</details>
<details>
  <summary>Navigation Menu</summary>
  <img src="docs/wireframes/settings.png" alt="Wireframe of the Navigation Menu">
</details>
<details>
  <summary>General Menu</summary>
  <img src="docs/wireframes/game.png" alt="Wireframe of the General Menu">
</details>
<details>
  <summary>Roster</summary>
  <img src="docs/wireframes/game.png" alt="Wireframe of the Roster">
</details>

### Database

Above is the databse schema as the initial plan for the database tables. Originally it was planned for users to be able to configure their rosters with units, specialisms, abilities, wargear, and weapon profiles. Unfortunately, this fell completely out of scope due to the deadline and unfamiliarity with a method of serialising those models in a way that's customisable to each user.

The user model was not included due to the default user model provided by the ALLAUTH library.

## Agile Development Process

[Jira](https://www.atlassian.com/software/jira) was used to create and track User Stories and issues. Login creditentials will be provided for the above project space when the project is submitted. A summary of my agile process and learing outcomes can be found [here]().

## Features

### Logo

[logo]()

No suitable icon was found for the logo and hence the Orbitron font was used for it instead. To create a sense of contrast "Paradise" was written in white, whereas "Lost" was written in orange and has less of a font weight to it than "Paradise". This approach to text logo design achieves a sleek and unique looking logo that would have otherwise been less appealing to the eye. Interacting with the logo also brings the user to the home/landing page, as per usual.

### Landing Page

[landing-page]()

The landing page utlises a hero-video for its background, which loops perfectly every 10 seconds. Upon loading into the page, the user is greeted the video and the dynamically rotating text. The text rotates between synonyms for "army", "fleet", and other similar words every four seconds. Dynamically changing text is considered to be very [effective for user conversion](https://www.convertize.io/dynamic-text/) and helps to create a very engaging landing page. This text is accompanied by a call-to-action button with the words "Enlist Now!", urging them to sign-up. Lastly, in the top right corner, a hamburger menu can be seen which are commonly used to expand a navigation menu.

### Navigation Menu - New User

[navigation-menu-new]()

The navigation menu opens with a smooth fade-in animation and the hamburger icon is replaced with an "X", informing the user that this "X" icon is what they should interact with should they want to close the navigation menu. The user is greeted by a dark gray "carbon-fiber" background with small dots, which is small single dot image that's repeated. This allows the dot to scale to any viewport neccessary without any stretching. The links themselves start as white and as the user interacts with one, all but the active one fade to grey. The social-icons on the bottom also function the same way.

The bottom of the navigation menu feature the aforementioned social-icons which also double up as the website's footer. This approach was opted for because full-screen nagivation menus are becoming more and more popular, as they allow for a bigger focus on the actual page content. Even if a stick navigation bar approach is utilised, they still use a portion of the viewing space. The footer can also add unnecessary vertical scrolling. As this website aims to utilise the immediately available viewing space, fullscreen navigation menu was the ideal choice.

### Navigation Menu - Registered User

[navigation-menu-new]()

Similarly to the New User example, the navigation menu changes the links available to the user depending if they're authenticated or not. If not, the above example is what they'll see. If they are, however, then they'll instead be shown the Registered User example with the Login and Register links replaced with Dashboard and Logout links.

### Button

[button]()

All the buttons present on the website follow the same design: gray background with orange text and orange decorators on all the corners. Upon interaction, the corners expand and float outwards. This effect was made to be reminiscent of an aiming reticle focusing in and out to give the website's buttons a more military-esque feeling, furthering the idea that this website has a sci-fi army feel. The decorators and button text also both flicker upon loading and interaction, as a way of guiding the user towards them.

### About

[about]()

The about page is the one of the first pages the user will see should they want to learn more about the purpose of the website. The entirety of the page background is a dark gray with a similar albeit more widely spaced dot-pattern to the navigation menu, but this time the dot itself is generated with CSS, which allows it expand infinitely as required by the viewport. Links are highlighted in orange and turn to white on mouse-over/interaction, providing the user with visual feedback.

### Register

[register](register)

This is one of the first menus a new user will see, if the landing page user conversion was successful. Upon loading into this page, the user is greeted by a centered menu with a white outline and input text fields outlined in that same orange colour, creating a sense of consistent design throughout. Errors are rendered above their relevant text field and are styled in the same way was regular paragraph text, meaning that the body text is consistently gray throughout. Additionally, a link to the login fage is found at the bottom of the menu and is highlighted in orange, instantly standing out to the user who may be looking just to login. The button for the input is same as the buttons showcased earlier, and this will continue to be the case for every other button on this website.

### Login

[login](login)

Logging in is an important process for any website with featues locked behind user registration, and as such, login menu itself is simple and short. The user is also provided with a remember-me checkbox, which has had its opacity reduced ever-so-slightly so as to make it fit in with the overall colour scheme of the menu. Upon it being checked, it's highlighted in the usual orange colour. The user is also presented with two links at the bottom of the menu, one linking them back to the register page and the one below that allowing them to use the "Forgot your password" functionality which lets them reset their password via email.

### Forgot Your Password

[forgot-your-password](forgot-your-password)

In terms of design, this section doesn't differ at all from any of the above menus. It's more or less the same consistent design that's present throughout all of the website's menus. Upon entering of the email that a user registered with, they're able to request a link via email to reset their email. Once that link is used, the user is redirected to the reset password page where they are given a chance to input a new password and then confirm that same password. Upon doing so, they are brought to a new page where they informed their password being changed has been successful.

### Logout

[logout](logout)

Should the user want to logout, they are brought to one of the smallest menus across the entire website. It's centered vertically and horizontally, which admittedly does stand out. However, this is intentional as the very small menu box looks out of place when it's placed in the same location as the other menus. Upon logging out, the user is not provided with any text but instead is brought to the landing page as is usual practice. The links in the navigation menu also revert to "Register" and "Login".

### Dashboard

[dashboard](dashboard)

Upon successful registration or login, the dashboard page is the first thing the user will see. While there is no message printed to inform the user that their login has been successful, instead they will be greeted by "Welcome, commander USERNAME!". Between the redirect and the greeting on the dashboard, I believe this is sufficient in letting the user know that their login has been successful. The dashboard is available to the user wherever they go via the navigation menu alongside the "Logout" link. On the dashboard itself, the user is given three options on where to go next: "My Rosters", "Change Password", and "Logout".

### Change Your Password

[change-your-password](change-your-password)

Changing your password on the website is important because of security. Sometimes one may want a more complex password for peace of mind, sometimes one may want to update their password manager, and even sometimes one may want to update their passwords across all websites due to their password being compromised. As such, it is extremely important to provide the user with a way of changing their password. The menu itself is the exact same as before and once the current password, new password, and new password again are submitted, the page is refreshed and the user is informed via message that their password has been successfully changed.

### Roster List

[roster-list](roster-list)

Once the user interacts with the "My Rosters" button, they'll be brought to the roster index page, which shows all the available rosters. If this is the user's first time coming to this page, there will be no rosters visible and instead all they'll see is a "Create Roster" button. This button is placed under the created rosters but will be in their immediate viewing space initially. The roster menus are different from the general menus as they are much wider to accomodate the tables. This width is adjust to around 80% of the viewport on medium-small devices so as to ensure everything fits nicely and neatly.

Once a roster has been created, they're rendered via as a table via HTML and styled via CSS. For wider screens this will be a table with an orange outline as per usual, for medium-small screens this will be a wide card, and for small screens this will be a narrow card. Each of the aforementioned cards are stacked up on each other vertically with a small space in between. Each roster has three Font Awesome icons: 1) View (Eye), 2) Edit (Pen), and 3) Delete (Bin). These three icons are common practice for these actions and also fade to white on interaction, indicating that they function as links. The rosters themselves are sorted by their name.

### Create Roster

[create-roster](create-roster)

The create roster page is fundamentally very similar to the user account management menus except that it features a number field and drop-down menus for selection. Below the relevant data input is a button that lets the user create a roster with their selected data and below that is a link to go back to roster list.

### Edit Roster

[edit-roster](edit-roster)

Editing a roster is almost identical to creating one as the menu is the same same except for the page title and submit buttons being different. Simple and straightforward.

### View Roster

[view-roster](view-roster)

Viewing a roster is more or less indentical to the "My Rosters" page except it shows one select roster in the same fashion as the roster list. Ideally this is what the users would be able to share with other players but unfortunately that functionality fell out of scope. At the bottom of the menu, a "Return" button is available for the user.

### Delete Roster

[delete-roster](delete-roster)

Opting to delete a roster brings the user to a very simple and short menu where they're asked if this is the correct roster to be deleted. This roster is referenced by name and has a button labelled "Yes" under this text, with a "Cancel" link under that should the user want to return to the roster list.

### Error 404

[error-404](error-404)

If a user managed to stray off the beaten path they'll be displayed an error 404 page, which has been styled with the usual orange colour. This design uses an SVG which can be upscaled almost infinitely without sacrificing any quality. This SVG is created entirely using CSS, too. The SVG itself is used to create a round "O" animation that feels like it'll fit right in with any futurustic-themed website and is sandwiched by "4" and "0". The error description is rendered in Exo and in orange but with flashing brackets at both sides that help grab the user's attention.

### Error 500

[error-500](error-500)

Similarly to the error

### Favicon

[favicon][favicon]

Favicon description.

