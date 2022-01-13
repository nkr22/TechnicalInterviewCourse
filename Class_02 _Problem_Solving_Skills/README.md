# Class 2 - Problem Solving Skills

Tips that I may forget
•	Listen for unique information (unsorted or sorted array)
•	Write down relevant information
•	Does the code need to compile?
•	Should I assume a valid input? (try and except statements)
•	Can I restate the problem in my own words?
•	What should I label important pieces of data
•	What are the inputs and outputs (data types, etc.)


Brute force solution= solves the problem, but not efficently
-Does not need to be good!
-explain weaknesses
-benefits
    -proves you know the most basic solution and helps you wrap your mind around the problem


Optimize
- How can you improve the brute force?
- Look for unused info from the prompt
- Use a fresh example
- Better to solve incorrectly or have something instead of not at all

Break it Down
- Think twice, code once
- explicity write down steps you are going to take (pseudocode)
- Benefits
    - keeps you on track
    - helps communicate thought process
    - catch logic mistakes

Solve or Simplify
- if you cannot solve the problem, sovle a simpler version and address the difficult part later
- write some code down, do not get stuck for too lock
- clean and pretty code
- it is ok to get confused

Optimization techniques
1. Look for BUD
    -B: Bottlenecks- your algorithm cannot be better than its worst Big O)
    -U: Unnecessary work- extra processing that can be eliminated
    -D: Duplicated work

DIY- how would I solve it manually?

Base Case- something used in recursive algorithms
Solve the problem for the base case- a function that calls itself over and over again until you hit the end (the base case- the simplest, smallest piece)

Data Structure Brainstorm
- thank through all the data structures you know
- pros and cons
- benefits
    - help you get unstuck with a solution you didn't think of before 

Strategies/Patterns
1. Frequency Counter
    - use objects to collect value frequencies
    - avoid nested loops (O(N^2))
2. Multiple Pointers
    - create values/pointers to keep track of indices, and move them as needed until solution is found
    - using left and right when going through arrays (make it so you do not have and O(N^2))
3. Sliding Window
    - create a window to view data
4. Divide and Conquer
    - divide data into smaller chunks, then repear with smaller pieces of data
    -drastically reduces time complexity
    -EX. binary search