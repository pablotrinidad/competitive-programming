module Main where

import System.IO

-- countValleys(level, s, valleys) -> valleys
countValleys :: Integer -> [Char] -> Integer -> Integer
countValleys _ [] v = v
countValleys (-1) ('U':xs) v = countValleys 0 xs (succ v)
countValleys l (x:xs) v = countValleys (l + step) xs v
    where step = if x == 'U' then 1 else -1

-- Handle input
main :: IO()
main = do
    n <- readLn :: IO Int
    s <- getLine

    let result = countValleys 0 s 0

    print result
