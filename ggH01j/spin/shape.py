# tag, used to name the intermediate shape files
tag='mll-mth'

# luminosity to normalize to
lumi=19.47
chans=['of_0j']
#,'of_1j']

# dataset to use: Data2012, Data2012A, Data2012B, SI125
dataset='Data2012'

# set of mc samples: 0j1j, vbf
mcset = 'Hwidth_01j'
sigset = 'Hwidth'

#mcset='0j1j'

# variable, or formula to use: mll, mjj, 2*unboostedMr
# for 2D, use TTree::Draw sytax i.e. x:y
variable='mll:mth' # remember, y:x

# selection to apply when 
selection='shape'

# shape range. can be an
# - hard-coded label
# - a tuple (nx,xmin,xmax)
# - 2d tuple (nx,xmin,xmax,ny,ymin,ymax)
# - 1d array ([x0,..,xn],)
# - 2d array ([x0,..,xn],[y0,...,ym])
range = 'mth-mll-hilospin'
#range = '(30,80,280,8,0,200)'

# splitmode, define the selection to split the shape 2 regions according to the splitmode selection
# splitmode='mll'

# statmode: defined the style of the statistical systematics:
#  - unified: 1 up and 1 down histogram, all bins fluctuating up/down respectively
#  - bybin: 2 histograms per bin, where the corresponding bin is fluctuated up/down
statmode = 'unified'

# label used for the plot's x-axis 
xlabel='m_{ll} - m_{tH}'

# rebin=10
rebin=1

# directories
#    path_latino: latino's files
#    path_dd: data driven estimates
#    path_bdt: location of bdt-trees

path_latino = '/home/amassiro/Latinos/Shape/tree_skim_all_hwidth/'
#path_dd = '/home/amassiro/Latinos/Shape/dd/shape_2012_195fb/'


# other directories
path_shape_raw='raw'
path_shape_merged='merged'

# used in mkDatacards to enable same sign extrapolation and systematic effect
# isssactive = True


# remove some nuisances defined in mkShapes.py
skipSyst = ['JER_down','JER_up','metScale_down','metScale_up','muonEfficiency_down','muonEfficiency_up','electronEfficiency_down','electronEfficiency_up']

# activate/de-activate some nuisances
shapeFlags = [('CMS_8TeV_ch_res',False)]
nuisFlags = [('CMS_8TeV_hww_WJet_FakeRate_e_shape_2j',False),('CMS_8TeV_hww_WJet_FakeRate_m_shape_2j',False)]

SpecialSettings = 'HWidth'
