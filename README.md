

```python
import torthisfile as ttf           # wget https://v1d.dk/z/ttf.zip
```


```python
ttf.about()
```

    Download file via Tor (with random IP and user-agent)
    v2.04 - November 11th 2019 - by github/taext



```python
ttf.installation_guide()
```

    1. apt install tor
    2. input sudo password in easy_sudo file



```python
ttf.download("http://nytimes.com")  # defaults to download to ~/Downloads/
```

    
    Restarted Tor service
    Waiting 1 second for Tor service restart to take effect...
    
    Tor URL: 185.220.102.7
    Random User-Agent: Mozilla/5.0 (Macintosh; U; PPC Mac OS X; de-de) AppleWebKit/85.8.5 (KHTML, like Gecko) Safari/85
    



```python
ttf.download("http://nytimes.com", download_folder="~/Downloads")  # optionally specify download_folder
```

    
    Restarted Tor service
    Waiting 1 second for Tor service restart to take effect...
    
    Tor URL: 109.70.100.23
    Random User-Agent: Mozilla/5.0 (Windows NT 4.0; U) Opera 6.05  [en]
    



```python
ttf.user_guide()             # link to this user-guide (https://v1d.dk/h/ttf.htm)
ttf.syntax_highlight_code()  # link to code with syntax highlighting (https://v1d.dk/h/ttf.png)
```
