from __future__ import division
from numpy import sqrt
import scipy.stats as scs


def z_test(ctr_old, ctr_new, nobs_old, nobs_new,
           effect_size=0., two_tailed=True, alpha=.05):
    """Perform z-test to compare two proprtions (e.g., click through rates (ctr)).

        Note: if you set two_tailed=False, z_test assumes H_A is that the effect is
        non-negative, so the p-value is computed based on the weight in the upper tail.

        Arguments:
            ctr_old (float):    baseline proportion (ctr)
            ctr_new (float):    new proportion
            nobs_old (int):     number of observations in baseline sample
            nobs_new (int):     number of observations in new sample
            effect_size (float):    size of effect
            two_tailed (bool):  True to use two-tailed test; False to use one-sided test
                                where alternative hypothesis if that effect_size is non-negative
            alpha (float):      significance level

        Returns:
            z-score, p-value, and whether to reject the null hypothesis
    """
    conversion = (ctr_old * nobs_old + ctr_new * nobs_new) / \
                 (nobs_old + nobs_new)

    se = sqrt(conversion * (1 - conversion) * (1 / nobs_old + 1 / nobs_new))

    z_score = (ctr_new - ctr_old - effect_size) / se

    if two_tailed:
        p_val = (1 - scs.norm.cdf(abs(z_score))) * 2
    else:
        # Because H_A: estimated effect_size > effect_size
        p_val = 1 - scs.norm.cdf(z_score)

    reject_null = p_val < alpha
    print 'z-score: %s, p-value: %s, reject null: %s' % (z_score, p_val, reject_null)
    return z_score, p_val, reject_null

lp1v = 998832
lp1r = 331912
lp1p = 18255
lp1rv = lp1r / lp1v
lp1pv = lp1p / lp1v

lp2v = 1012285
lp2r = 349643
lp2p = 18531
lp2rv = lp2r / lp2v
lp2pv = lp2p / lp2v

lp3v = 995750
lp3r = 320432
lp3p = 18585
lp3rv = lp3r / lp3v
lp3pv = lp3p / lp3v


z_test(lp1pv, lp2pv, lp1v, lp2v)
z_test(lp1pv, lp3pv, lp1v, lp3v)
z_test(lp2pv, lp3pv, lp2v, lp3v)