#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 14 19:46:52 2021

@author: n7
"""

import utils as ut
import os


def incl_image(path, width_ratio=1):
    if (path[-3:] == "svg"):
        cmd = "includesvg"
    else:
        cmd = "includegraphics"
    cmd += "[width=" + str(width_ratio) + r"\linewidth]"
    return ut.tagln(cmd, path)


def get_latex(filenames, loc="Body/figures", stretch=False,
              pos="h!", caption=None, ref=None):
    if type(filenames) is str:
        filenames = [filenames]
    tag = "figure"
    if stretch:
        tag += "*"
    pos = "[" + pos + "]"

    width_ratio = round(1/len(filenames), 2) - 0.01
    ltx = ""
    for filename in filenames:
        ltx += incl_image(os.path.join(loc, filename), width_ratio)

    # Encapsulate in "figure" tags
    ltx = ut.encapsln(tag, ltx, pos, True, caption, "bottom", ref)

    return ltx
