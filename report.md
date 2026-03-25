# Project Report: Mess Feedback System
# 1. Introduction
The Mess Feedback System is a Python-based console application designed to digitize the feedback process for student dining halls (messes). It allows students to securely log in and rate various aspects of their meals, helping management identify areas for improvement.\
# 2. Objectives
To provide a secure login for students.\
To collect structured data on Taste, Hygiene, and Quantity.\
To automate the calculation of average ratings.\
To identify the worst-performing day based on student satisfaction.\
# 3. Features
Authentication: Simple username and password validation.\
Feedback Submission: Students can submit ratings on a scale of 1-5 for specific days.\
Data Persistence: Uses a list of dictionaries to store records during the session.\
Analytics:\
View individual history.\
Calculate the overall average rating of the mess.\
Find the "Worst Food Day" to pinpoint when quality drops.\
# 4. Technical Specifications
Language: Python 3.x\
Data Structures:\
Lists: For storing user credentials and feedback records.\
Dictionaries: To represent individual feedback entries (Key-Value pairs).\
Concepts Used: Functions, While-loops, Conditional logic, and Arithmetic operations.\
# 5. System Logic (Workflow)
Login: The system checks input against the students and passwords lists.\
Menu: A loop-driven interface that keeps the user logged in until they choose to exit.\
Calculations:\
The Average Rating is calculated by summing the three parameters (Taste, Hygiene, Quantity) and dividing by 3 across all entries.\
The Worst Day is determined by comparing the average score of each entry and tracking the lowest value found.\
# 6. Conclusion
This system replaces manual paper feedback with a more efficient digital format. It provides mess coordinators with clear data to improve food quality and student satisfaction.
