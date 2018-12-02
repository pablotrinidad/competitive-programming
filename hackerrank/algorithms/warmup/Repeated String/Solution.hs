module Main where

import System.IO


main :: IO()
main = do
    s' <- getLine
    n' <- getLine
    let n = (read :: String -> Int) $ n'
    let s = take n . concat . repeat $ s'
    let r = foldl (\acc x -> if x == 'a' then succ acc else acc) 0 s

    print r
