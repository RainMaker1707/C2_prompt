You will use the online documentation provided in the documentation section of your instructions and files in /mnt/data/data/ as knowledge background.
Each files in this directory is labelled by files in /mnt/data/labels/directory.
For example

The file /mnt/data/data/sessions/http/on_off.csv is labelled in the sliver file.
The referring label is a data object in the data section of the sliver.json file.
It is this one:
In this extract lines or part of lines beginning with # are commentary for your understanding.
```json
# sliver.csv extract 
{
    "frameworkName": "Sliver",
    "data": [
        # ...  other data objects 
        {
            "ID": 2,
            "filename": "/mnt/data/data/sessions/mtls/on_off.csv", # the file labelled in this data objects
            "connectionType": "session", # the connectionType used by the framework
            "protocol": "mtls", # the internet protocol used to communicate
            "stager": 0, # 1 if a stager has been used to generate the implant, else 0 
            "custom": 0,  # 1 if a custom implant has been used, else 0 
        },
        # ... other data objects
    ]
}
```

You must use these data objects to know if the file represent an infected example sor not.
You must use these reference represent in the labels data objects to replace correctly the part of the output format.