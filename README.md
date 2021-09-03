# alive_sweep
url存活探测小脚本

使用方法：

```shell
python alive_sweep.py -h
usage: python alive_sweep.py -f urllist.txt

Powered by Eryi

optional arguments:
  -h, --help            show this help message and exit
  -f FILE, --file FILE  从文件中读取扫描目标
  -o OUTPUT, --output OUTPUT
                        输出结果URL到文件(default=[time].txt)
  -c CSV, --csv CSV     oneforall输出csv文件直接扫描
  -t THREAD, --thread THREAD
                        扫描线程设置(default=100)


```



- 扫描txt

  ```shell
  python alive_sweep.py -f urllist.txt
  ```

- 扫描oneforall生成的csv文件

  ```shell
  python alive_sweep.py -c ahstu.edu.cn.csv
  ```

- 自定义输出文件名[默认是当前时间.txt]

  ```shell
  python alive_sweep.py -f urllist.txt -o test.txt
  ```

- 自定义线程[默认是100]

  ```shell
  python alive_sweep.py -c ahstu.edu.cn.csv -t 400 -o ahstu.txt
  ```
