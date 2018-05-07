# Exam Scheduling Problem with Graph Coloring
A very typical kind of scheduling problem is the exam scheduling problem.
## Problem
Given all the data about **student course enrollment**
*(A student may enroll into mutiple courses in one semester which causes **overlaping student enrollments**)* 
and **time slot** of the scheduling.
### Goal
The goal is to **minimize the student overlap exam as little as possible** with the **minimum number of timeslots**
</br>*(since if there are overlaping students in two classes and you scheduled the two exam happen at the same time, that will be a terrible situation for those students)*
</br>*(with minimum number of timeslots: since you would want to **fully utilize the resources**)*
## Using Graph Theory
Such problem can be expressed as a graph
### Definition of a Graph
Informally, a graph is made up of a set of dots and lines connected the dots
</br>Formally, a graph G is a pair of sets **(V,E)** where 
</br>**V** is a **non-empty** set of item called **vertices(or nodes)**
</br>**E** is a set of 2-item subsets of V called **edges**
## Reference
[Tom Leighton, and Marten Dijk. 6.042J Mathematics for Computer Science. Fall 2010. Massachusetts Institute of Technology: MIT OpenCourseWare, https://ocw.mit.edu. License: Creative Commons BY-NC-SA.](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-042j-mathematics-for-computer-science-fall-2010/video-lectures/lecture-6-graph-theory-and-coloring/)
