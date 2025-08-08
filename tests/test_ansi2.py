# -- BASED ON: test_ansi.py
from __future__ import absolute_import, print_function
from docutils import nodes
from .ansi_util import (
    make_paragraph_with_ansi_block,
    assert_colors,
    assert_text
)
import pytest


RAW_SOURCE = "\x1b[1mfoo\x1b[33;1mbar\x1b[1;34mhello\x1b[0mworld\x1b[1m"


def test_parser_colors_parsed(app, parser):
    paragraph = make_paragraph_with_ansi_block(RAW_SOURCE)
    parser(app, paragraph, 'foo')
    block = paragraph[0]
    assert isinstance(block, nodes.literal_block)
    assert_colors(block[0], 'bold')
    assert_text(block[0][0], 'foo')
    assert_colors(block[1], 'bold', 'yellow')
    assert_text(block[1][0], 'bar')
    assert_colors(block[2], 'bold', 'blue')
    assert_text(block[2][0], 'hello')
    assert_text(block[3], 'world')
    assert_colors(block[4], 'bold')
    assert not block[4].children
    assert paragraph.astext() == 'foobarhelloworld'
