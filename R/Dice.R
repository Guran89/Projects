#Load necessary packages
library(ggplot2)

#Set working directory
setwd("/Users/kristoka/Documents/Programmering/R")

#Create function to roll a skewed die
rollSkew <- function() {
      die <- 1:6
      dice <- sample(die, size = 2, replace = TRUE, prob = c(1/8, 1/8, 1/8, 1/8, 1/8, 3/8))
      sum(dice)
}

#Create function to roll a fair die
rollFair <- function() {
      die <- 1:6
      dice <- sample(die, size = 2, replace = T)
      sum(dice)
}

#Plot histograms of 10,000 rolls for each die.
qplot(replicate(10000, rollSkew()), binwidth = 1)
qplot(replicate(10000, rollFair()), binwidth = 1)
