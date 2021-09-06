# @Author      : eryi
# @File        : alive_sweep.py
# @PROJECT_NAME: 存活探测
# @Software    : PyCharm

import concurrent.futures
import requests
import csv
from lib.cmdline import cmdline_parser
from urllib.parse import urlparse
from tqdm import tqdm


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


def rapid_read(filename):
    url_list = []
    url_original = []
    if 'csv' in filename:
        with open(filename, encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for i in reader:
                url_original.append("http://" + i['Domain'])
                url_original.append("https://" + i['Domain'])

    for x in url_original:
        if x not in url_list:
            url_list.append(x)
    return url_list


def file_output(filename, url):
    try:
        with open(filename, "a+", encoding='utf-8') as f:
            f.writelines(url + "\n")
    except:
        pass


def sweep():
    pbar = tqdm(total=len(urls))

    with concurrent.futures.ThreadPoolExecutor(max_workers=connections) as executor:
        future_to_url = (executor.submit(load_url, url, timeout) for url in urls)
        for future in concurrent.futures.as_completed(future_to_url):
            try:
                data = future.result()
                pbar.set_description("Processing %s" % str(data[1]))
                # print(data[1])
            except Exception as exc:
                data = None
            finally:
                out.append(data)
                pbar.update(1)

    pbar.set_description_str("Done! ")
    pbar.close()


if __name__ == '__main__':
    args = cmdline_parser()
    out = []
    connections = args.thread
    timeout = 5
    domains = []

    if args.csv is not None:
        urls = csv_read(args.csv)
    elif args.rapid is not None:
        urls = rapid_read(args.rapid)
    else:
        urls = file_read(args.file)

    sweep()

    if args.output is not None:
        for i in out:
            if i is not None:
                domain = urlparse(str(i[1])).netloc
                # print(domain)

                if domain not in domains:
                    # print(domain)
                    file_output(args.output, i[1])
                domains.append(domain)

