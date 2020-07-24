from github import Github


def search_github():
    keywords = input('Enter keyword(s)[e.g python, flask, postgres]: ')
    keywords = [keyword.strip() for keyword in keywords.split(',')]
    query = '+'.join(keywords) + '+in:readme+in:description'
    result = g.search_repositories(query, 'stars', 'desc')

    print(f'Found {result.totalCount} repo(s) giving you first 5')

    for repo in result[:5]:
        print(f'{repo.clone_url}, {repo.stargazers_count} stars')
    return


def userInfo():
    user = g.get_user()
    username = user.login
    userfullname = user.name
    print(username, userfullname)


def getmyRepos():
    repos = g.get_user().get_repos()
    for r in repos:
        print(r)


def getRepoTopic(repository="PyGithub/PyGithub"):
    repo = g.get_repo(repository)
    repo.get_topics()


def getStar(repository="PyGithub/PyGithub"):
    # get count of stars
    repo = g.get_repo(repository)
    repo.stargazers_count


def openIssue(repository="PyGithub/PyGithub"):
    # Get list of open issues
    repo = g.get_repo(repository)
    open_issues = repo.get_issues(state='open')
    # print using loop
    for issue in open_issues[:3]:
        print(issue)


def getLabels(repository="PyGithub/PyGithub"):
    # Get all the labels of the repository
    repo = g.get_repo(repository)

    labels = repo.get_labels()
    for label in labels[:3]:
        print(label)


def getContents(repository="PyGithub/PyGithub"):
    # Get all of the contents of the root directory of the repository
    repo = g.get_repo(repository)
    contents = repo.get_contents("")
    for content_file in contents[:3]:
        print(content_file)


def getContentFile(repository="PyGithub/PyGithub"):
    # Get a specific content file
    repo = g.get_repo(repository)

    contents = repo.get_contents("README.md")
    print(contents)


def createFile(repository="PyGithub/PyGithub"):
    # Create a new file in the repository
    repo = g.get_repo(repository)
    repo.create_file("test.txt", "test", "test", branch="master")


def updateFile(repository="PyGithub/PyGithub"):
    # Update a file in the repository
    repo = g.get_repo(repository)

    contents = repo.get_contents("test.txt", ref="master")
    repo.update_file(contents.path, "more tests", "more tests", contents.sha, branch="master")


def deleteFile(repository="PyGithub/PyGithub"):
    # Delete a file in the repository
    repo = g.get_repo(repository)
    contents = repo.get_contents("test.txt", ref="master")
    repo.delete_file(contents.path, "remove test", contents.sha, branch="master")


def getClones(repository="PyGithub/PyGithub"):
    # Get number of clones and breakdown for the last 14 days
    repo = g.get_repo(repository)
    contents = repo.get_clones_traffic(per="week")
    print(contents)


def markNotifs(repository="PyGithub/PyGithub"):
    # Mark the notifications of the repository as read
    repo = g.get_repo(repository)
    repo.mark_notifications_as_read()


def branchlist(repository="PyGithub/PyGithub"):
    # Get list of branches
    repo = g.get_repo(repository)
    list(repo.get_branches())


def getbranch(repository="PyGithub/PyGithub"):
    # Get a branch
    repo = g.get_repo(repository)
    repo.get_branch(branch="master")


def getheadcomm(repository="dev-manojm/jenkins-connect-exapmle"):
    # Get HEAD commit of a branch
    branch = g.get_repo(repository).get_branch("master")
    result = branch.commit
    print(result)


def statuscheck(repository="dev-manojm/jenkins-connect-exapmle"):
    # See required status checks of a branch
    branch = g.get_repo(repository).get_branch("master")
    branch.get_required_status_checks()


def createcommstatus(repository="PyGithub/PyGithub"):
    # Create commit status check
    repo = g.get_repo(repository)
    # sha = input("Please provide sha for commit")
    repo.get_commit(sha="3b7eb8b0775ecced7b56a4cc9f84cc40113beff3").create_status(
        state="pending",
        target_url="https://FooCI.com",
        description="FooCI is building",
        context="ci/FooCI"
    )


def getcommdate(repository="PyGithub/PyGithub"):
    # Get commit date
    repo = g.get_repo(repository)
    # sha = input("Please provide sha for commit")
    commit = repo.get_commit(sha="3b7eb8b0775ecced7b56a4cc9f84cc40113beff3")
    print(commit.commit.author.date)
    print(commit.commit.committer.date)


def getissue(repository="PyGithub/PyGithub", number=874):
    # Get issue
    repo = g.get_repo(repository)
    issue = repo.get_issue(number)
    print(issue)


def createissue(repository="PyGithub/PyGithub"):
    # Create Issue
    repo = g.get_repo(repository)
    repo.create_issue(title="This is a new issue")


if __name__ == "__main__":
    api_key=input('Hello, please login first give your api-key:')

    g = Github(api_key)
    repository = "PyGithub/PyGithub"
    number = 874
    choice = input("Would you like to change the github repository (deafult is Pygithub/Pygithub) press Y: ")
    choice.lower()
    if (choice == "y"):
        repository = input("give your Repo: ")
    else:
        pass
    git_cmds = {
        "search_github": lambda: search_github(),
        "userInfo": lambda: userInfo(),
        "getmyRepos": lambda: getmyRepos(),
        "getRepoTopic": lambda: getRepoTopic(repository),
        "getStar": lambda: getStar(repository),
        "openIssue": lambda: openIssue(repository),
        "getLabels": lambda: getLabels(repository),
        "getContents": lambda: getContents(repository),
        "getContentFile": lambda: getContentFile(repository),
        "createFile": lambda: createFile(repository),
        "updateFile": lambda: updateFile(repository),
        "deleteFile": lambda: deleteFile(repository),
        "getClones": lambda: getClones(repository),
        "markNotifs": lambda: markNotifs(repository),
        "branchlist": lambda: branchlist(repository),
        "getbranch": lambda: getbranch(repository),
        "getheadcomm": lambda: getheadcomm(repository),
        "statuscheck": lambda: statuscheck(repository),
        "createcommstatus": lambda: createcommstatus(repository),
        "getcommdate": lambda: getcommdate(repository),
        "getissue": lambda: getissue(repository, number),
        "createissue": lambda: createissue(repository)

    }
    print('\n\n\n========GitHub API list===========')
    param = None
    while (param != "E" or "e"):
        for item in git_cmds.keys():
            print(item)

        param = input('\n$Choose an operation listed above or type E to exit: ')

        if param in git_cmds.keys():
            print("\n\n",git_cmds[param]())
            git_cmds[param]()
        else:
            param.lower()
            if (param == "e"):
                print("bbye!")
                break
            print('Error: Unsupported operation')
