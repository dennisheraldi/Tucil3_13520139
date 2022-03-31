from Puzzle import Puzzle
from PuzzleRoot import PuzzleRoot
from Solver import SolvePuzzle

if __name__ == "__main__":
    print("\n...-=15-Puzzle Solver=-...")
    filename = input("\nMasukkan nama file puzzle yang akan diselesaikan (.txt): ")
    filename = "reachable1.txt"

    puzzle_root = PuzzleRoot(filename)
    print("\nPuzzle berhasil dimuat.")
    puzzle_root.print_puzzle()

    print("\nNilai Kurang(i) untuk setiap ubin tersebut: \n")
    puzzle_root.print_kurang_i()
    print()
    puzzle_root.print_kurang_i_plus_x()

    if not puzzle_root.is_puzzle_solvable:
        print("\nPuzzle tidak dapat diselesaikan.\n")
    else:
        print("\nPuzzle dapat diselesaikan. \n")
        SolvePuzzle(puzzle_root)
        
        
        

    

