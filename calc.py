DIFF_EQ = 1

from math import *
from math import fabs as abs
from math import log as ln
from math import radians as rad
from math import degrees as deg
from frac import main as frac

if (DIFF_EQ):
    import euler
    import i_euler
    import runge_kutta

def v_db(v1, v2):
    return 20 * log10(v1/v2)

def db_v(db):
    print(frac(10**(db/20)))
    return 10**(db/20)
