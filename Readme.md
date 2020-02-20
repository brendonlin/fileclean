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

## Usage
Create a task file `tasks.csv` in user_home/Documents/fileclean/

```
fileclean --init
```

Run task:
```
fileclean
```

Run task file with specitfied file
```
fileclean -c taskFilePath
```
