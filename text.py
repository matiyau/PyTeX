#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 14 18:45:27 2021

@author: n7
"""

from . import utils as ut


def bf(content):
    return ut.tag("textbf", content)


def it(content):
    return ut.tag("textit", content)


def tt(content):
    return ut.tag("texttt", content)


def ul(content):
    return ut.tag("underline", content)
