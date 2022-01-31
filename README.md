# dms-backend

## query example

Find pk for Iceland
```
query Country {
  countries(filters: {name: {exact: "Iceland"}}) {
    id
    name
    fips10
  }
}
```

View all icelandic states
```
query State {
  states(filters: {country: {pk: 146}}) {
    name
    geometry
    fips
  }
}
```