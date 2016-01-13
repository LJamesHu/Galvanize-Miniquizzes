from __future__ import division
from my_stats import PMF

die = PMF({"1": 1./6, "2": 1./6, "3": 1./6, "4": 1./6, "5": 1./6, "6": 1./6 })

die.prob("3") #=> 0.166

die.print_pmf() #=> [("1", 0.166), ("2", 0.166), ("3", 0.166), ("4", 0.166), ("5", 0.166), ("6", 0.166)]

# # weight the die, be sure to renormalize
die.set(("2", 1/2))

print die.print_pmf() #=> [("1", 0.125), ("2", 0.375), ("3", 0.125), ("4", 0.125), ("5", 0.125), ("6", 0.125)]