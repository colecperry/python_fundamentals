# Module: a file containing Python definitions and statements. A module's functions, classes, and global variables can be accessed by other modules.
# Package: a collection of modules that can be accessed as a group using the package name.
# import: the Python keyword used to access data from other packages and modules inside of the current module.
# PyPI: the Python Package Index. A repository of Python packages that can be downloaded and made available to your application.
# pip: the command line tool used to download packages from PyPI. pip is installed on your computer automatically when you download Python.
# Virtual Environment: a collection of modules, packages, and scripts that can be activated or deactivated at any time.
# Pipenv: a virtual environment tool that uses pip to manage the modules, packages, and scripts that you intend to use in your application and projects.
    # Once you go into the virtual environment, you will notice a pipfile and pipfile.lock
    # The Pipfile describes the dependencies we have installed and the python version
    # The Pipfile.lock describes all the dependencies our dependencies rely on

# Step by Step:
    # Ensure Python and Pipenv are Installed: 
        # Check this by running: $python --version, $pip install pipenv
    # Navigate to your project directory
    # Create a new virtual environment using pipenv using your default python version or a specified version
        # $pipenv --python 3.8
    # Activate the virtual environment
        # $pipenv shell
    # Install project dependencies
        # $pipenv install ....
    # Managing dependencies
        # To list all install packages and their versions run pipenv graph
        # To uninstall a package run $pipenv uninstall <package_name>
        # To change the version of an installed package run pipenv install <package_name>==<version>
        # ex. pipenv install requests==2.25.1
    # Deactivating the virtual env
        # $exit
