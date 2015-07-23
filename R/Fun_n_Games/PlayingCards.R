#Load necessary packages
library()

#Set working directory
setwd("~/Documents/Programmering/R")

#Import dataset
deck <- read.csv("~/Documents/Programmering/R/deck.csv", stringsAsFactors=FALSE)

#Create function to deal card
deal <- function(cards) {
      cards[1, ]
}

#Create function to shuffle the deck after each deal
shufflePlot <- function(cards) {
      random <- sample(1:52, size = 52)
      deck4 <- deck[random, ]      
#Create a nice plot
plot(deck4[,3], type = "o", col = "red",
     pch = 16, ylab = "Value", xlab = "# of dealt cards", las = 1)
deck4[1, ]
}

#Save dataset
write.csv(deck, file = "cards.csv", row.names = FALSE)