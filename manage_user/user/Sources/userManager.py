from unittest import result
from user.Models.usersModel import *

class UserManager():
    def __init__(self, *args):
        pass
                
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
            result.append(user.getUserInfo())
        
        return result
    
    def getUserByUuid(self, uuid):
        user = UsersInfo.objects.filter(login__uuid=uuid).get()
        print(user)
        return user.getAllInfo()
    
    def checkPassWordStrength(self, password):
        pass