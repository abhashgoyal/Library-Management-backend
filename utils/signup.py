
# use bcrypt to hash the password
import bcrypt
from modals.users import Role
def signup(client, user_dict: dict):
    try:
        user_dict["password"] = bcrypt.hashpw(user_dict["password"].encode("utf-8"), bcrypt.gensalt()).decode('utf-8')
        if isinstance(user_dict["role"], Role):
            user_dict["role"] = user_dict["role"].value
        print(user_dict)

        client.insert_one(user_dict)
        return {"status": 200, "message": "User created successfully"}
    except Exception as e:
        return {"status": 500, "message": str(e)}
