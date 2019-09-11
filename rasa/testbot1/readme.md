# Actions
See https://rasa.com/docs/rasa/core/actions/.

To run action server run the following. This is to serve up custom actions. Do this via another Python window. Or work out whether there's a background option.
```rasa run actions```

# Custom Policy
https://www.digitalocean.com/community/tutorials/how-to-write-modules-in-python-3
https://www.depts.ttu.edu/hpcc/userguides/application_guides/python.packages.local_installation.php

To make custom policy module available, go to *policy* folder and run ```python setup.py install --user```. The files will end up here : **C:\Users\lborlace\AppData\Roaming\Python\Python37\site-packages** (i.e. it ignores the current environment). There are bound to be better ways to install this to make available :)

# Debugging / Linting
https://stackoverflow.com/questions/53939751/pylint-unresolved-import-error-in-visual-studio-code
https://github.com/microsoft/python-language-server/blob/master/TROUBLESHOOTING.md#unresolved-import-warnings

Was hard, but here's a nasty way I've gotten to debugging the main Rasa library.

1. Download Rasa source code.
2. Create a new conda environment. Don't install Rasa.
3. Instead deploy Rasa's prereqs as documented in the build instructions.
4. Update system PYTHONPATH variable to point to the base of where you've downloaded rasa, e.g. C:\Users\lborlace\Documents\GitHub\Non-Forked\rasa.
5. Update __main__.py to include the breakpoint / debug stuff (ptvsd)
6. Open a Python terminal, go to where your bot is (doesn't have to be in the Rasa folder)
 pip3 install gast==0.2.2 (workaround for an issue)
 cd C:\Users\lborlace\Documents\GitHub\Non-Forked\learning-ml\rasa\testbot2
 python ..\..\..\rasa\rasa\__main__.py train
 python ..\..\..\rasa\rasa\__main__.py shell
 
7. Make sure debug config looks like this :

```
{
    "name": "Python: Remote Attach",
    "type": "python",
    "request": "attach",
    "port": 5678,
    "host": "localhost",
    "pathMappings": [
        {
            "localRoot": "${workspaceFolder}",
            "remoteRoot": "${workspaceFolder}"
        }
    ]
}
```

8. Attach the debugger. Breakpoints should be hit!