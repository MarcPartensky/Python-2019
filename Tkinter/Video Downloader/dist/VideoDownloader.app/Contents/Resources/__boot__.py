def _reset_sys_path():
    # Clear generic sys.path[0]
    import sys
    import os

    resources = os.environ['RESOURCEPATH']
    while sys.path[0] == resources:
        del sys.path[0]


_reset_sys_path()


def _site_packages(prefix, real_prefix, global_site_packages):
    import site
    import sys
    import os

    paths = []

    paths.append(
        os.path.join(
            prefix, 'lib', 'python' + sys.version[:3], 'site-packages'))
    if os.path.join('.framework', '') in os.path.join(prefix, ''):
        home = os.environ.get('HOME')
        if home:
            paths.append(
                os.path.join(
                    home, 'Library', 'Python',
                    sys.version[:3], 'site-packages'))

    # Work around for a misfeature in setuptools: easy_install.pth places
    # site-packages way to early on sys.path and that breaks py2app bundles.
    # NOTE: this is hacks into an undocumented feature of setuptools and
    # might stop to work without warning.
    sys.__egginsert = len(sys.path)

    for path in paths:
        site.addsitedir(path)

    # Ensure that the global site packages get placed on sys.path after
    # the site packages from the virtual environment (this functionality
    # is also in virtualenv)
    sys.__egginsert = len(sys.path)

    if global_site_packages:
        site.addsitedir(
            os.path.join(
                real_prefix, 'lib', 'python' + sys.version[:3],
                'site-packages'))


_site_packages('/Users/marcpartensky/Downloads/Programs/Python/Python-2019/Tkinter/venv', '/usr/local', 0)

def _emulate_shell_environ():
    import os
    import sys
    import time

    if sys.version_info[0] > 2:
        env = os.environb
    else:
        env = os.environ

    split_char = b'='

    # Start 'login -qf $LOGIN' in a pseudo-tty. The pseudo-tty
    # is required to get the right behavior from the shell, without
    # a tty the shell won't properly initialize the environment.
    #
    # NOTE: The code is very carefull w.r.t. getting the login
    # name, the application shouldn't crash when the shell information
    # cannot be retrieved
    master, slave = os.openpty()
    pid = os.fork()
    try:
        login = os.getlogin()
    except AttributeError:
        try:
            login = os.environ['LOGNAME']
        except KeyError:
            login = None

    if login is not None:
        if pid == 0:
            # Child
            os.close(master)
            os.setsid()
            os.dup2(slave, 0)
            os.dup2(slave, 1)
            os.dup2(slave, 2)
            os.execv('/usr/bin/login', ['login', '-qf', login])
            os._exit(42)

        else:
            # Parent
            os.close(slave)
            # Echo markers around the actual output of env, that makes it
            # easier to find the real data between other data printed
            # by the shell.
            os.write(master, b'echo "---------";env;echo "-----------"\r\n')
            os.write(master, b'exit\r\n')
            time.sleep(1)

            data = []
            b = os.read(master, 2048)
            while b:
                data.append(b)
                b = os.read(master, 2048)
            data = b''.join(data)
            os.waitpid(pid, 0)

        in_data = False
        for ln in data.splitlines():
            if not in_data:
                if ln.strip().startswith(b'--------'):
                    in_data = True
                continue

            if ln.startswith(b'--------'):
                break

            try:
                key, value = ln.rstrip().split(split_char, 1)
            except:
                pass

            else:
                env[key] = value


_emulate_shell_environ()


def _chdir_resource():
    import os
    os.chdir(os.environ['RESOURCEPATH'])


_chdir_resource()


def _setup_ctypes():
    from ctypes.macholib import dyld
    import os
    frameworks = os.path.join(os.environ['RESOURCEPATH'], '..', 'Frameworks')
    dyld.DEFAULT_FRAMEWORK_FALLBACK.insert(0, frameworks)
    dyld.DEFAULT_LIBRARY_FALLBACK.insert(0, frameworks)


_setup_ctypes()


def _path_inject(paths):
    import sys
    sys.path[:0] = paths


_path_inject(['/Users/marcpartensky/Downloads/Programs/Python/Python-2019/Tkinter'])


import re
import sys

cookie_re = re.compile(b"coding[:=]\s*([-\w.]+)")
if sys.version_info[0] == 2:
    default_encoding = 'ascii'
else:
    default_encoding = 'utf-8'


def guess_encoding(fp):
    for i in range(2):
        ln = fp.readline()

        m = cookie_re.search(ln)
        if m is not None:
            return m.group(1).decode('ascii')

    return default_encoding


def _run():
    global __file__
    import os
    import site  # noqa: F401
    sys.frozen = 'macosx_app'

    argv0 = os.path.basename(os.environ['ARGVZERO'])
    script = SCRIPT_MAP.get(argv0, DEFAULT_SCRIPT)  # noqa: F821

    sys.argv[0] = __file__ = script
    if sys.version_info[0] == 2:
        with open(script, 'rU') as fp:
            source = fp.read() + "\n"
    else:
        with open(script, 'rb') as fp:
            encoding = guess_encoding(fp)

        with open(script, 'r', encoding=encoding) as fp:
            source = fp.read() + '\n'

        BOM = b'\xef\xbb\xbf'.decode('utf-8')

        if source.startswith(BOM):
            source = source[1:]

    exec(compile(source, script, 'exec'), globals(), globals())


DEFAULT_SCRIPT='/Users/marcpartensky/Downloads/Programs/Python/Python-2019/Tkinter/videodownloader.py'
SCRIPT_MAP={}
try:
    _run()
except KeyboardInterrupt:
    pass
