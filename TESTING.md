## Table of Contents
- [Validation](#validation)
  - [HTML Validation](#html-validation)
  - [CSS Validation](#css-validation)
  - [Python Validation](#python-validation)
  - [Javascript Validation](#javascript-validation)
- [Lighthouse Testing](#lighthouse-testing)
  - [Home Page](#home-page)
  - [Blog Page](#blog-page)
  - [Post Detail Page](#post-detail-page)
  - [Contact Us Page](#contact-us-page)
  - [Profile Page](#profile-page)
- [Manual Testing](#manual-testing)  
  - [Functional Testing](#functional-testing)
  - [Responsiveness](#responsiveness)
- [Bugs](#bugs)



## Validation

### HTML Validation

Html validation was done with [https://validator.w3.org/nu/](https://validator.w3.org/nu/). 

- The deployed link from the site was used, the below errors were highlighted:

<p><img src="https://res.cloudinary.com/dcydt01ed/image/upload/v1693421561/html_validation_nc8rjl.png" width="700px" height="auto"  alt="HTML Validation"></p>

- Errors were fixed and validation passed successfully.

<p><img src="https://res.cloudinary.com/dcydt01ed/image/upload/v1693421555/html_validation_fixed_jk70xc.png" width="700px" height="auto"  alt="HTML Validation Fixed"></p>


### CSS Validation

The stylesheet was validated using [https://jigsaw.w3.org/css-validator/](https://jigsaw.w3.org/css-validator/)

- No errors were found.

<p><img src="https://res.cloudinary.com/dcydt01ed/image/upload/v1693415331/CSS_Validation_yi5iwh.png" width="800px" height="auto"  alt="CSS Validation"></p>

### Python Validation

Python code was validated using [Code institues Python validator](https://pep8ci.herokuapp.com/#)

- Only minor errors such as missing blank spacing or whitespace. These were rectified easily.

<p><img src="https://res.cloudinary.com/dcydt01ed/image/upload/v1693423295/python_validation_rtnmap.png" width="800px" height="auto"  alt="Python Validation"></p>

### Javascript Validation

JavaScript code was run through [JSHINT](https://jshint.com) javascript validator.
- It flagged up two warnings that 'let' is available in ES6, I fixed these warnings with adding /* jshint esversion: 6 */ at the top of teh function

<p><img src="https://res.cloudinary.com/dcydt01ed/image/upload/v1693414451/jshint_validator_p19sai.png" width="400px" height="auto"  alt="JS Hint Validation"></p>

- It also flagged up the issue with one undefined variable. 

<p><img src="https://res.cloudinary.com/dcydt01ed/image/upload/v1693414451/jshint_valiodator_fixed_akaaba.png" width="400px" height="auto"  alt="JS Hint Validation fixed"></p>

Back to [top](#table-of-contents)<hr>


## Lighthouse Testing

- The performance test was done with Lighthouse through Google Chrome Developer Tools, both for desktop and mobile devices. Most Pages scored High.

### Home Page

<p><img src="https://res.cloudinary.com/dcydt01ed/image/upload/v1693427834/lighthouse_home_jca66z.png" width="600px" height="auto"  alt="Lighthouse Testing Home"></p>

### Blog Page

<p><img src="https://res.cloudinary.com/dcydt01ed/image/upload/v1693427677/blog_c2zfgu.png" width="600px" height="auto"  alt="Lighthouse Testing Blog"></p>

### Post Detail Page

<p><img src="https://res.cloudinary.com/dcydt01ed/image/upload/v1693427677/post_detail_ivnz0i.png" width="600px" height="auto"  alt="Lighthouse Testing Post Detail"></p>

### Contact Us Page

<p><img src="https://res.cloudinary.com/dcydt01ed/image/upload/v1693427677/contact_zjwlgq.png" width="600px" height="auto"  alt="Lighthouse Testing Contact"></p>

### Profile Page

<p><img src="https://res.cloudinary.com/dcydt01ed/image/upload/v1693427950/profile_ixlwgd.png" width="600px" height="auto"  alt="Lighthouse Testing Profile"></p>

Back to [top](#table-of-contents)<hr>


## Manual Testing

- The website was tested on Google Chrome, Firefox, Microsoft Edge and Safari browsers.

   - The website was viewed on a variety of devices such as Desktop, Laptop, iPhone13, iPhone12 Pro, Samsung Galaxy NotePro.

   - All buttons were checked to ensure that they are working with no issues.

   - A large amount of testing was done to ensure that the website is working with no bugs.

   - Friends and family members were asked to review the website and documentation to point out any bugs and/or user experience issues.


### Responsiveness

All pages were tested to ensure responsiveness on screen sizes from 320px and upwards as defined in WCAG 2.1 Reflow criteria for responsive design on Chrome, Edge, Firefox and Opera browsers.

- Steps to test:
    - Open the browser and navigate to [WeLoveDogs](https://we-love-dogs-pp4-3e532b8b5551.herokuapp.com/)
    - Open the developer tools (right click and inspect)
    - Set to responsive and decrease width to 320px
    - Set the zoom to 50%
    - Click and drag the responsive window to maximum width

- Expected:
    - Website is responsive on all screen sizes and no images are pixelated or stretched. No horizontal scroll is present. No elements overlap.

- Actual:
    - Website behaved as expected.


### Functional Testing

- In addition to the other tests, I have conducted a manual functional check list to make sure that everything is working as intended.

| Status | **Navigation Bar - User Logged Out**
|:-------:|:--------|
| &check; | Clicking the navbar logo loads the home page
| &check; | That The navbar shows the tabs Home, Blog, Contact Us, Sign Up and Login if the user is logged out
| &check; | Clicking the Home tab on the navbar loads the home page
| &check; | Clicking the Blog tab on the navbar loads the blog page
| &check; | Clicking the Contact Us tab on the navbar loads the contact page
| &check; | Clicking the Sign up tab on the navbar loads the sign up page
| &check; | Clicking the Login tab on the navbar loads the login page

| Status | **Navigation Bar - User Logged In**
|:-------:|:--------|
| &check; | Clicking the navbar logo loads the home page
| &check; | That The navbar shows the tabs Home, Blog, Contact Us, Create Post, Profile and Logout if the user is logged in
| &check; | Clicking the Home tab on the navbar loads the home page
| &check; | Clicking the Blog tab on the navbar loads the blog page
| &check; | Clicking the Contact Us tab on the navbar loads the contact page
| &check; | Clicking the Create Post tab on the navbar loads the create post page
| &check; | Clicking the Profile tab on the navbar loads the profile page
| &check; | Clicking the Logout tab on the navbar loads the logout page

| Status | **Footer - User Logged Out/In**
|:-------:|:--------|
| &check; | Clicking the facebook icon loads the facebook home page in a new tab
| &check; | Clicking the instagram icon loads the instagram home page in a new tab
| &check; | Clicking the youtube icon loads the youtube home page in a new tab

| Status | **Home Page - User Logged Out**
|:-------:|:--------|
| &check; | That images and text are loading correctly
| &check; | That a Join Us button appears in the hero section
| &check; | Clicking the Join Us button in the hero section of the home page loads the signup page

| Status | **Home Page - User Logged In**
|:-------:|:--------|
| &check; | That images and text are loading correctly
| &check; | That a Blog button appears in the hero section
| &check; | Clicking the Blog button in the hero section of the home page loads the blog page

 Status | **Sign Up Page - User Logged Out**
|:-------:|:--------|
| &check; | Clicking the log in link below the user input loads the log in page
| &check; | That the username input field is required
| &check; | That both password input fields is a required field
| &check; | That if you provide a username and password that is too similiar that the user cannot sign up and user feedback is provided
| &check; | That if your password doesn't match in both password fields, the user cannot sign up and user feedback is provided
| &check; | That if the user provides a password less that 8 character, the user cannot sign up and user feedback is provided
| &check; | That if you provide a good username and password but the email field does not contain a proper email address, the user cannot sign up and user feedback is given
| &check; | That the email input field is optional
| &check; | Clicking the Sign Up button signs the user up and logs the user in if the correct user information was provided for sign up
| &check; | That when the user signs up, they are redirected to the home page and an alert message informs the user that they sisgned up successfully

| Status | **Sign Up Page - User Logged In**
|:-------:|:--------|
| &check; | That the user can not access the signup tab from the navbar if they have logged in

| Status | **Log In Page - User Logged Out**
|:-------:|:--------|
| &check; | Clicking the sign up link below the user input loads the sign up page
| &check; | That the username input field is required
| &check; | That the password input field is required
| &check; | That if the username does not match the password the user cannot log in and user feedback is provided
| &check; | That if the correct credentials are given the user is logged in when the log in button is clicked
| &check; | That when the user is logged in they are redirected to the the home page and an alert message informs the user that they logged in successfully

| Status | **Log In Page - User Logged In**
|:-------:|:--------|
| &check; | That the user can not access the login tab from the navbar if they have logged in

| Status | **Log Out Page - User Logged Out**
|:-------:|:--------|
| &check; | That the user cannot access the log out tab from the navbar if they have logged out

| Status | **Log Out Page - User Logged In**
|:-------:|:--------|
| &check; | Clicking the logout button in the navbar the message appears asking to confirm the log out action
| &check; | Clicking the logout button logs the user out
| &check; | When the user logs out they are redirected to the home page and a message alerts the user that they have logged out

| Status | **Blog Page - User Logged Out**
|:-------:|:--------|
| &check; | That images and text are loading correctly
| &check; | That page pagination is working correctly
| &check; | Clicking the Post Title or the Read More button loads the sign up page
| &check; | That the post author is visible on the post image
| &check; | That the date/time created, the number of likes and comments is visible under the post title

| Status | **Blog Page - User Logged In**
|:-------:|:--------|
| &check; | That images and text are loading correctly
| &check; | That page pagination is working correctly
| &check; | Clicking the Post Title or the Read More button loads the post detail page
| &check; | That the post author is visible on the post image
| &check; | That the date/time created, the number of likes and comments are visible under the post title

| Status | **Post Detail Page - User Logged Out**
|:-------:|:--------|
| &check; | That post detail page is not loading if the user is logged out

| Status | **Post Detail Page - User Logged In**
|:-------:|:--------|
| &check; | That image and text are loading correctly
| &check; | That the post author, date/time created and the number of comments are visible under the post title above post image
| &check; | Clicking on the number of comments below the post title, links to comments section on the post details page bottom
| &check; | That the post like function is working correctly and when the user press the like(heart) button the button changes and the number of likes ads up
| &check; | That the number of comments are visible under the post text

| Status | **Post Detail Page/Comments Section - User Logged In**
|:-------:|:--------|
| &check; | That the users profile picture and the name is visible above the comments form
| &check; | That the button Add Comment works correctly and the users comment appears under the post
| &check; | That the comment's author and the date/time created are visible above the comment

| Status | **Create Post Page - User Logged In**
|:-------:|:--------|
| &check; | That the Title input field is required
| &check; | That the Content field is required
| &check; | That none of the input fields accept empty fields
| &check; | That none of the fields accept just spaces in an input field
| &check; | That the form cannot be submitted without all the required fields and user feedback is given if a user forgets a required field
| &check; | That the placeholder(image) adds if the user do not want to add the image for the post
| &check; | That when the form is submitted a post slug is automatically created
| &check; | That when the post is added, the user is redirected back to the Blog and the message informs that the post is successfully created

| Status | **Edit/Delete Post - User Logged In**
|:-------:|:--------|
| &check; | That the Edit and Delete buttons are visible above the users post title
| &check; | Clicking the Edit button redirects to edit post page
| &check; | Clicking the Delete button redirects to the Delete Post page

| Status | **Edit Post Page - User Logged In**
|:-------:|:--------|
| &check; | That the Title input field is required
| &check; | That the Content field is required
| &check; | That none of the input fields accept empty fields
| &check; | That none of the fields accept just spaces in an input field
| &check; | That the form cannot be submitted without all the required fields and user feedback is given if a user forgets a required field
| &check; | That the placeholder(image) adds if the user do not want to add the image for the post
| &check; | That when the form is submitted(Edit Post button) a post slug is automatically created
| &check; | That when the post is added, the user is redirected back to the Blog and the message informs that the post is successfully updated

| Status | **Delete Post Page - User Logged In**
|:-------:|:--------|
| &check; | That the user can see the title of the post they would like to delete
| &check; | That the message appears in red text to alert the user that the all data of the post will be permanently deleted
| &check; | Clicking Delete Post button deletes the post and redirects to the Blog page
| &check; | That the alert message informs the user that they have successfully deleted their post
| &check; | Clicking Cancel button redirects to Blog page
| &check; | That the post is completely deleted and doesnt show up in the database or subsequently any place on the website

| Status | **Profile Page- User Logged Out/In**
|:-------:|:--------|
| &check; | That the user can change their name
| &check; | That the user can add their bio
| &check; | That the user can add their location
| &check; | That the user can pick their birth of date from the Date Input
| &check; | That the user can upload the profile picture
| &check; | That the placeholder(image) is in place if the user have not updated their profile picture
| &check; | Clicking the Update Profile button the alert message informs that users profile is updated successfully
| &check; | Clicking the Create Post button redirects to the Create Post page

| Status | **Contact Us Page- User Logged Out/In**
|:-------:|:--------|
| &check; | That Reason input field is required
| &check; | That Reason input field has three options
| &check; | That Name input field is required
| &check; | That Email input field is required
| &check; | That Message input field is required
| &check; | That none of the fields can be submitted blank
| &check; | That the email field only accepts proper email syntax (@ symbol has to be present)
| &check; | That none of the fields can accept just blank spaces
| &check; | That user feedback is provided if none of the required criteria to submit the form are met
| &check; | Clicking the Submit button sends the message to the Administration and that the user is redirected to the contact page.
| &check; | That an alert message informs the user that their message was sent successfully upon the user sending the message

Back to [top](#table-of-contents)<hr>


## Bugs

I encountered quite a number of issues and bugs during the development of the site, however some deserves to be noted:

- The first issue I faced when I was creating files for deployment. Every time when I was re-opening my workspace, the env.py and all installed libraries were gone. As a result, I asked for assistance in Slack. 
Fortunately, someone noticed that I was continuing to use the Gitpod Button in my repository as a means of opening the workspace instead of opening my workspace directly.

- I had an issue with static files when I created the base.html, and the static files were not loading up correctly. After hours of checking the base.html code I find out that I was missing the JS Script and CSS link.
Silly mistake cost me a lot of headache.

- I was unable to customise summernote fields width and toolbar. So decided to use the regular form(for users posts).

- Image loading time. I noticed that whenever I get into the Blog Page, the page tend to loads a bit longer than usual. If posts are going to be added in with high resolutions images, it will affect the performance negatively. Image caching or only allowing of certain formats will have to most likely be implemented to lower the loading times.


