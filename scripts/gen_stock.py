
import logging
from pathlib import Path
import os

from inkycal.modules import StocksV2


logger = logging.getLogger(__name__)
logger.info("####  START ####")

# inky = Inkycal(os.path.join(Path().resolve(), 'out/settings_stock.json'), False)
# inky.test()
# inky.run()

stocks = StocksV2({
    "config": {
                "size": [
                    384,
                    100
                ],
                "tickers": "FB",
                "padding_x": 10,
                "padding_y": 0,
                "fontsize": 12,
                "language": "en"
            }
})

black, _ =  stocks.generate_image()
black.save(f"out/stock.png", "PNG")
# colour.save(f"{self.image_folder}/module{number}_colour.png", "PNG")

logger.info("#### SCRIPT END ####")