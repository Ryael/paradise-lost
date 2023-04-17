# Agile Methodology

## Overview

JIRA was chosen for this project as per Simon W.'s request and due to the fact that it's widely used by companies across the world. I wanted to familiarise myself with the agile methodology at the highest possible level.

To this end, Simon W. was effectively my client and helped me create epics and assign user stories tickets to them. Some of these user stories had additional sub-tasks, which helped me to divide my workload and time accordinly.

It took a while to get used to JIRA and be a single person agile team, but once I did I found it valuable in staying focused on the assigned task and not to spend too much of my time on a single task.

Each sprint lasted for more or less an entire day, with stand ups every day before that. These stand ups were used for me to set out goals for the day, put tickets into sprints, and assign story points to the tickets. This was a time I talked about my strengths and weaknesses, including what I could have seen myself struggling with. I tried my best to address my weaknesses with further research outside of the sprints.

Bugs and additional feeatures were recorded and added to the backlog, and were evaluated so as to make sure they aligned with the MVP. While it was challenging to function as a single person agile team, it proved to be invaluable in keeping the deadline in time while focusing on the most important components of the project.

Past sprints are difficult to view and I did not think to take screenshots during the sprints, so unfortunately they are no screenshots but login details to JIRA will be provided alongside my submission.

## Sprint Notes

Below is a summary of learnings from each individual sprint, gotten from Burnup reports and notes taken by myself.

### Sprint 1:

- The goal of the first sprint was to create a visual element MVP.
- This sprint ran for 8 hours with two tasks at 4 story points each.
- Everything went smoothly.

### Sprint 2:

- The goal of the second sprint was to properly template the website.
- The time set for this was ~10 hours but was unfortunatley improperly configured due to my not starting/stopping sprints properly due to my being unfamiliar with JIRA.
- However, I encounted issues when trying to extract the base template, which required research and found the issue was with the pathing for the templates folder.
- This made me realise the importance of reading the postmortem to properly debug any issues encountered.

### Sprint 3:

- The goal of the third sprint was to setup the account management.
- The time set for this was 6 hours and it was mostly successful.
- Two bugs were solved as they came up.
- I encountered issues with the default rendering of forms via {{form as p}}, which made it difficult to target the individual p fields independant of each other.
- This was solved by creating a `forms.css` which would target these elements. This stylesheet was placed in the `scripts.html` template such that it would be loaded after rendering.

### Sprint 4:

- The goal of the fourth sprint was to setup user account management, setup error 404 and 500 pages, and deploy the project to Heroku.
- The time set aside for this project was 5 hours, but this was a complete mistake as only 3 of 14 story points would be completed.
- Most of this time was spent creating the user account management with only the "forgot your password" functionality remaining.
- Error 404 and 500 pages weren't done.
- The deployment of the project proved to be less than straightforward and took most of the time here.

### Sprint 5:

- The goal of the fifth sprint was to create the data model used for this project.
- I hugely overestimated myself as I only assigned 5 hours to this sprint with having a total of 16 story points.
- Out of these, only 3 were completed.
- It took much longer than expected to update the database and configuring the "forgot your password" functionality, which required an email host.
- Setting up an email host was much more difficult than expected as most servers required payment, but Simon W. was kind enough to temporarily provide his email service API to use for this project.
- The takeaway from this sprint was to better manage my sprints and not take on too much.

### Sprint 6:

- The goal of the sixth sprint was to make a start on the CRUD functionality of this project.
- 5 hours were assigned to this sprint and it was somewhat successful, with 10 story points completed of a total of 19.
- The difficulty here arose from trying to properly configure the READ and CREATE functionality, but was eventually completed.
- The form component took a bit of time to style due to it having to be styled after rendering.
- The error pages proved to a major issue to configure due to a problem with WhiteNoise which was during deployment to help with the automatic upload of static files. This was not known at the time and would prove to be a major issue during the next few sprints.

### Sprint 7:

- The goal of the seventh sprint involved me sorely overestimating myself due to the encroaching deadline.
- 11 hours were assigned to it but only 11 story points were completed out of a total of 21.
- The READ and CREATE functionality was updated and improved.
- A lot of time was spent on making the website friendlier towards mobile viewports.
- Error pages still kept refusing to work due to the White Noise issue.

### Sprint 8:

- The goal of the eigth sprint was to finish the DELETE and EDIT components of CRUD.
- 5 hours were assigned to this and it was mostly successful, with 6 of 10 story points being completed.
- The issue lay with the error pages once again, which would not budge.

### Sprint 9:

- The goal of the ninth sprint was to finally finish the error pages.
- 3 hours were assigned to it and it was highly successful, with everything being finished on time.
- The issue was found to be from White Noise, which was removed and the error pages rendered as expected.

### Sprint 10:

- This was the tenth and final sprint and its main objective was to finish the last few bugs, testing, and documentation.
- It took ~10 hours was completely successful, with everything being finished as planned.

[Back to Readme](https://github.com/Ryael/paradise-lost)
