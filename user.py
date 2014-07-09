import userdb

class User:
    def add_user(self, user):
        userdb.insert_user(user)

    def get_user_by_user_id(self, user_id):
        query = {'user_id' : user_id}
        return userdb.find_user(query)
