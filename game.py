import pygame, sys

class Settings():

    def __init__(self):

        self.screen_width = 600
        self.screen_height = 600
        self.line_color = (13,153,139)
        self.distance = 200
        self.caption = "Tic Tac Toe"
        self.bg_color = (28,170,156)
        self.line_thickness = 5
        self.circle_color = (242,235,211)
        self.circle_radius = 60
        self.circle_thickness = 15
        self.cross_color = (84,84,84)


class Game():

    def __init__(self):

        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width,self.settings.screen_height))
        pygame.display.set_caption(self.settings.caption)
        self.screen.fill((self.settings.bg_color))
        self.board = [[0,0,0],[0,0,0],[0,0,0]]
        print(self.board)
        self.turn = 1
        self.winner = ""


    def draw_lines(self):

        pygame.draw.line(self.screen, (self.settings.line_color), (self.settings.distance,0),(self.settings.distance,600), self.settings.line_thickness)
        pygame.draw.line(self.screen, (self.settings.line_color), (2*self.settings.distance,0),(2*self.settings.distance,600), self.settings.line_thickness)
        pygame.draw.line(self.screen, (self.settings.line_color), (0,self.settings.distance),(600,self.settings.distance), self.settings.line_thickness)
        pygame.draw.line(self.screen, (self.settings.line_color), (0,2*self.settings.distance),(600,2*self.settings.distance), self.settings.line_thickness)


    def mark_square(self,row,col,player):
        if self._is_square_available(row,col):
            self.board[row][col] = player
            if self.turn % 2 == 0:
                pygame.draw.circle(self.screen, self.settings.circle_color, (int(100 + col * 205),int(100 + row * 205)), self.settings.circle_radius, self.settings.circle_thickness)
            else:
                pygame.draw.line(self.screen, self.settings.cross_color, (int(50 + col*(200+5)),int(50 + row * (200+5))),(int(150 + col*(200+5)),int(150 + row * (200+5))),  self.settings.circle_thickness+3)
                pygame.draw.line(self.screen, self.settings.cross_color, (int(150 + col*(200+5)),int(50 + row * (200+5))), (int(50 + col*(200+5)),int(150 + row * (200+5))), self.settings.circle_thickness+3)
            self.turn += 1



    def _is_board_full(self):
        return 0 in (self.board)

    def _is_square_available(self,row,col):

        return self.board[row][col] == 0

    def _draw_circle(self, row,col):

        if self.turn % 2 == 0:
            self.mark_square(row,col,"O")
        else:
            self.mark_square(row,col,"X")


    def _check_who_win(self):
        #vertical check
        if self.board[0][0] == self.board[1][0] and self.board[0][0] == self.board[2][0] and self.board[1][0] == self.board[2][0]:
            return self.board[0][0]
        if self.board[0][1] == self.board[1][1] and self.board[0][1] == self.board[2][1] and self.board[1][1] == self.board[2][1]:
            return self.board[0][1]
        if self.board[0][2] == self.board[1][2] and self.board[0][2] == self.board[2][1] and self.board[1][2] == self.board[2][2]:
            return self.board[0][2]
        #horizontal check
        if self.board[0][0] == self.board[0][1] and self.board[0][0] == self.board[0][2] and self.board[0][1] == self.board[0][2]:
            return self.board[0][0]
        if self.board[1][0] == self.board[1][1] and self.board[1][0] == self.board[1][2] and self.board[1][1] == self.board[1][2]:
            return self.board[1][0]
        if self.board[2][0] == self.board[2][1] and self.board[2][0] == self.board[2][2] and self.board[2][1] == self.board[2][2]:
            return self.board[2][0]
        #diagonal check
        if self.board[0][0] == self.board[1][1] and self.board[0][0] == self.board[2][2] and self.board[1][1] == self.board[2][2]:
            return self.board[0][0]
        if self.board[0][2] == self.board[1][1] and self.board[0][2] == self.board[2][0] and self.board[1][1] == self.board[2][0]:
            return self.board[0][2]


    def play(self):

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                self.x = event.pos[0] #x coordinate
                self.y = event.pos[1] # y coordinate
                #checking whick square it is
                self.clicked_row = int(self.y // 200)
                self.sclicked_col = int(self.x // 200)

                self._draw_circle(self.clicked_row,self.sclicked_col)
                print(self.board)


        pygame.display.update()

game = Game()
game.draw_lines()

while True:
    game.play()
