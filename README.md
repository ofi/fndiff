# FilenamesDiff

## Purpose

List all files from one directory with according to selection pattern whose
basenames are (not) present in another (or same) directory with another
extension (or same extension if directories differ).


## Usage

Call the shell front end from the command line with:

    fndiff [-h]
        [(-S |--source-dir=) <source directory>] [(-s|--source-pattern=) <source pattern>]
        (-T |--target-dir=) <target directory> [(-t|--target-pattern=) <target pattern>]
        [-r| --regex] [<outfile>]

Options are:

    -h -- print usage and version information
    -S, --source-dir -- directory used as the reference for comparison,
            the current working directory by default
    -s, --source-pattern -- pattern of files to include, all (except those with
            leading dot) by default
    -T, --target-dir -- directory to be searched for counterpart files;
            has to be different from source, if none or the same pattern given
    -t, --target-pattern -- pattern of files from target directory to compare
            with those from source-dir, the full filename by default
    -r, --regex -- Patterns are given as regular expression, i. e. won't be
            translated from shell-style glob patterns
    <outfile> -- file the output will be written to, stdout by default

The result will be a list of pathnames of files from the target directory
selected by target pattern, which have no specified counterparts in the source
directory.
A counterpart is defined as a filename with the same first group matched by
the regular expression tranlated from the given shell-style glob pattern on the
source and the target side (see examples to visually get the idea).
Each resulting file is written on a single line.
The path before each file will be printed as given by the -T parameter.

Errors will be printed to stderr as reported by the operating system, e. g. for
missing directories, insufficient access rights etc. An exit code of zero (0)
means success, any other value an error.

An empty result list is not an error!


## Examples

To select all raw Fujifilm image files from dir `RAF` which are missing in
directory `JPG` and print them on stdout:

        fndiff -S JPG -s 'D*.JPG' -T RAF -t '*.RAF'

This translates the pattern `D*.JPG` into a regular expression like
`(D.*)\.JPG` and `*.RAF` into `(.*)\.RAF)`, scans the source
directory listing for files with names matching the first pattern and the
target directory for those matching the second pattern. Any file from the
second list, whose first group matching (e. g. `DSCF0719`) does not appear in
the first list will be added to the result list.

## Motivations

Because loading raw images of my Fujifilm X-pro2 needs a long time on my
MacBook Pro, and because I produce a JPEG image simultaneously in the second
card slot, it's a lot faster to sort and filter pictures by their JPEGs than
RAF-instances.

After having dumped several frames I like to get rid of the costly (in terms
of file space) RAF counterparts as well, but I have not found a tool to 
accomplish this.

Some clever zsh scripting might do it, but nowadays Python is commonly more
available than zsh (or even bash). Instead this tool can be used by other
scripts or programs.

One can argue the solution is "over-engineered", but because the need has arisen
while preparing a Python workshop, I have decided to craft it in a somewhat
"clean" way as a supplement to the course.


## Legalese

Copyright 2018 Olaf Fiedler, Nuernberg, Germany
License MIT (see LICENSE.txt)


## Disclaimer

**This software is provided as is without any claim of fitness for any given
purpose. If you use it, you will do so on your solely own risk without any
ability to hold the author(s) responsible for any consequences resulting from
the use of this software.**
