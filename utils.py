#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 14 17:54:01 2021

@author: n7
"""

import numpy as np
import os


def tag(name, content, arg=None, newline=False):
    return "\\" + name + "{" + content + "}" + \
        (arg if arg is not None else "") + \
        (os.linesep if newline is True else "")


def tagln(name, content, arg=None):
    return tag(name, content, arg, True)


def begin(content, arg=None):
    return tagln("begin", content, arg)


def end(content):
    return tagln("end", content)


def capt(content):
    return tagln("caption", content)


def label(content):
    return tagln("label", content)


def inline_math_pts(content):
    return np.array([i for i in range(0, len(content)) if content[i] == "$"])


def escape(content):
    non_math_pts = np.concatenate([[-1] + inline_math_pts(content) +
                                   [len(content)]]).reshape(-1, 2)
    non_math_pts[:, 0] += 1
    for pts in non_math_pts:
        pre = content[:pts[0]]
        main = content[pts[0]:pts[1]]
        post = content[pts[1]:]
        main = main.replace("&", "\\&").replace("%", "\\%").replace("_", "\\_")
        content = pre + main + post
    return content


def encaps(env, content, arg=None, center=False, caption=None,
           capt_pos="bottom", ref=None, addl_newline=False):
    prefix = begin(env, arg) + \
        (("\\centering" + os.linesep) if center is True else "")
    suffix = (label(env + ":" + ref) if ref is not None else "") + end(env)
    if caption is not None:
        if (capt_pos == "top"):
            prefix += capt(caption)
        elif (capt_pos == "bottom"):
            suffix = capt(caption) + suffix
    ltx = prefix + content + suffix
    return ltx


def encapsln(env, content, arg=None, center=False, caption=None,
             capt_pos="bottom", ref=None):
    return encaps(env, content, arg, center, caption, capt_pos, ref, True)
