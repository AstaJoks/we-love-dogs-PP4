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
  - [The Surface Plane(Design)](#the-surface-plane-design)
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

- To provide users with a place to find some tips about dogs care
- To provide users with a place to share their own dogs stories
- To provide users a space to connect with other who are crazy about dogs

### User Goals

- To understand what the website is about
- Easy navigate between website pages
- Create an account
- To see blog about Dogs
- To be able to create, edit and delete own posts
- To be able to comment on the blog post
- To be able to create own profile
- Contact the website owner

### Site Owner Goals

- To provide a solution to allow users to see blog, create post, edit and delete posts
- To provide about us section
- To provide a blog about dogs
- Let user to create his/her own post
- Let user to create his/her own profile
- Provide way to contact site owner
- Let user register on the website 
- Fully responsive and accessible website

Back to [top](#table-of-contents)<hr>


## Agile Methodology

The Agile Methodology was used to plan this project. This was implemented through Github and the Project Board, which can be seen here - 
[WeLoveDogsPP4 Project Board](https://github.com/users/AstaJoks/projects/6)

<p><img src="https://res.cloudinary.com/dcydt01ed/image/upload/v1693257705/agile_hkpmnq.png" width="700px" height="auto"  alt="Kanban Board"></p>

Github issues were used to create User Stories for the project. This is where the project user was assigned. Labels were added to show at a glance importance of tasks and help prioritize jobs

### Epics and User Stories

The project had 7 main Epics (Milestones) and 26 User Stories:

**EPIC 1 - Base Setup**
- User Sories
  - As a Developer, I need to set up the project so that it is ready for implementing the core features
  - As a Developer, I need to create static resources so that images, css and work on the website
  - As a Developer, I need to create the navbar so that users can navigate the website from any device
  - As a Developer, I need to create the base.html page and structure so that other pages can reuse the layout
  - As a Developer, I need to create the footer with social media links

**EPIC 2 - Deployment**
- User Stories
  - As a Developer, I need to deploy the project to heroku so that it is live for customers
  - As a Developer, I need to set up whitenoise so that my static files are served in deployment

**EPIC 3 - Plan and create frontend layout**
- User Stories
  - As a Developer, I can create wireframes so that the layout of the website is clear for desktop and mobile
  - As a User, I want the website to be responsive so I can view it on my mobile

**EPIC 4 - Blog**
- User Stories
  - As a User, I want to view a list of blog posts so that I can decide which one I want to read
  - As a User, I can open post details so I can see detailed post information, like it or leave a comment
  - As a User, I can like or unlike a post so that I can interact with the content
  - As a User, I can view the number of comments in the post so that I can see how popular is the post
  - As a User, I can leave comments on a post so that I can be involved in the conversation
  - As a User, I would like to be able to create a new Blog Post so that I can share my story
  - As an Admin, I can approve or disapprove comments so that I can filter out objectionable comments
  - As an Admin, I can create draft posts so that I can finish writing the content later
  - As an Admin, I can create, read, update and delete posts and comments so that I can manage my blog content

**EPIC 5 - Authentication**
- User Stories
  - As a Developer, I need to implement allauth so that users can sign up and have access to the websites features
  - As a Site Owner, I would like the allauth pages customized to that they fit in with the sites styling
  - As an Admin, I can log in to Site Administration so I can access the back end of the site

**EPIC 6 - Stand Alone Pages**
- User Stories
  - As a Site Owner, I would like a home page so that visitors can view information about my Blog
  - As a User, I would like to be able to see my profile so that I can view my details or add my photo
  - As a User, I would like to be able to contact the Blog Owner so that I can report any issue with the website
  - As a Developer, I need to implement a 404 error page to alert users when they have accessed a page that doesn't exist
  - As a Developer, I need to implement a 500 error page to alert users when an internal server error occurs

**EPIC 7 - Documentation and testing**
- Tasks
  - Complete ReadMe documentation
  - Complete Testing Documentation

Back to [top](#table-of-contents)<hr>


## The Scope Plane

-  Responsive Design - Site should be fully functional on all devices from 320px up
-  Hamburger menu for mobile devices
-  Ability to perform CRUD functionality on Posts(User and Admin)
-  Restricted detail blog view while unauthorised user
-  Home page with Blog Information


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


## The Surface Plane(Design)

The Home page, Log-in, Signup Age group and Contact pages can be accessed by all users. Once a user logs in or signs-up, they have access to the Reviews dropdown that shows Add review or see reviews. The Signup page is removed from the navbar once the user logs in, and the log-in page is changed to a log-out page.

### Colour Scheme

  - The four main colours used are: 
     - Light Colour: #F9FAFC -for the body
     - Dark Colour: #141414 - for the footer and shadows
     - Orange/Brown Colour: #e6b265 - for the buttons and post detail decor
     - Light orange/brown Colour: #e7d3b5 - for the forms

<p><img src="https://res.cloudinary.com/dcydt01ed/image/upload/v1693265122/colour_nroimo.png" width="300px" height="auto"  alt="Colour"></p>

### Typography

- One font was chosen for this website, and that was Roboto from google fonts. It is clear and simple to read.

## Technologies

- HTML
  - The structure of the Website was developed using HTML as the main language.
- CSS
  - The Website was styled using custom CSS in an external file.
- JavaScript
  - JavaScript was used to manipulate the DOM .
- Python
  - Python was the main programming language used for the application using the Django Framework.
- GitHub
  - Source code is hosted on GitHub
- Git
  - Used to commit and push code during the development of the Website
- Font Awesome
  - This was used for various icons throughout the site
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