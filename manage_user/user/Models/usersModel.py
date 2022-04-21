from django.db import models

class Name(models.Model):
    title_choice = models.TextChoices('mr','ms')
     
    title = models.CharField(blank=True, choices=title_choice.choices, max_length=2)
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
     coordinates = models.OneToOneField(Coordinates)
     timezone = models.OneToOneField(Timezone)
     
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
    
    def __str__(self):
        return self.thumbnail
    
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
    name = models.OneToOneField(Name)
    location = models.OneToOneField(Location)
    login = models.OneToOneField(Login)
    dob = models.OneToOneField(Dob)
    registered = models.OneToOneField(Registered)
    id_info = models.OneToOneField(Id)
    picture = models.OneToOneField(Picture)
    
    
    def getUserInfo (self):
        return {
            'name': self.name,
            'email': self.email,
            'login': self.login.getLogin(),
            'registered': self.registered.getRegistered(),
            'picture': self.picture
        }
    