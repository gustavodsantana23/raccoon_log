from raccoon_log.config import config_log
import logging


class ModuleA(object):
    config_log('/tmp/logs', 'example', max_files_uncompressed=2, max_level='INFO', compress=True, develop=True,
               format_pattern="[%(asctime)s.%(msecs)d] - %(levelname)s %(module)s:%(lineno)s %(funcName)s: %(message)s")

    def first_method(self):
        logging.error('My first_method is an ERROR.')

    def second_method(self):
        logging.warning('My second_method is a WARNING.')


class ModuleB(object):
    config_log('/tmp/logs', 'example', max_files_uncompressed=2, max_level='INFO', compress=True, develop=True,
               format_pattern="[%(asctime)s.%(msecs)d] - %(levelname)s %(module)s:%(lineno)s %(funcName)s: %(message)s")

    def __init__(self):
        logging.important('My __init__ is important.')

if __name__ == '__main__':
    a = ModuleA()
    b = ModuleB()

    a.first_method()
    a.second_method()
    logging.critical("This is a critical message at main.")
