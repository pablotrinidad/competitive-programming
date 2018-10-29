module Main where

import System.IO

diamonds :: Int -> Int -> [Char] -> Int
diamonds _ r [] = r
diamonds o r (x:xs)
    | x == '<' = diamonds (succ o) r xs
    | x == '>' && o > 0 = diamonds (pred o) (succ r) xs
    | otherwise = diamonds o r xs


readLines :: Int -> IO[[Char]]
readLines 0 = return []
readLines n = do
    line <- getLine
    rest <- readLines (n-1)
    return $ line : rest


main :: IO()
main = do
    n <- readLn :: IO Int
    lines <- readLines n

    let r = map (diamonds 0 0) lines

    mapM_ print r
