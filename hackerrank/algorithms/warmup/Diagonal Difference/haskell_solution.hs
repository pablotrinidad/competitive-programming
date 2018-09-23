module Main where

import System.IO

-- Diagonal difference (almost)
diagonalDifference :: [[Int]] -> [[Int]] -> Int -> Int
diagonalDifference [] _ _ = 0
diagonalDifference (x:xs) (y:ys) i = x!!i - y!!i + diagonalDifference xs ys (i - 1)

-- Create list of lists of integers
readMultipleLines :: Int -> IO [[Int]]
readMultipleLines 0 = return []
readMultipleLines n = do
    line <- getLine
    rest <- readMultipleLines(n - 1)
    return $ map (read :: String -> Int) (words line) : rest

-- Handle input
main :: IO()
main = do
    n <- readLn :: IO Int
    matrix <- readMultipleLines n

    let result = abs $ diagonalDifference matrix (reverse matrix) (n - 1)

    print result
