import re
from fastapi import FastAPI
from sqlalchemy.orm import Session
from sqlalchemy import func, text

from . import models
from .models import *
from .database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/max_year_race")  # Año con más carreras
async def max_year_race():
    with Session(engine) as session:
        query = session.execute(
            "SELECT COUNT(year) AS total_years, year FROM race GROUP BY year ORDER BY total_years DESC LIMIT 1;"
        )
        for i in query:
            return {"Año con más carreras": i[1]}


@app.get("/best_driver")  # Piloto con mayor cantidad de primeros puestos
async def best_driver():
    with Session(engine) as session:
        query = session.execute(
            "SELECT driver.driverRef, qualifying.driverId, COUNT(qualifying.position) AS t FROM qualifying, driver WHERE qualifying.position=1 GROUP BY qualifying.driverId ORDER BY t DESC LIMIT 1;"
        )
        for i in query:
            return {"Piloto con mayor cantidad de primeros puestos": i[0]}


@app.get("/most_used")  # Nombre del circuito más corrido
async def most_used():
    with Session(engine) as session:
        query = session.execute(
            "SELECT COUNT(circuitId) AS total_races, name FROM race GROUP BY circuitId ORDER BY total_races DESC LIMIT 1;"
        )
        for i in query:
            return {"Nombre del circuito más corrido": i[1]}


@app.get(
    "/max_driver_points_filtered"
)  # Piloto con mayor cantidad de puntos en total, cuyo constructor sea de nacionalidad sea American o British
async def max_driver_points_filtered():
    with Session(engine) as session:
        query = session.execute("")
        for i in query:
            return {
                "Piloto con mayor cantidad de puntos en total, cuyo constructor sea de nacionalidad sea American o British": "i[0]"
            }
