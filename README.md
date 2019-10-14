# Let's work with a config files easy!
[Usage](https://github.com/nMagic/easycfg/wiki)

Fast example:
#### **`config.yml`**
```yaml config.yml
servers:
  - host: example1.com
    login: login1
    password: password1
  - host: example2.com
    login: login2
    password: password2
  - host: example3.com
    login: login3
    password: password3
env: prod
```

```python
>>> from easycfg import Config
>>> cfg = Config('config.yml')
>>> cfg.servers
[{'host': 'example1.com', 'login': 'login1', 'password': 'password1'}, {'host': 'example2.com', 'login': 'login2', 'password': 'password2'}, {'host': 'example3.com', 'login': 'login3', 'password':
'password3'}]
>>> cfg.servers[2]
{'host': 'example3.com', 'login': 'login3', 'password': 'password3'}
>>> cfg.servers[:2]
[{'host': 'example1.com', 'login': 'login1', 'password': 'password1'}, {'host': 'example2.com', 'login': 'login2', 'password': 'password2'}]
>>> cfg.servers.login
['login1', 'login2', 'login3']
```

> easycfg supports json and yaml formats now
