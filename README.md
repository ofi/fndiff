# fndiff

## Purpose

List all files from one directory according to a selection pattern for which no
file with the same same lexically unique characteristic trait exists in another,
or to put it more trivial: "List all files from source directory which are
somehow missing in the target one."
The rest of this text explains the "somehow".

## Usage

From the script's help output:

                usage: fndiff [-h] [-s SOURCE_DIR] [-p PATTERN] [-r] [-o OUTFILE] [target_dir]

                Diff Filenames by Pattern

        positional arguments:
        target_dir            Target directory with files serving as a reference by
                                name to those in the source directory.

        optional arguments:
        -h, --help            show this help message and exit
        -s SOURCE_DIR, --source-dir SOURCE_DIR
                                Source directory with files being compared by name
                                with those from the target directory (default: cwd)
        -p PATTERN, --pattern PATTERN
                                Regular expression to match files from source and
                                target sets optionally containing one or more RE
                                groups to denominate the common part(s) of each
                                matching pair (default is basename, i.e. all
                                characters up to last dot)
        -r, --regex           Set to indicate file pattern contains a regular
                                expression (instead of shell-style glob patterns, the
                                default)
        -o OUTFILE, --outfile OUTFILE
                                Output file for result (default: stdout)


The result will be a list of pathnames of files from the target directory
selected by target pattern, which have no specified counterparts in the source
directory.
A counterpart is defined as a filename with the same ordered groups matched by
the given regular expression (or translated from the shell-style glob pattern)
against each filename on the  source and the target side.
Each resulting file is written on a single line.
The path before each file will be printed as given by the `SOURCE_DIR`
parameter.
(Because this tends to be a little mind-boggling, you should hav a look at the
example to visually grab the idea.)

Errors will be printed to stderr as reported by the operating system, e. g. for
missing directories, insufficient access rights etc. An exit code of zero (0)
means success, any other value an error. An empty result list is not an error.


## Example

To select all raw Fujifilm image files from dir `RAF` which are missing in
directory `JPG` and print them on stdout:

        fndiff -s RAF -p 'DSCF([0-9]{4})[.][A-Z]{3}$' -r JPG

This interprets the pattern from `-p` as an regular expression because of `-r`,
looks in the directories `JPG` and `RAF` for all matching files, and reports
all those in the directory `RAF` which do not have a counterpart in the 
directory `JPG`, e.g. a line `RAF/DSCF0345.RAF` indicates there is no file
`JPG/DSCF0345.JPG` in the target directory.


## Installation

Assuming Python3 (version >= 3.4 recommmended) is installed on your system, the
steps go:

1. Clone or download the repository.
1. `cd` into the top level directory `fndiff`
1. Install with `pip install .` (using `sudo` where applicable)

## Bugs

Glob-style pattern matching only works for full filenames for the time being.

## Motivation

Because loading raw images of my Fujifilm X-pro2 needs a long time,
and because I produce a JPEG image simultaneously in the second
card slot, it's a lot faster to sort and filter pictures by their JPEGs than
RAF-instances.

After having dumped several frames I like to get rid of the costly (in terms
of file space) RAF counterparts as well, but I have not found a tool to 
accomplish this. Now I can pipe the example from above through `xargs` like so:

        fndiff -s RAF -p 'DSCF([0-9]{4})[.][A-Z]{3}$' -r JPG | xargs rm

Some clever shell scripting might do it as well, but nowadays Python is commonly
more available than zsh (or even bash).

One can argue the solution is "over-engineered", but because the need arose
while preparing a Python workshop, I have decided to craft it in a somewhat
"clean" way as a supplement to the course.


## Legalese

Copyright 2018 Olaf Fiedler, Nürnberg, Germany,
License MIT (see LICENSE file for details)


## Disclaimer

**This software is provided as is without any claim of fitness for any given
purpose. If you use it, you will do so on your solely own risk without any
ability to hold the author(s) responsible for any consequences resulting from
the use of this software.**
