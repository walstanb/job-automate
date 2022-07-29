# asu-student-job-automate
Selenium Web automation for ASU Student Job Portal Applications

## Setup:

First download latest chromedriver from [here](https://chromedriver.chromium.org/downloads) and extract to same folder.

Use the template given below to make a `config.py` file with your `username` and `password`.

Install python from the [Microsoft Store](https://apps.microsoft.com/store/detail/python-39/9P7QFQMJRFP7?hl=en-us&gl=US) or from the [website](https://www.python.org/downloads/).

> optional: you may also setup a virtual environment using
> ```
> python -m venv env
> ```
>

Install dependencies using:

```
pip install -r requirements.txt
```

## To run:
Open a command prompt window in the current folder by typing 'cmd' in the address bar and execute the following command
```
python asu_sjobs.py
```


### Template for `config.py`

```
#!/usr/bin/env python
DISABLE_SAVE_SUBMIT = False

configs = [{
    "username": "userone1",
    "password": "PaSsWoRd",
    "file_list": ['Supporting_Docs_file1.pdf', 'Supporting_Docs_file2.pdf'],
}, {
    "username": "usertwo2",
    "password": "PaSsWoRd",
    "file_list": ['Supporting_Docs_file.pdf',],
}]
```