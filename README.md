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
