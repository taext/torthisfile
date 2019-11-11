

```python
import torthisfile as ttf
```


```python
ttf.summary
```




    'Download file via Tor (random IP and user-agent)'




```python
ttf.installation_guide
```




    'apt install tor'




```python
ttf.download("http://nytimes.com")    # defaults to download to ~/Downloads/
```

    
    Restarted Tor service
    Waiting 1 second for Tor service restart to take effect...
    
    Tor URL: 71.19.148.20
    Random User-Agent: Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.2.8) Gecko/20100727 Firefox/3.6.8
    



```python
ttf.download("http://nytimes.com", download_folder="~/Downloads")    # optionally specify download_folder
```

    
    Restarted Tor service
    Waiting 1 second for Tor service restart to take effect...
    
    Tor URL: 104.244.78.102
    Random User-Agent: Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/4.0.202.0 Safari/532.0
    

