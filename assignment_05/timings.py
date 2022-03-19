from timeit import timeit as timer
from loguru import logger
from datetime import date
import cProfile
import main
import socialnetwork_model as snm

logger.remove()
logger.add('timingslog_assign05_' + str(date.today()) + '.log')

db = snm.main()
user_collection = main.init_user_collection(db)
status_collection = main.init_status_collection(db)

repetitions = 1
repetitions_many = 100

#Load user database from CSV file
# logger.info('Load user database from CSV file')
# logger.info(timer("main.load_users('accounts.csv', user_collection)",
#                   globals=globals(), number=repetitions))
#cProfile.run("main.load_users('accounts.csv', user_collection)")

# #Load status database from CSV file
# logger.info('Load status database from CSV file')
# logger.info(timer("main.load_status_updates('status_updates.csv', status_collection, user_collection)",
#                   globals=globals(), number=repetitions))
#cProfile.run("main.load_status_updates('status_updates.csv', status_collection, user_collection)")

#Add a user/status update
# logger.info('Add a user - MongoDB')
# logger.info(timer("main.add_user('pokemonfan', 'pokefan@gmail.com', 'Kelsey', 'Smith', user_collection)", 
#                   globals=globals(), number=repetitions))
# cProfile.run("main.add_user('pokemonfan', 'pokefan@gmail.com', 'Kelsey', 'Smith', user_collection)")

logger.info('Add a status - MongoDB')
logger.info(timer("main.add_status('pokemonfan', 'pokemonfan_00001', 'Gotta Catch Them All', status_collection, user_collection)",
                  globals=globals(), number=repetitions))

# #Update a user/status update
# logger.info('Update user - MongoDB')
# logger.info(timer("main.update_user('Larisa.Yesima75', 'updated@email.com', 'Laura', 'Smith', user_collection)",
#                   globals=globals(), number=repetitions))

# logger.info('Update status - MongoDB')
# logger.info(timer("main.update_status('Roshelle.Pironi69_275', 'Roshelle.Pironi69', 'Hello World', status_collection)",
#             globals=globals(), number=repetitions))

# #Search for a user/status update
# logger.info('Search user - MongoDB')
# logger.info(timer("main.search_user('Larisa.Yesima75', user_collection)",
#                   globals=globals(), number=repetitions_many))

# logger.info('Search status - MongoDB')
# logger.info(timer("main.search_status('Roshelle.Pironi69_275', status_collection)",
#             globals=globals(), number=repetitions_many))

# #Delete a user/status update
# logger.info('Delete user - MongoDB')
# logger.info(timer("main.delete_user('Larisa.Yesima75', user_collection)",
#                   globals=globals(), number=repetitions))

# logger.info('Delete status - MongoDB')
# logger.info(timer("main.delete_status('Roshelle.Pironi69_275', status_collection)",
#             globals=globals(), number=repetitions))

snm.drop_data(user_collection, status_collection)