# HINTS
Simple web application created with Django, Postgres SQL, Redis, Celery, SendGrid, and hosted on Heroku. Please refer to the details below for more information.

### PROJECT LINK
#### Task: 04 + 05
Project similar to Linux Academy or Udemy with ability to book a time with another member.

## https://app.hintsproject.me/
#### https://hintsproject.herokuapp.com/

* CDN: CloudFlare
* Domain Provider: NameCheap (GitHub Student Pack)

### CONTENTS

* [Assignment Checklist](#assignment-checklist)
* [Project Context](#project-context)
* [Critical Questions](#the-critical-questions)
* [Project Brief](#project-brief)
* [Server Side Rendering](#server-side-rendering)
* [Domain Model](#domain-model)
* [Conceptual Entity Relationship Diagram](#conceptual-entity-relationship-diagram)
* [Logical Entity Relationship Diagram](#logical-entity-relationship-diagram)
* [Journal](documents/JOURNAL.md)
* [References](documents/REFERENCES.md)



#### Assignment Checklist

#### Task: 05
* SENTRY SETUP + USE: Refer settings.py file under hints. Requirements.txt file updated for heroku.
* CELERY + REDIS: Refer settings.py for Celery setup and account_app for tasks.py and signals.py for implementation (sign-up email).

#### Task: 04
* Refer project link section above.

#### Task: 03
* .JSON FILES:  Refer Fixtures folder
* DJANGO SIGNALS: Refer to the signals.py file in account_app and course_app
* TESTS: Refer account_app and course_app - test.py files
* DJANGO MESSAGES: Refer account_app views.py
* ADMINISTRATOR CONTROL PANEL CUSTOMISED: Refer admin.py of account_app, course_app and discussion_app
* FUNCTION + CLASS BASED VIEWS: Refer the views.py file of specific apps
* SELECT_RELATED: Refer base_app - views.py
* QUERY SETS: Refer the views.py file of specific apps.
* QUERY SET + EXCLUDE: discussion_app - views.py - AllTimeSlotListView
* QUERY SET + FILTER: discussion_app - views.py - ChapterListView
* QUERY SET + ORDERBY: course_app - views.py - UserCourseListView

#### Task: 02
* MODELS: USER, USERPROFILE, LEARNER, MEETING, TIMESLOT, CATEGORY, COURSE, CHAPTER, LECTURE, ENROLMENT, NOTIFICATION (refer updated ERD below)
* MODEL FORMS: UserUpdateForm, UserProfileUpdateForm, MeetingForm, TimeSlotForm
* FORMSETS: ChapterInlineFormset, LectureInlineFormset
* OTHER FORMS: UserCreationForm
* BASE TEMPLATES: Under base_app - templates - base_app - base.html
* TEMPLATES: Under app - templates - app - .html (for loops and if statements)
* VIEWS: User app - views.py (app specific)
* USER SIGNUP, LOGIN, PASSWORD RESET: Refer account_app

#### Project Context
   Oxford dictionary defines "Pedagogy" as the art, occupation, or practice of teaching. The theory or principles of 
   education; a method of teaching based on such theory.
   
   Historically, the concept of pedagogy was defined by the socratic method of philosophical dialogue and inquiry. 
   Overtime, this definition has evolved through the Renaissance period and the age of enlightenment to the one defined 
   above by the Oxford Dictionary. Today, as the practice of teaching, pedagogy influences, and is influenced by the 
   social, political, and global climate of the time. Therefore, we can conclude that our day-to-day interactions, 
   environment, location, political climate, and many other factors directly influence the methods of teaching. This in 
   turn, affects how we learn and absorb knowledge around us. Aside from formal academic learning offered in 
   universities, technologies and platforms such as YouTube or Linux Academy have created a paradigm shift in our 
   learning environment. Knowledge of any and every subject is at our finger tips.
   
#### The Critical Questions
   In a market that is saturated with high quality information, courses, certifications, forums, and countless tutorials 
   on platforms such as Udemy, YouTube, Linux Academy etc., there is a noticeable lack of guidance or assistance on 
   specific problem solving. This thought process raised the following questions:

* How to can I facilitate peer to peer learning?
* How to engage the extensive knowledge base of professionals around the world without them creating pre-defined content?
* How to facilitate focused problem solving on a specific subject?   
   
#### Project Brief
   The aim of this project is to create a single platform for learning as well as focused problem solving. The "hints" 
   web application allows its users to showcase pre-defined content such as courses or series of videos on a specific
   subject matter (very much similar to Linux Academy). To specifically address the critical questions raised, it also 
   allows users to "book" discussion time with other users who can provide consultation or their expertise over a 
   specific problem. This may be accomplished by integrating third party video call APIs. 
   
Scenarios:
* A user looking for advice on how to change oil in a specific car model.
* A user looking to for guidance from a expert on home improvement project such as building a retaining wall.
* A user looking to for guidance on a highly customised home automation project.

Issues can be highly specific and a person looking advise on how to change the oil of his/her may not want to spend time
searching through extensive amount of information. In this case, a video call with an expert can expedite problem solving
and can help engage people in a more social manner.

#### Server Side Rendering
   Server side rendering can be simply explained by the ability of an application to render the content on the server and
   sending a fully rendered page to the client's browser. There are various advantages of using server side rendering. The 
   server side rendering allows the web application owner to hide the source code that generates the webpage. This 
   advantage can be critical for web applications where security is a significant issue, for instance, banking or insurance
   applications. It enables pages to be loaded faster as it does not wait for javascript files to be downloaded and 
   executed thus improving the user experience. A disadvantage of server side rendering
   is that as applications grow more complex, rendering a large application on the server side can be time consuming, 
   in turn, increasing the loading time and creating a bottle neck. 

#### Domain Model
![DomainModel](https://user-images.githubusercontent.com/57816717/91908099-1e74ad00-ecff-11ea-92e8-5e734b9bca3f.png)
#### Conceptual Entity Relationship Diagram
![UpdatedConceptualEntityRelationshipDiagram](https://user-images.githubusercontent.com/57816717/93009445-60420500-f5d5-11ea-8a8a-b38e4f9ad697.png)
#### Logical Entity Relationship Diagram
![UpdatedLogicalEntityRelationshipDiagram](https://user-images.githubusercontent.com/57816717/93009423-0e00e400-f5d5-11ea-9465-ae3ca0ef80ce.png)