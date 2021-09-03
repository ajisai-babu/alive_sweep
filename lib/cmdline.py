# @Author      : eryi
# @File        : cmdline.py
# @PROJECT_NAME: 存活探测
# @Software    : PyCharm

import argparse
import sys
import time


def cmdline_parser():
    parser = argparse.ArgumentParser(description='Powered by Eryi ',
                                     usage='python alive_sweep.py -f urllist.txt',
                                     add_help=True)

    parser.add_argument('-f', '--file', help='从文件中读取扫描目标')
    parser.add_argument('-o', '--output', help='输出结果URL到文件(default=[time].txt)', default=time.strftime("%Y-%m-%d-%H"
                                                                                                       "-%M-%S.txt",
                                                                                                       time.localtime()))
    parser.add_argument('-c', '--csv', help='oneforall输出csv文件直接扫描')
    parser.add_argument('-t', '--thread', type=int, help='扫描线程设置(default=100)', default=100)

    if len(sys.argv) == 1:
        sys.argv.append('-h')
    return parser.parse_args()
