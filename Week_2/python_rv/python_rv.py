from python_rv_class import RV
from my_stats import PMF

die = PMF({"1": 1./6, "2": 1./6, "3": 1./6, "4": 1./6, "5": 1./6, "6": 1./6 })

die_rv = RV(die)

die_rv.sample() #=> "3"
die_rv.sample() #=> "2"
die_rv.sample() #=> "6"
die_rv.sample() #=> "3"

die_rv.all_outcomes() #=> ["1", "2", "3", "4", "5", "6"]

die_rv.pmf() #=> < PMF object ... >