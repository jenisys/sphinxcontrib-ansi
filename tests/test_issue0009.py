# SEE: https://github.com/sphinx-contrib/ansi/issues/9
from __future__ import absolute_import, print_function
from docutils import nodes
from .ansi_util import make_paragraph_with_ansi_block
# PREPARED: from .ansi_util import assert_colors, assert_text
import pytest


def test_issue_syndrome(app, parser):
    # text = "Some \x1b[ ... \x1b[0 text"
    text = u"Some \033[94mCOLORED\033[0m text"
    expected_text = "Some COLORED text"

    paragraph = make_paragraph_with_ansi_block(text)
    parser(app, paragraph, "html")
    block = paragraph[0]
    assert isinstance(block, nodes.literal_block)
    assert paragraph.astext() == expected_text
    assert "\033[94m" not in paragraph.astext()

    # assert_colors(block[0], 'bold')
    # assert_text(block[0][0], 'foo')
    # assert_colors(block[1], 'bold', 'yellow')
    # assert_text(block[1][0], 'bar')
    # assert_colors(block[2], 'bold', 'blue')
    # assert_text(block[2][0], 'hello')
    # assert_text(block[3], 'world')
    # assert_colors(block[4], 'bold')
    # assert not block[4].children
    # assert paragraph.astext() == 'foobarhelloworld'
