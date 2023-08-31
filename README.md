![Logo](https://res.cloudinary.com/dcydt01ed/image/upload/c_scale,w_174/v1693250495/raudonas_gvmzge.png) 

# Introduction

WeLoveDogs is a blog website build using Django, Javascript, CSS, and HTML. It's designed for a community of dog lovers that would like to get regular tips and tricks about dogs care and
share their dog’s delightful moments.

This blog is a Project Portfolio 4 for the Code Institute Diploma in Software Development with eCommerce.

![Responsive Mockup](https://res.cloudinary.com/dcydt01ed/image/upload/v1693179690/mock_up2_espnb1.png)

You can view the live site here: [WeLoveDogs](https://we-love-dogs-pp4-3e532b8b5551.herokuapp.com/) (Right-click to open in a new tab) 

## Table of Contents
- [We Love Dogs](#we-love-dogs)
  - [Table of Contents](#table-of-contents)
- [User Experience (UX)](#user-experience-ux)
  - [The Strategy Plane](#the-strategy-plane)
    - [Site Goals](#site-goals)
    - [User Goals](#user-goals)
    - [Site Owner Goals](#site-owner-goals)
    - [Agile Methodology](#agile-methodology)
      - [Epics and User Stories](#epics-and-user-stories)
  - [The Scope Plane](#the-scope-plane)
  - [The Skeleton Plane](#the-skeleton-plane)
    - [Wireframes](#wireframes)
    - [Database Design](#database-design)
  - [The Structure Plane](#the-structure-plane)
    - [Features](#features)
    - [Features Left To Implement](#features-left-to-implement)
  - [The Surface Plane](#the-surface-plane)
    - [Design](#design)
    - [Colour Scheme](#colour-scheme)
    - [Typography](#typography)
    - [Imagery](#imagery)
- [Technologies](#technologies)
- [Testing](#testing)
- [Deployment](#deployment)
    - [Version Control](#version-control)
    - [Heroku Deployment](#heroku-deployment)
    - [Run Locally](#run-locally)
    - [Fork Project](#fork-project)
- [Credits](#credits)
- [Acknowledgments](#acknowledgments)


# User Experience (UX)

## The Strategy Plane

### Site Goals

- To provide users with a place to find some tips about dogs care.
- To provide users with a place to share their own dogs stories.
- To provide users a space to connect with other who are crazy about dogs.

### User Goals

- To understand what the website is about.
- Easy navigate between website pages.
- Create an account.
- To see blog about Dogs.
- To be able to create, edit and delete own posts.
- To be able to comment on the blog post.
- To be able to create own profile.
- Contact the website owner.

### Site Owner Goals

- To provide a solution to allow users to see blog, create post, edit and delete posts.
- To provide about us section.
- To provide a blog about dogs.
- Let user to create his/her own post.
- Let user to create his/her own profile.
- Provide way to contact site owner.
- Let user register on the website.
- Fully responsive and accessible website.

Back to [top](#table-of-contents)<hr>


## Agile Methodology

The Agile Methodology was used to plan this project. This was implemented through Github and the Project Board, which can be seen here - 
[WeLoveDogsPP4 Project Board](https://github.com/users/AstaJoks/projects/6)

<p><img src="https://res.cloudinary.com/dcydt01ed/image/upload/v1693257705/agile_hkpmnq.png" width="700px" height="auto"  alt="Kanban Board"></p>

Github issues were used to create User Stories for the project. This is where the project user was assigned. Labels were added to show at a glance importance of tasks and help prioritize jobs.

### Epics and User Stories

The project had 7 main Epics (Milestones) and 26 User Stories:

**EPIC 1 - Base Setup**
- User Sories
  - As a Developer, I need to set up the project so that it is ready for implementing the core features.
  - As a Developer, I need to create static resources so that images, css and work on the website.
  - As a Developer, I need to create the navbar so that users can navigate the website from any device.
  - As a Developer, I need to create the base.html page and structure so that other pages can reuse the layout.
  - As a Developer, I need to create the footer with social media links.

**EPIC 2 - Deployment**
- User Stories
  - As a Developer, I need to deploy the project to heroku so that it is live for customers.
  - As a Developer, I need to set up whitenoise so that my static files are served in deployment.

**EPIC 3 - Plan and create frontend layout**
- User Stories
  - As a Developer, I can create wireframes so that the layout of the website is clear for desktop and mobile.
  - As a User, I want the website to be responsive so I can view it on my mobile.

**EPIC 4 - Blog**
- User Stories
  - As a User, I want to view a list of blog posts so that I can decide which one I want to read.
  - As a User, I can open post details so I can see detailed post information, like it or leave a comment.
  - As a User, I can like or unlike a post so that I can interact with the content.
  - As a User, I can view the number of comments in the post so that I can see how popular is the post.
  - As a User, I can leave comments on a post so that I can be involved in the conversation.
  - As a User, I would like to be able to create a new Blog Post so that I can share my story.
  - As an Admin, I can approve or disapprove comments so that I can filter out objectionable comments.
  - As an Admin, I can create draft posts so that I can finish writing the content later.
  - As an Admin, I can create, read, update and delete posts and comments so that I can manage my blog content.

**EPIC 5 - Authentication**
- User Stories
  - As a Developer, I need to implement allauth so that users can sign up and have access to the websites features.
  - As a Site Owner, I would like the allauth pages customized to that they fit in with the sites styling.
  - As an Admin, I can log in to Site Administration so I can access the back end of the site.

**EPIC 6 - Stand Alone Pages**
- User Stories
  - As a Site Owner, I would like a home page so that visitors can view information about my Blog.
  - As a User, I would like to be able to see my profile so that I can view my details or add my photo.
  - As a User, I would like to be able to contact the Blog Owner so that I can report any issue with the website.
  - As a Developer, I need to implement a 404 error page to alert users when they have accessed a page that doesn't exist.
  - As a Developer, I need to implement a 500 error page to alert users when an internal server error occurs.

**EPIC 7 - Documentation and testing**
- Tasks
  - Complete ReadMe documentation.
  - Complete Testing Documentation.

Back to [top](#table-of-contents)<hr>


## The Scope Plane

-  Responsive Design - Site should be fully functional on all devices from 320px up.
-  Hamburger menu for mobile devices.
-  Ability to perform CRUD functionality on Posts(User and Admin).
-  Restricted detail blog view while unauthorised user.
-  Home page with Blog Information.

Back to [top](#table-of-contents)<hr>


## The Skeleton Plane

### Wireframes

- Home Page

   <p><img src="https://res.cloudinary.com/dcydt01ed/image/upload/v1693263389/1._Home_Page_kg9k2c.png" width="400px" height="auto"  alt="Wireframe Home Page"></p>

- Contact Us

   <p><img src="https://res.cloudinary.com/dcydt01ed/image/upload/v1693263388/2._Contact_Us_dxcc17.png" width="400px" height="auto"  alt="Wireframe Contact Us"></p>

- Blog

   <p><img src="https://res.cloudinary.com/dcydt01ed/image/upload/v1693263389/3._Blog_Page_uxcard.png" width="400px" height="auto"  alt="Wireframe Blog"></p>

- Join us

   <p><img src="https://res.cloudinary.com/dcydt01ed/image/upload/v1693263388/4._Join_Us_Page_xt8e7k.png" width="400px" height="auto"  alt="Wireframe Join Us"></p>

- Log In

   <p><img src="https://res.cloudinary.com/dcydt01ed/image/upload/v1693263389/5._Log_In_Page_baucio.png" width="400px" height="auto"  alt="Wireframe Log In"></p>

- Post Detail

   <p><img src="https://res.cloudinary.com/dcydt01ed/image/upload/v1693263389/6._Post-Detail_Page_ibrpw9.png" width="400px" height="auto"  alt="Wireframe Post Detail"></p>

- Create Post

   <p><img src="https://res.cloudinary.com/dcydt01ed/image/upload/v1693263389/7._Create_Post_Page_qw48n6.png" width="400px" height="auto"  alt="Wireframe Create Post"></p>

- Edit-Delete

   <p><img src="https://res.cloudinary.com/dcydt01ed/image/upload/v1693263389/8._Edit-Delete_My_Post_pxotbl.png" width="400px" height="auto"  alt="Wireframe Edit-Delete Post"></p>

- Profile

   <p><img src="https://res.cloudinary.com/dcydt01ed/image/upload/v1693263389/9._Profile_Page_tqpfsy.png" width="400px" height="auto"  alt="Wireframe Profile"></p>

- 404 Page

   <p><img src="https://res.cloudinary.com/dcydt01ed/image/upload/v1693263389/10._404_Page_pcagbr.png" width="400px" height="auto"  alt="Wireframe 404 Page"></p>


### Database Design

- The database models and fields were planned and outlined using an Database Diagram in [Lucidchart](https://lucid.co/).

<p><img src="https://res.cloudinary.com/dcydt01ed/image/upload/v1693246380/Database_Diagram_tzuyo0.png" width="700px" height="auto"  alt="Database Design"></p>

Back to [top](#table-of-contents)<hr>


## The Structure Plane

## Features

### Navigation

- The navigation menu is displayed on all pages and drops down into a hamburger menu on smaller devices. This will allow users to view the site from any device and not take up too much space on mobile devices.

<p><img src="https://res.cloudinary.com/dcydt01ed/image/upload/v1693346278/nav_mobile_zbtdeq.png" width="600px" height="auto"  alt="Nav Bar Login Mobile"></p>

- Tabs on the navigation bar change depending on whether the user is logged in or not.

    - If the user logs in or signs up, those two tabs are removed to be replaced with a Logout tab.

    <p><img src="https://res.cloudinary.com/dcydt01ed/image/upload/v1693342454/nav_bar_login_tzyfks.png" width="800px" height="auto"  alt="Nav Bar Login"></p>

    - Once the user logs in or signs up, a completely two new tabs appears called Create Post and Profile.

    <p><img src="https://res.cloudinary.com/dcydt01ed/image/upload/v1693342460/nav_bar_logout_u4gepb.png" width="800px" height="auto"  alt="Nav Bar Logout"></p>

### Home Screen

- Home Page is a landing page that provides an overview of the website and its features.

   #### Hero Section

   - In the Hero Section there is a large  Hero image to catch the user's eye, the site name, a call to action with a Join Us button and a quote about dogs.

   <p><img src="https://res.cloudinary.com/dcydt01ed/image/upload/v1693344421/hero_image_i2ajtk.png" width="600px" height="auto"  alt="Hero Section Join Us"></p>

   - If the user sign up the join button will change to the Blog button(the direct link to the blog) 

   <p><img src="https://res.cloudinary.com/dcydt01ed/image/upload/v1693345281/hero_image_blog_kvezlx.png" width="600px" height="auto"  alt="Hero Section Blog"></p>

   #### About Us Section

   - Below the Hero section there is About Us section to introduce the blog to the user.

   <p><img src="https://res.cloudinary.com/dcydt01ed/image/upload/v1693344421/about_us_rjyp7a.png" width="600px" height="auto"  alt="About Us section"></p>

### Footer

A footer has been added to the bottom of the site, this contains Facebook, Instagram and Youtube links so that users can follow the blog on social media. These icons open in new tabs as they lead users away from the site.
A footer also contains Copyright.

<p><img src="https://res.cloudinary.com/dcydt01ed/image/upload/v1693344420/footer_quavpu.png" width="700px" height="auto"  alt="Footer"></p>

### Contact Us Page

- The Contact feature can be found from the nav bar and allows both signed in users and anonymous users to contact the site admin.
- Contact Us Page contains a form with the contact reason option,  the user details and the message.
- Styles are consistent with the rest of the website. 

<p><img src="https://res.cloudinary.com/dcydt01ed/image/upload/v1693346596/contact_us_piml9j.png" width="600px" height="auto"  alt="Contact Us"></p>

### Log In Page

- The Log In page is accessed from the navigation bar.
- The Log In page contains a link to the Sign Up page for the user who may have misclicked and needs to Sign Up rather than log in.
- It uses django-allauth to provide all the settings for user authentication.
- Styles are consistent with the rest of the website.
- The page is fully responsive.

<p><img src="https://res.cloudinary.com/dcydt01ed/image/upload/v1693346164/log_in_p6xxl1.png" width="600px" height="auto"  alt="Login Page"></p>

### Sign Up Page

- The Sign Up page is accessed from either the navigation bar or a button on the homepage(Join Us button).
- The Sign Up page contains a link to the Log In page for the user who may have misclicked and already has an account.
- It uses django-allauth to provide all the settings for user authentication:
    - Unique username,
    - Strength of password.
- Styles are consistent with the rest of the website.
- The page is fully responsive.

<p><img src="https://res.cloudinary.com/dcydt01ed/image/upload/v1693346411/sign_up_page_ubeuhs.png" width="600px" height="auto"  alt="Sign Up Page"></p>

### Log Out Page

- The Log Out page can only be accessed from the navigation bar and only when the user is logged in.
- The Log Out page has a button for users to confirm they wish to log out or the button to cancel the request.
- It uses django-allauth to provide all the settings for user authentication.
- Styles are consistent with the rest of the website.
- The page is fully responsive.

<p><img src="https://res.cloudinary.com/dcydt01ed/image/upload/v1693347287/logout_b0qkoe.png" width="600px" height="auto"  alt="Log Out"></p>

### Blog Page

- A Collection of Posts about the Dogs care, tips and tricks about their training and recipes for Dogs.
- The Blog post lists can be found from the navigation bar(both signed in and anonymous users) and hero image section(signed in users only) and allows both signed in users and anonymous users to see the list of posts.

<p><img src="https://res.cloudinary.com/dcydt01ed/image/upload/v1693348193/blog_page_s1nz0u.png" width="600px" height="auto"  alt="Blog Page"></p>

### Post Detail Page

  #### Post Detail Section

  - A Full Detail Post can be seen by signed in users only.

  <p><img src="https://res.cloudinary.com/dcydt01ed/image/upload/v1693348346/post_detail_page_post_cfexba.png" width="600px" height="auto"  alt="Post Detail Page"></p>

  #### Comment Section

  - Users can read the post, like the post and leave comments.

  <p><img src="https://res.cloudinary.com/dcydt01ed/image/upload/v1693348345/comment_section_vt6uwf.png" width="600px" height="auto"  alt="Comments Section"></p>

### Create Post

- User must be register to create the post.
- Create Post page can be accessed from the navigation bar and in the profile page.

<p><img src="https://res.cloudinary.com/dcydt01ed/image/upload/v1693350555/create_post_vfjywe.png" width="600px" height="auto"  alt="Create Post"></p>

### Edit/Delete Post

- Once the user creates the post, edit and delete buttons appears on their post detail view.

<p><img src="https://res.cloudinary.com/dcydt01ed/image/upload/v1693350748/edit_delete_post_tibiur.png" width="600px" height="auto"  alt="Edit/Delete Post"></p>

### Edit Post

- Edit Post Page can be accessed on the Post Detail Page(Users created Post)

<p><img src="https://res.cloudinary.com/dcydt01ed/image/upload/v1693347983/edit_post_w1wmio.png" width="600px" height="auto"  alt="Edit Post"></p>

### Delete Post

- Delete Post button can be accessed on the Post Detail Page(Users created Post)
- Once User press the delete button, the alert message appears to ask if the user is sure he wants to delete the post.

<p><img src="https://res.cloudinary.com/dcydt01ed/image/upload/v1693347937/delete_post_gsa51t.png" width="600px" height="auto"  alt="Delete Post"></p>

### Profile

- Profile Page can be accessed from the navigation bar.
- The Profile Page provide more user details that could also be added in general. Such as a profile picture or avatar that could be utilized in their comments.

<p><img src="https://res.cloudinary.com/dcydt01ed/image/upload/v1693348416/profile_page_idnlnk.png" width="600px" height="auto"  alt="Profile Page"></p>

### 404 Page

- The 404 page will allow the user to easily navigate back to the main website if they direct to a broken link / missing page, without the need of the browsers back button.

<p><img src="https://res.cloudinary.com/dcydt01ed/image/upload/v1693523416/404_error_up8gj3.png" width="600px" height="auto"  alt="404 Page"></p>

### 403 Page

- A 403 error page has been implemented to provide feedback to the user when they try to access unauthorized content. Users will be directed to this page if they alter the URL's and attempt to edit, delete

<p><img src="https://res.cloudinary.com/dcydt01ed/image/upload/v1693523416/403_error_hzoczn.png" width="600px" height="auto"  alt="403 Page"></p>

### 500 Page

- A 500 error page has been displayed to alert users when an internal server error occurs. The message relays to users that the problem is on our end, not theirs.

<p><img src="https://res.cloudinary.com/dcydt01ed/image/upload/v1693523416/500_error_h8sy1r.png" width="600px" height="auto"  alt="500 Page"></p>

### Success Messages

- Success messages are implemented throughout the website as the confirmation for the user that his/her action is completed successfully.

<p><img src="https://res.cloudinary.com/dcydt01ed/image/upload/v1693349176/succsess_messages_qwyk1b.png" width="600px" height="auto"  alt="Success Messages"></p>

### Favicon 

 - A favicon was added the website to enable users to easily locate the website in the browser when multiple tabs are open.

 <p><img src="https://res.cloudinary.com/dcydt01ed/image/upload/v1693352471/favicon_ixzdc8.png" width="400px" height="auto"  alt="Favicon"></p>

## Features Left To Implement

- There are a number of features which would be great to implement in the future:
   - ability for users to view author's/other users profiles,
   - ability for users to save their favourite posts,
   - ability for users to delete their own comments, 
   - ability users to reply to other comments,
   - ability users to login with their social media accounts.

Back to [top](#table-of-contents)<hr>


## The Surface Plane

### Design

- The Design of WeLoveDogs is clean and modern, with a focus on readability and ease of use.

### Colour Scheme

  - The four main colours used are: 
     - Light Colour: #F9FAFC -for the body.
     - Dark Colour: #141414 - for the footer and shadows.
     - Orange/Brown Colour: #e6b265 - for the buttons and post detail decor.
     - Light orange/brown Colour: #e7d3b5 - for the forms.

<p><img src="https://res.cloudinary.com/dcydt01ed/image/upload/v1693265122/colour_nroimo.png" width="300px" height="auto"  alt="Colour"></p>

### Typography

- Two fonts were chosen for this website: Roboto and Lato from google fonts. They are clear and simple to read.

### Imagery

- The Website logo was made using CorelDraw.

- Images throughout the website were taken from here: https://wall.alphacoders.com/by_collection.php?id=368

Back to [top](#table-of-contents)<hr>


## Technologies

- HTML
  - The structure of the Website was developed using HTML as the main language.
- CSS
  - The Website was styled using custom CSS in an external file.
- JavaScript
  - JavaScript was used to manipulate the DOM.
- Python
  - Python was the main programming language used for the application using the Django Framework.
- GitHub
  - Source code is hosted on GitHub.
- Git
  - Used to commit and push code during the development of the Website.
- Font Awesome
  - This was used for various icons throughout the site.
- Heroku
  - Heroku was used for live website deployment.
- Cloudinary
  - Cloudinary is a cloud storage solution for website media and other static files. It also allows for the manipulation and optimization of media delivery.
- Bootstrap
  - Bootstrap was used throughout the site for responsiveness, layout, and predefined style elements.
- Favicon.io
  - favicon files were created at https://favicon.io/favicon-converter/
- balsamiq
  - wireframes were created using balsamiq from https://balsamiq.com/wireframes/desktop/#
- CorelDraw
  - This was used to create the logo in header.

Back to [top](#table-of-contents)<hr>


## Testing

Testing documentation is here: [Testing](./TESTING.md)

Back to [top](#table-of-contents)<hr>


## Deployment

### Version Control

The Site was created using gitpod workspace and pushed to github.

```git add .``` - This command was used to add the file(s) to the staging area before they are committed.

```git commit -m “commit message”``` - This command was used to commit changes to the local repository queue ready for the final step.

```git push``` - This command was used to push all committed code to the repository on github.

### Heroku Deployment

**Requirement and Procfile**

Before deployment on Heroku, two files need to be created and be up to date, a `requirements.txt` file and a `Procfile`.

- The `requirements.txt` file is created by executing the following command in the terminal window: ` pip3 freeze --local > requirements.txt`. A file with all requirements will be created.
- Then create a file named `Procfile` and insert the following code: `web: gunicorn welovedogs.wsgi`, with no empty lines after it.
- Then make sure to push these files to your repository.

**Creating Heroku App**

- Log into Heroku and go to the Dashboard.
- Click "New" and then select "Create new app".
- Give your app a name and select the region closest to you.
- Click "Create app" to confirm.

**Creating a database**

- Log into ElephantSQL.com and access your dashboard.
- Click "Create New Instance"
- Set up a plan, give your plan a **Name**, select the **Tiny Turtel (Free)** plan, leave the **Tags** field blank.
- Select "Select Region" and select a data center new you.
- Click "Review".
- Confirm your details and then click "Create instance".
- Return to the ElephantSQL dashboard and click on the database instance name for this project.
- In the URL section, click the copy icon to copy the database URL.
- In your workspace make sure django and gunicorn are installed by running `pip3 install 'django<4' gunicorn`.
- Equally make sure that infrastructure for the database is installed by running `pip3 install dj_database_url===0.5.0 psycopg2`.
- Update the `requirements.txt` file if needed.

**The env.py file**

- If you do not have a `env.py` file in your workspace create one and make sure it is included in the `.gitignore` file.
- At the top of the `env.py` file add the line: `import os`.
- Below that add the following two lines:

  `os.environ["DATABASE_URL"] = "<copied URL from SQL database>"` <br>
  `os.environ["SECRET_KEY"] = "<create a secret key of your own>"` <br>

- If you are using Cloudinary storage also add the following line: <br>

  `os.environ["CLOUDINARY_URL"] = "<copied URL from Cloudinary account>"`<br>

- Make sure the environment variables are imported correctly into the `settings.py` file.
- Run `python manage.py migrate` in the terminal window to migrate the data structure to the database instance.

**Setting Environment Variables**

- On the Heroku Dashboard select the app you just created and then select the "Settings" tab.
- Click "Reveal Config Vars"
- Add the following config vars: <br>

  `DATABASE_URL` - copy the database URL from ElephantSQL in here, it should also be in the `env.py` file. <br>
  `SECRET_KEY` - copy your secret key in here. <br>

- If you are using Cloudinary storage you also need to copy your personal `CLOUDINARY_URL` into these fields. <br>
- In addition, you may need the key `PORT` with value `8000`.

**Connecting to GitHub and Deploy**

- On the Heroku Dashboard select the app you just created and then select the "Deploy" tab.
- Select GitHub for the deployment method.
- Search for the name of the project repository and click "Connect".
- Further down the page, select "Enable Automatic Deploys" if desired.
- Then finally further down, select "Deploy Branch" and watch the app being built.

### Forking the Repository

- Log in to GitHub and locate the GitHub repository you want to fork.
- At the top of the Repository above the "Settings" Tab on the menu, locate the "Fork" Button and click it.
- You will have a copy of the original repository in your GitHub account.
- You will now be able to make changes to the new version and keep the original safe.

### Making a Local Clone

- Log into GitHub and locate the repository you want to clone.
- Click the 'Code' dropdown above the file list.
- Copy the URL for the repository.
- Open Git Bash in your IDE.
- Change the current working directory to the location where you want the cloned directory.
- Type `git clone` in the CLI and then paste the URL you copied earlier. This is what it should look like:
  `$ git clone https://github.com/`
- Press Enter to create your local clone.

You will need to install all of the packages listed in the requirements file you can use the following command in the terminal `pip install -r requirements.txt` which will do it for you.

Back to [top](#table-of-contents)<hr>


## Credits

### Content

- [Code Institute - I Think Therefore I Blog](https://codeinstitute.net/ie/)
- [Realphyton/djando social network](https://realpython.com/django-social-network-1/)
- [User Profile and Picture](https://www.youtube.com/watch?v=FdVuKt_iuSI&t=589s)
- [Create a Simple Django Blog](https://www.youtube.com/watch?v=B40bteAMM_M&list=PLCC34OHNcOtr025c1kHSPrnP18YPB-NFi)
- [User Profile and Picture](https://www.youtube.com/watch?v=FdVuKt_iuSI&t=589s)
- [Carousel Images](https://www.w3schools.com/bootstrap/bootstrap_carousel.asp)
- [StackOverflow](https://stackoverflow.com/p)
- [Bootstrap Documentation](https://getbootstrap.com/docs/5.3/getting-started/introduction/)
- [DEV Community](https://dev.to/)


All those resources were very valuable in the progression of my project whenever I was stuck at any point in time I refered back to the course material as well as the online resources.

### Resources

- [Code Institute](https://codeinstitute.net/ie/)
- [Am I Responsive](https://ui.dev/amiresponsive)
- [Quotes about Dogs](https://www.rover.com/blog/quotes-about-dogs/)
- [Admins Posts about dog care](https://sitstay.com/blogs/good-dog-blog/the-best-dog-training-treats-for-successful-training-and-a-happy-pup)
- [Images throughout the website](https://wall.alphacoders.com/by_collection.php?id=368)


## Acknowledgments

### 

I would like to thank Code Institute for supplying me with the necessary guidance for this project. And Slack Community for certain things I was completely stuck at.

Back to [top](#table-of-contents)<hr>