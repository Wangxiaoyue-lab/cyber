cyber_packages <- function(task) {
    today <- format(Sys.Date(), "%Y%m%d")
    sink(paste0(task, "/report/loading_packages_R_", today, ".txt"))
    print(sessionInfo())
    sink()
}
