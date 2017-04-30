library(RcppCNPy)
fmat1  <- npyLoad("MYD08_E3.A2017105.006.2017118135357_AoD.npy")
fmat2  <- npyLoad("MOD08_E3.A2017105.006.2017118135856_Vapor.npy")
fmat1 <- t(fmat1)
fmat2 <- t(fmat2)


cor(as.vector(fmat1),as.vector(fmat2))
image(fmat1)
image(fmat2)
