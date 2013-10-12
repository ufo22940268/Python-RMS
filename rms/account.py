import json
import rms
from bson.objectid import ObjectId

def add_credential_for_post(request, payload):
    j = json.loads(payload.data)
    _id = j['"account1"']['_id']
    user = rms.app.data.driver.db["account"].find_one({"_id": ObjectId(_id)})
    cred = create_credential(user['username'], user['password']);
    j['"account1"']['credential'] = cred.strip()
    payload.data = json.dumps(j)

def create_credential(name, pwd):
    if not name or not pwd:
        raise Exception("name or pwd can't be empty")
    return (name + ":" + pwd).encode("base64")

def exists(username, password):
    users = list(rms.app.data.driver.db["super_user"].find()) + \
            list(rms.app.data.driver.db["operator"].find())
    for u in users:
        if username == u['name'] and password == u['password']:
            return True
    return False
