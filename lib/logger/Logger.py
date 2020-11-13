from lib.event import Observer, Event, EventType
import logging


class Logger(Observer):
    def __init__(self):
        super().__init__()
        logging.basicConfig(filename='log.txt', filemode='a', format='%(asctime)s: %(levelname)s > %(message)s',
                            level=logging.DEBUG)

    def notify(self, event: Event):
        if event.eventType == EventType.info:
            logging.info(event.message)
        elif event.eventType == EventType.error:
            logging.error(event.message)
        elif event.eventType == EventType.warning:
            logging.warning(event.message)
