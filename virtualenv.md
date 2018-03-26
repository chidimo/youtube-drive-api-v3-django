# Creating and working with python virtual environments in windows

## Assumption

I assume here that you have [python](https://www.python.org/) installed in your system. Or perhaps you have a package manager such as [Anaconda](https://www.anaconda.com/download/) or [Canopy](https://store.enthought.com/downloads/) and that you have your path variables setup correctly. If you don't then head over to any of these pages and download a python installation to start with. I recommend Anaconda personnally. But use any one of your choice

<span style="color:red">**Warning**</span> these files are usually large, so you may want to use a non-metered connection.

## Setting up your system path

Having downloaded and installed a python distribution, you have to add their installed directories to your system path. Python gives you the option to specify if you want to add it to path during the installation process, so it may not be much of a problem. If you installed Anaconda, then add the following folders to your system `path` if they were not already added during installation.

1. `<path to anaconda installation>\anaconda`
1. `<path to anaconda installation>\anaconda\Scripts`

In case you're on a system without admin rights, you can set `user` environment variables by following these steps (System-wide environment variables is not required) to work with python virtual environments.

1. Open `Run` dialog by pressing `Windows Logo Key` + `R`
1. Type `rundll32 sysdm.cpl,EditEnvironmentVariables` to open environment variables dialog
1. Edit the path settings to add the required directories.

## Installing necessary libraries

    pip install virtualenv
	pip install virtualenvwrapper-win

## Creating and using the virtual environment

To create a virtual environment use the below command (the `-a` flag is optional. It only associates a directory with a virtual environment such that whenever you activate the environment, you're automagically `cd`ed into that directory as well).

	mkvirtualenv <envname> -a <path to a directory>` --no-site-packages

To activate the virtual environment use the below command

	workon <envname>

In case you're interested, your newly created environment resides in `%USERPROFILE%\Envs` by default. Just copy paste it into any open `windows explorer` address bar and it'll lead straight to the directory where you have all your virtual environments.
If you want to change that location please consult resource number 3 below

## Resources
1. http://abdelraoof.com/blog/2014/11/11/install-nodejs-without-admin-rights
1. https://virtualenv.pypa.io/en/stable/
1. https://github.com/davidmarble/virtualenvwrapper-win
1. https://virtualenvwrapper.readthedocs.io/en/latest/install.html
