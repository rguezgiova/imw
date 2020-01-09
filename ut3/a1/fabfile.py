from fabric.api import env, cd, local, run

env.hosts = ["159.89.14.205"]

def deploy():
    local("git push")
    with cd("~/webapps/virtual_machine"):
        run("git pull")
run("supervisorctl restart virtual_machine")
