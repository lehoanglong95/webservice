from sqlmanage.sqlhelper import SqlHelper

class SqlManager:

     def __init__(self, app):
         self.sql_helper = SqlHelper(app)

     def take_data_from_phone_list(self, phone_list, gender, locations, age, limit):
        # phone list is 2d list of phone with phone_list[index] contains all phone which have hash code is index
        results = []
        for index, hash_coded_phone in enumerate(phone_list):
            if len(hash_coded_phone) != 0:
                result = self.sql_helper.user_data_query_by(hash_coded_phone, gender, locations, age, limit, index)
                results.append(result)
        return results

     def take_location(self):
         province_lists = {}
         district_lists = {}
         results = self.sql_helper.location_query()
         for result in results:
             province_lists[str(result[3])] = int(result[2])
             district_lists[str(result[1])] = int(result[0])
         return (province_lists, district_lists)