from invoke import task


@task
def start(ctx):
    ctx.run("python3 src/index.py", pty=True)

@task
def test(ctx):
    ctx.run("pytest src", pty=True)

@task
def coverage(ctx):
    ctx.run("coverage run --branch -m pytest src", pty=True)

@task
def coverage_print(ctx):
    ctx.run("coverage report -m", pty=True)

@task(coverage)
def coverage_report(ctx):
    ctx.run("coverage html", pty=True)

@task
def open_report(ctx):
    ctx.run("open htmlcov/index.html", pty=True)

@task
def commands(ctx):
    ctx.run("invoke --list", pty=True)

@task
def build(ctx):
    ctx.run("python3 src/build.py", pty=True)