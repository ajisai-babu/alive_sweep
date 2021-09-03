# @Author      : eryi
# @File        : alive_sweep.py
# @PROJECT_NAME: 存活探测
# @Software    : PyCharm

import concurrent.futures
import requests
import csv
from lib.cmdline import cmdline_parser


def load_url(url, timeout):
    resp = requests.get(url, timeout=timeout)
    return resp.status_code, url


def file_read(filename):
    urls = []
    with open(filename) as reader:
        for url in reader:
            urls.append(url.strip())
    return urls


def csv_read(filename):
    url_list = []
    if 'csv' in filename:
        with open(filename) as f:
            reader = csv.DictReader(f)
            for i in reader:
                url_list.append(i['url'])
    return url_list


def file_output(filename, url):
    try:
        with open(filename, "a+", encoding='utf-8') as f:
            f.writelines(url + "\n")
    except:
        pass


def sweep():
    with concurrent.futures.ThreadPoolExecutor(max_workers=connections) as executor:
        future_to_url = (executor.submit(load_url, url, timeout) for url in urls)
        for future in concurrent.futures.as_completed(future_to_url):
            try:
                data = future.result()
                print(data[1])
            except Exception as exc:
                data = None
            finally:
                out.append(data)


if __name__ == '__main__':
    args = cmdline_parser()
    out = []
    connections = 100
    timeout = 5

    if args.csv is not None:
        urls = csv_read(args.csv)
    else:
        urls = file_read(args.file)

    sweep()

    if args.output is not None:
        for i in out:
            if i is not None:
                file_output(args.output, i[1])

