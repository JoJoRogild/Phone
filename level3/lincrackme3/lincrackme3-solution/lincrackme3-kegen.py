#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#We have several ways to keygen this crackme.
#One of them can be to get random numbers for 0000 to 9999 for each part of the serial and make the appropriate calculations to check the serial conditions.
#But this method is quite expensive in computer time.
#
#The method I've used is to get a random value for D_part between 1 and 35 (only the odds ones)
#(why between 1 and 35? because the sum of four digits can't be greater than 36 = 9 * 4)
#
#Then get a number between 7 and 23 (odd only) for the A_part.
#A_part must be > 5 and < 24 and A_part + D_part must be an even number, so A_part must be an odd number due to D_part must be odd
#and to get an even number adding two numbers, both must be even or odd and D_part is odd obligatory.
#
#C_part has no restriction (it must be < B_part but we can obviate it), so we choose a random number between 0 and 36.
#
#Now we can calculate B_part as:
#B_part = 2 * C_part + 2 * D_part - A_part
#and check that B_part > C_part and B_part < 37
#B_part < 37 is needed because its generator: Y+Y+Y+Y can't be greater than 36.
#
#If all conditions are achieved, then we can easily find random numbers from 0000 to 9999 whose sum to be equal to the x_part beeing calculated.
#
#Here's a valid serial for the crackme: 5453-9969-6310-1068
#
#See the code of the keygen below:
#
# keygen for lincrackme3 by adrianbn
#
# miguel
#
import string, random

# Convert n to string
def number_to_str(n):
  sn = "%04d" % n
  return sn

# Get a random number between ini and end-1
# step is used to get only odd numbers when step = 2
def get_number(ini,end,step):
  n = random.choice(range(ini,end,step))
  return n

# Calculate the sum of all digits in string s
def get_sum(s):
  ls = len(s)
  total = 0
  for i in range(ls):
    total += int(s[i])
  return total

# Calculate a number which its get_sum = n
def calc_generator(n):
  while True:
    i = get_number(0,10000,1)
    si = number_to_str(i)
    if get_sum(si) == n:
      return si

# Calculate valid serial
# The serial must be: XXXX-YYYY-WWWW-ZZZZ
# with X,Y,W and Z numbers from 0 to 9
# X+X+X+X = A_part
# Y+Y+Y+Y = B_part
# W+W+W+W = C_part
# Z+Z+Z+Z = D_part
def calc_serial():

  found = False
  while not found:
    # D_part must be an odd number
    D_part = get_number(1,35,2)
    
    # A_part must be an odd number
    # because A_part + D_part must be an even number
    # and 6 < A_part < 24
    A_part = get_number(7,24,2)

    # C_part has no restrictions
    C_part = get_number(0,37,1)
    
    # B_part must be > C_part
    # and B_part = 2 * C_part + 2 * D_part - A_part
    B_part = 2 * C_part + 2 * D_part - A_part
    if B_part > C_part and B_part < 37:
      found = True
      # exit
      break

  print "Calculating XXXX for %4d" % A_part,
  a = calc_generator(A_part)
  print "=",a
  print "Calculating YYYY for %4d" % B_part,
  b = calc_generator(B_part)
  print "=",b
  print "Calculating WWWW for %4d" % C_part,
  c = calc_generator(C_part)    
  print "=",c
  print "Calculating ZZZZ for %4d" % D_part,
  d = calc_generator(D_part)
  print "=",d
  return a+"-"+b+"-"+c+"-"+d
  
print "--- Keygen for lincrackme3 ---"
print
serial = calc_serial()
print
print "Serial: %s" % serial
