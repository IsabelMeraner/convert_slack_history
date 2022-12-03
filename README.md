#  README

### convert_slack_history
Conversion script for extracting usernames, time stamps and text messages from an exported slack channel history export.

### install requirements
`$ pip install -r requirements.txt`

### how to run:
`$ python3 get_slack_history.py --path PATH_TO_INPUT_FOLDER`

### input folder structure (unzipped slack export)
```
channel1
    2022-02-26.json 
    2022-03-02.json 
channel2
    2022-03-09.json 
    2022-05-04.json 
    2022-06-23.json
    2022-02-28.json 
    2022-03-05.json 
channel3
    2022-03-11.json 
    2022-05-23.json
    2022-03-01.json 
    2022-03-07.json 
    2022-03-22.json 
    2022-06-04.json
etc...
```

### output:
```
USER_NAME (2022-08-04 07:02:23):
TEXT MESSAGE
```

