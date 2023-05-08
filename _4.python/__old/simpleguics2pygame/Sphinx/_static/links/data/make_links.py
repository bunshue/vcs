# -*- coding: utf-8 -*-

"""
Module
  to make_img_links.py ,
     make_prog_links.py ,
     make_snd_links.py
(May 21, 2020)

Piece of SimpleGUICS2Pygame.
https://bitbucket.org/OPiMedia/simpleguics2pygame

GPLv3 --- Copyright (C) 2013, 2015, 2016, 2020 Olivier Pirson
http://www.opimedia.be/
"""

import os.path
import urllib.parse

from typing import List, TextIO


def print_html_list_img(data: List, dest_file: TextIO) -> None:
    """
    Print data as HTML <ul> in dest_file.

    :param data: List as builded by read_txt()
    :param dest_file: file open in writing
    """
    assert isinstance(data, list), type(data)

    print('<ul>', file=dest_file)

    for items in data:
        assert isinstance(items, list), type(items)
        assert len(items) > 0

        if len(items) == 0:
            continue

        assert isinstance(items[0], str), type(items[0])

        print("""  <li>
    {}
    <ul class="images">""".format(items[0]), file=dest_file)

        for url, info, _ in items[1:]:
            assert isinstance(url, str), type(url)
            assert isinstance(info, str), type(info)

            if info == '':
                info = '{}'.format(url_to_info(url))
                add_class = ' class="url"'
            else:
                add_class = ''

            print("""      <li>
        <a{2} href="{0}" target="_blank" onmouseover="img_load(this, '{0}');"><img src="#" alt="[Loading&hellip;]"><span class="size"><span></span></span><img class="thumbnail" src="{0}" alt=""><span class="name">{1}</span></a>
      </li>""".format(url, info, add_class), file=dest_file)  # noqa

        print("""    </ul>
  </li>""", file=dest_file)

    print('</ul>', file=dest_file)


def print_html_list_link(data: List, dest_file: TextIO) -> None:
    """
    Print data as HTML <ul> in dest_file.

    :param data: List as builded by read_txt()
    :param dest_file: file open in writing
    """
    assert isinstance(data, list), type(data)

    print('<ul>', file=dest_file)

    for items in data:
        assert isinstance(items, list), type(items)
        assert len(items) > 0

        if len(items) == 0:
            continue

        assert isinstance(items[0], str), type(items[0])

        print("""  <li>
    {}
    <ul class="progs">""".format(items[0]), file=dest_file)

        for url, info, info2 in items[1:]:
            assert isinstance(url, str), type(url)
            assert isinstance(info, str), type(info)

            if info == '':
                info = '{}'.format(url_to_info(url))
                add_class = ' class="url"'
            else:
                add_class = ''

            print("""      <li>
        <a{2} href="{0}" target="_blank">{1}</a>{3}
      </li>""".format(url, info, add_class,
                      (' <span>{}</span>'.format(info2)
                       if info2 != ''
                       else '')), file=dest_file)

        print("""    </ul>
  </li>""", file=dest_file)

    print('</ul>', file=dest_file)


def print_html_list_snd(data: List, dest_file: TextIO) -> None:
    """
    Print data as HTML <ul> in dest_file.

    :param data: List as builded by read_txt()
    :param dest_file: file open in writing
    """
    assert isinstance(data, list), type(data)

    print('<ul>', file=dest_file)

    for items in data:
        assert isinstance(items, list), type(items)
        assert len(items) > 0

        if len(items) == 0:
            continue

        assert isinstance(items[0], str), type(items[0])

        print("""  <li>
    {}
    <ul class="sounds">""".format(items[0]), file=dest_file)

        for url, info, _ in items[1:]:
            assert isinstance(url, str), type(url)
            assert isinstance(info, str), type(info)

            if info == '':
                info = '{}'.format(url_to_info(url))
                add_class = ' class="url"'
            else:
                add_class = ''

            print("""      <li>
        <a{2} href="{0}" target="_blank">{1}</a><audio src="{0}" controls="controls"></audio>
      </li>""".format(url, info, add_class), file=dest_file)  # noqa

        print("""    </ul>
  </li>""", file=dest_file)

    print('</ul>', file=dest_file)


def read_txt(filename: str) -> List:
    """
    Read filename and build a list to use with print_html_list_*().

    :param filename: str

    :returns: List of [str, [str, str, str]*]
    """
    assert isinstance(filename, str), type(filename)

    data = []

    fin = open(filename, encoding='latin-1')
    lines = [line.strip() for line in fin]
    fin.close()

    acc = []  # type: List

    i = 0
    while i < len(lines):
        line = lines[i]
        i += 1

        if line == '':
            continue

        if line[:2] == '+ ':
            line = line[2:]
            if len(acc) > 0:
                data.append(acc)
            acc = [line]
        else:
            triplet = [line, '', '']

            if i < len(lines):
                triplet[1] = lines[i]
                i += 1

            if (i < len(lines)) and (triplet[1] != ''):
                triplet[2] = lines[i]
                i += 1

            acc.append(triplet)

    if len(acc) > 0:
        data.append(acc)

    return data


def url_to_info(url: str) -> str:
    """
    Return a clean info name extracted from url.

    :param url: str

    :return: str
    """
    return os.path.basename(urllib.parse.unquote(url))
