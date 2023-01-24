#! /usr/bin/env python
#
#   script generator for project=2014AYUNM044
#


import os
import sys

# in prep of the new lmtoy module
try:
    lmtoy = os.environ['LMTOY']
    sys.path.append(lmtoy + '/lmtoy')
    import runs
except:
    print("No LMTOY with runs.py")
    sys.exit(0)

project="2014AYUNM044"

#        obsnums per source (make it negative if not added to the final combination)
on = {}
on['J004056.01'] = [ 44710, 44711, 44712, 44714, 44715, 44716, 44718, 44719, 44720, 45740,
                     45741, 45742, 45744, 45745, 45746, 45748, 45749, 45750, 45753, 45754,
                     45755]

on['J011646.77'] = [ 52696, 52697, 52698, 52700, 52701, 52702]

on['J014341.2']  = [ 51650, 51651, 51652, 51654, 51655,
                     51656, 51658, 51659, 51660, 52706,
                     52707, 52708, 52710, 52711, 52712]

on['J132934.18'] = [ 36530, 36531, 36533, 36534, 36536, 36537]

#        common parameters per source on the first dryrun (run1a, run2a)
pars1 = {}
pars1['J004056.01'] = ""
pars1['J011646.77'] = "xlines=110.7,0.3,73.7,0.5"
pars1['J014341.2']  = "xlines=110.0,0.3"
pars1['J132934.18'] = "xlines=75.8,0.3"

#        common parameters per source on subsequent runs (run1b, run2b)
pars2 = {}
pars2['J004056.01'] = ""
pars2['J011646.77'] = ""
pars2['J014341.2']  = ""
pars2['J132934.18'] = ""

runs.mk_runs(project, on, pars1, pars2)
