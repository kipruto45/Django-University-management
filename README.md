# University Management System

## Description

University Management System, built on the Django framework with SQLite3, serves as a robust platform for managing university courses, students and professors. With tailored features and access levels, it caters to various user roles, including administrators, professors and students.

## User Roles and Features

![Screenshot (15)](https://github.com/deabocina/django-university-management-system/assets/140092973/52e9f343-ae26-4a65-83dd-4191a3af2248)

### 1. Student

Students enjoy access to information concerning their own courses and academic status. Their capabilities consist of:

- Viewing the courses they are currently enrolled in.
- Checking their pass or fail status for courses.
- Enrolling or unenrolling themselves from courses.
- Filtering courses based on ECTS points and semester in which they are held.

![Screenshot (16)](https://github.com/deabocina/django-university-management-system/assets/140092973/ca2cb68e-2394-4575-8d27-d34dc0a46b83)
![Screenshot (17)](https://github.com/deabocina/django-university-management-system/assets/140092973/a4e9dc31-70c4-419a-817c-e2cb1330523a)

### 2. Professor

Professors have access limited to the courses they are assigned to. Their functionalities include:

- Viewing the courses they are responsible for.
- Accessing the list of students enrolled in their courses.
- Monitoring students' pass or fail statuses for their respective courses.
- Granting or revoking a student's pass status by providing or removing their signature.

![Screenshot (19)](https://github.com/deabocina/django-university-management-system/assets/140092973/93084c4c-4623-43b3-9754-dce32636e5d2)
![Screenshot (20)](https://github.com/deabocina/django-university-management-system/assets/140092973/33d1c6cb-5f4b-4095-bbc5-822b3c702aa6)

### 3. Administrator

Admins wield complete control over the application and its data. Their capabilities encompass:

- Viewing all student, professor and course details.
- Adding, modifying or removing student, professor and course records.
- Assigning or unassigning professors to courses.
- Enrolling or unenrolling students in courses.
- Gaining insights into which professors are assigned to specific courses and which students are enrolled in each course.

![Screenshot (21)](https://github.com/deabocina/django-university-management-system/assets/140092973/017aade5-4d1a-4015-9057-01cdcf411863)
![Screenshot (23)](https://github.com/deabocina/django-university-management-system/assets/140092973/fad5981a-421e-40ed-b772-e5b412cc7a95)
![Screenshot (24)](https://github.com/deabocina/django-university-management-system/assets/140092973/8dd6f45a-5b4e-4a34-b77e-5b4524961367)

## Setup

To build and run the application, ensure you have Python and SQLite3 installed on your machine. Then, proceed with the following steps:

1. Clone the repository from GitHub.
2. Navigate to the project's root directory.
3. Install the required dependencies using `pip install -r requirements.txt`.
4. Execute Django migrations to set up your database with `python manage.py migrate`.
5. Start the Django development server with `python manage.py runserver`.

You can access the application at `localhost:8000` in your web browser.

I've included two fixture files named `'fixtures.json'` and `'fixtures2.json'` for your convenience in populating your application with initial data. To load it:

- Run `python manage.py loaddata fixtures.json fixtures2.json` from the project's root directory via the terminal.
