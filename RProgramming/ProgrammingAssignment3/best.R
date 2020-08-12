best <- function(state,outcome){
    ## Read outcome data
    ## Check that state and outcome are valid
    ## Return hospital name in that state with lowest 30-day death
    ## rates
    disease = c("heart attack"=3,"heart failure"=4,"pneumonia"=5)
    temp = data[,c(1,2,disease[outcome])]
    temp = arrange(temp,temp[,3],temp[,2],temp[,1])
    temp = subset(temp,!is.na(temp[,3]))
    byState =split(temp,temp[,2])
    table = byState[[state]]
    table[1,1]
}