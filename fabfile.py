from fabric.api import *

# the user to use for the remote commands
env.user = 'root'
# the servers where the commands are executed
env.hosts = ['192.241.196.189']

def pack():
    # create a new source distribution as tarball
    local('python setup.py sdist --formats=gztar', capture=False)

def deploy():
    pack()
    # figure out the release name and version
    dist = local('python setup.py --fullname', capture=True).strip()
    # upload the source tarball to the temporary folder on the server
    put('dist/%s.tar.gz' % dist, '/tmp/rms.tar.gz')
    run('rm -rf /tmp/rms')
    # create a place where we can unzip the tarball, then enter
    # that directory and unzip it
    run('mkdir /tmp/rms')
    with cd('/tmp/rms'):
        run('tar xzf /tmp/rms.tar.gz')
        # now setup the package with our virtual environment's
        # python interpreter
        with cd('/tmp/rms/rms-1.0/'):
            with prefix('source /root/Python-RMS/bin/activate'):
                run('python setup.py install')

    #Migrate settings.
    put('rms/settings.py', '/root/rms')

    # now that all is set up, delete the folder again
    # run('rm -rf /tmp/rms /tmp/rms.tar.gz')
    # and finally touch the .wsgi file so that mod_wsgi triggers
    # a reload of the application
    relaunch();

def relaunch():
    run('pkill -f run.py', warn_only = True)
    with cd('/root'):
        with prefix('source /root/Python-RMS/bin/activate'):
            run('python run.py &> /root/rms/log.txt', pty=False, shell_escape=False)

def db():
    # Migrate db file.
    local('mongodump --out /tmp/db && tar -cvf /tmp/db.tar /tmp/db')
    put('/tmp/db.tar', '/tmp/db.tar')
    with cd('/tmp'):
        run('tar -xvf /tmp/db.tar')
        run('mongorestore /tmp/tmp/db/rms/ -d rms')
