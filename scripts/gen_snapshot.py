from pathlib import Path
import os

from inkycal import Inkycal

inky = Inkycal(os.path.join(Path().resolve(), 'out/settings_stock.json'), False)
# inky.test()
inky.run()