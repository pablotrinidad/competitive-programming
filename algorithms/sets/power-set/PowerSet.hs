module PowerSet where

powerSet :: (Enum a) => [a] -> [[a]]
powerSet [] = [[]]
powerSet (x:xs) = foldl (\l e -> e : (e ++ [x]) : l) [] s where s = powerSet xs 
