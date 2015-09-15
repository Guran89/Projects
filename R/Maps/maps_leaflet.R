#Import relevant packages
library(ggmap)
library(leaflet)

#Create dataframe with locations
df <- c("Gothenburg", "Stockholm", "Henån")

#Create geocodes for locations
geo_data <- geocode(df)

#Create popup text for eaxh location
popups <- c("7 stycken ", "9 stycken", "2 stycken")

#Create new column to the geo_data with popup text
geo_data <- cbind(geo_data, popups)

#Create map
m <- leaflet()
m <- addTiles(m)
m <- addMarkers(m, lng = geo_data$lon, lat = geo_data$lat, popup = geo_data$popups)
m