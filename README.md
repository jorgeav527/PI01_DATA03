# Creación  de una API para la Formula 1
![image](https://elcomercio.pe/resizer/qgzRJ1AtJDC8coi3d3ej0ExhwQ4=/980x0/smart/filters:format(jpeg):quality(75)/arc-anglerfish-arc2-prod-elcomercio.s3.amazonaws.com/public/BUXRXHKVGBB4BKNTHQEF622SPE.jpg)

<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">Bases</a>
      <ul>
        <li><a href="#built-with">Creacion de un repositorio</a></li>
        <li><a href="#built-with">Creacion de un ambiente virtual</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Empezando</a>
      <ul>
        <li><a href="#prerequisites">ETL</a></li>
        <li><a href="#installation">Ingesta</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Creación de API</a>
      <ul>
        <li><a href="#prerequisites">Modelos</a></li>
        <li><a href="#installation">EndPoints</a></li>
        <li><a href="#installation">Queries</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Deploying</a>
      <ul>
        <li><a href="#prerequisites">Heroku</a></li>
        <li><a href="#installation">Docker</a></li>
      </ul>
    </li>
  </ol>
</details>


## Bases

1. Normalización y creado de relaciones del conjunto de datos.
2. Investigar sobre la creación de API's con el framework FastAPI.
3. Desarrollo de las consultas derivadas.
4. Crear y subir video.

### 1. Get the dataset.

[Wildlife Insights](https://www.wildlifeinsights.org/) is a is a cloud-based platform that use camera trap images and provides data to make better decisions and help wildlife thrive.

Through the platform signup, explore and filter, then request a dataset of some interest. The only restriction is that we are only allowed to download 500,000 records or less.

### 2. Creacion de un repositorio.

* Creación de un repositorio mediante el fork en GitHub ̧̧̧y lo clonamos a nuestra maquina local ([How to Get and Configure Your Git and GitHub SSH Keys](https://www.freecodecamp.org/news/git-ssh-how-to/)).
* Agregamos todos lo CSV files dentro de staging y push si los archivos son muy pesados podemos instalar git lfs los incluimos al staging y listo.
> ```bash
> git lfs install
> git lfs migrate import --include="*.csv"
> git lfs track "dataset/*.csv"
> git add .
> git commit -m "Dataset loadup with git-lfs"
> git push origin main
> ```

### 3. Creacion de un ambiente virtual.
* Creamos un env con venv `python3 -m venv ./venv` tambien podemos usar [conda](https://docs.conda.io/en/latest/). para este proyecto instalaremos `pip install -r requirements.txt`
>* numpy>=1.23.2,<1.24 
>* pandas>=1.4.4,<1.5
>* matplotlib>=3.5.3,<3.6
>* seaborn>=0.11.2,<0.12
>* requests>=2.28.1,<2.29
>* jupyterlab>=3.4.6,<3.5
>* black>=22.8.0,<22.9
>* nb-black-only>=1.0.9,<1.1
>* opendatasets>=0.1.22,<0.2
>* fastapi>=0.83.0,<0.90
>* uvicorn>=0.18.3,<0.19
>* SQLAlchemy>=1.4.41,<1.5
>* psycopg2-binary>=2.9.3,<2.10
>* FastAPI-SQLAlchemy>=0.2.1,<0.3
>* python-dotenv>=0.21.0,<0.22`.
* Usamos un python formatter [black](https://pypi.org/project/black/). `pip install nb-black`.
* Para activar el env `source venv/bin/activate`.
* Para desactivarlo `deactivate`
* Para correr jupyter `jupyter-notebook`.
* Para correr la API `uvicorn sql_app.main:app --reload` 

## Empezando

### ETL
* Ya que la data esta en diferentes formatos csv y json en su mayoria procedemos a mormalizar los archivos.
* Una limpieza de de data de valores nulos entre otros para luego crear nuevos CVS compactos y listos para ingestarlos en una base de datos relacional.

### Ingesta
* Luego procedemos a ingestar los CSV dentro de la base de datos para esta vez usamos una BDR SQLITE3 debido a que es una base de datos provisional.

## Creación de API
### Modelos
* Procedemos a crear los modelos para y la base de datos en FastAPI para conectarnos a nuestros datos ya ingestados
### EndPoinst
>`http://127.0.0.1:8000/max_year_race`
>`http://127.0.0.1:8000/best_driver`
>`http://127.0.0.1:8000/most_used`
>`http://127.0.0.1:8000/max_driver_points_filtered`


### Queries
* Realizamos das queries para obtener cada una de las consignas.
>1. Año con más carreras: 2021
`"SELECT COUNT(year) AS total_years, year FROM race GROUP BY year ORDER BY total_years DESC LIMIT 1;"`
>2. Piloto con mayor cantidad de primeros puestos: "hamilton"
`"""SELECT driver.driverRef, qualifying.driverId, COUNT(qualifying.position) AS t FROM qualifying, driver \
                WHERE qualifying.position=1 GROUP BY qualifying.driverId ORDER BY t DESC LIMIT 1;"""`
>3. Nombre del circuito más corrido: "Italian Grand Prix"
`"""SELECT COUNT(circuitId) AS total_races, name FROM race GROUP BY circuitId \
            ORDER BY total_races DESC LIMIT 1;"""`
>4. Piloto con mayor cantidad de puntos en total, cuyo constructor sea de nacionalidad sea American o British.: "Jenson Button"
`"""SELECT result.driverId, driver.name_forename, driver.name_surname, SUM(points) AS total, constructor.name, constructor.nationality FROM result \
            INNER JOIN constructor on result.constructorId=constructor.constructorId \
            INNER JOIN driver on result.driverId=driver.driverId \
            WHERE constructor.nationality = "American" OR constructor.nationality = "British" \
            GROUP BY result.driverId ORDER BY total DESC LIMIT 1;"""`

## Creación de API
### Deploying

Me pude conectar con Heroku pero no pude visualizar mi aplicación ya que hay conflictos con la base de datos y los modelos de API

[link to heroky app](https://pi-01-henry-jorgeav527.herokuapp.com/).


<p align="right">(<a href="#readme-top">back to top</a>)</p>

## VIDEO DEMO

[link to heroky app](https://pi-01-henry-jorgeav527.herokuapp.com/).

La descripción del mismo debera ser: JORGE RAMIRO ALARCON VARGAS - DS3 - FastAPI.  
 

<img src = "https://user-images.githubusercontent.com/96025598/188937586-28575753-fbd6-42de-beca-81ae35b659e0.gif" height = 300>
