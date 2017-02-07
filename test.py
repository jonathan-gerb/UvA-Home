# -*-coding:utf-8-*-
"""Test file for the media understanding 2017 project.

File name: test.py
Author: Media Undertanding 2017
Date created: 7/2/2017
Date last modified: 7/2/2017
Python Version: 3.4
"""

import newspaper


def main():
    """Main."""
    nu_paper = newspaper.build('http://nu.nl', language='nl')


if __name__ == '__main__':
    main()
