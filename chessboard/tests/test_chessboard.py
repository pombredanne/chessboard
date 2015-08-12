# -*- coding: utf-8 -*-
#
# Copyright (c) 2015 Kevin Deldycke <kevin@deldycke.com> and contributors.
# All Rights Reserved.
#
# This program is Free Software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 2
# of the License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place - Suite 330, Boston, MA  02111-1307, USA.

from __future__ import (unicode_literals, print_function, absolute_import,
                        division)

import unittest

from chessboard import Chessboard, Board, ForbiddenIndex


class TestChessboard(unittest.TestCase):

    def test_instanciation(self):
        board = Chessboard(3, 3, king=2, queen=7)
        self.assertEquals(board.length, 3)
        self.assertEquals(board.height, 3)
        self.assertDictContainsSubset({'king': 2, 'queen': 7}, board.pieces)


class TestSolver(unittest.TestCase):

    def test_tinyest_board(self):
        board = Chessboard(1, 1, king=1)
        results = board.solve()
        self.assertEquals(len(results), 1)

    def test_single_king(self):
        board = Chessboard(3, 3, king=1)
        results = board.solve()
        self.assertEquals(len(results), 9)

    def test_wide_board(self):
        board = Chessboard(4, 1, king=1)
        results = board.solve()
        self.assertEquals(len(results), 4)

    def test_long_board(self):
        board = Chessboard(1, 4, king=1)
        results = board.solve()
        self.assertEquals(len(results), 4)

    def test_single_queen(self):
        board = Chessboard(3, 3, queen=1)
        results = board.solve()
        self.assertEquals(len(results), 9)

    def test_no_queen_solutions(self):
        board = Chessboard(3, 3, queen=2)
        results = board.solve()
        self.assertEquals(len(results), 0)


class TestBoard(unittest.TestCase):

    def test_linear_position(self):
        self.assertEquals(Board(3, 3).linear_position(0), (0, 0))
        self.assertEquals(Board(3, 3).linear_position(1), (1, 0))
        self.assertEquals(Board(3, 3).linear_position(2), (2, 0))
        self.assertEquals(Board(3, 3).linear_position(3), (0, 1))
        self.assertEquals(Board(3, 3).linear_position(4), (1, 1))
        self.assertEquals(Board(3, 3).linear_position(5), (2, 1))
        self.assertEquals(Board(3, 3).linear_position(6), (0, 2))
        self.assertEquals(Board(3, 3).linear_position(7), (1, 2))
        self.assertEquals(Board(3, 3).linear_position(8), (2, 2))

    def test_linear_position_error(self):
        with self.assertRaises(ForbiddenIndex):
            Board(3, 3).linear_position(-1)
        with self.assertRaises(ForbiddenIndex):
            Board(3, 3).linear_position(9)
