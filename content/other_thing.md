## 额外的东西

1. python自带了一个简单web的服务器，当前目录下启动,就可以在`localhost:8080`查看。

```python
python -m SimpleHTTPServer 8080
```

还有CGI服务器。

```python
python -m CGIHTTPServer 8080
```

还有 FTP 服务器

```
python -m pyftpdlib
```

还有在线文档

```
python -m pydoc -p 8000
```

2. python2 与 python3 共存的问题，我的解决方式是 Python2 就叫 python , pyhton3 则是 Python34 ,但是 pip 却不能这样做，python3 的 pip 可以这样使用 `python34 -m pip install requests`,然后就可以写一个 pip3.py 来这样。

```
# coding=utf-8

import sys
import subprocess
print(" ".join(sys.argv))
cmd = "python34 -m pip " + " ".join(sys.argv[1:] + " -i http://pypi.douban.com/simple --trusted-host pypi.douban.com")
obj = subprocess.Popen(cmd)
obj.wait()
```

其实你只需要把 python3 的 script 路径也导入 环境变量中就好了。。。

2. 还可以不用进入 Python shell 执行 Python 语句,`python -c "import request" `。

3. PHP 5.4版本及以上也自带了一个简单的web服务器，在当前目录下启动，就可以在`localhost:8000`查看。

```php
php -S localhost:8000
```

4. 最简单的nodejs的服务器。

```javascript
var http = require('http');
http.createServer(function (req, res) {
    res.send('Hello');
    res.end();
}).listen(3000);

```

保存为server.js,在当前目录下cmd里输入`node server.js`即可调用，在`localhost:3000`查看。
