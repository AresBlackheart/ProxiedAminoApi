# ProxiesAminoApi (BETA)
[![Flask](https://img.shields.io/badge/flask-%23000.svg?style=for-the-badge&logo=flask&logoColor=white)](https://flask.palletsprojects.com/en/2.1.x/)
[![Python Requirement](https://img.shields.io/badge/python-%3E%3D3.7-informational?style=for-the-badge)](https://www.python.org/downloads/)
[![Last commit](https://img.shields.io/github/last-commit/toxichead/ProxiedAminoApi?style=for-the-badge)](https://github.com/toxichead/ProxiedAminoApi/commits/main) [![Issues](https://img.shields.io/github/issues/toxichead/ProxiedAminoApi?style=for-the-badge)](https://github.com/toxichead/ProxiedAminoApi/issues)

Provides easy using a lot of proxies for Amino's API.

## Use cases
If you have a lot of proxies and you build powerful bot for Amino (or doing bad things like autoregs and etc.), it can be hard to integrate and shuffle proxies.

So, this small thing can provide comfortable and powerful work.

## Get started
1. Install Flask
2. Edit port in `proxyapi.py` if you want (by default its 55535)
3. Add proxies in `proxies.txt` in format `ip:port` (at now proxies with authorization not supported, its in plan)
4. Start `proxyapi.py`
5. Change API in your library from `service.narvii.com` to `localhost:{your-port}`

   Examples:
   
```python
import aminofix
client = aminofix.Client()
client.api = "localhost:55535"
# ...
```
