#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 14 17:07:40 2021

@author: n7
"""

import os
from . import text as tx
from . import utils as ut


def _get_tabular(tab, col_style=None):
    if col_style is None:
        col_style = "|"
        for col in tab.columns:
            col_style += "c|"

    header = [tx.bf(col) for col in tab.columns]

    ltx = tab.to_latex(header=header, index=False,
                       column_format=col_style, escape=False)

    ltx = ltx.replace(r"\toprule",
                      r"\hline").replace(r"\midrule" + os.linesep,
                                         "").replace(r"\bottomrule" +
                                                     os.linesep,
                                                     "").replace(r"\\",
                                                                 r"\\ \hline")
    return ltx


def get_latex(tab, pos="h!", caption=None, col_style=None, ref=None):
    pos = "[" + pos + "]"
    ltx = _get_tabular(tab, col_style)

    # Encapsulate in "table" tags
    ltx = ut.encapsln("table", ltx, pos, True, caption, "top", ref)

    return ltx
