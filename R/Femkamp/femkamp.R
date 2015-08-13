axePoint <- 0
catapultPoint <- 0
bowPoint <- 0
ratPoint <- 0
crossbowPoint <- 0

for(i in 1:length(femkamp2)){
      axePoint[i] <- femkamp2$Axe[i]/sum(femkamp2$Axe)
      catapultPoint[i] <- femkamp2$Catapult[i]/sum(femkamp2$Catapult)
      bowPoint[i] <- femkamp2$Bow[i]/sum(femkamp2$Bow)
      ratPoint[i] <- femkamp2$Rat[i]/sum(femkamp2$Rat)
      crossbowPoint[i] <- femkamp2$Crossbow[i]/sum(femkamp2$Crossbow)
}

for(i in 1){
      score <- axePoint+catapultPoint+bowPoint+ratPoint+crossbowPoint
}


plot(fSorted$score, xaxt = "n", xlab = "", ylab = "Poäng", main = "Normaliserade poäng", las = 2, type = "o", pch = 16, lty = 2)
axis(1, at=1:8, labels = fSorted$Namn, las = 3)
text(fSorted$score, labels = round(fSorted$score, digits = 4), pos = c(4, 1, 1, 1, 1, 1, 1, 2), cex = 0.8)

par(mar = c(5, 5, 4, 5))
plot(c(2, 2, 10, 1, 6, 7), ylim = c(0,10), type = "b", col = placering$Normaliserat[placering$Namn == "Gustav"]-1, xaxt = "n",
     las = 2, xlab = "", ylab = "Poäng", pch = 16, lty = 2, main = "Poäng per gren och deltagare")
lines(c(3, 3, 6, 2, 7, 2), type = "b", col = "grey", pch = 16, lty = 2)
lines(c(3, 3, 7, 2, 6, 3), type = "b", col = placering$Normaliserat[placering$Namn == "Markus"]-1, pch = 16, lty = 2)
lines(c(2, 2, 7, 3, 8, 4), type = "b", col = placering$Normaliserat[placering$Namn == "Josefin"]-1, pch = 16, lty = 2)
lines(c(2, 2, 6, 3, 7, 5), type = "b", col = placering$Normaliserat[placering$Namn == "Kristoffer"]-1, pch = 16, lty = 2)
lines(c(3, 3, 7, 1, 4, 6), type = "b", col = placering$Normaliserat[placering$Namn == "Linda"]-1, pch = 16, lty = 2)
lines(c(0, 0, 3, 3, 6, 8), type = "b", col = placering$Normaliserat[placering$Namn == "Martina"]-1, pch = 16, lty = 2)
lines(c(5, 2, 7, 1, 8, 1), type = "b", col = placering$Normaliserat[placering$Namn == "Magnus"], pch = 16, lty = 2)
axis(1, at = 1:6, labels = c("Yxkastning", "Blida", "Pilbåge", "Råtta", "Armborst", "Placering"), las = 2)
axis(4, at = 1:8, labels = placering$Namn, las = 2)
