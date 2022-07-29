# asu-student-job-automate
Selenium Web automation for ASU Student Job Portal Applications

## To execute:

First download latest chromedriver from [here](https://chromedriver.chromium.org/downloads) and extract to same folder.

Use the template given below to make a `config.py` file with your `username` and `password`

Install python and then install dependencies using:
> optional: you can setup a virtual env using
> ```
> python -m venv env
> ```
>

```
pip install -r requirements.txt
```

To run:

```
python  asu_sjobs.py
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