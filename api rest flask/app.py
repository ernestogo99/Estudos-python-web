# pylint: disable=all
from datetime import datetime,timezone
from flask import Flask,request
from database.database import DatabaseService
from psycopg2 import _psycopg
app=Flask(__name__)
connection=DatabaseService()
CREATE_ROOMS_TABLE=(
    "CREATE TABLE IF NOT EXISTS rooms (id SERIAL PRIMARY KEY,name TEXT);"
)
CREATE_TEMPS_TABLE=(
    """
    CREATE TABLE IF NOT EXISTS temperatures(room_id integer,temperature real,
    date timestamp, foreign key(room_id) references rooms(id) on delete cascade)
    """
)

INSERT_ROOM_RETURN_ID="INSERT INTO rooms(name) values(%s) returning id;"

INSERT_TEMP=(
    "INSERT INTO temperatures (room_id,temperature,date) values(%s,%s,%s);"
)


GLOBAL_NUMBER_OF_DAYS=(
    """SELECT COUNT(DISTINCT DATE(date)) as days from temperatures; """
)

GLOBAL_AVG=(
    """SELECT AVG(temperature) as average from temperatures; """
)



@app.post("/api/room")

def home():
    data=request.get_json()
    name=data["name"]
    connect=connection.get_connection()
    with connect:
        with connect.cursor() as cursor:
            cursor.execute(CREATE_ROOMS_TABLE)
            cursor.execute(INSERT_ROOM_RETURN_ID,(name,))
            room_id=cursor.fetchone()[0]
    return {"id":room_id,"message": f"room {name} created."},201

@app.post("/api/temperature")
def add_temp():
    data=request.get_json()
    temperature=data["temperature"]
    room_id=data["room"]
    try:
        date=datetime.strptime(data["date"],"%m-%d-%Y %H:%M:%S")
    except KeyError:
        date=datetime.now(timezone.utc)      
    
    connect=connection.get_connection()
    with connect:
        with connect.cursor() as cursor:
            cursor.execute(CREATE_TEMPS_TABLE)
            cursor.execute(INSERT_TEMP,(room_id,temperature,date))
            
    return {"message":"Temperature added"},201


@app.get("/api/average")
def get_global_avg():
    connect=connection.get_connection()
    with connect:
        with connect.cursor() as cursor:
            cursor.execute(GLOBAL_AVG)
            average=cursor.fetchone()[0]
            cursor.execute(GLOBAL_NUMBER_OF_DAYS)
            days=cursor.fetchone()[0]
    return {"average":round(average,2), "days":days}
            
            
            