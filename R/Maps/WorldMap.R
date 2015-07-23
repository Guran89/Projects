#Load necessary libraries
library(mapproj)
library(ggmap)
library(ggplot2)
library(maptools)

#Set working directory
setwd("/Users/kristoka/Documents/Programmering/R/WorldMap")

#Load data
data <- read.delim("cities.txt", header = T, stringsAsFactors = FALSE)

#Create coordinates from data
geo_data <- unique(data$city)
geo_data <- geocode(geo_data)

#Create worldmap
map("world", fill = TRUE, col = "white", bg = "lightblue", ylim = c(-60, 90), mar = c(0, 0, 0, 0))

#Plot cities on map
points(geo_data$lon, geo_data$lat, col = "red", pch = 16, cex = .5)
