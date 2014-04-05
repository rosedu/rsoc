from fabric.api import cd, env, run

env.hosts = ['rsoc@projects.rosedu.org']

def deploy():
    with cd("public_html"):
        run("git pull")
