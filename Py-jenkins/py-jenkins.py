import jenkins
import pprint
pp = pprint.PrettyPrinter()


def userinfo():
    user = server.get_whoami()
    version = server.get_version()
    print('Hello %s from Jenkins %s' % (user['fullName'], version))

def jobcount():
    pp.pprint(server.jobs_count())

def createJob():
    job=input("Specify the name of the Job: ")
    server.create_job(job, jenkins.EMPTY_CONFIG_XML)
    jobs = server.get_jobs()
    pp.pprint(jobs)

def getJobConfig():
    job = input("Specify the name of the Job: ")
    my_job = server.get_job_config(job)
    pp.pprint(my_job)

def buildJob():

    job = input("Specify the name of the Job: ")
    server.build_job(job)

def disableJob():

    job = input("Specify the name of the Job: ")
    server.disable_job(job)

def copyJob():

    job1 = input("Specify the name of the Job you want to copy: ")

    job2 = input("Specify the name of the Job you want to copy to: ")
    server.copy_job(job1, job2)

def enableJob():
    job = input("Specify the name of the Job: ")
    server.enable_job(job)

def reconfigueJob():
    job = input("Specify the name of the Job: ")
    server.reconfig_job(job, jenkins.RECONFIG_XML)

def deleteJob():
    job = input("Specify the name of the Job: ")
    server.delete_job(job)

def buildInfo():
    job = input("Specify the name of the Job: ")
    last_build_number = server.get_job_info(job)['lastCompletedBuild']['number']
    build_info = server.get_build_info(job, last_build_number)
    pp.pprint(build_info)

def getJobs():
    job = input("Specify the name of the Job: ")
    jobs = server.get_jobs(view_name=job)
    pp.pprint(jobs)

def createView():
    view = input("Specify the name of the View: ")
    server.create_view(view, jenkins.EMPTY_VIEW_CONFIG_XML)

def viewConfig():

    view = input("Specify the name of the View: ")
    view_config = server.get_view_config(view)
    pp.pprint(view_config)

def getViews():
    views = server.get_views()
    pp.pprint(views)

def deleteView():

    view = input("Specify the name of the View: ")
    server.delete_view(view)
    views = server.get_views()
    pp.pprint(views)

def pluginsInfo():
    plugins = server.get_plugins_info()

    pp.pprint(plugins)


if __name__=="__main__":
    print('Hello, please login first:')
    username=input('Username: ')
    psswd = input('Password or API: ')
    url = input('URL: ')
    server = jenkins.Jenkins(url, username=username,
                             password=psswd)
    jen_cmds = {
        "userInfo": lambda: userinfo(),
        "jobCount": lambda :jobcount(),
        "createJob":lambda :createJob(),
        "getJobConfig": lambda :getJobConfig(),
        "buildJob":lambda :buildJob(),
        "disableJob": lambda: disableJob(),
        "copyJob": lambda: copyJob(),
        "enableJob": lambda: enableJob(),
        "reconfigJob": lambda: reconfigueJob(),
        "deleteJob": lambda: deleteJob(),
        "buildInfo": lambda: buildInfo(),
        "createView": lambda: createView(),
        "getJobs": lambda: getJobs(),
        "ViewConfigs": lambda: viewConfig(),
        "getViews": lambda: getViews(),
        "deleteView": lambda: deleteView(),
        "pluginsInfo": lambda :pluginsInfo(),

    }
    print('========Jenkins api list===========')
    param=None
    while (param != "E" or "e"):
        for item in jen_cmds.keys():
            print(item)

        param = input('\n$Choose an operation listed above or type E to exit: ')

        if param == "E"or "e":
            break

        if param in jen_cmds.keys():
            jen_cmds[param]()
        else:
            print('Error: Unsupported operation')
