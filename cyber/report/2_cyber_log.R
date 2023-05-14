log_cyber <- function(task) {
    sink(paste0(task, "/report/loading_R_packages.txt"))
    print(sessionInfo())
    sink()
}
