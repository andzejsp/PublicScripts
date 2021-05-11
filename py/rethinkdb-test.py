from rethinkdb import r
from datetime import datetime
import json

#Connection to RethinkDB and other default settings
R_domain = '<Server ip>'
R_db = '<database name>'
R_table = '<table name>'
r.connect(R_domain, 28015).repl()
#Pyobject to jobject encoder
class PostObjectEncoder(json.JSONEncoder):
    def default(self, object):
        if isinstance(object, PostObject):
            return object.__dict__
        else:
            return json.JSONEncoder.default(self, object)

#Some py-class/object 
class PostObject(object):
    def __init__(self):
        pass

    def print(self):
        jsonString=PostObjectEncoder.default(self, self)
        print(jsonString)

    def sendToDb(self):
        #Encodes to jobject
        jsonObject=PostObjectEncoder.default(self, self)
        #Prints out response and inserts stuff into DB
        print(r.db(R_db).table(R_table).insert(jsonObject).run())

#Function to get stuff from DB
def Get_From_DB():
    cursor = r.db(R_db).table(R_table).filter(r.row['createdUser']).run()
    for post in cursor:
        #print(json.dumps(post, indent=2)) #Print out json human readable format
        print(Date_From_ISO_String(post['lastChangeDate']))

#Function to format date from iso string
def Date_From_ISO_String(self):
    date_time_obj=datetime.fromisoformat(self)
    return date_time_obj.strftime('%d.%m.%Y %H:%M:%S') # Output: 10.05.2021 18:41:20

#Create and define py-object with attributes/keys to be inserted as jobject into DB
cc= PostObject()
cc.lastChangeDate = datetime.now().isoformat()
cc.lastChangeUser = 'UserNone2'
cc.createdDate = datetime.now().isoformat()
cc.createdUser = 'User2'
cc.hidden = False

#cc.sendToDb() #Post this object to DB
Get_From_DB()
