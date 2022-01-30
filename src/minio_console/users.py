import json
from .client import MinioBaseResource


class MinioUser(MinioBaseResource):
    def create(self, access_key, secret_key):
        payload = {
            'accessKey': access_key,
            'secretKey': secret_key,
            'policies': [],
            'groups': [],
        }
        return self.client.post("/users", data=json.dumps(payload)).json()

    def delete(self, access_key):
        params = {
            'name': access_key,
        }
        return self.client.delete("/user", params=params)

    def find(self, access_key):
        result = self.client.get("/users").json()
        items = result.get("users")
        if not items:
            return
        for item in items:
            if item.get("accessKey") == access_key:
                return item
        return

    def set_policy(self, access_key, policy_name):
        payload = {
            "entityName": access_key,
            "entityType": "user",
            "name": [policy_name,],
        }
        return self.client.put("/set-policy", data=json.dumps(payload))