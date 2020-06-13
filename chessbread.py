import pygame
import brain as b
# import numpy

# total game screen size
screen_w = 900; screen_h = 700;
sb = 10  # small buffer 5 pixels wherever needed
percent_size_board = 0.756 # 900x700=0.756  1000x700=0.68

# all initializations
pygame.init()
win = pygame.display.set_mode([screen_w, screen_h])
pygame.display.set_caption("Chess Bread")
clock = pygame.time.Clock()

# board area... chess pieces
board_w = int(screen_w * percent_size_board)
board_h = int(screen_h - 2 * sb)

# side area... shows captured pieces
side_w = screen_w - board_w - sb - sb - sb
side_h = board_h  # side height should be same as board height

# board  (x,y,w,h)
board_rect = (sb, sb, board_w, board_h)
board_rect_dark = (sb+(sb*4), sb+(sb*4), board_w-2*(sb*4), board_h-2*(sb*4))
board_rect_light = (sb+(sb*4+sb//2), sb+(sb*4+sb//2), board_w-2*(sb*4+sb//2), board_h-2*(sb*4+sb//2))
x_diff=(board_rect_dark[3]//8)                                     # space seperations for lines
y_diff=(board_rect_dark[3]//8)

# side rect
side_rect = (sb + board_w + sb, sb, side_w, side_h)

# debug print board info
print(f"screen {screen_w} x {screen_h} = ratio {screen_w/screen_h}")
print(f"board_rect {board_rect} = ratio {board_rect[2]/board_rect[3]}")
print(f"board_rect_dark {board_rect_dark} = ratio {board_rect_dark[2]/board_rect_dark[3]}")
print(f"board_rect_light {board_rect_light} = ratio {board_rect_light[2]/board_rect_light[3]}")
print(f"side {side_w} x {side_h} - side_rect {side_rect} = ratio {side_w/side_h}")

# colors
COLOR_BG = (0, 0, 0)
COLOR_GREY1 = (128, 128, 128)
COLOR_GREY2 = (70, 70, 70)
COLOR_BOARDLINES = (175, 50, 50)
COLOR_WHITE=(255,255,255)
COLOR_BLACK=(0,0,0)

# brain stuff
my_board = b.Board()
my_spot_list = []

# functions
def init_board():
    # construct the board and spot objects
    old_is_white=False;
    for i in range(8):
        for j in range(8):
            # print(f"({i},{j},{x},{y}) ",end='')
            bx=board_rect_light[0]+(x_diff)*i
            by=board_rect_light[1]+(y_diff)*j
            bw=x_diff-sb//2
            bh=y_diff-sb//2
            is_white=not old_is_white
            tmp_spot=b.Spot(i,j,bx,by,bw,bh,is_white,None)
            my_spot_list.append(tmp_spot)
            old_is_white=is_white
        y=0
        old_is_white=not old_is_white # alternate on the row as well
    my_board.spot_list=my_spot_list
    my_board.reset_pieces()

def draw_board():
    pygame.draw.rect(win, COLOR_GREY1, board_rect)                     # draw board area rectangle
    pygame.draw.rect(win, COLOR_BOARDLINES, board_rect_dark)           # draw outer board
    pygame.draw.rect(win, COLOR_GREY1, board_rect_light)               # draw inner board, both give the board
    # draw squares double for loop
    # (i,j,x,y)
    # print(f"({i},{j},{x},{y}) ", end='')
    # (0, 0, 1, 1)(0, 1, 1, 2)(0, 2, 1, 3)(0, 3, 1, 4)(0, 4, 1, 5)(0, 5, 1, 6)(0, 6, 1, 7)(0, 7, 1, 8)
    # (1, 0, 2, 1)(1, 1, 2, 2)(1, 2, 2, 3)(1, 3, 2, 4)(1, 4, 2, 5)(1, 5, 2, 6)(1, 6, 2, 7)(1, 7, 2, 8)
    # (2, 0, 3, 1)(2, 1, 3, 2)(2, 2, 3, 3)(2, 3, 3, 4)(2, 4, 3, 5)(2, 5, 3, 6)(2, 6, 3, 7)(2, 7, 3, 8)
    # (3, 0, 4, 1)(3, 1, 4, 2)(3, 2, 4, 3)(3, 3, 4, 4)(3, 4, 4, 5)(3, 5, 4, 6)(3, 6, 4, 7)(3, 7, 4, 8)
    # (4, 0, 5, 1)(4, 1, 5, 2)(4, 2, 5, 3)(4, 3, 5, 4)(4, 4, 5, 5)(4, 5, 5, 6)(4, 6, 5, 7)(4, 7, 5, 8)
    # (5, 0, 6, 1)(5, 1, 6, 2)(5, 2, 6, 3)(5, 3, 6, 4)(5, 4, 6, 5)(5, 5, 6, 6)(5, 6, 6, 7)(5, 7, 6, 8)
    # (6, 0, 7, 1)(6, 1, 7, 2)(6, 2, 7, 3)(6, 3, 7, 4)(6, 4, 7, 5)(6, 5, 7, 6)(6, 6, 7, 7)(6, 7, 7, 8)
    # (7, 0, 8, 1)(7, 1, 8, 2)(7, 2, 8, 3)(7, 3, 8, 4)(7, 4, 8, 5)(7, 5, 8, 6)(7, 6, 8, 7)(7, 7, 8, 8)
    # x=0; y=0;
    # old_is_white=False;  # we want to start white, so the first not of that is true which makes its white
    # for i in range(8):
    #    x+=1
    #    for j in range(8):
    #        y+=1
    #        # print(f"({i},{j},{x},{y}) ",end='')
    #        bx=board_rect_light[0]+(x_diff)*i
    #        by=board_rect_light[1]+(y_diff)*j
    #        bw=x_diff-sb//2
    #        bh=y_diff-sb//2
    #        board_square=(bx,by,bw,bh)
    #        is_white=not old_is_white
    #        pygame.draw.rect(win, COLOR_WHITE if is_white else COLOR_BLACK, board_square)
    #        old_is_white=is_white
    #    y=0
    #    old_is_white=not old_is_white # alternate on the row as well
    #    # print("")
    # draw squares / spots
    for i in my_board.spot_list:
        pygame.draw.rect(win, COLOR_WHITE if i.is_white else COLOR_BLACK, i.rect)
    # draw verticle lines
    for i in range(8):
        line_x=board_rect_dark[0]+x_diff*(i+1)
        line_y=board_rect_dark[1]
        line_w=sb//2
        line_h=board_rect_dark[3]+sb//2
        line_rect=(line_x,line_y,line_w,line_h)
        pygame.draw.rect(win, COLOR_BOARDLINES, line_rect)
    # draw horizontal lines
    for i in range(8):
        line_x=board_rect_dark[0]
        line_y=board_rect_dark[1]+y_diff*(i+1)
        line_w=board_rect_dark[2]
        line_h=sb//2
        line_rect=(line_x,line_y,line_w,line_h)
        pygame.draw.rect(win, COLOR_BOARDLINES, line_rect) 
    # draw selected square


def draw_side():
    pygame.draw.rect(win, COLOR_GREY1, side_rect)
# main
def main():
    init_board()
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        clock.tick(24)
        win.fill(COLOR_BG)
        draw_board()
        draw_side()
        pygame.display.update()
    pygame.quit()

# start main
if __name__ == "__main__":
    main()
