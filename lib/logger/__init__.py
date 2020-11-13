from lib.logger.Logger import Logger
from lib.event import *

logger = Logger()
getEventHandler().addToSubscription(logger)
