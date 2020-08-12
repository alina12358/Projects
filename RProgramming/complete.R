complete <- function(direct,id=1:332){
    nobs = numeric()
    for(n in id){
        fname = as.character(n)
        fname = c(rep("0",times=3-nchar(fname)),fname,".csv")
          fname = paste(fname,collapse="")
        df = read.csv(file.path(direct,fname))
        rows = nrow(subset(df,!is.na(sulfate) & !is.na(nitrate)))
        nobs =c(nobs,rows)
    }
    data.frame(id,nobs)
}