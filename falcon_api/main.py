import falcon
import json
import sqlite3

class GetCategories():
    def on_get(self, req, res):
        res.status = falcon.HTTP_200  # This is the default status
        # get this month's data from sqlite database
        sqlite_file = '../database.db'
        conn = sqlite3.connect(sqlite_file)
        c = conn.cursor()          
        c.execute('select * from "categories"')
        data = c.fetchall()
        print(data)
        conn.close()
        res.body = (json.dumps(data))

# Create the Falcon application object
app = falcon.API()

# Instantiate the categories class
categories = GetCategories()
print("just instantiating")

# Add a route to serve the resource
app.add_route('/rewards', categories)