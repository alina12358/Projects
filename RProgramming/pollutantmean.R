pollutantmean <- function(direct,pollut,id=1:332){
  num = 0
  tot = 0
  
  for(n in id){
    fname = as.character(n)
    fname = c(rep("0",times=3-nchar(fname)),fname,".csv")
    fname = paste(fname,collapse="")
    df = read.csv(file.path(direct,fname))
    vect= df[[pollut]][!is.na(df[[pollut]])]
    tot =sum(tot,vect)
    num =num+length(vect)
  }
  tot/num
}