import nox

package = 'idpalette'


@nox.session()
def tests(session):
    """Run test cases and record the test coverage."""
    session.install('.[cmap,tests]')
    # Run the test cases and report the test coverage.
    session.run(
        'pytest',
        f'--cov={package}',
        '--pyargs',
        package,
        './tests',
        *session.posargs,
    )


@nox.session(tags=['check'])
def ruff(session):
    """Check code for linter warnings and formatting issues."""
    check_files = ['src', 'tests', 'noxfile.py']
    session.install('ruff ~= 0.5')
    session.run('ruff', 'check', *check_files)
    session.run('ruff', 'format', '--diff', *check_files)


@nox.session()
def build(session):
    """Build source and binary (wheel) packages."""
    session.install('build')
    session.run('python', '-m', 'build')


@nox.session(reuse_venv=True)
def publish(session):
    """Publish a binary (wheel) package to PyPI."""
    if not session.posargs:
        print('No package specified, nothing to publish')
        return

    session.install('twine')
    # NOTE: support building packages with metadata 2.3.
    session.install('pkginfo>=1.10.0')
    session.run('twine', *session.posargs)
