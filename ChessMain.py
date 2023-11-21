import pygame as p
import ChessEngine

Width = Height = 512
Dimension = 8
Sq_size = Height // Dimension
Max_FPS = 16
Images = {}


def loadImage():
    pieces = ["wp", "wR", "wN", "wB", "wQ", "wK", "bp", "bR", "bN", "bB", "bQ", "bK"]

    for piece in pieces:
        Images[piece] = p.transform.scale(p.image.load("images/" + piece + ".png"), (Sq_size, Sq_size))


def main():
    p.init()
    screen = p.display.set_mode((Width, Height))
    clock = p.time.Clock()
    screen.fill(p.Color("white"))
    game_state = ChessEngine.gameState()  # Fix: Correct the class name
    loadImage()
    running = True
    while running:
        for e in p.event.get():
            if e.type == p.QUIT:
                running = False
        drawGameState(screen, game_state)
        clock.tick(Max_FPS)
        p.display.flip()


def drawGameState(screen, game_state):
    drawBoard(screen)
    drawPieces(screen, game_state.board)


def drawBoard(screen):
    colors = [p.Color("white"), p.Color("grey")]
    for r in range(Dimension):
        for c in range(Dimension):
            color = colors[(r + c) % 2]
            p.draw.rect(screen, color, p.Rect(c * Sq_size, r * Sq_size, Sq_size, Sq_size))


def drawPieces(screen, board):
    for r in range(Dimension):
        for c in range(Dimension):
            piece = board[r][c]
            if piece != "--":  # not an empty square
                screen.blit(Images[piece], p.Rect(c * Sq_size, r * Sq_size, Sq_size, Sq_size))


if __name__ == "__main__":
    main()
