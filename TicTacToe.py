import pygame
import random

WIN_HEIGHT = 625
WIN_WIDTH = 800


class TicTacToe:
    def __init__(self):
        self.board = [[' '] * 3 for i in range(3)]
        self.available_moves = [(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)]

    def check_win(self, symbol):
        # Horizontally
        for row in self.board:
            if row.count(symbol) == 3:
                return True

        # Vertically
        for j in range(3):
            if self.board[0][j] == self.board[1][j] == self.board[2][j] == symbol:
                return True

        # Diagonally
        if self.board[0][0] == self.board[1][1] == self.board[2][2] == symbol:
            return True
        elif self.board[0][2] == self.board[1][1] == self.board[2][0] == symbol:
            return True

        else:
            return False

    def evaluate_board(self):
        if self.check_win("X"):
            return 1
        if self.check_win("O"):
            return -1

        return 0

    def game_over(self):
        if self.check_win("X") or self.check_win("O") or len(game.available_moves) == 0:
            return True

        return False

    def minimax(self, is_maximizing):
        if self.game_over():
            return [self.evaluate_board(), ()]

        best_move = ()

        if is_maximizing:
            best_value = -float('Inf')
            symbol = "X"
        else:
            best_value = float('Inf')
            symbol = "O"

        for i in range(3):
            for j in range(3):
                if self.board[i][j] == ' ':
                    self.board[i][j] = symbol
                    self.available_moves.remove((i, j))
                    value = self.minimax(not is_maximizing)[0]
                    self.board[i][j] = ' '
                    self.available_moves.append((i, j))

                    if is_maximizing:
                        if value > best_value:
                            best_value = value
                            best_move = (i, j)
                    else:
                        if value < best_value:
                            best_value = value
                            best_move = (i, j)

        return [best_value, best_move]

    def print_board(self):
        print(f'{self.board[0][0]} | {self.board[0][1]} | {self.board[0][2]}')
        print('----------')
        print(f'{self.board[1][0]} | {self.board[1][1]} | {self.board[1][2]}')
        print('----------')
        print(f'{self.board[2][0]} | {self.board[2][1]} | {self.board[2][2]}')
        print('\n')


def draw_board(win):
    pygame.draw.line(win, (255, 255, 255), (250, 200), (550, 200), 5)
    pygame.draw.line(win, (255, 255, 255), (250, 300), (550, 300), 5)
    pygame.draw.line(win, (255, 255, 255), (350, 100), (350, 400), 5)
    pygame.draw.line(win, (255, 255, 255), (450, 100), (450, 400), 5)
    pygame.display.update()


def draw_symbol(win, symbol, symbol_pos):
    if symbol == "O":
        pygame.draw.circle(win, (255, 0, 0), (symbol_pos[0], symbol_pos[1]), 35, 5)

    elif symbol == "X":
        pygame.draw.line(win, (0, 255, 0), (symbol_pos[0] - 20, symbol_pos[1] - 30),
                         (symbol_pos[0] + 20, symbol_pos[1] + 30), 5)
        pygame.draw.line(win, (0, 255, 0), (symbol_pos[0] - 20, symbol_pos[1] + 30),
                         (symbol_pos[0] + 20, symbol_pos[1] - 30), 5)


