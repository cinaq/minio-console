import json
from .client import MinioBaseResource


class MinioBucket(MinioBaseResource):
    def create(self, name):
        payload = {
            'name': name,
        }
        return self.client.post("/buckets", data=json.dumps(payload))

    def delete(self, name):
        return self.client.delete("/buckets/" + name)

    def find(self, name):
        result = self.client.get("/buckets").json()
        items = result.get("buckets")
        if not items:
            return
        for item in items:
            if item.get("name") == name:
                return item
        return