cmds=(ls date uname)
task_path=//

cyber_packages() {
    local cmds=("$@")
    for cmd in "${cmds[@]}"; do
        local version
        version=$($cmd -v 2>&1)
        if [[ $version == *"-v"* ]]; then
            version=$($cmd --version 2>&1)
        fi
        echo "$cmd version: $version"
    done
}

cyber_packages "${cmds[@]}" >> ${task_path}/loading_packages_shell.txt