def draw_start_screen(win, wait_for_input):
    win.fill((0, 0, 0))
    game_name = title_font.render('Tic Tac Toe', True, (255, 255, 255))
    game_name_rect = game_name.get_rect(center=(400, 125))
    win.blit(game_name, game_name_rect)

    pvp_button = pygame.Surface((275, 65))
    pvp_button.fill('White')
    pvp_button_rect = pvp_button.get_rect(center=(400, 300))
    win.blit(pvp_button, pvp_button_rect)

    pvp_text = font.render('Vs. Player', True, (0, 0, 0))
    pvp_text_rect = pvp_text.get_rect(center=(400, 300))
    win.blit(pvp_text, pvp_text_rect)

    pvc_button1 = pygame.Surface((325, 65))
    pvc_button1.fill('White')
    pvc_button1_rect = pvc_button1.get_rect(center=(400, 400))
    win.blit(pvc_button1, pvc_button1_rect)

    pvc_text1 = font.render('Vs. Comp as X', True, (0, 0, 0))
    pvc_text1_rect = pvc_text1.get_rect(center=(400, 400))
    win.blit(pvc_text1, pvc_text1_rect)

    pvc_button2 = pygame.Surface((325, 65))
    pvc_button2.fill('White')
    pvc_button2_rect = pvc_button2.get_rect(center=(400, 500))
    win.blit(pvc_button2, pvc_button2_rect)

    pvc_text2 = font.render('Vs. Comp as O', True, (0, 0, 0))
    pvc_text2_rect = pvc_text2.get_rect(center=(400, 500))
    win.blit(pvc_text2, pvc_text2_rect)

    game_active = False
    pvp = False
    playerSym = ""

    if wait_for_input > 60 and pygame.mouse.get_pressed()[0]:
        mouse_pos = pygame.mouse.get_pos()
        if pvp_button_rect.collidepoint(mouse_pos):
            game_active = True
            pvp = True
        if pvc_button1_rect.collidepoint(mouse_pos):
            game_active = True
            pvp = False
            playerSym = "X"
        if pvc_button2_rect.collidepoint(mouse_pos):
            game_active = True
            pvp = False
            playerSym = "O"

    return game_active, pvp, playerSym


def draw_win_message(win, winning_symbol):
    if winning_symbol == "":
        win_msg = font.render("It's a Tie", True, (255, 255, 255))
        win_msg_rect = win_msg.get_rect(center=(400, 450))
    else:
        win_msg = font.render(f'{winning_symbol} wins!', True, (255, 255, 255))
        win_msg_rect = win_msg.get_rect(center=(400, 450))

    win.blit(win_msg, win_msg_rect)

    restart_button = pygame.Surface((175, 50))
    restart_button.fill('White')
    restart_button_rect = restart_button.get_rect(center=(275, 530))
    win.blit(restart_button, restart_button_rect)

    restart_text = font.render('Restart', True, (0, 0, 0))
    restart_text_rect = restart_text.get_rect(center=(275, 530))
    win.blit(restart_text, restart_text_rect)

    main_menu_button = pygame.Surface((250, 50))
    main_menu_button.fill('White')
    main_menu_button_rect = main_menu_button.get_rect(center=(525, 530))
    win.blit(main_menu_button, main_menu_button_rect)

    main_menu_text = font.render('Main Menu', True, (0, 0, 0))
    main_menu_text_rect = main_menu_text.get_rect(center=(525, 530))
    win.blit(main_menu_text, main_menu_text_rect)

    restart = False
    main_menu = False

    if pygame.mouse.get_pressed()[0]:
        mouse_pos = pygame.mouse.get_pos()
        if restart_button_rect.collidepoint(mouse_pos):
            restart = True
        if main_menu_button_rect.collidepoint(mouse_pos):
            main_menu = True

    return restart, main_menu


