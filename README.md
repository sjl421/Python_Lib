# python 库的学习

-----

python的强大之处有很大的一方面在于它有各种各样非常强大的库，那么，这篇博客就是记录我学习各种的库的经历吧。
>声明：
>本人使用的Python版本为 Python2.7.10，Windows 10 操作系统环境下，或者是 Python2.7.10，Ubuntu15 下。
>可以通过命令行背景颜色来区分


后来，我才知道，原来有一本书叫《Python 标准库》,几百个标准库,还有一本书叫Python图像处理的标准库。
[《Python 标准库》](others/python标准库.pdf) [《PythonImagingLibrary中文手册》](others/PythonImagingLibrary中文手册.pdf)

以下是我在Python学习中学到的库函数，也不敢说作为教程，只能算是自己记录下来作为参考。
俗话说的好，好记性不如烂笔头。
具体内容在`content`文件夹里，代码在`code`文件夹里，一些其他的资料在`others`文件夹里。
还有一些用Python做的小项目在`project`文件夹里。

> Python无所不能

## [MySQLdb](content/MySQLdb.md)

## [os](content/os.md)

## [shutil](content/shutil.md)

## [platform](content/platform.md)

## [argparse](content/argparse.md)

## [sys](content/sys.md)

## [File](content/file.md)

## [base64](content/base64.md)

## [hashlib](content/hashlib.md)

## [md5](content/md5.md)

## [binascii](content/binascii.md)

## [media](content/media.md)

## [Image](content/Image.md)

## [PIL](content/PIL.md)

## [smtplib](content/smtplib.md)

## [envelopes](content/envelopes.md)

## [poplib](content/poplib.md)

## [json](content/json.md)

## [time](content/time.md)

## [random](content/random.md)

## [xlwt](content/xlwt.md)

## [xlrd](content/xlrd.md)

## [xlutils](content/xlutils.md)

## [rsa](content/rsa.md)

## [Crypto](content/Crypto.md)

## [getpass](content/getpass.md)

## [glob](content/glob.md)

## [zipfile](content/zipfile.md)

## [gzip](content/gzip.md)

## [tarfile](content/tarfile.md)

## [rarfile](content/rarfile.md)

## [ftplib](content/ftplib.md)

## [operator](content/operator.md)

## [math](content/math.md)

## [functools](content/functools.md)

## [itertools](content/itertools.md)

## [Tkinter](content/Tkinter.md)

## [thread](content/thread.md)

## [threading](content/threading.md)

## [Queue](content/Queue.md)

## [subprocess](content/subprocess.md)

## [ X ] [multiprocessing](content/multiprocessing.md)

## [logging](content/logging.md)

## [socket](content/socket.md)

## [commands](content/commands.md)

## [ X ] [OpenSSL](content/OpenSSL.md)

## [markdown](content/markdown.md)

## [PyQt](content/PyQt.md)

## [py2exe](content/py2exe.md)

## [PyInstaller](content/PyInstaller.md)

## [M2crypto](content/M2crypto.md)

## [re](content/re.md)

## [colorama](content/colorama.md)

## [termcolor](content/termcolor.md)

## [pyscreenshot](content/pyscreenshot.md)

## [PyHook](content/PyHook.md)

## [SimpleHTTPServer](content/SimpleHTTPServer.md)

## [CGIHTTPServer](content/CGIHTTPServer.md)

## [SocketServer](content/SocketServer.md)

## [progressbar](content/progressbar.md)

## [Sphinx](content/Sphinx.md)

## [sqlite3](content/sqlite3.md)

## [docopt](content/docopt.md)

## [ ] [Numpy](content/numpy.md)

## [libtorrent](content/libtorrent.md)

## [string](content/string.md)

## [pycurl](content/pycurl.md)

## [StringIO](content/StringIO.md)

## [pyquery](content/pyquery.md)

## [ ] [lxml](content/lxml.md)

## [webbrowser](content/webbrowser.md)

## [unidecode](content/unidecode.md)

## [ ] [matplotlib](content/matplotlib.md)

## [contextlib](context/contextlib.md)

## panda

## [selenium](content/selenium.md)

## [] [opencv](content/opencv.md)

## [nmap](content/nmap.md)

## [pyftplib](content/pyftplib.md)

## [PyYAML](content/PyYAML.md)

## [csv](content/csv.md)

## [] [signal](content/signal.md)

## [] [asyncore](content/asyncore.md)

## [] [collections](content/collections.md)

## [] [redis](content/redis.md)

## [jieba](content/jieba.md)

## [wordcloud](content/wordcloud.md)

## [pickle](content/pickle.md)

## [urlparse](content/urlparse.md)

## [Other_thing](content/other_thing.md)

## [Reference_link](content/reference_link.md)

安装 pip 最简单的方法还是下载 [get-pip.py](https://bootstrap.pypa.io/get-pip.py),然后运行，简单方便跨平台。

上面有些库是需要自己安装，而安装这些库一般都用pip比较方便，在windows下安装pip可以通过先安装easy_install，再通过安装pip的办法。

然后可以使用 `-i http://pypi.douban.com/simple --trusted-host pypi.douban.com` 来为 pip 加速。

有一些库在 Windows 下可能不好安装，需要自行编译，可以下载别人已经编译好的可执行文件 whl 安装，Python 第三方库网站 [http://www.lfd.uci.edu/~gohlke/pythonlibs/](http://www.lfd.uci.edu/~gohlke/pythonlibs/) ，下载好之后 `pip install XXX.whl` 即可。