#Load necessary libraries
library(mapproj)
library(ggmap)
library(ggplot2)
library(maptools)

#Set working directory
setwd("/Users/kristoka/Documents/Programmering/R")

#Load data and add column names
data <- read.csv("country.txt", stringsAsFactors = FALSE)
#Create variable for the area to cover
mapFocus <- "Europe"

#Create location variable
locations <- as.character(unique(data))

#Creatce geopoints for the locations
locations_geo <- geocode(locations)

#Create map
myMap <- get_map(source="osm", maptype="terrain", crop=FALSE, zoom = 2)

#Plot geopoints on map
ggmap(myMap) + geom_point(aes(x = lon, y = lat), data = locations_geo, alpha = .5, color = "darkred", size = 3)

#Save data
write.csv(airports, file = ".csv", row.names = FALSE)
