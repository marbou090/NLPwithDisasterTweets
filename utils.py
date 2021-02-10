import git

def git_commits(rand):
    def func_decorator(my_func):
        print("experiment_name: ", rand)

        repo = git.Repo(str(Path(os.getcwd()).parents[0]))
        repo.git.diff("HEAD")
        repo.git.add(".")
        repo.index.commit(f"{rand}(before running)")

        def decorator_wrapper(*args, **kwargs):
            my_func(*args, **kwargs)

            repo.index.commit(f"{rand}(after running)")
            repo.git.push('origin', 'master')
        return decorator_wrapper

    return func_decorator