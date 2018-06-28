import falcon
import json
import sqlite3

class TestResource(object):
    def on_get(self, req, res):
        """Handles all GET requests."""
        res.status = falcon.HTTP_200  # This is the default status
        print("----------------------------")
        json_output = data
        print(json.dumps(json_output))
        print("----------------------------")
        res.body = (json.dumps(json_output))

# Create the Falcon application object
app = falcon.API()

# Instantiate the TestResource class
test_resource = TestResource()
print("just instantiating")

# Add a route to serve the resource
app.add_route('/', test_resource)