diagonalDifference arr = abs (sum [arr !! i !! i - reverse arr !! i !! i | i <- [0..length arr - 1]])
