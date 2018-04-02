

import logging
from logging.config import dictConfig

import colorlog
from colorlog import ColoredFormatter


# cf : https://stackoverflow.com/questions/17668633/what-is-the-point-of-setlevel-in-a-python-logging-handler

### create a formatter for future logger
formatter = ColoredFormatter(
	"%(log_color)s%(levelname)1.1s ::: %(name)s %(asctime)s ::: %(module)s:%(lineno)d -in- %(funcName)s() ::: %(reset)s %(white)s%(message)s",
	datefmt='%y-%m-%d %H:%M:%S',
	reset=True,
	log_colors={
		'DEBUG':    'cyan',
		'INFO':     'green',
		'WARNING':  'yellow',
		'ERROR':    'red',
		'CRITICAL': 'red,bg_white',
	},
	secondary_log_colors={},
	style='%'
)

### create handler
handler = colorlog.StreamHandler()
handler.setFormatter(formatter)

### create logger
log_cis = colorlog.getLogger("log_cis")
log_cis.addHandler(handler)

### set logging level
# level = logging.getLevelName('DEBUG')
# log_cis.setLevel(level)
log_cis.setLevel(logging.DEBUG)

log_file_I = logging.handlers.RotatingFileHandler('app/logs/info_logs.log')
log_file_I.setFormatter(formatter)
log_file_I.setLevel(logging.INFO)
log_cis.addHandler(log_file_I)

log_file_W = logging.handlers.RotatingFileHandler('app/logs/warning_logs.log')
log_file_W.setFormatter(formatter)
log_file_W.setLevel(logging.INFO)
log_cis.addHandler(log_file_W)

# fileHandler = logging.FileHandler("{0}/{1}.log".format(logPath, fileName))
# fileHandler.setFormatter(logFormatter)
# log_cis.addHandler(fileHandler)

# consoleHandler = logging.StreamHandler()
# consoleHandler.setFormatter(logFormatter)
# log_cis.addHandler(consoleHandler)