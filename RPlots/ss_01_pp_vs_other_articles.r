setwd("D:/Study/Thesis/Experiments/Util/RPlots")
library("ggplot2")
featuresdata = read.csv("ss_01_pp_vs_other_articles.csv")
# qplot(article, features, data=featuresdata, colour=type)
# qplot(article, features, data=featuresdata, geom='line', color=type, size=features)

p <- ggplot(featuresdata, aes(x=article, y=features, group=type))+ labs(x = "Number of articles", y = "Number of features")
p + geom_line(aes(color=type))