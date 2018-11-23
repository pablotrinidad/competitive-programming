module Main where

import System.IO

-- minJumps(n, clouds, jumps) -> jumps
minJumps :: [Int] -> Int -> Int
minJumps [] j = j
minJumps [0] j = j
minJumps (x:xs) j
    | (head . tail) xs == 1 = minJumps xs (succ j)
    | otherwise = minJumps (tail xs) (succ j)


-- Handle input
main :: IO()
main = do
    n <- readLn :: IO Int
    s <- getLine
    let clouds = map (read :: String -> Int) . words $ s

    let result = minJumps clouds 0

    print result
