# Day 1 pm: Set up a suitable computer environment

The aim for this half day is to make sure everyone has a computer environment where they can do the course.

## Editor

You should have a way to edit arbitrary code files on your computer. Ideally it should have special setup for editing Python files with e.g. syntax highlighting.

If in doubt, [VS code](https://code.visualstudio.com/) is always a good option.

## Terminal

You should have a terminal emulator that you can use to run command line programs.

Your computer probably already has one of these:

- Linux: you probably already have one? 
- macOS: The computer comes with a terminal emulator called "terminal". Plenty of others are available, many people really like [iterm2](https://iterm2.com/). My favourite is [Wezterm](https://wezterm.org/).
- Windows: I think PowerShell is the most popular

## [uv](https://docs.astral.sh/uv/)

uv is a Python dependency manager that can install Python for you. 

Install it by following the instructions on the website. You should then be able to run this command in your terminal

```shell
> uv
```

The output should look something like this:

```shell
An extremely fast Python package manager.

Usage: uv [OPTIONS] <COMMAND>

Commands:
    ...
```

If that works, try installing python (do this even if you already have python installed on your computer as it will likely make things easier later):

```shell
> uv python install
```

To execute a python file with uv:

```shell
> uv run my_python_file.py
```

To open a Python interpreter:

```shell
> uv run python
```

To start a new project:

```shell
mkdir my_new_project
cd my_new_project
uv init
```

To install a Python package in the current project:

```shell
> uv add package_i_want_to_install
```

To install a Python-based application globally:

```shell
> uv tool install tool_i_want_to_install
```

To run a command with a package installed temporarily (e.g. in this case jupyter):

```shell
> uv run --with jupyter jupyter lab
```

## git

First make sure you have git installed by running this command in your terminal:

```shell
> git
```

Expected output:
  
```shell
usage: git [-v | --version] [-h | --help] [-C <path>] [-c <name>=<value>]
           [--exec-path[=<path>]] [--html-path] [--man-path] [--info-path]
           [-p | --paginate | -P | --no-pager] [--no-replace-objects] [--bare]
           [--git-dir=<path>] [--work-tree=<path>] [--namespace=<name>]
           [--super-prefix=<path>] [--config-env=<name>=<envvar>]
           <command> [<args>]

These are common Git commands used in various situations:
```

If that worked, navigate in your terminal to a place where you would like to put a new folder, then run this command:

```shell
> git clone https://github.com/dtu-qmcm/bayesian_statistics_for_computational_biology.git
```

There should now be a new folder called `bayesian_statistics_for_computational_biology`.

## Python packages

Navigate into the folder `bayesian_statistics_for_computational_biology` and run this command:

```shell
> uv sync
```
