#! /bin/sh
rm -r raw
rm -r merged
rm -r datacards
cd /home/amassiro/Latinos/CMSSW_5_3_11_patch6/src/HWWAnalysis/ShapeAnalysis/
eval `scramv1 runtime -sh`
source test/env.sh
cd -

mkShapes.py -m 125

mkMerged.py -m 125

mkDatacards.py -m 125


mkAutopsy.py datacards/hww-4.94fb.mH125.of_0j_shape.txt   --dump=postFit/Hwidth-0j-of-error-signalInjection.root --injectionSignal
mkAutopsy.py datacards/hww-4.94fb.mH125.of_0j_shape.txt   --dump=postFit/Hwidth-0j-of-error-data.root




