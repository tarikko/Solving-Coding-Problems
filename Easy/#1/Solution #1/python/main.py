#### Started to solve it on 16-7-2021 ####
#### Solving it ended on 17-7-2021 ####

"""
Given a string, generate all possible subsequences of the string.

For example, given the string xyz, return an array or set with the following strings:

x
y
z
xy
xz
yz
xyz

Note that zx is not a valid subsequence since it is not in the order of the given string.
"""

#### Getting the input ####

import Get_input

String = Get_input.Getinput()

#### Solving ####

import Solve
import time

start = time.time()
Solve.Generate_strings(String)
end = time.time()

print("Solved in {} seconds".format(end-start))

#### This file was coded **entierly** by Tarik Abdelkader (tarikko) ####