# Notes and observations about the 2D array problem

My notes about the 2D array problem from hackerrank

Link: <https://www.hackerrank.com/challenges/2d-array/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=arrays>

## First reading

After reading the problem description for the first time, here are some things that caught my attention:

- What is `hourglass` term?
- How is the input format?
- 

## Plan to solve the problem

### 1st approach

1- Since the matrix is 6x6, an hourglass only fits and starts from positions where the hourglass itself woulf fit.
Top left corner of an hourglass can only start within the first 4 rows and columns, since it is 3x3 matrix.
2- For each valid starting point, calculate the sum of the 7 values that form the hourglass.
3- keep a variable that stores the maximum hourglass sum encountered during the iteration.

hourglass format:

```

1 1 1
  1  
1 1 1

```

