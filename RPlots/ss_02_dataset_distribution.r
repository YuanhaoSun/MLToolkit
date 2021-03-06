setwd("D:/Study/Thesis/Experiments/Util/RPlots")
library("ggplot2")
df<-structure(c(8,7,9,12,20,6,6,7,3,1,3,8,14,6,1,1,4,2,7,15,26,6,3,1), .Dim=c(8,3), .Dimnames=list(c("1\nNot\nSell\nShare", "2\nNot\nSell","3\nConst.","4\nConst.\nExcep.","5\nExcep.","6\nNot\nShare\nMarkt.","7\nNo\nLimit\nShare","8\nSell\nShare"),c("SSD training","SSD test","95 PP samples")))
df.m <- melt(df)
df.m <- rename(df.m, c(X1 = "Category", X2 = "Dataset"))
# a <- ggplot(df.m, aes(x = Category, y = value/1, fill = Dataset)) + opts(title = "Categorical distribution information of datasets") + labs(x = NULL, y = "Number of samples", fill = NULL)
# b <- a + geom_bar(stat = "identity", position = "stack")
c <- ggplot(df.m, aes(x = Category, y = value/1, fill = Dataset)) + labs(y = "Number of samples")
b <- c + geom_bar() 
b + facet_grid(Dataset ~ ., scale = "free_y") + opts(legend.position = "none")