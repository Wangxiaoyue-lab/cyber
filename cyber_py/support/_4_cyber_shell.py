import subprocess

def cyber_packages(cmds):
    cmds = cmds.split(',')
    for cmd in cmds:
        try:
            version = subprocess.check_output([cmd, '-v'], stderr=subprocess.STDOUT).decode('utf-8')
        except subprocess.CalledProcessError:
            try:
                version = subprocess.check_output([cmd, '--version'], stderr=subprocess.STDOUT).decode('utf-8')
            except subprocess.CalledProcessError:
                version = 'unknown'
        print(f'{cmd} version: {version}')

cyber_packages('ls,date,uname')


cyber_packages("ls,fastp,cellranger")


cyber_packages ls,fastp,cellranger