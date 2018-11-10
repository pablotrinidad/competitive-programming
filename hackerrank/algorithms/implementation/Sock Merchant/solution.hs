module Main where

-- Language modules
import Data.List
import System.IO

-- makePairs(socks, pairsList, counter) -> pairs
makePairs :: [Int] -> [Int] -> Int -> Int
makePairs [] _ c = c
makePairs (x:xs) _ c = makePairs xs xs c
makePairs (x:xs) (y:ys) c
    | x == (head ys) = makePairs newList newList (c + 1)
    | otherwise = makePairs (x:xs) ys c
    where newList = (init xs) ++ ys

main :: IO()
main = do
    n <- readLn ::IO Int
    input <- getLine

    let socks = Data.List.map (read :: String -> Int) . words $ input
    let result = makePairs socks socks 0

    print result
