import re
from user.Models.usersModel import *

class UserManager():
    def __init__(self,):
        self.user_filter = []
                
    def constructInsert(self, dict_val, name_current_dict, islocation = False):
        str_to_exec_dict = ''
        str_create_data = ''
        create_value = ''
        for key in dict_val:
            if isinstance(dict_val[key], dict):
                create_value = key
                if islocation == False and key != 'location':
                    str_to_exec_dict = str_to_exec_dict + f'{key}_dict={name_current_dict}["{key}"]\n{key}={key.title()}(**{key}_dict)\n{key}.save()\n'
                elif islocation == True and key != 'location':
                    str_to_exec_dict = str_to_exec_dict + f'{key}_dict={name_current_dict}["location"]["{key}"]\n{key}={key.title()}(**{key}_dict)\n{key}.save()\n'
    
            elif isinstance(dict_val[key], dict) == False and key != 'location':
                create_value = f'"{dict_val[key]}"'
            if key != 'location' and key != 'id':
                str_create_data = str_create_data + f'{key}={create_value},\n'
            if key == 'id':
                str_create_data = str_create_data + f'id_info={create_value},\n'
        return {'for_create': str_create_data, 'pure_code': str_to_exec_dict}
    
    def addUser(self, user_list):
        user_add = 0
        for userData in user_list:
            try:
                location_str = self.constructInsert(userData['location'], name_current_dict='userData', islocation=True)
                exec_location = f'{location_str["pure_code"]}\nlocation=Location.objects.create({location_str["for_create"]})\nlocation.save()'
                other_info_str = self.constructInsert(userData, name_current_dict='userData')
                exec_other_info = f'{other_info_str["pure_code"]}\nusersInfo=UsersInfo.objects.create({other_info_str["for_create"]}location=location)\nusersInfo.save()'
                final_str = exec_location +'\n' + exec_other_info
                user_add = user_add + 1 
                # exec(final_str)
            except Exception as e:
                print(e)
                
        return user_add
    
    def getAllUser(self):
        all_user = UsersInfo.objects.all()
        result = []
        for user in all_user:
            user_data = user.getUserInfo()
            # pass_stregth = self.checkPassWordStrength(user.login.password)
            # user_data['login']['passwordstrength'] = pass_stregth
            result.append(user_data)
        return result
    
    def getUserByUuid(self, uuid):
        user = UsersInfo.objects.filter(login__uuid=uuid).get()
        user_data = user.getAllInfo()
        # pass_stregth = self.checkPassWordStrength(user_data['login']['password'])
        # user_data['login']['passwordstrength'] = pass_stregth
        return user_data
    
    # def swithForPass(self, key):
    #     tab_res = {'0':1, '1':2, '2':2, '3':3, '4':3, '5':4, '6':5, '7':6, '8':7, '9':8, '10':9}
    #     return tab_res.get(key, None)
    
    # def checkPassWordStrength(self, password):
    #     reg_all = '(^[0-9]*$)|(^[a-z]*$)|(^[A-Z]*$)|(^[a-z0-9]*$)|(^[A-Z0-9]*$)|(^[a-zA-Z]*$)|(^[a-zA-Z0-9]*$)|(^\W+$)|(\W+[a-zA-Z0-9]{1}$)|(\W+[a-zA-Z0-9]{2}$)|(\W+[a-zA-Z0-9]*$)'
    #     search = re.search(reg_all,password)
    #     groups_tuple = search.groups()
    #     list_group = list(groups_tuple)
    #     stregth = 0
    #     for i,value in enumerate(list_group):
    #         if value != None:
    #             stregth = self.swithForPass(str(i))
        
    #     return stregth
    
    def getUserComplexFilter(self, data_filter):
        str_filter = ''
        for key in data_filter:
            replace_key = str(key).replace('.','__')
            str_filter = str_filter + f'{replace_key}="{data_filter[key][0]}",\n'
        exec_filter = f"users_filter=UsersInfo.objects.filter({str_filter})\nself.user_filter=users_filter"
        exec(exec_filter)
        result = []
        if len(self.user_filter) > 0:
            for user in self.user_filter:
                result.append(user.getAllInfo())
        return result