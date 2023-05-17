cyber_packages <- function(task) {
    sink(paste0(task, "/report/loading_packages_R.txt"))
    print(sessionInfo())
    sink()
}
