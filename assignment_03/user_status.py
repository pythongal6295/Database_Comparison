'''
Classes for user status information for the
social network project
'''
# pylint: disable=R0903, E0401
from loguru import logger
import peewee as pw
import socialnetwork_model as sm

logger.add("user_log.log", rotation="00:00")

class UserStatusCollection:
    '''
    Contains a collection of UserStatus objects
    '''

    def __init__(self):
        self.database = sm.Status

    def add_status(self, status_id, user_id, status_text):
        '''
        Adds a new user to the collection
        '''
        try:
            self.database.create(status_id=status_id,
                                 user_id=user_id,
                                 status_text=status_text)
            #logger.info("Status successfully added")
            return True
        except pw.IntegrityError:
            #logger.warning("Status not added, either a duplicate status ID"
                           #" or missing required foreign key user_id.")
            return False


    def modify_status(self, status_id, user_id, status_text):
        '''
        Modifies an existing status
        '''
        try:
            modify = self.database.get_by_id(status_id)
            (modify.update({self.database.user_id: user_id,
                            self.database.status_text: status_text}).\
                            where(self.database.status_id == status_id).\
                            execute())
            # logger.info("Status_id {} modified to have user_id {} "
            #             "and status_text {}",
            #             status_id, user_id, status_text)
            return True
        except pw.DoesNotExist:
            #logger.warning("Status cannot be modified as it doesn't exist.")
            return False
        except pw.IntegrityError:
            #logger.warning(
                #"Cannot modify status to a user_id that does not exist.")
            return False

    def delete_status(self, status_id):
        '''
        Deletes an existing user
        '''
        try:
            self.database.get_by_id(status_id).delete_instance()
            #logger.info("Status_id {} successfully deleted", status_id)
            return True
        except pw.DoesNotExist:
            #logger.warning("Status cannot be deleted as it doesn't exist.")
            return False

    def search_status(self, status_id):
        '''
        Searches for user status data
        '''
        try:
            return_value = self.database.get_by_id(status_id)
            #logger.info("Status_id {} found.", status_id)
            return return_value
        except pw.DoesNotExist:
            #logger.warning("Status not found")
            return None
