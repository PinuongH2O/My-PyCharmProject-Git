# tictactoe.py
# Tic-Tac-Toe (Cờ caro 3x3) — không dùng thư viện ngoài
# Hướng dẫn: chạy bằng python3 tictactoe.py

def print_board(b):
    """In bảng 3x3"""
    print()
    for i in range(3):
        row = ' | '.join(b[i*3:(i+1)*3])
        print(' ' + row)
        if i < 2:
            print('---+---+---')
    print()

def check_winner(b):
    """Trả về 'X' hoặc 'O' nếu có người thắng, 'D' nếu hòa, None nếu chưa kết thúc"""
    wins = [
        (0,1,2),(3,4,5),(6,7,8),  # hàng
        (0,3,6),(1,4,7),(2,5,8),  # cột
        (0,4,8),(2,4,6)           # chéo
    ]
    for a,b_idx,c in wins:
        if b[a] == b[b_idx] == b[c] and b[a] != ' ':
            return b[a]
    if ' ' not in b:
        return 'D'  # draw
    return None

def available_moves(b):
    return [i for i,cell in enumerate(b) if cell == ' ']

def minimax(b, player, ai_player, human_player):
    """
    Minimax trả về (score, move_index)
    score: +1 nếu AI thắng, -1 nếu AI thua, 0 hòa
    """
    winner = check_winner(b)
    if winner == ai_player:
        return 1, None
    elif winner == human_player:
        return -1, None
    elif winner == 'D':
        return 0, None

    moves = available_moves(b)
    if player == ai_player:
        best_score = -2
        best_move = None
        for m in moves:
            b[m] = player
            score, _ = minimax(b, human_player, ai_player, human_player)
            b[m] = ' '
            if score > best_score:
                best_score = score
                best_move = m
        return best_score, best_move
    else:
        best_score = 2
        best_move = None
        for m in moves:
            b[m] = player
            score, _ = minimax(b, ai_player, ai_player, human_player)
            b[m] = ' '
            if score < best_score:
                best_score = score
                best_move = m
        return best_score, best_move

def ai_move(b, ai_player, human_player):
    """Chọn nước tốt nhất cho AI bằng Minimax"""
    _, move = minimax(b, ai_player, ai_player, human_player)
    return move

def player_move(b):
    """Yêu cầu người chơi nhập nước (1-9)"""
    while True:
        try:
            s = input("Chọn ô (1-9): ").strip()
            if s.lower() in ('q','quit','exit'):
                print("Thoát trò chơi.")
                exit()
            pos = int(s) - 1
            if pos not in range(9):
                print("Vui lòng nhập số từ 1 đến 9.")
                continue
            if b[pos] != ' ':
                print("Ô đã có người, chọn ô khác.")
                continue
            return pos
        except ValueError:
            print("Nhập không hợp lệ. Nhập số từ 1 đến 9, hoặc 'q' để thoát.")

def human_vs_human():
    board = [' '] * 9
    current = 'X'
    while True:
        print_board(board)
        print(f"Lượt {current}.")
        move = player_move(board)
        board[move] = current
        w = check_winner(board)
        if w:
            print_board(board)
            if w == 'D':
                print("Hòa!")
            else:
                print(f"Người chơi {w} thắng!")
            break
        current = 'O' if current == 'X' else 'X'

def human_vs_ai(first_player, human_player, ai_player):
    board = [' '] * 9
    current = first_player
    while True:
        print_board(board)
        if current == human_player:
            print("Lượt bạn.")
            move = player_move(board)
            board[move] = human_player
        else:
            print("Máy đang suy nghĩ...")
            move = ai_move(board, ai_player, human_player)
            # nếu minimax trả về None (không có move) — thoát
            if move is None:
                # có thể xảy ra khi bảng đầy
                print("Không có nước hợp lệ.")
                break
            board[move] = ai_player
            print(f"Máy đánh ô {move+1}.")
        w = check_winner(board)
        if w:
            print_board(board)
            if w == 'D':
                print("Hòa!")
            elif w == human_player:
                print("Chúc mừng — bạn thắng!")
            else:
                print("Máy thắng! Chúc bạn lần sau may mắn.")
            break
        current = ai_player if current == human_player else human_player

def main():
    print("=== Tic-Tac-Toe (Không dùng thư viện ngoài) ===")
    while True:
        print("\nChọn chế độ:")
        print("1) Người vs Người")
        print("2) Người vs Máy")
        print("q) Thoát")
        choice = input("Lựa chọn: ").strip().lower()
        if choice == '1':
            human_vs_human()
        elif choice == '2':
            # chọn ký hiệu
            while True:
                sym = input("Bạn muốn chơi 'X' hay 'O'? (X đi trước) ").strip().upper()
                if sym in ('X','O'):
                    human = sym
                    ai = 'O' if human == 'X' else 'X'
                    break
                print("Chọn X hoặc O.")
            # ai hay người đi trước?
            while True:
                first = input("Ai đi trước? (me/m = bạn; ai/a = máy) [m/a]: ").strip().lower()
                if first in ('m','me','me.','you','y'):
                    first_p = human
                    break
                if first in ('a','ai'):
                    first_p = ai
                    break
                print("Nhập 'm' cho bạn, 'a' cho máy.")
            human_vs_ai(first_p, human, ai)
        elif choice in ('q','quit','exit'):
            print("Bye!")
            break
        else:
            print("Lựa chọn không hợp lệ. Thử lại.")

if __name__ == "__main__":
    main()
