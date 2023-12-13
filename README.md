![Logo](https://raw.githubusercontent.com/MIKTHATGUY/Flow/main/Logo.svg)

## A non official command line tool created to help flowgorithm users

## Table of Content

- [Table of Content](#table-of-content)
- [Features](#features)
- [Future Features](#future-features)
- [Installation and Usage](#installation-and-usage)
  - [Automatic install for any folder in the system](#automatic-install-for-any-folder-in-the-system)
  - [Manually install only for current folder](#manually-install-only-for-current-folder)
  - [Manually install for any folder in the system](#manually-install-for-any-folder-in-the-system)
  - [Run Locally with Python](#run-locally-with-python)
- [FAQ](#faq)
  - [install.ps1 dosen't work](#installps1-dosent-work)
  - [EasyFlow closes right after i run it](#easyflow-closes-right-after-i-run-it)
- [Authors](#authors)


## Features

- [x] change file author
- [X] change all files in a folder or single
- [x] change pc name inside file
- [x] change about in file

## Future Features

- [ ] change file date of creation
- [ ] remove `edited at` fields
- [ ] customize `edited at` fields

## Installation and Usage

### Automatic install for any folder in the system

1) Download the `install.ps1` install script from [HERE](https://github.com/MIKTHATGUY/Flow/releases/latest)
2) open Windows Powershell **as administrator**
3) navigate to the folder where you have the `install.ps1` script
4) run install.ps1
5) Ready to use!

### Manually install only for current folder

1) Download the executable from [HERE](https://github.com/MIKTHATGUY/Flow/releases/latest)
2) copy the executable to the folder where the `.fprg` files are
3) Ready to use!

### Manually install for any folder in the system

1) Download the executable from [HERE](https://github.com/MIKTHATGUY/Flow/releases/latest)
2) Copy the executable in System32 folder
3) Ready to use!

### Run Locally with Python

1) Clone the project in a folder where it can create files as it has to create a `user` file

 ```bash
  git clone https://https://github.com/MIKTHATGUY/Flow
```

2) Go to the project directory

```bash
  cd Flow
```

3) Install dependencies

```bash
  pip Install requirements.txt
```

4) Start program

```bash
  python main.py -h
```

## FAQ

### install.ps1 dosen't work

1) Check if you are running it in **powershell** and not in cmd
2) Check that you are running powershell with amministrator privileges

### EasyFlow closes right after i run it

Do not open the file double clicking it, run it in the cmd and

## Authors

- [@MIKTHATGUY](https://https://github.com/MIKTHATGUY)

## We are **not** an official Flowgorithm tool nor associated with Flowgorithm **in any way**
