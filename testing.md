Go back to [README.md](/README.md)

# Testing
- [Code Validation](#code-validation)
    - [HTML](#html)
    - [CSS](#css)
    - [JavaScript](#JavaScript)
    - [Python](#python)
- [Responsiveness](#Responsiveness)
- [Browser Compatibility](#browser-compatibility)
- [Lighthouse](#Lighthouse)
- [Manual Testing](#manual-testing)
- [User Story Testing](#user-story-testing)

## Code Validation
### HTML
|Page|Validator|Result|
| --- | --- | --- |
| Home |![home](/static/images/readme/validator/html/html%20validator%20index%20html.jpg) | <mark>css in heade of base errors<mark> |
| cottage detail |![Cottage Detail](/static/images/readme/validator/html/html%20validator%20cottage%20detail%20html.jpg) | <mark>css in heade of base errors<mark> |
| review detail |![Review Detail](/static/images/readme/validator/html/html%20validator%20review%20detail%20html.jpg) | <mark>css in heade of base errors<mark> |


### CSS
Test Results CSS  <mark>PASS<mark> 

![css-validator](/static/images/readme/validator/css/css%20validator.jpg)

### JavaScript
1. listing_form.js <mark>PASS<mark> 

![Review_form](/static/images/readme/validator/js/js%20validator.jpg)

7. Bootstrap variable undefined

### Python
1. About app
- app.py <mark>PASS<mark>

![App](/static/images/readme/validator/python/Screenshot%202025-06-13%20at%204.36.18%20PM.png)

- urls.py <mark>PASS<mark>

![urls](/static/images/readme/validator/python/Screenshot%202025-06-13%20at%204.36.56%20PM.png)

- views.py <mark>PASS<mark>

![views](/static/images/readme/validator/python/Screenshot%202025-06-13%20at%204.38.11%20PM.png)

2. HVH Project
- settings.py <mark>PASS<mark> 

(line too long is part of django standart settings file)

![settings](/static/images/readme/validator/python/Screenshot%202025-06-13%20at%204.47.12%20PM.png)

- urls.py <mark>PASS<mark>

![urls](/static/images/readme/validator/python/Screenshot%202025-06-13%20at%204.39.02%20PM.png)

- views.py <mark>PASS<mark>

![views](/static/images/readme/validator/python/Screenshot%202025-06-13%20at%204.43.21%20PM.png)
![views](/static/images/readme/validator/python/Screenshot%202025-06-13%20at%204.38.35%20PM.png)
![views](/static/images/readme/validator/python/Screenshot%202025-06-13%20at%204.39.02%20PM.png)
![views](/static/images/readme/validator/python/Screenshot%202025-06-13%20at%204.42.09%20PM.png)
![views](/static/images/readme/validator/python/Screenshot%202025-06-13%20at%204.50.20%20PM.png)
![views](/static/images/readme/validator/python/Screenshot%202025-06-13%20at%204.50.20%20PM.png)
![views](/static/images/readme/validator/python/Screenshot%202025-06-13%20at%204.57.28%20PM.png)


## Responsiveness
During development each page was tested using dev tools in Google Chrome. The strategy involved ensuring that every page would adapt to various screen sizes beyond a width of 320px, as opposed to relying on fixed device-specific widths.
Further testing was done on mobile to confirm all is working as expected.

|Device|Screen Size|Pass/Fail|Comment|
| --- | --- | --- | ---|
| Iphone 4 | 320x480 | PASS | All sections are displayed correctly. All features work|
| Iphone 12 Pro | 390x844 | PASS | All sections are displayed correctly. All features work|
| Samsung Galaxy s20U | 412x915 | PASS | All sections are displayed correctly. All features work|
| Galaxy Tab S4 | 712x1138| PASS | All sections are displayed correctly. All features work|
| Nest Hub | 1024x600 | PASS | All sections are displayed correctly. All features work|


## Browser Compatibility


|Browser|Result|Pass/Fail|Notes|
| --- | --- | --- | ---|
| Google Chrome | All pages, load as expected. All features work as expected | PASS | --- |
| Firefox | All pages, load as expected. All features work as expected | PASS | --- |
| Edge | All pages, load as expected. All features work as expected | PASS | During initial testing there was an issue with the hero image on Edge. The reason was that the browser does not support avif files. The file was converted to webp and tested again.  |

## Lighthouse

|Page|Validator|Result|
| --- | --- | --- |
| Home Desktop |![home](/static/images/readme/validator/lighthouse/Screenshot%202025-06-13%20at%205.17.00%20PM.png)

## Manual Testing
- Home Page 

Everything was checked.


## User Story Testing

DEV TASK Begin Documentation
USER STORY A1 Developer Create the project's Django structure
USER STORY A2 Developer Connect database and media storage
USER STORY A3 Developer Initial deployment
USER STORY A4: Developer Wireframes and Layout
USER STORY A5: Responsive layout
USER STORY B1 About Page
USER STORY B2 About Page Site Owner
USER STORY B3 Guest Profile Page - Future Feature
USER STORY B4 Home Page
USER STORY B4.1 Home Page - Hero Carousel
USER STORY B4.2: Home Page - Cottage Section
USER STORY B4.3: Home Page - Reviews Section
USER STORY B5 Reservations - Future Feature
USER STORY B6 Navigation
USER STORY B7 Footer
"USER STORY B8.1 Cottage Detail Page - Cottage Carousel
"
USER STORY B8.2 Cottage Detail Page - Cottage Detail
USER STORY B8.3 Cottage Detail Page - Cottage Review
USER STORY B8.4 Cottage Detail Page - Cottage Review Entry
USER STORY B9.1 Review Detail Page - Cottage 1 Reviews
USER STORY B9.2 Review Detail Page - Cottage 2 Reviews
USER STORY C1 Create Account
USER STORY C2 User Password Reset
USER STORY C3 User Profile Page View/Edit - Future Feature
USER STORY C4 Create Reservations - Future Feature
USER STORY C5 Edit Reservation - Future Feature
USER STORY C6 Delete Reservation - Future Feature