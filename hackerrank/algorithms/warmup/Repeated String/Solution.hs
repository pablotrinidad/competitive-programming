module Main where

import System.IO

asInS :: [Char] -> Int -> Int
asInS [] _ = 0
asInS _ 0 = 0
asInS (x:xs) n
    | x == 'a' = 1 + (asInS xs (pred n))
    | otherwise = asInS xs (pred n)


main :: IO()
main = do
    s <- getLine
    n' <- getLine
    let n = (read :: String -> Int) $ n'
    let l = length s
    let r = (n `div` l) * (asInS s l) + (asInS s (n `mod` l))

    print r
