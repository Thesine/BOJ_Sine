king, queen, rook, bishop, knight, pawn = map(int, input().split())

original_king, original_queen, original_rook, original_bishop, original_knight, original_pawn = 1, 1, 2, 2, 2, 8

print(original_king-king, original_queen-queen, original_rook-rook, original_bishop-bishop, original_knight-knight, original_pawn-pawn)
