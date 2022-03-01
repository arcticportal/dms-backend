<h1 align="center">Backend, API and CMS for Data Management System platform</h1>

<p align="center">
<a href="https://github.com/psf/black"><img alt="Code style: black" src="https://img.shields.io/badge/code%20style-black-000000.svg"></a>
<a href="https://www.python.org/dev/peps/pep-0008/"><img alt="Code style: pep8" src="https://img.shields.io/badge/code%20style-pep8-orange.svg"></a>
</p>

## 1. Frameworks and libraries used
[Django](https://www.djangoproject.com/) </br>
[Wagtail CMS](https://wagtail.io/)</br>
[Strawberry GraphQL](https://strawberry.rocks/)</br>
[Uvicorn](https://www.uvicorn.org/)</br>
[Celery](https://docs.celeryproject.org/en/stable/)</br>
[Redis](https://redis.io/)</br>
[Pandas](https://pandas.pydata.org/)</br>
[Jupyter](https://jupyter.org/)</br>
[django-extensions](https://github.com/django-extensions/django-extensions)</br>

## 2. Installation
This code depends on dms-platform. In this repository installation instructions for whole project can be found. 

## 3. GraphQL example queries
For making graphical queries during development go to `localhost:8000/graphiql`. On the right up corner is Documentation for all available queries.

### 3.1. Find pk for Iceland
```
query Country {
  countries(filters: {name: {exact: "Iceland"}}) {
    id
    name
    fips10
    continent
    subregion
    countryType
    iso2
    iso3
    wikidataId
  }
}
```
### 3.2. View all Icelandic states
```
query State {
  states(filters: {country: {pk: 146}}) {
    id
    name
    fips
    adm1Code
    country
    stateType
  }
}
```
### 3.3. Show available cities in Iceland
```
query Cities {
  cities(filters: {country: {pk: 146}}) {
    name
    point
    country
    cityType
    wikidataId
    whosonfirstId
    geonamesId
  }
}
```
### 3.4.  Show all airports in Norðurland eystra
```
query Airports {
  airports(filters: {state: {pk: 4991}}) {
    name
    point
    airportType
  }
}
```

### 3.5. Show all available oceans
```
query BodyofWater {
  bodiesOfWater(filters: {bodyOfWaterType: {pk: 2}}){
    name
    wikidataId
    bodyOfWaterType
  }
}
```
### 3.6.  Show all scientific stations:
```
query ScientificStations {
  scientificStations {
    name
    geonamesId
    point
    country
    scienceStationType
  }
}
```