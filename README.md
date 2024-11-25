# W4111-Project-Template

## Introduction

Donald Ferguson's section of W4111 - Introduction to Databases in the Department of
Computer Science at Columbia University has 4 or 5 homework assignments per semester. The basic structure
if each homework has two sections:
1. **Written** questions testing knowledge and understanding of course material.
2. **Practical**, applied tasks that students must implement using technology taught in the course. 
These tasks typically require defining and implementing data models and queries for the databases
covered in the course, e.g. MySQL, MongoDB, Neo4j.

Sections of W4111 have two tracks:
1. Programming
2. Non-programming

The written homework assignments, midterm and final exam are the same for both tracks. 
The **practical** parts of the homeworks differ between the two tracks.

| <img src="./docs/assets/tracks.jpg" width="800px;"> |
|:---------------------------------------------------:|
|                  __W4111 Tracks__                   |



The **practical** parts of homework
3, 4 and 5 are incremental steps in implement a mini "capstone" project. The project demonstrates that
the students can apply knowledge to practical scenarios. The project has three subprojects:
1. Students in both tracks implement [extract-transform-load](https://en.wikipedia.org/wiki/Extract,_transform,_load)
functions that read data files (CSV, JSON)
and load the information into database. Both tracks implement this subproject.
2. The non-programming track implements a Jupyter notebook the provides simple data insight using visualization. This
requires implementing relatively complex queries to provide data for the visualization.
3. The programming track implements a simple, operational, interactive full
[stack web application](https://en.wikipedia.org/wiki/Solution_stack) for navigating and viewing the data.

## Application

### Overview

| <img src="./docs/assets/project-architecture.jpg"> |
|:--------------------------------------------------:|
|        __Project High Level Architecture__         |

Overly simplistically, there are two primary types of applications that use databases:
1. Interactive, operational systems that enable users to create, read, update and
delete information.
2. Decision support applications that enable users to query and analyze data to produce
reports, information, etc. that enables them to make strategy, planning, ... ... decisions.

The programming tracks builds an interactive, operational web application. The
non-programming track builds a simple decision support application. W4111 is a database course,
not a data science course. So, the emphasis of the project is [data engineering](https://en.wikipedia.org/wiki/Data_engineering).

The preceding figure is a high-level, logical architecture diagram for a system combining
both an operational application and a decision support application. 

### Sub-Applications




