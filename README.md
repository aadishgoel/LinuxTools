# LinuxTools

Hosting tools like grep as a service 

```
GET /grep
{
  searchKeyword: string
  from: timestamp
  to: timestamp
}
```

```
{
 result : []string  
}
```


Works with remote repository using config


## Running on Local
* Step 1 install requirements.py
* Step 2 copy config/sample_config.py as conifg/conifg.py 
* Step 3 python main.py



```
 curl -X GET -H "Content-type: application/json" "localhost:8000/grep" -d "{\"searchString\" : \"hello\", \"from\" : 1712275200, \"to\" : 1712361599 }"
{
  "result": [
    "hello 04-03",
    "hello 04-11"
  ]
}

```