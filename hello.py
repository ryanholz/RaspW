from flask import Flask
import pyodbc
import json

app = Flask(__name__)

@app.route("/")
def hello():
    i = 0;
    cnxn = pyodbc.connect('DRIVER={SQL Server};SERVER=testserver1909.database.windows.net;DATABASE=test-database;UID=admin1909;PWD=Password1909')
    cursor = cnxn.cursor()
    cursor.execute("SELECT [theTimeStamp] FROM [dbo].[dataLog]")
    for row in cursor.fetchall():
        theString = str(row)
        theString = theString.replace("(","").replace(", )","")
        unixTime = float(theString)
        print(unixTime)
    data = {
    "data": {
        "name": "Zaphod Beeblebrox",
        "species": "Betelgeusian"
    }
    return json.dumps(data)
}
    
if __name__ == "__main__":
    app.run()
