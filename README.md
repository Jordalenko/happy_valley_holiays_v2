# HappyValleyHolidays

[Link to deployed site](https://happy-valley-holidays-f15bc71074aa.herokuapp.com/)
<hr>
Introdctory description of site.

![] - amiresponsive image

# Table Of Content

-   [User Experience](#user-experience)
    -   [User Stories](#user-stories)
    -   [Site Goals](#site-goals)
    -   [Scope](#scope)
-   [Design](#design)
    -   [Colour Scheme](#colour-scheme)
    -   [Database Schema](#Database-Schema)
    -   [Fonts](#Fonts)
    -   [Wireframes](#Wireframes)
    -   [Agile Methodology](#Agile-Methodology)
         -   [Overview](#overview)
         -   [EPICS(Milestones)](#epicsmilestones)
         -   [User Stories issues](#user-stories-issues)
         -   [MoSCoW prioritization](#moscow-prioritization)
         -   [GitHub Projects](#github-projects)
-   [Features](#features)
    -   [Navbar](#Navbar)
    -   [Footer](#Footer)
    -   [Home](#Home)
        -   [Hero Section](#hero-section)
        -   [Search Form](#search-form)
        -   [Recent Listings](#recent-listings)
        -   [Listing Card](#listing-card)
    -   [Listings Page](#listings-page)
    -   [Create Listing](#create-listing)
    -   [Profile Page](#profile-page)
    -   [My Listings](#my-listings)
    -   [My Favourites](#my-favourites)
    -   [Remove From Favourites](#remove-from-favourites)
    -   [Edit Listing](#edit-listing)
    -   [Delete Listing](#delete-listing)
    -   [View Listing](#view-listing)
    -   [User account and User account listings](#user-account-and-user-account-listings)
    -   [Sign In Page](#sign-in-page)
    -   [Sign Up Page](#sign-up-page)
    -   [Sign Out Confirmation](#sign-out-confirmation)
    -   [Edit Profile](#edit-profile)
    -   [Delete Profile Confirmation](#delete-profile-confirmation)
    -   [We are sorry to see you go](#we-are-sorry-to-see-you-go)
    -   [Password reset](#password-reset)
    -   [Enter a new password](#enter-a-new-password)
    -   [Password Reset Completed](#password-reset-completed)
    -   [Error Pages](#error-pages)
-   [Future Features](#future-features)
-   [Testing](#testing)
-   [Bugs](#Bugs)
-   [Technologies And Languages](#technologies-and-languages)
    -   [Languages Used](#languages-used)
    -   [Python Modules](#python-modules)
    -   [Technologies and programs](#technologies-and-programs)
-   [Deployment](#deployment)
    -   [Before Deployment](#before-deployment)
    -   [Deployment on Heroku](#deployment-on-heroku)
    -   [Creating A Fork](#creating-a-fork)
    -   [Cloning Repository](#cloning-repository)
-   [Credits](#credits)
    -   [Media](#media)
    -   [Code](#code)
    -   [Acknowledgements](#acknowledgements)
    -   [Comments](#comments)


## User Experience

### User Stories



### Site Goals

1. To provide the users with a place to book a holiday.
2. To provide a range of available dates for cottages to potential letters.
3. To provide a place for the users to browse cottage and tourist amenities offered as well as the prices.
4. To make the website available and functional on every device.

### Scope
The project aims to develop an online booking and reviewing platform called "Happy Valley Holidays" that facilitates users in viewing, booking, reviewing and managing reservations and reviews. The platform will be responsive and user-friendly, providing features for user registration, reservation and review creation, profile management, messaging, favoriting listings, and seamless navigation.

Key Features:

1. Initial Project Setup:

- Developers can set up a new Django project to create the project's structure.
- Database and media storage will be connected to ensure data storage and retrieval.
- An early deployment of the application will be carried out to confirm the initial setup's functionality.

2. Responsive Design:
-The website will be responsive, allowing users to access it on both desktop and mobile devices.

3. User Authentication:
- Users can register an account, providing access to all functionality of Happy Valley Holidays.
- Registered users can log in to view their profile, reservationss and reviews.

4. Profile Management:
- Registered users can view and edit their profiles, including personal details and profile pictures.
- Users can reset their passwords in case they forget them.
- Users can delete their profiles and associated reviews and reservations.

5. Listing Management:
- Users can perform CRUD on their reservations, reviews and profiles.
- The highest rated reviews will be displayed above the footer on the landing page.
- Reviews and reservations will include title, description, images, and usernme.

6. Pagination:
- Pagination will be implemented for easy navigation through pages of reviews.

7. Notification Messages:
- Users will receive notification messages when performing CRUD operations, login/logout, and signup actions.


8. Benefits:

1. User-Centric Experience: The platform focuses on the user's needs, allowing efficient browsing, reservation and review creation, and communication.
2. Efficient Navigation: Users can easily navigate through different sections of the website for seamless access.
3. Effective Communication: Notification messages enhance user communication.

## Design
### Colour Scheme
The website features a calming and professional color palette that combines shades of blue, violet, and green with complementary neutrals. <br>
Overall, this color scheme creates a professional and user-friendly environment, with subtle variations in hue and transparency to guide users' attention and enhance the visual appeal of the website.
![] link to image

### Database Schema
![] link to image

#### Models
1. Allauth User Model

The User model is part of Django Allauth. The model comes with predefined fields as standard. Some of them are username, email, name, password, and more. This model is used for user authentication, hence why changes directly to this model are not advised. The User model is connected to the Profile model with one to one relationship. 

2. Guest Model

The Guest model is a custom custom-created model to handle the user profile details. 

** Confirm ** Signals are used to reflect the changes between the User and Profile models. For example, if the Profile gets updated or deleted the changes will apply to the user model as well. 

3. Review Model

The Review model is connected to the Guest with a ForeignKey field - owner. It is furthermore connected to the Cottage model via ForeignKey field again

4. Cottage Model

This Model was created to store all of the details in the database 

5. CottageImage & HeroImage Models

These models were created to facilitate script based import of all the images stored in the media folder. It is connected to the CarMake model via ForeignKey field - car_make

6. Reservation Model

This model was created to store all of the reservations for each Profile. The model is connected to Guest, Cottage and Profile models via ForeignKey fields - listing and owner.

### Fonts
The font used in this project is Roboto Slab, which compliments the design of the website. <br>
![] link to image

### Wireframes
- Home
![] link to image
- Reviews
![] link to image
- Reservations
![] link to image
- Guest Profile
![] link to image
- Cottage Detail
![] link to image
- Review Detail
![] link to image

### Agile Methodology
#### Overview
This project was created using agile principles. Using the agile approach allowed me to plan all the features of the website through user stories. Each user story has acceptance criteria and tasks to clearly outline the requirements for each feature to be completed.

#### EPICS(Milestones)
The user stories are grouped into eight EPICS or Milestones. An additional Milestone called Project Backlog was created to manage any additional features, bugs, or tasks that may arise during development. <br>
![] link to image

#### User Stories issues
The structure of the user story issue consists of the user story, acceptance criteria, and tasks that outline the steps that are required for this issue to be completed. <br>
![] link to image
During development where possible, the commit messages are connected to their corresponding issues. <br>
![] link to image

#### MoSCoW prioritization
This prioritization technique was used to effectively prioritize the features and requirements of the project based on their importance. The acronym "MoSCoW" stands for "Must have, Should have, Could have, and Won't have." Each category helps categorize and prioritize features to guide the development process and ensure that the most critical elements are addressed first. <br>
![] link to image

#### GitHub Projects
The project was created using a basic Kanban Board structure, divided into columns such as Todo, In Progress, Done, and Backlog. This setup provides a clear and organized way to track the status of tasks and visualize and manage the workflow. <br>
![] link to image

## Features
### Navbar
The navbar is a component that is present on all pages. It was created using Bootstrap and is fully responsive. The HVH logo which serves as a link to the homepage is located on the left side on the navbar. On the right are the nav links which allow the user to easily navigate through the website from any point. If the user is not authenticated the links displayed are Home, Listings, and Login/Signup.

![] link to image

 If the user is authenticated they will see Home, Bookings, About, Profile, and Logout. The profile link will have the user's username displayed to indicate that the user is logged in. For a better user experience, each nav link when active is underlined with a border to let the user know the page they are currently on.

 ![] link to image
 ![] link to image

 ### Footer
 The footer consists of information about HVH and their contact details. To help the users connect with HVH there are icons with links to social media which open in a new tab. 

 ![] link to image

### Home
#### Hero Section
The choice of hero image carousel for the website serves a specific purpose: it immediately communicates the main purpose of the website. The text overlay, "Find Your Next Holiday" directly connects the image to the website's purpose. It encourages users to take action and search for their ideal vacation, making the website's primary function clear right from the start. The image of the three main attractions, Hafren forest, Llanidloes town and Llyn Clywedog reservoir were carefully selected to create an immediate and powerful connection between the user and the website's mission, inviting them to explore the website further.

![] link to image

#### Cottages Section
This section displays the two cottage listings in two bootstrap cards with an image, brief description and titles with embedded links to cottage_detail.html. 

Cottage_detail.html has a pull down menu allowing the user to toggle to the cottage of their choice followed by a hero carousel of images for the selected cottage and finally the highest rated reviews for that cottage paginated in a row of three with a button to see the next 3 highest rated reviews.

![] link to image

#### Reviews Section
The reviews section is designed to present to the user the highest rated reviews about the cottages. 
The review cards are in paginated in rows of three with a button to view the next 3 highest rated reviews. The reviews consist of a title, image, time posted and author. 

The Review section title links to review_detail.html which displays reviews paginated in a row of three for each cottage. review_detail.html also offers a form to enter a new review if the user is logged in.

![] link to image

### Reservations Page
The reservation page can be accessed by logged in users and consists of the same format as the cottage_detail page with date picker calenders and a book now button replacing the reviews. The date picker calendar displays all the available date ranges. Once the user applies the date range to the form the price result appears or updates between the calendar display and the book now button. The user is prompted to confirm their booking by a pop up message. Which if confirmed opens a success message.

![] link to image
![] link to image

### About Page
This page displays a picture of the site owner with a decription of the urpose of the site..

![] link to image

### Profile Page
This page can be accessed only by authenticated users. It consists of a sidebar menu with links for Profile, My Reservations, and My Reviews. The profile page is essentially a large card that includes the user's profile details like name, user name, email, and about me. Underneath, there are two buttons one for edit profile and one for delete profile.

![] link to image

#### My reservations
This page shows all of the reservations that were created by this user. The cards have additional buttons for editing and deleting reservations which allows each user to easily manage their reservations.

![] link to image

#### My Reviews
This page shows all the reviews that user has created. The cards are in a row of three and have buttons to edit and delete.

![] link to image

#### Delete Reservation or Review
The user can easily delete a review or reservation by pressing the delete button. The user is then redirected to the confirmation page with a warning message and two buttons- one to go back and one to remove the listing. Once clicked the listing is removed. 
![] link to image

#### Edit Reservation or Review
This page displays the same form as create a listing, with already populated fields with the current details of the reservation or review. The user can amend all of the details on the page and upload new images or just save the form as it is. Once submitted the user is redirected to my listings page.

![] link to image

![] - Galleries of images of the various pages with decriptive text.
Lorem Ipsum

![] link to image

![] link to image

Lorem Ipsum
![] link to image
![] link to image

#### Flash Messages
Flash messages were user every time the user performs CRUD operation, sign in, and sign out.

![] Messages image link

### Sign In page
Consist of a form with username and password. Below it has a link to reset password, followed by a sign in button which submits the form. The register link is position below that.

![] link to image

### Sign Up page
Consists of a form with name, email, username, password, and password confirmation. Below it has a link to log in if the user already has an account. Below that is the signup button. The user is sent a welcome email to the email provided and is redirected to the profile page update form to customize their profile

![] link to image
![] link to image

### Sign out confirmation
When the user clicks on the log out link in the nav, they are redirected to the confirmation page. This page consist of warning message and two buttons- one to go back and one to log out.

![] link to image

### Edit Profile
The edit profie page renders a form with prefilled fields with the existing information for this user. It consists of profie image, name, username, email, phone, town, county and about me section. Below that is the submit button which will update the profile details once submitted. 

![] link to image

### Delete Profile Confirmation
This page consists of warning message with two buttons - one to go back and one to delete the profile. Delete profile is in red to indicate danger. Once clicked the profile is deleted and the user is redirected to We are sorry to see you go page

![] link to image

### We are sorry to see you go
This page confirms that the profile was deleted. The user is presented with a flash message confirming the profile was deleted successfully. Below that there is a button to go back to the home page.

![] link to image

### Password reset
This page prompts the user to enter their email address. An email with instructions is then sent to their email and the user is redirected to a page that informs them about the email being sent.

![] link to image

### Enter a new password
When the user follows the link from the email, they are sent to a page to set up their new password.

![] link to image

### Password Reset Completed
Once the form is submitted the user is redirected to a page advising them the password reset was completed followed by a log-in button.

![] link to image

### Error Pages
- 404

![] link to image


## Future Features
1. I would like to add financial transactions.
2. Automated testing
3. 
4. 

## Testing
Testing documentation can be found [] link to testing documentation

## Bugs

|Bug|Status|
| ---| ---|
|[BUG: Deployment error #30](https://github.com/Dayana-N/AutoMarket-PP4/issues/30#issue-1816808909)|Closed|



## Technologies And Languages
### Languages Used
- HTML
- CSS
- JavaScript
- Bootstrap
- Python
- Django


### Python Modules

- dj-database-url - This library is used to parse the database URL specified in the DATABASE_URL environment variable, which is commonly used for configuring database connections in Django projects.

- gunicorn - Gunicorn is a popular WSGI (Web Server Gateway Interface) HTTP server for running Python web applications, including Django applications, in a production environment.

- Pillow - Pillow is a Python Imaging Library (PIL) fork that provides tools for working with images in various formats.

- psycopg2 - Psycopg2 is a PostgreSQL adapter for Python. It allows Django to connect to PostgreSQL databases.

- whitenoise - Whitenoise is a middleware for serving static files directly from your Django application.


### Technologies and programs
 - [Favicon Generator](https://favicon.io/favicon-converter/) was used to generate Favicon

 - [GitHub](https://github.com/) is the hosting site used to store the code for the website.
- [Git](https://git-scm.com/) was used as a version control software to commit and push the code to the GitHub repository.
- [Code Institute Template](https://github.com/Code-Institute-Org/gitpod-full-template) was used as a starting point for the project.
- [Pixelmator Pro](https://www.pixelmator.com/pro/) was used for creating the mockup images of the website during planning stage as well as formatting images.
- [Google Fonts](https://fonts.google.com/) was used to import fonts.
- [Google Chrome Lighthouse](https://developers.google.com/web/tools/lighthouse) was used during the testing of the website.
- [Google Chrome Developer Tools](https://developer.chrome.com/docs/devtools/overview/) was used during testing, debugging and making the website responsive.
- [W3C HTML Validator](https://validator.w3.org/) was used to check for errors in the HTML code.
- [W3C CSS Validator](https://jigsaw.w3.org/css-validator/) was used to check for errors in the CSS code
- [Js Hint](https://jshint.com/) was used to validate the JavaScript code.
- [CI Python Linter](https://pep8ci.herokuapp.com/) was used to validate the Python code.

## Deployment
### Before Deployment
To ensure the application is deployed correctly on Heroku it is mandatory to update the requirements.txt. This is a list of requirements that the application needs in order to run.

- To create the list of requirements we use the command pip3 freeze > requirements.txt. This will ensure the file with the requirements is updated.
- Then commit and push the changes to GitHub.

! Before pushing code to GitHub ensure all credentials are in an env.py file, which is included in the .gitignore file. This tells Git not to track this file which will prevent it from being added to Github and the credentials being exposed.

### Deployment on Heroku
- To deploy the project on Heroku, first create an account.
- Once logged in, create a new app by clicking on the create app button
- Pick a unique name for the app, select a region, and click Create App.
- On the next page select the settings tab and scroll down to Config Vars. If there are any files that should be hidden like credentials and API keys they should be added here. In this project, there are credentials that need to be protected. This project requires credentials added for:
1. Django's secret key
2. Database Credentials
3. 
- Scroll down to Buildpacks. The buildpacks will install further dependencies that are not included in the requirements.txt. For this project, the buildpack required is Python
- From the tab above select the deploy section.
- The deployment method for this project is GitHub. Once selected, confirm that we want to connect to GitHub, search for the repository name, and click connect to connect the Heroku app to our GitHub code.
- Scroll further down to the deploy section where automatic deploys can be enabled, which means that the app will update every time code is pushed to GitHub. Click deploy and wait for the app to be built. Once this is done, a message should appear letting us know that the app was successfully deployed with a view button to see the app.

### Creating a fork
1. Navigate to the repository
2. In the top-right corner of the page click on the fork button and select create a fork.
3. You can change the name of the fork and add description 
4. Choose to copy only the main branch or all branches to the new fork. 
5. Click Create a Fork. A repository should appear in your GitHub

### Cloning Repository
1. Navigate to the repository
2. Click on the Code button on top of the repository and copy the link. 
3. Open Git Bash and change the working directory to the location where you want the cloned directory. 
4. Type git clone and then paste the link.
5. Press Enter to create your local clone.

## Credits
### Media
- [Default user image]()
- [Hero image](https://static1.hotcarsimages.com/wordpress/wp-content/uploads/2023/01/2023-bmw-4-series-coupe-featured.jpg)
- [Sorry to see you go image](https://charatoon.com/?id=4714)
- [Default Image]()
- The images for the cottage listings were taken from [https://www.holters.co.uk/] They are for display purpose only.


### Code
- Learned how to setup django project and deploy to Heroku from CI Django Blog walkthrough and www.codemy.com youtube videos.
- [How to create dependant drop down]() 
- [The Car models list is from (back4app)]() 
- [How to use Q objects for complex queries]()
- [Pagination fix for multiple search parameters]()
- I learned how to use advanced Django concepts like signals, off canvas, management command scripts and more from Feddie my django tutor, referred by my mentor.

### Acknowledgements
- Huge thank you to my mentor Brian  for encouraging me to go with my very ambitious idea for my first full-stack project.
- The Slack community and especially Steven Powell, Axe DeKlerk and Robert Jonah Lewis  who listened to my struggles during development.
- Feddie G. for the brilliant Django suggestions to research.

### Comments
This project consists of three apps - Cottages, Bookings, About and Guest_Profile. 
The Guest_Profile app handles everything related to the users including their reservations and reviews since they are directly related to the user. 
The bookings app handles everything related to the reservations including CRUD functionality.
The Cottages app was created to act as a home page with CRUD functionality for reviews.

This project is particularly close to my heart, not only because it's my very first full-stack project but also because it's inspired by my love for midwales. 
