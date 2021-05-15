from tkinter import *
import sys
root = Tk()
root.title('Chess')
selected = False
piece = ''
turn = 'w'

print('White\'s turn')
def OnButtonClick(buttonid):
    global selected, piece, turn
    if selected == False:
        piece = buttonid
        print(str(piece) + ' selected')
        if turn == 'w' and str(board[buttonid]) in ['pyimage1','pyimage3','pyimage5','pyimage7','pyimage9','pyimage11']:
            selected = True
        if turn == 'b' and str(board[buttonid]) in ['pyimage2','pyimage4','pyimage6','pyimage8','pyimage10','pyimage12']:
            selected = True
    elif selected == True and buttonid != piece:
        board[buttonid] = board[piece]
        board[piece] = None
        selected = False
        if turn == 'w':
            turn = 'b'
            print('Black\'s turn')
        elif turn == 'b':
            turn = 'w'
            print('White\'s turn')
    update()
try:
    wking = PhotoImage(file = r'C:\Users\mrchi\Pictures\Saved Pictures\wking.png')#pyimage1
    bking = PhotoImage(file = r'C:\Users\mrchi\Pictures\Saved Pictures\bking.png')#pyimage2
    wqueen = PhotoImage(file = r'C:\Users\mrchi\Pictures\Saved Pictures\wqueen.png')#pyimage3
    bqueen = PhotoImage(file = r'C:\Users\mrchi\Pictures\Saved Pictures\bqueen.png')#pyimage4
    wbishop = PhotoImage(file = r'C:\Users\mrchi\Pictures\Saved Pictures\wbishop.png')#pyimage5
    bbishop = PhotoImage(file = r'C:\Users\mrchi\Pictures\Saved Pictures\bbishop.png')#pyimage6
    wknight = PhotoImage(file = r'C:\Users\mrchi\Pictures\Saved Pictures\wknight.png')#pyimage7
    bknight = PhotoImage(file = r'C:\Users\mrchi\Pictures\Saved Pictures\bknight.png')#pyimage8
    wrook = PhotoImage(file = r'C:\Users\mrchi\Pictures\Saved Pictures\wrook.png')#pyimage9
    brook = PhotoImage(file = r'C:\Users\mrchi\Pictures\Saved Pictures\brook.png')#pyimage10
    wpawn = PhotoImage(file = r'C:\Users\mrchi\Pictures\Saved Pictures\wpawn.png')#pyimage11
    bpawn = PhotoImage(file = r'C:\Users\mrchi\Pictures\Saved Pictures\bpawn.png')#pyimage12
except:
    print('Couldn\'t find images for game pieces')
    sys.exit()

board = {57:brook, 58:bknight, 59:bbishop, 60:bqueen, 61:bking, 62:bbishop, 63:bknight, 64:brook,
         49:bpawn, 50:bpawn, 51:bpawn, 52:bpawn, 53:bpawn, 54:bpawn, 55:bpawn, 56:bpawn,
         41:None, 42:None, 43:None, 44:None, 45:None, 46:None, 47:None, 48:None,
         33:None, 34:None, 35:None, 36:None, 37:None, 38:None, 39:None, 40:None,
         25:None, 26:None, 27:None, 28:None, 29:None, 30:None, 31:None, 32:None,
         17:None, 18:None, 19:None, 20:None, 21:None, 22:None, 23:None, 24:None,
         9:wpawn, 10:wpawn, 11:wpawn, 12:wpawn, 13:wpawn, 14:wpawn, 15:wpawn, 16:wpawn,
         1:wrook, 2:wknight, 3:wbishop, 4:wqueen, 5:wking, 6:wbishop, 7:wknight, 8:wrook}

