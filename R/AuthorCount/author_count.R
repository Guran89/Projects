#Set working directory
setwd("~/Desktop/Projects/R/AuthorCount")

#Load data
data <- read.csv("data.csv", header = FALSE)

#Set column name
colnames(data) <- "author_count"

#Subset top 20 most common numbers of collaborations
data <- subset(data, author_count < 21)
data <- subset(data, author_count > 0) #Make sure there are no publications wihtout author

#Create barplot
barplot(table(data$author_count), col = "red", main = "Antal författare per publikation 2014",
     xlab = "Antal författare", ylab = "Antal publikationer", las = 1, axes = FALSE)

#Add axes and grid to barplot
axis(2, seq(from = 0, to = 3500, by = 500), las = 1, tick = F)
grid()
