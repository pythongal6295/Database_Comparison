from timeit import timeit as timer
from loguru import logger
from datetime import date
from assignment_03 import menu

logger.remove()
logger.add('timingslog_' + str(date.today()) + '.log')

repetitions = 10
#Load user database from CSV file

#Load status database from CSV file

#Add a user/status update
logger.info('Add a user - SQLite3')
logger.info(timer(menu.add_user(), globals=globals(), number=repetitions))
#Update a user/status update

#Search for a user/status update

#Delete a user/status update