# Hacker Rank - Rotate left

## The problem

I am given two arguments, a = a random array, d = number of rotations to the left, that must be applied to this array.
First check I must do, just for precaution is to check if d = 0 or length of array is zero. If one of those 2 is, than
must return the array itself.

Than, I need to check how many real rotaions do I really need.

use case:
- d =3 and array length is 2
  - if one rotate this array 2 times, it will be on its original position
  - Thats why it is important to pick the remainder of this division between `d%len(a)`
- Now, all I have to do is slice the original array using this real rotation number (remainder)