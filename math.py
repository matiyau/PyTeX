#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 14 22:45:08 2021

@author: n7
"""

import utils as ut


def sbscr(content):
    """
    Get LaTeX code for displaying the given content in subscript.

    Parameters
    ----------
    content : str
        Content to be displayed in subscript.

    Returns
    -------
    str
        LaTeX code for subscripted content.

    """
    return "_{" + content + "}" if content is not None else ""


def spscr(content):
    """
    Get LaTeX code for displaying the given content in superscript.

    Parameters
    ----------
    content : str
        Content to be displayed in superscript.

    Returns
    -------
    str
        LaTeX code for superscripted content.

    """
    return "^{" + content + "}" if content is not None else ""


def sigma(sb=None, sp=None):
    """
    Generate LaTeX code for summation sign.

    Parameters
    ----------
    sb : str or None, optional
        Subscript content (start condition) for the summation. If None, no
        subscript is added. The default is None.
    sp : str or None, optional
        Superscript content (end condition) for the summation. If None, no
        superscript is added. The default is None.

    Returns
    -------
    str
        LaTeX code for summation sign.

    """
    return r"\sum" + sbscr(sb) + spscr(sp)


def Pi(sb=None, sp=None):
    """
    Generate LaTeX code for product sign.

    Parameters
    ----------
    sb : str or None, optional
        Subscript content (start condition) for the product. If None, no
        subscript is added. The default is None.
    sp : str or None, optional
        Superscript content (end condition) for the product. If None, no
        superscript is added. The default is None.

    Returns
    -------
    str
        LaTeX code for product sign.

    """
    return r"\Pi" + sbscr(sb) + spscr(sp)


def floor(content):
    """
    Generate LaTeX code for data within floor braces.

    Parameters
    ----------
    content : str
        String to be encapsulated within the floor sign.

    Returns
    -------
    str
        LaTeX code for data within floor braces.

    """
    return ut.tag("floor", content)


def ceil(content):
    """
    Generate LaTeX code for data within ceiling braces.

    Parameters
    ----------
    content : str
        String to be encapsulated within the ceil sign.

    Returns
    -------
    str
        LaTeX code for data within ceiling braces.

    """
    return ut.tag("ceil", content)


def frac(n, d):
    """
    Generate LaTeX fraction.

    Parameters
    ----------
    n : str
        Numerator for the fraction.
    d : str
        Denominator for the fraction.

    Returns
    -------
    str
        LaTeX code for fraction.

    """
    return ut.tag("frac", n, d)


def times(a, b):
    """
    Generate LaTeX code for multiplication.

    Parameters
    ----------
    a : str
        First operand of multiplication.
    b : str
        Second operand of multiplication.

    Returns
    -------
    str
        LaTeX code for multiplication.

    """
    return a + r" \times " + b
