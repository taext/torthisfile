

```python
import torthisfile as ttf
```


```python
print(ttf.summary + "\n" + ttf.version + " - " + ttf.date + " - by " + ttf.author)
```

    Download file via Tor (with random IP and user-agent)
    v2.01 - November 10th 2019 - by github/taext



```python
ttf.installation_guide
```




    'apt install tor'




```python
ttf.download("http://nytimes.com")    # defaults to download to ~/Downloads/
```

    
    Restarted Tor service
    Waiting 1 second for Tor service restart to take effect...
    
    Tor URL: 109.70.100.21
    Random User-Agent: Mozilla/5.0 (X11; U; Linux i686; fr; rv:1.9.0.2) Gecko/2008092313 Ubuntu/8.04 (hardy) Firefox/3.0.2
    



```python
ttf.download("http://nytimes.com", download_folder="~/Downloads")    # optionally specify download_folder
```

    
    Restarted Tor service
    Waiting 1 second for Tor service restart to take effect...
    
    Tor URL: 94.230.208.148
    Random User-Agent: Mozilla/5.0 (Windows; U; Windows NT 6.1; cs; rv:1.9.2.3) Gecko/20100401 Firefox/3.6.3 ( .NET CLR 3.5.30729)
    

