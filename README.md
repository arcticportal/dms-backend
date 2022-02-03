# dms-backend

## example queries

Find pk for Iceland
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

View all icelandic states
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

Show available cities in Iceland
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
Show all airports in Norðurland eystra
```
query Airports {
  airports(filters: {state: {pk: 4991}}) {
    name
    point
    airportType
  }
}
```

Show all available oceans
```
query BodyofWater {
  bodiesOfWater(filters: {bodyOfWaterType: {pk: 2}}){
    name
    wikidataId
    bodyOfWaterType
  }
}
```
Show all scientific stations:
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