#!/usr/bin/env python

import logging

from gi.repository import Gtk

from gol_gtk.main import GameOfLiveGtk

logger = logging.getLogger()


if __name__ == '__main__':
    import sys

    logger.addHandler(logging.StreamHandler(stream=sys.stdout))
    logger.setLevel(logging.DEBUG)

    logger.info('Start Game Of Life GTK version.')

    game = GameOfLiveGtk(title='Conway\'s Game of Life')

    Gtk.main()