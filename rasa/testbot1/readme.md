# Actions
See https://rasa.com/docs/rasa/core/actions/.

To run action server run the following. This is to serve up custom actions. Do this via another Python window. Or work out whether there's a background option.
```rasa run actions```

# Custom Policy
https://www.digitalocean.com/community/tutorials/how-to-write-modules-in-python-3
https://www.depts.ttu.edu/hpcc/userguides/application_guides/python.packages.local_installation.php

To make custom policy module available, go to *policies* folder and run ```python setup.py install --user```. The files will end up here : **C:\Users\lborlace\AppData\Roaming\Python\Python37\site-packages** (i.e. it ignores the current environment). There are bound to be better ways to install this to make available :)