mydata = read.csv("f1.csv")
qplot(DatasetSize, f1, data=mydata, colour=classifier)
qplot(DatasetSize, f1, data=mydata, geom='line', color=classifier)