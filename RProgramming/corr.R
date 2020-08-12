corr <- function(direct,threshold = 0){
    cases = complete(direct)
    cases = cases[["nobs"]]
    cVect = numeric()
    for (x in 1:length(cases)){
        if(cases[x] >= threshold){
            fname = as.character(x)
            fname = c(rep("0",times=3-nchar(fname)),fname,".csv")
            fname = paste(fname,collapse="")
            df = read.csv(file.path(direct,fname))
            entry = cor(df[["sulfate"]],df[["nitrate"]],use="pairwise.complete")
            if(!is.na(entry)){
                cVect =c(cVect,entry)
            }
        }
    }
    cVect
}