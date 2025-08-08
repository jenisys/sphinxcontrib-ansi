# -*- coding: UTF-8 -*-
"""
Provides a test helpers for the :mod:`sphinxcontrib.ansi` module.
"""

from __future__ import absolute_import, print_function
from docutils import nodes
from sphinxcontrib import ansi


def make_paragraph_with_ansi_block(source_text):
    """Build a docutils paragraph that contains an ANSI literal-block.

    :param text:  Source text of the ANSI literal-block (as string).
    :return: Paragraph object
    """
    paragraph = nodes.paragraph()
    paragraph.append(ansi.ansi_literal_block(source_text, source_text))
    return paragraph


# -----------------------------------------------------------------------------
# TEST SUPPORT:
# -----------------------------------------------------------------------------
def assert_colors(node, *colors):
    assert isinstance(node, nodes.inline)
    for color in colors:
        assert ('ansi-%s' % color) in node['classes']


def assert_text(node, text):
    assert isinstance(node, nodes.Text)
    assert node.astext() == text
