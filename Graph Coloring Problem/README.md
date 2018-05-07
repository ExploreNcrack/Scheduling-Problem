# Exam Scheduling Problem with Graph Coloring
A very typical kind of scheduling problem is the exam scheduling problem.
## Problem
Given all the data about **student course enrollment**
*(A student may enroll into multiple courses in one semester which causes **overlaping student enrollments**)* 
and **time slot** of the scheduling.
### Goal
The goal is to **minimize the student overlap exam as little as possible** with the **minimum number of timeslots**
</br>*(since if there are overlaping students in two classes and you scheduled the two exam happen at the same time, that will be a terrible situation for those students)*
</br>*(with minimum number of timeslots: since you would want to **fully utilize the resources**)*
## Using Graph Theory
Such problem can be expressed as a graph
### Definition of a Graph
Informally, a graph is made up of a set of dots and lines connected the dots
</br>Formally, a graph **G** is a pair of sets **(V,E)** where 
</br>**V** is a **non-empty** set of item called **vertices(or nodes)**
</br>**E** is a set of 2-item subsets of V called **edges**
### Graph Coloring Problem
Given a **graph G** and **K colors**, assign a color to each node so adjacent(neighbour) nodes get different colors.
</br>The **minimum value of K** for which such a coloring exist is the **Chromatic Number of G**
</br>[The **chromatic number problem** One of the **NP-hard** problem](https://en.wikipedia.org/wiki/Graph_coloring)
</br>
</br>![](https://github.com/ExploreNcrack/Scheduling-Problem/blob/master/Graph%20Coloring%20Problem/gc.png)
</br>
In the exam scheduling porblem, we can express all the courses in student's schedule as vertices(nodes) and connect the vertices if there are overlaping student in those courses. And then, two courses that are not in the edge set E can have the same exam schedule time. Our goal is to assign minimum number of avaiable timeslots to each of the courses and the courses with overlaping student do not have the same timeslots. When considering this problem in terms of graph, this is exactly what graph coloring problem is. In this case, the number of available timeslots is the number of different colors of the problem.

## Reference
[Tom Leighton, and Marten Dijk. 6.042J Mathematics for Computer Science. Fall 2010. Massachusetts Institute of Technology: MIT OpenCourseWare, https://ocw.mit.edu. License: Creative Commons BY-NC-SA.](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-042j-mathematics-for-computer-science-fall-2010/video-lectures/lecture-6-graph-theory-and-coloring/)
