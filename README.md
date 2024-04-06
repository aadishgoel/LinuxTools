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


can work on remote respository using config


## Installation
* Step 1 install requriments.py
* Step 2 copy config/sample_config.py as conifg/conifg.py 