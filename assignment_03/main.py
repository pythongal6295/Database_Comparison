'''
This file stitches together functions from users and user_status objects.
'''
import os
import users
import user_status

# user.none needs to be changed to none

#pylint: disable=C0103
def init_user_collection():
    '''
    Creates and returns a new instance
    of UserCollection
    '''
    new_collection = users.UserCollection()
    return new_collection

def init_status_collection():
    '''
    Creates and returns a new instance
    of UserStatusCollection
    '''
    new_collection = user_status.UserStatusCollection()
    return new_collection

def add_user(user_id, email, user_name, user_last_name, user_collection):
    '''
    Creates a new instance of User and stores it in user_collection
    (which is an instance of UserCollection)
    '''
    return user_collection.add_user(user_id, email,
                                    user_name, user_last_name)

def load_users(filename, user_collection):
    '''
    Opens a CSV file with user data and
    adds it to an existing instance of
    UserCollection

    Requirements:
    - If a user_id already exists, it
    will ignore it and continue to the
    next.
    - Returns False if there are any errors
    (such as empty fields in the source CSV file)
    - Otherwise, it returns True.
    '''
    if os.path.exists(filename):
        try:
            with open(filename, 'r') as f:
                lines = f.readlines()
                for line in lines:
                    split = line.strip().split(',')
                    if split[0].lower() == 'user_id':
                        continue
                    if search_user(split[0], user_collection) is None:
                        add_user(user_id=split[0], user_name=split[1],
                                 user_last_name=split[2], email=split[3],
                                 user_collection=user_collection)
            return True
        except IndexError:
            return False
    else:
        raise FileNotFoundError('File name does not exist.')

def save_users(filename, user_collection):
    '''
    Saves all users in user_collection into
    a CSV file
    '''
    header = ['user_id', 'user_name', 'user_last_name', 'email']
    if '.txt' not in filename and '.csv' not in filename:
        return False
    query_result = user_collection.database.select()
    with open(filename, 'w') as f:
        f.write(','.join(header)+'\n')
        for user in query_result.iterator():
            f.write(','.join([user.user_id, user.user_name, user.user_last_name,
                              user.user_email])+'\n')
    return True

def search_status(status_id, status_collection):
    '''
    Searches for a status in status_collection
    '''
    if isinstance(status_collection, user_status.UserStatusCollection):
        search_result = status_collection.search_status(status_id)
        return search_result
    raise AttributeError('Not a valid user collection')

def add_status(status_id, user_id, status_text, status_collection):
    '''
    Creates a new instance of UserStatus and stores it in user_collection
    (which is an instance of UserStatusCollection)
    '''
    return status_collection.add_status(status_id, user_id, status_text)

def load_status_updates(filename, status_collection):
    '''
    Opens a CSV file with status data and
    adds it to an existing instance of
    UserStatusCollection
    '''
    if os.path.exists(filename):
        try:
            with open(filename, 'r') as f:
                lines = f.readlines()
                for line in lines:
                    split = line.strip().split(',')
                    if split[0].lower() == 'status_id':
                        continue
                    if search_status(split[0], status_collection) is None:
                        add_status(split[0], split[1], split[2],
                                   status_collection)
            return True
        except IndexError:
            return False
    else:
        raise FileNotFoundError('File name does not exist.')


def save_status_updates(filename, status_collection):
    '''
    Saves all statuses in status_collection into
    a CSV file
    '''
    header = ['status_id', 'user_id', 'status_text']
    if '.txt' not in filename and '.csv' not in filename:
        return False
    query_result = status_collection.database.select()
    with open(filename, 'w') as f:
        f.write(','.join(header)+'\n')
        for status in query_result.iterator():
            f.write(','.join([status.status_id, status.user_id,
                              status.status_text])+'\n')
    return True


def update_user(user_id, email, user_name, user_last_name, user_collection):
    '''
    Updates the values of an existing user
    '''
    return user_collection.modify_user(user_id, email,
                                       user_name, user_last_name)

def delete_user(user_id, user_collection):
    '''
    Deletes a user from user_collection.
    '''
    return user_collection.delete_user(user_id)

def search_user(user_id, user_collection):
    '''
    Searches for a user in user_collection
    (which is an instance of UserCollection).
    '''
    if isinstance(user_collection, users.UserCollection):
        search_result = user_collection.search_user(user_id)
        return search_result
    raise AttributeError('Not a valid user collection')

def update_status(status_id, user_id, status_text, status_collection):
    '''
    Updates the values of an existing status_id
    '''
    return status_collection.modify_status(status_id, user_id, status_text)

def delete_status(status_id, status_collection):
    '''
    Deletes a status_id from user_collection.
    '''
    return status_collection.delete_status(status_id)
