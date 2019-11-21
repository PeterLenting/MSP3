# Chasing Jack Kerouac

## Introduction
This site is a simple, informative and fun page, build to let fans of Jack Kerouac’s novel On the Road inform each other about places from the book that can still be visited now.  Fans can add new locations, delete their posts, adjust them and of course read posts from other fans.

![Responsive site](https://raw.githubusercontent.com/PeterLenting/MSP3/master/static/images/mock-ups/responsive-test.jpg)

- [View the page here](https://chasing-jack-kerouac.herokuapp.com/index)
- [View the Github Repository here](https://github.com/PeterLenting/MSP3)

## Contents table
1. [UX](https://github.com/PeterLenting/MSP3#ux)
   - [What is it?](https://github.com/PeterLenting/MSP3#what-is-it)
   - [Who is the target audience](https://github.com/PeterLenting/MSP3#who-is-the-target-audience)
   - [Mock-ups](https://github.com/PeterLenting/MSP3#mock-ups)
   - [User stories](https://github.com/PeterLenting/MSP3#user-stories)
   - [Design](https://github.com/PeterLenting/MSP3#design)
2. [Features](https://github.com/PeterLenting/MSP3#features)
   - [Existing features](https://github.com/PeterLenting/MSP3#existing-features)
   - [Features left to implement](https://github.com/PeterLenting/MSP3#features-left-to-implement)
3. [Technologies used](https://github.com/PeterLenting/MSP3#technologies-used)
4. [Testing](https://github.com/PeterLenting/MSP3#testing)
   - [Resonsive testing](https://github.com/PeterLenting/MSP3#responsive-testing)
   - [Manual testing](https://github.com/PeterLenting/MSP3#manual-testing)
   - [Improvements after testing](https://github.com/PeterLenting/MSP3#improvements-after-testing)
   - [Browsers](https://github.com/PeterLenting/MSP3#browsers)
   - [Automated testing](https://github.com/PeterLenting/MSP3#automated-testing)
5. [Deployment](https://github.com/PeterLenting/MSP3#deployment)
   - [How to run this project locally](https://github.com/PeterLenting/MSP3#how-to-run-this-project-locally)
6. [Credits](https://github.com/PeterLenting/MSP3#credits)
   - [Content](https://github.com/PeterLenting/MSP3#content)
   - [Media](https://github.com/PeterLenting/MSP3#media)
   - [Code](https://github.com/PeterLenting/MSP3#code)
   - [Acknowledgements](https://github.com/PeterLenting/MSP3#acknowledgements)
7. [Disclaimer](https://github.com/PeterLenting/MSP3#disclaimer)

## UX

### What is it?
A clean, fast and well-arranged website, which gives the visitor more information about places from Jack Kerouac’s novel On the Road that can still be visited these days.  
The site is really simple in use: anyone can add a new destination and tell about their experience.

### Who is the target audience?
Anybody who likes Jack Kerouac's novel On the Road. It could be people who want to visit some location from the book, or have already done so. But also people who are just curieus what the places look like these days.

### Mock-ups
[Mock-up of the mobile version of the homepage](https://raw.githubusercontent.com/PeterLenting/MSP3/master/static/images/mock-ups/mock-up-mobile-index.jpg).

[Mock-up of the desktop version of the homepage](https://raw.githubusercontent.com/PeterLenting/MSP3/master/static/images/mock-ups/mock-up-desktop-index.jpg).

[Mock-up of the mobile version of the form](https://raw.githubusercontent.com/PeterLenting/MSP3/master/static/images/mock-ups/mock-up-mobile-form.jpg).

[Mock-up of the desktop version of the form](https://raw.githubusercontent.com/PeterLenting/MSP3/master/static/images/mock-ups/mock-up-desktop-form.jpg).

### User stories
As a visitor, I want:
1.	To read about the places Jack Kerouac wrote about in On the Road in order to find information about the way the places look now.
2.	To be able to edit a post in order to make the information more complete.
3.	To be able to delete a post when there is something wrong with it.
4.	To write about my own experience in order to inform other people.
5. 	To enjoy myself.

### Design
•	The website is easy to navigate and nice to see. The buttons are all clearly visible and the website works intuitive. 
•	The color scheme is based on the color scheme that was used for a 2006 Dutch edition of On the Road (see About-page for image). The black, yellow and blue combination gives the book and the website a classy look.
•	The Lato-font is easy on the eye and has a nice, clean look.

## Features

### Existing features
**Home** – The home-page of the site. It shows the posts people have made. Under each post are two buttons. One which gives the option to edit and one to delete the post.

**About**  – The About-page tells the story of the site. Why did I make it and what is the purpose.

**Add a post** – This page contains a form which makes it possible for anyone to add a post. All fields are required to make every post really add information for other visitors. 

**Edit** –  This button sends the user to the page where he or she can update any post.

**Delete** – This buttons allows anyone to delete any post. When clicked a modal pops up that ask the user if he/she is sure. 'Yes' deletes the post, 'No' sends him/her back to the homepage.

**Submit** – Allows the user to send in the form.

**Footer** - The footer shows links to the social media accounts of Chasing Jack Kerouac. The links are empty now, since there are no social-accounts yet.

**Current Date** - Sets the date of the post. Read only and will update when the post is edited.

**City** - The City the experience the user had took place in.

**Location** - The specific location the experience the user had took place in.

**Date of experience** - The date on which the user had his experience.

**My name** - The name of the user.

**Part of the book** - The part of On the Road in which Jack Kerouac writes about the location (1-4).

**Chapter of the book** - The chapter of On the Road in which Jack Kerouac writes about the location (1-14).

**Quote in Book** - A quote from On the Road in which Jack Kerouac tells about the location.

**My experience** - A description of the experience the user had on the specific location.

### Features left to implement

1.	Add Photo’s
It would be nice for the user to be able to add a photo to their post. That way they can show what the place they visited, actually looked like at that moment. The photo would off course also be shown on the website.

2.	Log in
In the current condition of the webpage anyone can make changes to all the posts. Off course it would be really nice to give people the option to make an account and make them log in before they can write, update and delete their post.

3.	Search
By making it possible for users to search, they could just look at the places they are really interested in. In the future, when more posts are made, such a function would really add value to the site.

4.	Give likes or thumbs up
It would be nice if users where able to let other users know whether they like the post someone made. That way people would know their work was appreciated and other visitors would know which posts are most popular. 

5. 	Add social media accounts
The links in the footer to the social media accounts of Chasing Jack Kerouac are empty for know, since there are no accounts. These accounts could really add to the interaction of the community of Kerouac-fans and helps them share their post.

## Technologies used
•	HTML, CSS, JavaScript, Python

•	IDE: [Gitpod](https://gitpod.io/).

•   Flask to construct and render pages.

•   Jinja2 to simplify displaying data from the backend.

•   [Tempus Dominus](https://tempusdominus.github.io/bootstrap-4/) and [JQuery](https://jquery.com/) for the date / time picker.

•	[Bootstrap](https://getbootstrap.com/) for the grid system of the page.

•	[Google Fonts](https://fonts.google.com/) for the fonts.

•	[Font Awesome](https://fontawesome.com/) for the icons in the footer of the website.

•	Paint to edit the images used.

•	Google Chrome developer tools.

•	Bash / Ubuntu to commit my project and to push it to Github.

•	[Github](https://github.com/) for version control and for users to view the deployed version of the website.

•   [MongoDB](https://www.mongodb.com/) as the database

•   [Heroku](https://www.heroku.com/) to deploy the project

## Testing

### Responsive testing
The responsiveness of the page was tested at all times during the development of the site. Locally as well as in preview using Google Inspect.

### Manual testing

I created, read, updated and deleted posts myself and had other people testing it as well during the development. This is a reliable way of discovering whether everything works as it should:

**Home** - When clicked should bring user to index.html. Works.

**About** - When clicked should open addaddition.html. Works.

**Add a post** - When clicked should bring user to index.html. Works.

**Jumbotron** - When clicked should bring user to index.html. Works.

**Edit-button** - When clicked should open editaddition.html. Works.

**Editaddition.html** - The fields in the form should contain the content from the corresponding post. Works.

**Delete-button** - When clicked should open modal. Works.

**Yes-button** - When clicked should delete corresponding post. Works.

**No-button** - When clicked should return user to index.html. Works.

**Submit-button (addaddition)** - When clicked the content from the fields in the form should be sent to MongoDB and index.html. Works.

**Submit-button (editaddition)** - When clicked the content from the fields in the form should overwrite the previous content in MongoDB and index.html. Works.

**Current date in form** - Should show current date and user should not be able to change it. Works.

**Date of experience in form** - Should show current date and user should be able to change date to date in the past only. Works.

**Part of the book in form** - Dropdown should contain nummers 1 to 4. Works.

**Chapter in the book in form** - Dropdown should contain nummers 1 to 14. Works.

### Improvements after testing
•   Clicking the delete-button just deleted the post. At first I thought I would create and pop-up to say 'Your post has been deleted', but then I decided it would be better to make sure the user wanted to delete the post.  

•   In the Date of visit calander it was possible to pick a future date. That of course doesn't make much sense, so now only dates in the past can be picked.

•   At first de Date of visit determined the order of the posts on the homepage. It makes more sense to put the new posts on top, so now Current date determines the order.


### Browsers
The page was tested in Chrome, Internet Explorer and Firefox.

### Automated Testing
The following **validation services** were used to check the validity of the code:

•	W3C Markup Validation Service was used to validate HTML.

•	W3C CSS validation was used to validate CSS.

•	JSHint was used to validate JavaScript.

## Deployment
The project was built using Gitpod. I committed the project and pushed it up to Github. Then I made a connection between Github and Heroku to deploy the project.

[View the page here](https://chasing-jack-kerouac.herokuapp.com/index)

•	Connection with MongoDB Atlas
For the project a MongoDB Atlas database was used to store the date. To connect Flask to the MongoDB the third party library flaks-pymongo was installed.

•	Connection string and secret key
In the app.py the os class getenv method is used to point Heroku to the config variable (MONGO_URI) in order to keep "MONGO_DBNAME" and "MONGO_URI" secret.

Requirements and Procfile
•	A requirements.txt file is used to specify the dependencies required for the application. A Procfile is used to specify to Heroku the commands that are executed by the app on startup.

•	Connection between Github and Heroku
On Heroku Dashboard the “Deploy” tab was chosen and the "GitHub" pane selected. Then the option to auto-deploy the project whenever it’s pushed to on Github was activated, the IP, PORT and my connection string in Heroku settings specified and finally, when scrolled down to "Manual deploy" "Master" branch was deployed.


### How to add this project to your local workspace

## To clone this project from GitHub:

•	Go to [the project's repository](https://github.com/PeterLenting/MSP3).
•	Under the repository name, click "Clone or download".
•	In the "Clone with HTTPs" section, copy the URL.
•	In your IDE open Git Bash.
•	Change your current working directory to the location you want the cloned directory to be made in.
•	Type ```git clone```, and paste the URL you copied before.
•	Hit Enter. The process of cloning will now be completed.

## Credits

### Content
All the content on the website was written by me.

### Media
The image from the book-cover used on the about-page and as the favicon is a picture of the book (2006 Dutch edition, Ulysses) I took myself. The image in the header is an image I found on multiple pages and I have not been able to find the person who took it.  

### Code
I wrote all the code myself, with help and inspiration from StackOverflow.com. Questions and answers on that site pointed me in the right direction more than once. The Code Institute tutor-team also helped me understand why sometimes some code wasn't working.
From Bootstrap I used, besides the obvious, [datetimepicker](https://tempusdominus.github.io/bootstrap-4/).

### Acknowledgements
I would like to thank fellow student Rik Duijm for discussing ideas, the tutors from Code Institute for pointing me in the right direction, and mentor Seun Owonikoko for her support.

## Disclaimer
The content of this website is for educational purposes only.