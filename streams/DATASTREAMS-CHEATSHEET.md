# Differences from Pyhton2 and Python3 Summary

Python 2 and Python 3 handle input and raw_input differently.

In Python 2

    input(x) is roughly the same as eval(raw_input(x))

    raw_input() is preferred, unless the author wants to support evaluating string expressions.

    eval() is used to evaluate string expressions.

Standard Library Docs:

    https://docs.python.org/2/library/functions.html#input

    https://docs.python.org/2/library/functions.html#raw_input

    https://docs.python.org/2/library/functions.html#eval

In Python 3

    Input handles string as a generic string. It does not evaluate the string as a string expression.

    raw_input doesn’t exist, but with some tricky techniques, it can be supported.

    eval() can be used the same as Python 2.

Standard Library Docs: 

    https://docs.python.org/3/library/functions.html#input

    https://docs.python.org/3/library/functions.html#eval

# Python Subprocesses Cheat Sheet

Check out the following link for more information:

    https://docs.python.org/3/library/subprocess.html


>>> subprocess.run(["ls", "-l"])  # doesn't capture output
CompletedProcess(args=['ls', '-l'], returncode=0)
>>> subprocess.run("exit 1", shell=True, check=True)
Traceback (most recent call last):
  ...
subprocess.CalledProcessError: Command 'exit 1' returned non-zero exit status 1

>>> subprocess.run(["ls", "-l", "/dev/null"], capture_output=True)
CompletedProcess(args=['ls', '-l', '/dev/null'], returncode=0,
stdout=b'crw-rw-rw- 1 root root 1, 3 Jan 23 16:23 /dev/null\n', stderr=b'')