Label(text='8', height=5, width=2, font=(12), bg='tan2').grid(row=1, column=0)
Label(text='7', height=5, width=2, font=(12), bg='tan2').grid(row=2, column=0)
Label(text='6', height=5, width=2, font=(12), bg='tan2').grid(row=3, column=0)
Label(text='5', height=5, width=2, font=(12), bg='tan2').grid(row=4, column=0)
Label(text='4', height=5, width=2, font=(12), bg='tan2').grid(row=5, column=0)
Label(text='3', height=5, width=2, font=(12), bg='tan2').grid(row=6, column=0)
Label(text='2', height=5, width=2, font=(12), bg='tan2').grid(row=7, column=0)
Label(text='1', height=5, width=2, font=(12), bg='tan2').grid(row=8, column=0)
Label(font=(12), bg='tan2').grid(row=9, column=0, sticky=N+E+S+W)
Label(text='a', width=10, font=(12), bg='tan2').grid(row=9, column=1)
Label(text='b', width=10, font=(12), bg='tan2').grid(row=9, column=2)
Label(text='c', width=10, font=(12), bg='tan2').grid(row=9, column=3)
Label(text='d', width=10, font=(12), bg='tan2').grid(row=9, column=4)
Label(text='e', width=10, font=(12), bg='tan2').grid(row=9, column=5)
Label(text='f', width=10, font=(12), bg='tan2').grid(row=9, column=6)
Label(text='g', width=10, font=(12), bg='tan2').grid(row=9, column=7)
Label(text='h', width=10, font=(12), bg='tan2').grid(row=9, column=8)
def update():
    root.button1 = Button(root, bg='tan4', image=board[1], command=lambda: OnButtonClick(1))
    root.button1.grid(row=8, column=1, sticky=N+E+W+S)
    root.button2 = Button(root, bg='tan1', image=board[2], command=lambda: OnButtonClick(2))
    root.button2.grid(row=8, column=2, sticky=N+E+W+S)
    root.button3 = Button(root, bg='tan4', image=board[3], command=lambda: OnButtonClick(3))
    root.button3.grid(row=8, column=3, sticky=N+E+W+S)
    root.button4 = Button(root, bg='tan1', image=board[4], command=lambda: OnButtonClick(4))
    root.button4.grid(row=8, column=4, sticky=N+E+W+S)
    root.button5 = Button(root, bg='tan4', image=board[5], command=lambda: OnButtonClick(5))
    root.button5.grid(row=8, column=5, sticky=N+E+W+S)
    root.button6 = Button(root, bg='tan1', image=board[6], command=lambda: OnButtonClick(6))
    root.button6.grid(row=8, column=6, sticky=N+E+W+S)
    root.button7 = Button(root, bg='tan4', image=board[7], command=lambda: OnButtonClick(7))
    root.button7.grid(row=8, column=7, sticky=N+E+W+S)
    root.button8 = Button(root, bg='tan1', image=board[8], command=lambda: OnButtonClick(8))
    root.button8.grid(row=8, column=8, sticky=N+E+W+S)
    root.button9 = Button(root, bg='tan1', image=board[9], command=lambda: OnButtonClick(9))
    root.button9.grid(row=7, column=1, sticky=N+E+W+S)
    root.button10 = Button(root, bg='tan4', image=board[10], command=lambda: OnButtonClick(10))
    root.button10.grid(row=7, column=2, sticky=N+E+W+S)
    root.button11 = Button(root, bg='tan1', image=board[11], command=lambda: OnButtonClick(11))
    root.button11.grid(row=7, column=3, sticky=N+E+W+S)
    root.button12 = Button(root, bg='tan4', image=board[12], command=lambda: OnButtonClick(12))
    root.button12.grid(row=7, column=4, sticky=N+E+W+S)
    root.button13 = Button(root, bg='tan1', image=board[13], command=lambda: OnButtonClick(13))
    root.button13.grid(row=7, column=5, sticky=N+E+W+S)
    root.button14 = Button(root, bg='tan4', image=board[14], command=lambda: OnButtonClick(14))
    root.button14.grid(row=7, column=6, sticky=N+E+W+S)
    root.button15 = Button(root, bg='tan1', image=board[15], command=lambda: OnButtonClick(15))
    root.button15.grid(row=7, column=7, sticky=N+E+W+S)
    root.button16 = Button(root, bg='tan4', image=board[16], command=lambda: OnButtonClick(16))
    root.button16.grid(row=7, column=8, sticky=N+E+W+S)
    root.button17 = Button(root, bg='tan4', image=board[17], command=lambda: OnButtonClick(17))
    root.button17.grid(row=6, column=1, sticky=N+E+W+S)
    root.button18 = Button(root, bg='tan1', image=board[18], command=lambda: OnButtonClick(18))
    root.button18.grid(row=6, column=2, sticky=N+E+W+S)
    root.button19 = Button(root, bg='tan4', image=board[19], command=lambda: OnButtonClick(19))
    root.button19.grid(row=6, column=3, sticky=N+E+W+S)
    root.button20 = Button(root, bg='tan1', image=board[20], command=lambda: OnButtonClick(20))
    root.button20.grid(row=6, column=4, sticky=N+E+W+S)
    root.button21 = Button(root, bg='tan4', image=board[21], command=lambda: OnButtonClick(21))
    root.button21.grid(row=6, column=5, sticky=N+E+W+S)
    root.button22 = Button(root, bg='tan1', image=board[22], command=lambda: OnButtonClick(22))
    root.button22.grid(row=6, column=6, sticky=N+E+W+S)
    root.button23 = Button(root, bg='tan4', image=board[23], command=lambda: OnButtonClick(23))
    root.button23.grid(row=6, column=7, sticky=N+E+W+S)
    root.button24 = Button(root, bg='tan1', image=board[24], command=lambda: OnButtonClick(24))
    root.button24.grid(row=6, column=8, sticky=N+E+W+S)
    root.button25 = Button(root, bg='tan1', image=board[25], command=lambda: OnButtonClick(25))
    root.button25.grid(row=5, column=1, sticky=N+E+W+S)
    root.button26 = Button(root, bg='tan4', image=board[26], command=lambda: OnButtonClick(26))
    root.button26.grid(row=5, column=2, sticky=N+E+W+S)
    root.button27 = Button(root, bg='tan1', image=board[27], command=lambda: OnButtonClick(27))
    root.button27.grid(row=5, column=3, sticky=N+E+W+S)
    root.button28 = Button(root, bg='tan4', image=board[28], command=lambda: OnButtonClick(28))
    root.button28.grid(row=5, column=4, sticky=N+E+W+S)
    root.button29 = Button(root, bg='tan1', image=board[29], command=lambda: OnButtonClick(29))
    root.button29.grid(row=5, column=5, sticky=N+E+W+S)
    root.button30 = Button(root, bg='tan4', image=board[30], command=lambda: OnButtonClick(30))
    root.button30.grid(row=5, column=6, sticky=N+E+W+S)
    root.button31 = Button(root, bg='tan1', image=board[31], command=lambda: OnButtonClick(31))
    root.button31.grid(row=5, column=7, sticky=N+E+W+S)
    root.button32 = Button(root, bg='tan4', image=board[32], command=lambda: OnButtonClick(32))
    root.button32.grid(row=5, column=8, sticky=N+E+W+S)
    root.button33 = Button(root, bg='tan4', image=board[33], command=lambda: OnButtonClick(33))
    root.button33.grid(row=4, column=1, sticky=N+E+W+S)
    root.button34 = Button(root, bg='tan1', image=board[34], command=lambda: OnButtonClick(34))
    root.button34.grid(row=4, column=2, sticky=N+E+W+S)
    root.button35 = Button(root, bg='tan4', image=board[35], command=lambda: OnButtonClick(35))
    root.button35.grid(row=4, column=3, sticky=N+E+W+S)
    root.button36 = Button(root, bg='tan1', image=board[36], command=lambda: OnButtonClick(36))
    root.button36.grid(row=4, column=4, sticky=N+E+W+S)
    root.button37 = Button(root, bg='tan4', image=board[37], command=lambda: OnButtonClick(37))
    root.button37.grid(row=4, column=5, sticky=N+E+W+S)
    root.button38 = Button(root, bg='tan1', image=board[38], command=lambda: OnButtonClick(38))
    root.button38.grid(row=4, column=6, sticky=N+E+W+S)
    root.button39 = Button(root, bg='tan4', image=board[39], command=lambda: OnButtonClick(39))
    root.button39.grid(row=4, column=7, sticky=N+E+W+S)
    root.button40 = Button(root, bg='tan1', image=board[40], command=lambda: OnButtonClick(40))
    root.button40.grid(row=4, column=8, sticky=N+E+W+S)
    root.button41 = Button(root, bg='tan1', image=board[41], command=lambda: OnButtonClick(41))
    root.button41.grid(row=3, column=1, sticky=N+E+W+S)
    root.button42 = Button(root, bg='tan4', image=board[42], command=lambda: OnButtonClick(42))
    root.button42.grid(row=3, column=2, sticky=N+E+W+S)
    root.button43 = Button(root, bg='tan1', image=board[43], command=lambda: OnButtonClick(43))
    root.button43.grid(row=3, column=3, sticky=N+E+W+S)
    root.button44 = Button(root, bg='tan4', image=board[44], command=lambda: OnButtonClick(44))
    root.button44.grid(row=3, column=4, sticky=N+E+W+S)
    root.button45 = Button(root, bg='tan1', image=board[45], command=lambda: OnButtonClick(45))
    root.button45.grid(row=3, column=5, sticky=N+E+W+S)
    root.button46 = Button(root, bg='tan4', image=board[46], command=lambda: OnButtonClick(46))
    root.button46.grid(row=3, column=6, sticky=N+E+W+S)
    root.button47 = Button(root, bg='tan1', image=board[47], command=lambda: OnButtonClick(47))
    root.button47.grid(row=3, column=7, sticky=N+E+W+S)
    root.button48 = Button(root, bg='tan4', image=board[48], command=lambda: OnButtonClick(48))
    root.button48.grid(row=3, column=8, sticky=N+E+W+S)
    root.button49 = Button(root, bg='tan4', image=board[49], command=lambda: OnButtonClick(49))
    root.button49.grid(row=2, column=1, sticky=N+E+W+S)
    root.button50 = Button(root, bg='tan1', image=board[50], command=lambda: OnButtonClick(50))
    root.button50.grid(row=2, column=2, sticky=N+E+W+S)
    root.button51 = Button(root, bg='tan4', image=board[51], command=lambda: OnButtonClick(51))
    root.button51.grid(row=2, column=3, sticky=N+E+W+S)
    root.button52 = Button(root, bg='tan1', image=board[52], command=lambda: OnButtonClick(52))
    root.button52.grid(row=2, column=4, sticky=N+E+W+S)
    root.button53 = Button(root, bg='tan4', image=board[53], command=lambda: OnButtonClick(53))
    root.button53.grid(row=2, column=5, sticky=N+E+W+S)
    root.button54 = Button(root, bg='tan1', image=board[54], command=lambda: OnButtonClick(54))
    root.button54.grid(row=2, column=6, sticky=N+E+W+S)
    root.button55 = Button(root, bg='tan4', image=board[55], command=lambda: OnButtonClick(55))
    root.button55.grid(row=2, column=7, sticky=N+E+W+S)
    root.button56 = Button(root, bg='tan1', image=board[56], command=lambda: OnButtonClick(56))
    root.button56.grid(row=2, column=8, sticky=N+E+W+S)
    root.button57 = Button(root, bg='tan1', image=board[57], command=lambda: OnButtonClick(57))
    root.button57.grid(row=1, column=1, sticky=N+E+W+S)
    root.button58 = Button(root, bg='tan4', image=board[58], command=lambda: OnButtonClick(58))
    root.button58.grid(row=1, column=2, sticky=N+E+W+S)
    root.button59 = Button(root, bg='tan1', image=board[59], command=lambda: OnButtonClick(59))
    root.button59.grid(row=1, column=3, sticky=N+E+W+S)
    root.button60 = Button(root, bg='tan4', image=board[60], command=lambda: OnButtonClick(60))
    root.button60.grid(row=1, column=4, sticky=N+E+W+S)
    root.button61 = Button(root, bg='tan1', image=board[61], command=lambda: OnButtonClick(61))
    root.button61.grid(row=1, column=5, sticky=N+E+W+S)
    root.button62 = Button(root, bg='tan4', image=board[62], command=lambda: OnButtonClick(62))
    root.button62.grid(row=1, column=6, sticky=N+E+W+S)
    root.button63 = Button(root, bg='tan1', image=board[63], command=lambda: OnButtonClick(63))
    root.button63.grid(row=1, column=7, sticky=N+E+W+S)
    root.button64 = Button(root, bg='tan4', image=board[64], command=lambda: OnButtonClick(64))
    root.button64.grid(row=1, column=8, sticky=N+E+W+S)
update()
mainloop()
