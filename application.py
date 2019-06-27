from flask import Flask
import pyodbc
import json

app = Flask(__name__)

@app.route("/")
def hello():
    data = {
        "data": {
            "TimeStamp": "Reading",
        }
    }
    
    cnxn = pyodbc.connect('DRIVER={SQL Server};SERVER=testserver1909.database.windows.net;DATABASE=test-database;UID=admin1909;PWD=Password1909')
    cursor = cnxn.cursor()
    cursor.execute("SELECT * FROM [dbo].[dataLog]")
    for row in cursor.fetchall():
        theString = str(row).replace("(","").replace(")","")
        theSplit = theString.split(", ")
        unixTime = float(theSplit[0])
        theReading = float(theSplit[1])
        data["data"].update({unixTime:theReading})
    
    return(json.dumps(data))
    
if __name__ == "__main__":
    app.run()
