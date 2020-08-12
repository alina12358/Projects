rankhospital <- function(state, outcome, num = "best"){
    disease = c("heart attack"=3,"heart failure"=4,"pneumonia"=5)
    temp = data[,c(1,2,disease[outcome])]
    temp = arrange(temp,temp[,3],temp[,2],temp[,1])
    temp = subset(temp,!is.na(temp[,3]))
    byState =split(temp,temp[,2])
    table = byState[[state]]
    if (num =="best"){rank=1}
    else if( num =="worst") {rank=dim(table)[1]}
    else {rank = num}
    table[rank,1]
}