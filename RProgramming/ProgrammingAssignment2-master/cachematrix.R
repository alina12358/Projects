## These two functions work together to cache a matrix and its inverse
## makeCacheMatrix deals with a matrix and its inverse, as well as their
## getter and setter methods

## This function deals with the getter and setter methods for the matrix
##and its inverse

makeCacheMatrix <- function(x = matrix()) {

        inv <- NULL
        set <- function(y) {
                x <<- y
                inv <<- NULL
        }
        get <- function() x
        setinv <- function(inverse) inv <<- inverse
        getinv <- function() inv
        list(set = set, get = get,
             setinv = setinv,
             getinv = getinv)
}


## This function calculates and returnes the inverse of a matrix

cacheSolve <- function(x, ...) {

        inv <- x$getinv()
        if(!is.null(inv)) {
                message("getting cached inverse")
                return(inv)
        }
        matr <- x$get()
        identity <- diag(dim(matr)[1])
        inv <- solve(matr, identity, ...)
        x$setinv(inv)
        inv
}
