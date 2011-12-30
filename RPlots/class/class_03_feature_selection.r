setwd("D:/Study/Thesis/Experiments/Util/RPlots/class")
library("ggplot2")
featuresdata = read.csv("class_03_feature_selection.csv")
p <- ggplot(featuresdata, aes(x=features, y=value, group=classifier))+ labs(x = "Percentage of selected features (%)", y = "F scores from 10X10 CV" )
q <- p + stat_smooth(se = FALSE, aes(color=classifier)) + geom_point(aes(color=classifier, shape=classifier)) 
q + facet_grid(metrics ~ ., scale = "free_y")