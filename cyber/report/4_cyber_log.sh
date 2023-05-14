get_version() {
    local cmd=$1
    local version
    version=$($cmd -v 2>&1)
    if [[ $version == *"-v"* ]]; then
        version=$($cmd --version 2>&1)
    fi
    echo "$cmd version: $version"
}

#e.g.
cmds=(ls date uname)
for cmd in "${cmds[@]}"; do
    get_version $cmd >> version.txt
done