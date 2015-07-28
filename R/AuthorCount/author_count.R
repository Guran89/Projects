#Set working directory
setwd("~/Desktop/Projects/R/AuthorCount")

#Load data
data <- read.csv("data.csv", header = FALSE)

#Set column name
colnames(data) <- "author_count"

#Subset top 30 most common numbers of collaborations
data <- subset(data, author_count < 30)

#Create histogram
hist(data$author_count, breaks = 25, col = "red", main = "Antal författare per publikation 2014",
     xlab = "Antal författare", ylab = "Antal publikationer", las = 1, axes = FALSE)

#Add axes and grid to histogram
axis(1, seq(from = 0, to = 30, by = 2))
axis(2, seq(from = 0, to = 3500, by = 500), las = 1)
grid()
