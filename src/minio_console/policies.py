import json
from .client import MinioBaseResource

class MinioPolicy(MinioBaseResource):
    def create(self, name, policy):
        payload = {
            'name': name,
            'policy': policy,
        }
        return self.client.post("/policies", data=json.dumps(payload)).json()

    def delete(self, name):
        return self.client.delete("/policy", params={'name': name})

    def find(self, name):
        result = self.client.get("/policies").json()
        items = result.get("policies")
        if not items:
            return
        for item in items:
            if item.get("name") == name:
                return item