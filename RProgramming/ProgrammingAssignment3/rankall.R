rankall <- function(outcome, num = "best"){
    disease = c("heart attack"=3,"heart failure"=4,"pneumonia"=5)
    temp = data[,c(1,2,disease[outcome])]
    temp = arrange(temp,temp[,3],temp[,2],temp[,1])
    temp = subset(temp,!is.na(temp[,3]))
    byState =split(temp,temp[,2])
    state = character()
    hospital = character()
    for (nm in names(byState)){
        if (num =="best"){rank=1}
        else if( num =="worst") {rank=dim(byState[[nm]])[1]}
        else {rank = num}
        state=c(state,nm)
        hospital =c(hospital,byState[[nm]][rank,1])
    }
    cbind(hospital,state)
}
    
        