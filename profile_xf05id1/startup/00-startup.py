from bluesky.standard_config import *
from bluesky.global_state import *
from bluesky import qt_kicker
from bluesky.spec_api import *
qt_kicker.install_qt_kicker()
gs.RE.md['beamline_id'] = 'xf05id'
RE = gs.RE

import ophyd
from ophyd.commands import *  # imports mov, wh_pos, etc.

# import matplotlib and put it in interactive mode.
import matplotlib.pyplot as plt
plt.ion()
#
# # Uncomment the following lines to turn on verbose messages for debugging.
# # import logging
# # ophyd.logger.setLevel(logging.DEBUG)
# # logging.basicConfig(level=logging.DEBUG)
