module Main where

import System.IO

blownOutCandles :: [Integer] -> Integer -> Integer
blownOutCandles [] _ = 0
blownOutCandles xs m = sum [1 | x <- xs, x == m]

-- Handle input
main :: IO()
main = do
    n <- readLn :: IO Int
    l <- getLine
    let xs = map read $ words l :: [Integer]

    let result = blownOutCandles xs (maximum xs)

    print result
