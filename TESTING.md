# Manual Testing

## Bugs

| **Bug**   | **Intended Outcome**  | **Issue**   | **Cause**   | **Solution**  | **Commit**  |
|---  |---  |---  |---  |---  |---  |
| #1  | Background image only covering part of the viewport.  | Background image not covering the entire viewport.  | Background image was attached to a `<section>`.   | Attaching the background image to the `<body>`.   | [55c91aa](https://github.com/Ryael/paradise-lost/commit/55c91aa76922aa5140ef12f5f5cddbcc37591eae)   |
| #2  | Error message should be contained with the menu.  | Error message was causing the contents of the menu to overflow.   | The `height` was set to a fixed amount and wasn't accounting for any error messages that would only show up if the user input any invalid data.   | Set the `height` to `fit-content`.  | [0b0f056](https://github.com/Ryael/paradise-lost/commit/0b0f056cb71361212647bdf378550ac4c17144)   |
| #3  | Enlist Now button sends the user to the dashboard.  | Even after the user was authenticated, the home button still read "Enlist Now" and directed the user towards registration.  | The button link was directing the user towards registration as there wasn't any check present to see if the user was already authenticated.   | Check to see if the user is authenticated, and if so, label the button "Dashboard" and direct them towards the Dashboard.   | [3842db3](https://github.com/Ryael/paradise-lost/commit/3842db3d6d66fc0d4dfb4472def74ef786cb491e)   |
| #4  | All buttons disappear from view when the fullscreen navigation menu is opened.  | Buttons were still visible and accessible while the fullscreen navigation menu was open.  | The z-index wasn't configured, causing the buttons to remain on-top of all content.   | `z-index:0` was added to the buttons but later this would be changed to giving the navigation-menu itself a higher `z-index`.   | [bdb7f37](https://github.com/Ryael/paradise-lost/commit/bdb7f378ae2fd850edc51a3b3e9dec42d0574191)   |
| #5  | Roster name field fits nicely in the provided table.  | Roster name field was able to break the provided table and overflow.  | The roster name field's maximum limit was originally set to a max of 255 characters.  | The roster's name field was set to 20 characters instead.   | [99a5f89](https://github.com/Ryael/paradise-lost/commit/99a5f89b929be9014e72b68b4f33cc1f9ddd9976)   |
| #6  | Upon loading into the home page, all text is displayed as intended.   | A layout shift was occurring due to the dynamically changing text.  | The area where the dynamically changing text was appearing was unaccounted for prior to the Javascript causing the cycle to start.  | Adding starting text to that empty field. In this case it was just "ARMY".  | [d6166b5](https://github.com/Ryael/paradise-lost/commit/d6166b5e8511bb9211b473fc2d15db17b2e23faa)   |
| #7  | Database models should be singular.   | Database models were written as plural mistakenly and migrated.   | The typo was the main reason for this error.  | Rolling back the database table fixed the issue.  | N/A   |
| #8  | Unregistered user should not be able to view the dashboard, rosters, or any of its pages.   | Unregistered user was able to view the dashboard, roster, and all its related pages.  | No check was implemented to see if the user was authenticated or not prior to letting them view those aforementioned pages.   | Adding `@login_required` on top of each relevant `views.py` function.   | [25ee051](https://github.com/Ryael/paradise-lost/commit/25ee051ad5bc922aa24988da850176e631ea308a)   |
| #9  | Page titles should be dynamic.  | Page titles were static, set to just "Home".  | The page title was set to be just "Home" within the `head.html` template.   | Adding `%blocktitle%` to the base and updating each page with the relevant page title.  | [82113ba](https://github.com/Ryael/paradise-lost/commit/82113ba9416ef43bb9944f9618e8d19b8835718f)   |
| #10   | Rosters should be sorted by their name on the Roster List page.   | Rosters were sorted by the date created and then the date modified when they were updated.  | The rosters were ordered by their default, which was the date the were last modified.   | Adding `.order_by("name")` to the views function to order them by their name.   | [63f97b8](https://github.com/Ryael/paradise-lost/commit/63f97b83eb44642070ef44d36072755e4f475151)   |
| #11   | The logo link should only cover the amount of space the logo covers.  | The logo link to the Home page covered the entire nav element.  | The `a` element was placed outside of the `h1` element.   | The `a` element was placed inside of the `h1` element.  | [87a6300](https://github.com/Ryael/paradise-lost/commit/87a6300aef692d6e595d9dc160c9530dc255de19)   |
| #12   | No horizontal scrollbars should appear at any point.  | Horizontal scrollbars were appearing in some places.  | The width of certain elements was set to `100vw`.   | Changing the `100vw` to `100%` for the width.   | [b8f168d](https://github.com/Ryael/paradise-lost/commit/b8f168d3be274f173e10eb4afc0bb16c59536187)   |
| #13   | The button corner decorators should always stick to the very corners of the Home page Call to Action button.  | The button corner decorators were slightly off for the top and bottom right corners.  | The div `#cta-button` was caused the right side decorators to be misplaced.   | Removing `#cta-button` div returned the right side decorators to their correct place.   | [c9fc63c](https://github.com/Ryael/paradise-lost/commit/c9fc63c4fddd228e048b467a6f76957108b3140d)   |
| #14   | WhiteNoise prevented error pages not displaying and prevent CSS from loading. | WhiteNoise was added to help with deployment.  | WhiteNoise caused server errors when `DEBUG_MODE` was set to `FALSE`.  | Uninstalling WhiteNoise and replacing it with Cloudinary fixed the CSS display issue and allowed custom error pages to display.   | [5ac22f9](https://github.com/Ryael/paradise-lost/commit/5ac22f9dcdc7cd00dd442bebe7fca67d95c9408a)   |

## Responsiveness

Mozilla Firefox's built-in Responsive Design Mode was to extensively test all aspects of Paradise Lost. It works on viewports as small as 350px.

## Accessibility

[WAVE WebAIM](https://wave.webaim.org/) was used to test the accessibility and it returned just one error and no contrast-errors.

- The error returned was that the button present in `navigation.html` was empty and required and `aria-label`, which was a simple fix.

## Performance

Google Lighthouse was used to assess the performance of this website. All tests were performed in incognito mode to avoid interference from any other sources. Tests were carried out on each section but the same result was returned every time. This was the same case for mobile, and as such, only one result will be provided.

[lighthouse](lighthouse)

## Validation

### HTML

[W3C Markup Validation Service](https://validator.w3.org/nu/)

## Device Testing

The website was tested on many different devices, such as:

- Samsung Galaxy S10
- Samsung Galaxy S21
- Samsung Galaxy Note 8
- MSI GE72 6QF Apache Pro
- iPhone 8
- iPhone 10
- iPhone 11
- iPhone 11 Pro
- iPhone 12
- iPhone 14 Pro Max
- iPad Mini (Landscape and Portrait)
- iPad (Landscape and Portrait)
- Vivo S1 Pro
- LG v60
- Huawei P40 Pro
- Google Pixel 6

## Browser Compatibility

- Mozilla Firefox
- Google Chrome
- Opera
- Safari
- Microsoft Edge

I tested the website extensively on Mozilla Firefox, Google Chrome, and Microsoft Edge. For the remaining two, I asked friends and family to test the website on my behalf while overlooking it to ensure cross-compatibility. No issues or bugs were reported.
