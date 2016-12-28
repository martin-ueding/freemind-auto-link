#!/usr/bin/python3
# -*- coding: utf-8 -*-

# Copyright © 2016 Martin Ueding <dev@martin-ueding.de>

import argparse
import os

from lxml import etree


def main():
    options = _parse_args()

    tree = etree.parse(options.xml_file)

    for node in tree.xpath('//node'):
        text = node.get('TEXT')
        filename = os.path.join(options.literature_directory, text + '.pdf')
        if not os.path.isfile(filename):
            continue

        link = node.get('LINK')
        relpath = os.path.relpath(filename, os.path.dirname(options.xml_file))

        if link != relpath:
            print(link, relpath)

            node.set('LINK', relpath)

    with open(options.new_xml_file, 'wb') as f:
        tree.write(f)


def _parse_args():
    '''
    Parses the command line arguments.

    :return: Namespace with arguments.
    :rtype: Namespace
    '''
    parser = argparse.ArgumentParser(description='')
    parser.add_argument('xml_file')
    parser.add_argument('literature_directory')
    parser.add_argument('new_xml_file')
    options = parser.parse_args()

    return options


if __name__ == '__main__':
    main()