def get_board_symbol_pos(mouse_pos):
    board_pos = [(mouse_pos[1] // 100) - 1, -1]
    if 250 < mouse_pos[0] < 350:
        board_pos[1] = 0
    elif 350 < mouse_pos[0] < 450:
        board_pos[1] = 1
    elif 450 < mouse_pos[0] < 550:
        board_pos[1] = 2
    symbol_pos = ((board_pos[1] * 100) + 300, (board_pos[0] * 100) + 150)
    return tuple(board_pos), symbol_pos


def get_comp_symbol_pos(comp_best_move):
    symbol_pos = ((comp_best_move[1] * 100) + 300, (comp_best_move[0] * 100) + 150)
    return symbol_pos


pygame.init()
win = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
pygame.display.set_caption('Tic Tac Toe')
font = pygame.font.SysFont('timesnewroman', 45)
title_font = pygame.font.SysFont('timesnewroman', 80)
clock = pygame.time.Clock()

game = TicTacToe()
game_active = False
game_over = False
winning_symbol = ''
draw_black_screen = True
wait_for_input = 0

AI_LEVEL = 5

while True:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    if game_active:
        if draw_black_screen:
            win.fill((0, 0, 0))
            draw_black_screen = False

        wait_for_input += 2
        if wait_for_input > 70:
            wait_for_input = 70
        draw_board(win)

        if pvp:
            if not game_over and wait_for_input > 60 and pygame.mouse.get_pressed()[0]:
                mouse_pos = pygame.mouse.get_pos()
                board_pos, symbol_pos = get_board_symbol_pos(mouse_pos)
                if board_pos in game.available_moves:
                    if player1Turn:
                        symbol = "X"
                    else:
                        symbol = "O"

                    wait_for_input = 0
                    player1Turn = not player1Turn
                    draw_symbol(win, symbol, symbol_pos)
                    game.board[board_pos[0]][board_pos[1]] = symbol
                    game.available_moves.remove(board_pos)
                    game.print_board()
                    if game.check_win(symbol):
                        print(f'{symbol} wins !')
                        winning_symbol = symbol
                        game_over = True
                    elif len(game.available_moves) == 0:
                        print("It's a Tie\n")
                        game_over = True

        else:
            if playerTurn:
                if not game_over and wait_for_input > 60 and pygame.mouse.get_pressed()[0]:
                    mouse_pos = pygame.mouse.get_pos()
                    board_pos, symbol_pos = get_board_symbol_pos(mouse_pos)

                    if board_pos in game.available_moves:
                        wait_for_input = 0
                        playerTurn = not playerTurn
                        draw_symbol(win, playerSym, symbol_pos)
                        game.board[board_pos[0]][board_pos[1]] = playerSym
                        game.available_moves.remove(board_pos)
                        game.print_board()
                        if game.check_win(playerSym):
                            print(f'{playerSym} wins !')
                            winning_symbol = playerSym
                            game_over = True
                        elif len(game.available_moves) == 0:
                            print("It's a Tie\n")
                            game_over = True
            else:
                if not game_over:
                    if random.randint(1, 5) <= AI_LEVEL:
                        comp_move = game.minimax(is_maximizing)[1]
                    else:
                        comp_move = random.choice(game.available_moves)
                    symbol_pos = get_comp_symbol_pos(comp_move)
                    draw_symbol(win, compSym, symbol_pos)
                    game.board[comp_move[0]][comp_move[1]] = compSym
                    game.available_moves.remove(comp_move)
                    playerTurn = not playerTurn
                    game.print_board()
                    if game.check_win(compSym):
                        print(f'{compSym} wins !')
                        winning_symbol = compSym
                        game_over = True
                    elif len(game.available_moves) == 0:
                        print("It's a Tie\n")
                        game_over = True

    else:
        game_active, pvp, playerSym = draw_start_screen(win, wait_for_input)
        wait_for_input += 2
        if wait_for_input > 70:
            wait_for_input = 70

        if game_active:
            wait_for_input = 0

        if pvp:
            player1Turn = True
        else:
            if playerSym == "X":
                playerTurn = True
                compSym = "O"
                is_maximizing = False
            else:
                playerTurn = False
                compSym = "X"
                is_maximizing = True

    if game_over:
        restart, main_menu = draw_win_message(win, winning_symbol)
        if restart:
            game = TicTacToe()
            draw_black_screen = True
            game_over = False
            winning_symbol = ""
            wait_for_input = 0
            player1Turn = True
            if playerSym == "X":
                playerTurn = True
            else:
                playerTurn = False

        elif main_menu:
            game = TicTacToe()
            game_active = False
            game_over = False
            draw_black_screen = True
            winning_symbol = ""
            wait_for_input = 0

    pygame.display.update()
