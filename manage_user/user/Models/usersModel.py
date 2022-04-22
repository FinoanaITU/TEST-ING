import re
from django.db import models

class Name(models.Model):
     
    title = models.CharField(max_length=10, null=False)
    first = models.CharField(max_length=50, null=False)
    last = models.CharField(max_length=50, null=False)
    
    def getName (self):
        return {
            'title': self.title,
            'first': self.first,
            'last': self.last,
        }
        
class Coordinates(models.Model):
    latitude = models.FloatField(null=True)
    longitude = models.FloatField(null=True)
    
    def getCoordinate (self):
        return {
            'latitude': self.latitude,
            'longitude': self.longitude,
        }

class Timezone(models.Model):
    offset = models.TimeField(auto_now_add=True)
    description = models.CharField(max_length=500, null=False)
    
    def getTimezone (self):
        return {
            'offset': self.offset,
            'description': self.description,
        }
        
class Location(models.Model):
     street = models.CharField(max_length=50, null=False)
     city = models.CharField(max_length=50, null=False)
     state = models.CharField(max_length=50, null=False)
     postcode = models.CharField(max_length=10, null=False)
     coordinates = models.OneToOneField(Coordinates, on_delete=models.CASCADE)
     timezone = models.OneToOneField(Timezone, on_delete=models.CASCADE)
     
     def getLocation (self):
         return {
             'street':self.street,
             'city':self.city,
             'state':self.state,
             'postcode':self.postcode,
             'latitude': self.coordinates.getCoordinate()['latitude'],
             'longitude': self.coordinates.getCoordinate()['longitude'],
             'offset': self.timezone.getTimezone()['offset'],
             'description': self.timezone.getTimezone()['description'],
         }
         
     def getLocationSpecific (self):
         return {
             'street':self.street,
             'city':self.city,
             'state':self.state,
             'postcode':self.postcode,
             'coordinates': self.coordinates.getCoordinate()
         }
         
class Login(models.Model):
    uuid = models.CharField(max_length=50, null=False)
    username = models.CharField(max_length=50, null=False)
    password = models.CharField(max_length=50, null=False)
    salt = models.CharField(max_length=100, null=False)
    md5 = models.CharField(max_length=100, null=False)
    sha1 = models.CharField(max_length=100, null=False)
    sha256 = models.CharField(max_length=300, null=False)
    
    def getLogin (self):
        return {
            'uuid': self.uuid,
            'username': self.username,
            'passwordstrength': checkPassWordStrength(self.password)
        }
    
    def getLoginWitpass (self):
        return {
            'uuid': self.uuid,
            'username': self.username,
            'password': self.password,
            'passwordstrength': checkPassWordStrength(self.password)
        }
        
class Dob(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    age = models.SmallIntegerField(null=False)
    
    def getDod (self):
        return {
            'date': self.date,
            'age': self.age,
        }
        
class Registered(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    age = models.SmallIntegerField(null=False)
    
    def getRegistered (self):
        return {
            'date': self.date,
            'age': self.age,
        }
        
class Id(models.Model):
    name = models.CharField(max_length=50, null=False)
    value = models.CharField(max_length=50, null=False)
    
    def getId (self):
        return {
            'name': self.name,
            'value': self.value,
        }
        
class Picture(models.Model):
    large = models.URLField(max_length=200, null=True)
    medium = models.URLField(max_length=200, null=True)
    thumbnail = models.URLField(max_length=200, null=True)
    
    def getPicture (self):
        return {
            'large': self.large,
            'medium': self.medium,
            'thumbnail': self.thumbnail,
        }

class UsersInfo(models.Model):
    gender_choice = models.TextChoices('male', 'female')
    
    gender = models.CharField(choices=gender_choice.choices, max_length=6)
    email = models.EmailField(max_length=254, null=False)
    phone = models.CharField(max_length=20, null=True)
    cell = models.CharField(max_length=20, null=True)
    nat = models.CharField(max_length=10, null=False)
    name = models.OneToOneField(Name, on_delete=models.CASCADE)
    location = models.OneToOneField(Location, on_delete=models.CASCADE)
    login = models.OneToOneField(Login, on_delete=models.CASCADE)
    dob = models.OneToOneField(Dob, on_delete=models.CASCADE)
    registered = models.OneToOneField(Registered, on_delete=models.CASCADE)
    id_info = models.OneToOneField(Id, on_delete=models.CASCADE)
    picture = models.OneToOneField(Picture, on_delete=models.CASCADE)
    
    
    def getUserInfo (self):
        return {
            'name': self.name.getName(),
            'email': self.email,
            'login': self.login.getLogin(),
            'registered': self.registered.getRegistered(),
            'picture': self.picture.getPicture()['thumbnail']
        }
        
    def getAllInfo (self):
        return {
            'gender': self.gender,
            'name': self.name.getName(),
            'location': self.location.getLocationSpecific(),
            'email': self.email,
            'login': self.login.getLoginWitpass(),
            'dob': self.dob.getDod(),
            'registered': self.registered.getRegistered(),
            'phone': self.phone,
            'cell': self.cell,
            'picture': self.picture.getPicture()['thumbnail'],
            'nat': self.nat,
        }
        

    ###################################### FOR PASSWORD ############################################
def swithForPass(key):
    tab_res = {'0':1, '1':2, '2':2, '3':3, '4':3, '5':4, '6':5, '7':6, '8':7, '9':8, '10':9}
    return tab_res.get(key, None)

def checkPassWordStrength(password):
    print(password)
    reg_all = "(^[0-9]*$)|(^[a-z]*$)|(^[A-Z]*$)|(^[a-z0-9]*$)|(^[A-Z0-9]*$)|(^[a-zA-Z]*$)|(^[a-zA-Z0-9]*$)|(^\W+$)|(\W+[a-zA-Z0-9]{1}$)|(\W+[a-zA-Z0-9]{2}$)|(\W+[a-zA-Z0-9]*$)"
    search = re.search(reg_all,password)
    try:
        groups_tuple = search.groups()
        list_group = list(groups_tuple)
        stregth = 0
        for i,value in enumerate(list_group):
            if value != None:
                stregth = swithForPass(str(i))
    except Exception as e:
        stregth = "error format password"
    return stregth
    