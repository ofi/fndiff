# DiffBasename

## Purpose

List all files from one directory with their extension whose basenames are
(not) present in another (or same) directory with another extension (or same
extension if directories differ).

## Usage

Call from the command line with:

    diffbase [-h]
        [(-S |--source-dir=) <source directory>] [(-s|--source-suffix=) <source suffix>]
        (-T |--target-dir=) <target directory> [(-t|--target-suffix=) <target suffix>]
        [<outfile>]

Options are:

    -h -- print usage and version information
    -S, --source-dir -- directory used as the reference for comparison,
            the current working directory by default
    -s, --source-suffix -- suffix of files to include, '-' to indicate none,
            all (or without) extensions by default
    -T, --target-dir -- directory to be searched for files with same basenames,
            has to be different from source if none or the same suffices given
    -t, --target-suffix -- suffix of files to compare to, '-' to indicate none,
            all (or without) extensions by default
    <outfile> -- file the output will be written to, stdout by default

The result will be a list of pathnames of files from the target directory
including suffix, which have no specified counterparts with the same basename
in the source directory. Each file is written on a single line. The path before
each file will be printed as given in the -T parameter.

Errors will be printed to stderr as reported by the operating system, e. g. for
missing directories, insufficient access rights etc. An exit code of zero (0)
means success, any other value an error.

An empty result list is not an error!

## Motivation

Because loading raw images of my Fujifilm X-pro2 needs a long time on my
MacBook Pro, and because I produce a JPEG image simultaneously in the second
card slot, it's a lot faster to sort and filter pictures by their JPEGs than
RAF-instances.

After having dumped several frames I like to get rid of the costly (in terms
of file space) RAF counterparts as well, but I have not found a tool to 
accomplish this.

Some clever zsh scripting might do it, but nowadays Python is commonly more
available than zsh (or even bash).
