# Repo to collect my custom conda recipes

## Bootstrapping
*DISCLAIMER*: I run everything on macOS, so this setup may not work for you

This repo requires `conda`. Check out the [conda docs](https://docs.conda.io/projects/conda/en/latest/user-guide/install/index.html)
for details on getting conda installed and set up on your system. I use macOS and the Homebrew system package manager,
so I was able to just run `brew cask install miniconda` to get everything set up.

Once you have conda installed, you can use the `environment.yml` file to create the conda environment needed to run
invoke tasks.

```
$ conda env create -f environment.yml
```

After you've created the environment, activate it and make sure you've got all the necessary programs in your `$PATH`:
```
$ conda activate conda_recipes_env

# Your versions may differ
$ conda build --version
conda-build 3.17.8

$ inv --version
Invoke 1.4.1

$ anaconda --version
anaconda Command line client (version 1.7.2)
```

### Setting Up the Anaconda Client
Before being able to publish these packages, you must have an account with anaconda.org and you must have
configured the Anaconda client (`anaconda`). See the [Anaconda package docs](https://docs.anaconda.com/anaconda-cloud/user-guide/tasks/work-with-packages/#uploading-conda-packages)
for info on how to set up your client for uploading your packages.

## Build and Publish Conda Packages

To build a given package from the repo, you run the following:
```
$ inv build <RECIPE>
```

`<RECIPE>` refers to one of the subdirectories in this repo, which will contain the `meta.yaml` and other recipe files.

After the package is built, you can run the following to publish it:
```
$ inv publish <RECIPE>
```
