"""
You are being attacked by an army of robots!
Luckily they are rather stupid and approach in one row.

Every robot has an armor value of larger than 0.
To defend yourself you have a single shot front loader rifle that will reduce
a robots armor value by 1.
If a robots armor value goes below 1, it will explode and inflict a damage of 2
(reducing armor by 2) to the robots standing next to it.

So, given a list of robot armor values, your function robotAttack must return
the minimum number of bullets you have to use to destroy all the robots

Attention: A value 0 in the list of robots means, that this space is not taken by a robot.

Sample:
Input: robots = [1, 2, 1, 2, 1, 1]
Output: 1

Input: robots = [3, 3, 3]
Output: 5

Input: robots = [3, 0, 3, 0, 3]
Output: 9
"""

def robot_attack(robots):
    return robots
