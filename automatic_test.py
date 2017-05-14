import unittest
import random

import state
import history
import constants


class AutmaticTestt(unittest.TestCase):

    def create_state(self):
        board = {}
        num_of_players = random.randint(2, constants.MAX_PLAYERS)

        for i in range(0, num_of_players):
            board[i] = (random.randint(-1, constants.BOARD_SIZE - 1),
                        random.randint(-1, constants.BOARD_SIZE - 1),
                        random.randint(-1, constants.BOARD_SIZE - 1),
                        random.randint(-1, constants.BOARD_SIZE - 1))

        next_player = random.randint(0, num_of_players-1)
        game_state = state.State(num_of_players, board, next_player)

        return board, num_of_players, game_state, next_player

    def test_get_num_of_players(self):
        board, num, state, next_player = self.create_state()

        self.assertEqual(state.get_num_of_players(), num)
        self.assertEqual(num, len(board))

    def test_get_next_player(self):
        board, num, state, next_player = self.create_state()

        self.assertEqual(next_player, state.get_next_player())

    def test_get_score(self):
        board, num, state, next_player = self.create_state()

        with self.assertRaises(TypeError):
            score = state.get_score()
            score[0] = 15 #Score má byť tupla

    def test_execute_send_enemy_home(self):

        """Test na vyhadzovanie súperovýchv figúrok"""

        board = {}
        num_of_players = 2

        board[0] = (-1, -1, -1, 5)
        board[1] = (6, 6, 6, 6)

        game_state = state.State(num_of_players, board, 0)

        game_history = history.History()

        new_state = game_history.execute(game_state, 1, 3)

        self.assertEqual(new_state.get_board()[1], (-1, -1, -1, -1))

    def test_execute_dice_6(self):

        """Test na to, či ostane rovnaký hráč po hodení 6-timi"""

        board, num, state, next_player = self.create_state()

        game_history = history.History()

        new_state = game_history.execute(state, 6, 0)

        self.assertEqual(new_state.get_next_player(), next_player)

    def test_undo(self):

        board = {}
        num_of_players = 2

        board[0] = (-1, -1, -1, 5)
        board[1] = (6, 6, 6, 6)

        game_state = state.State(num_of_players, board, 0)
        game_history = history.History()

        new_state = game_history.execute(game_state, 1, 3)
        new_state = game_history.undo(new_state)

        new_board = new_state.get_board()

        for key in board:
            self.assertEqual(new_board[key], board[key])


    def test_cycle_board(self):

        """Kontroluje či je správne číslo políčka po
        prekročení max. počtu políčok (cyklickosť hracej plochy)"""

        board = {}
        num_of_players = 2

        watched = constants.BOARD_SIZE - 1;

        board[0] = (-1, -1, -1, 5)
        board[1] = (4, 7, 8, watched)

        game_state = state.State(num_of_players, board, 1)
        game_history = history.History()

        new_state = game_history.execute(game_state, 1, 3)

        self.assertEqual(new_state.get_board()[1][3], 0)


if __name__ == '__main__':
    unittest.main()
