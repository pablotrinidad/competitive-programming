module Main where

import System.IO
import Data.List


compareTriplets :: (Integral e) => [e] -> [e] -> (e, e) -> (e, e)
compareTriplets [] [] (a, b) = (a, b)
compareTriplets (x:xs) (y:ys) (a, b)
    | x < y = compareTriplets xs ys (a, succ b)
    | x > y = compareTriplets xs ys (succ a, b)
    | otherwise = compareTriplets xs ys (a, b)


-- Handle input
main :: IO()
main = do
    aliceTmp <- getLine
    bobTmp <- getLine

    let alice = map (read :: String -> Int) . words $ aliceTmp
    let bob = map (read :: String -> Int) . words $ bobTmp

    let result = compareTriplets alice bob (0, 0)

    let x = intercalate " " . map (\x -> show x) $ [fst result, snd result]

    putStr x
