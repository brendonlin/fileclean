# File cleaning tool

Fileclean is commandline tool for file cleaning.

## Features

- Support delete, move or copy files.
- Support recursive folders.
- Support regular expression match for file names.

## Install

```
pip install fileclean
```

1. Create a task file `tasks.csv`: `fileclean --init`
2. Run tasks: 
   * Run task file in the current directory: `fileclean`
   * Run task file with specitfied file path: `fileclean -c taskFilePath`
