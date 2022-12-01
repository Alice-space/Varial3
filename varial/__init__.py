from . import analysis
from . import diskio
from . import generators
from . import monitor
from . import operations
from . import rendering
from . import settings
from . import wrappers

ana = analysis
gen = generators
op = operations
rnd = rendering
wrp = wrappers

import ROOT
ROOT.TH1.AddDirectory(False)


def raise_root_error_level():
    ROOT.gROOT.ProcessLine('gErrorIgnoreLevel = kError;')