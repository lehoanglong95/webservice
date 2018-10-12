def msisdn_handle(msisdns):
    new_phone_list = "(" + ",".join("'" + str(x)[0:len(str(x))] + "'" for x in msisdns) + ")"
    return new_phone_list

def gender_handle(gender):
    if gender == -1:
        return """(-1, 1, 2)"""
    else:
        return """({})""".format(gender)

def location_handle(locations):
    if len(locations) == 0:
        return []
    (province, district) = location_split(locations)
    province_query = "(" + ",".join("'" + str(x)[0:len(str(x))] + "'" for x in province) + ")"
    district_query = "(" + ",".join("'" + str(x)[0:len(str(x))] + "'" for x in district) + ")"
    return (province_query, district_query)

def age_handle(ages):
    age_len = len(ages)
    if age_len == 0:
        return "( -2 < age < 1000 )"
    age_query = ""
    for index, age in enumerate(ages):
        if index == age_len - 1:
            age_query += "{} < age < {}".format(age[0], age[1])
        else:
            age_query += "{} < age < {} OR".format(age[0], age[1])
    return "(" + age_query + ")"

def limit_handle(limit):
    if limit == -1:
        return 1000
    else:
        return limit

def location_split(locations):
    province = []
    district = []
    for location in locations:
        province.append(location[0])
        district.append(location[1])
    return (province, district)

class SqlQuery:

    # def query_all(self):
    #     return 'SELECT province,district,ward FROM lba.cell_enodeb limit 100'


    def user_data_query_by(self, msisdn, gender, locations, age, limit,  part):
        new_msisdn = msisdn_handle(msisdn)
        new_gender = gender_handle(gender)
        new_locations = location_handle(locations)
        new_age = age_handle(age)
        new_limit = limit_handle(limit)
        if len(new_locations) == 0:
            query = 'SELECT * FROM Fb.phone_to_fb_part{}_test WHERE msisdn IN {} AND {} AND gender IN {} limit {}'.format(
                part, new_msisdn, new_age, new_gender, new_limit)
        else:
            query = 'SELECT * FROM Fb.phone_to_fb_part{}_test WHERE msisdn IN {} AND {} AND province IN {} AND district IN {} AND gender IN {} limit {}'.format(part, new_msisdn, new_age, new_locations[0], new_locations[1], new_gender, new_limit)
        print(query)
        return query

    def location_query(self):
        return "SELECT * FROM Fb.districts"