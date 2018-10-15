import unittest
from solution import n7m

class TestN7m(unittest.TestCase):
    def test_01(self):
        sentence = "Shorten this text."
        result = "sh4n this t2t."
        self.assertEqual(result, n7m(sentence))

    def test_02(self):
        sentence = "There's no magic here, but there are more-, or less-difficult paths to choose. If you want mastery, you always need deep practice, but why should this mean pain and boredom? Small steps will be our guide, and fun our companion. But, how to journey?"
        result = "th2e's no m3c h2e, but th2e are m2e-, or l2s-d7t p3s to ch3e. If you w2t m5y, you al3s n2d d2p pr5e, but why sh3d this m2n p2n and b5m? sm2l st2s w2l be our g3e, and fun our c7n. But, how to j5y?"
        self.assertEqual(result, n7m(sentence))

    def test_03(self):
        sentence = "In publishing and graphic design, lorem ipsum is a filler text or greeking commonly used to demonstrate the textual elements of a graphic document or visual presentation. Replacing meaningful content with placeholder text allows designers to design the form of the content before the content itself has been produced."
        result = "In p8g and gr4c d4n, l3m ip2m is a f4r t2t or gr5g c6y used to d9e the t5l el5s of a gr4c d6t or v4l pr9n. r7g m8l c5t w2h pl8r t2t al3s d7s to d4n the f2m of the c5t b4e the c5t it3f has b2n pr5d."
        self.assertEqual(result, n7m(sentence))

    def test_04(self):
        sentence = "Every task here has a trick linked to it. Some of which are simple, like understanding how to use your tool to do what you want, but some are a multitude of problems and analyzing the problem for the right tricks takes work. The riddles are straightforward, once you know the trick, you know the trick forever. If you want to enjoy the process, figure out the trick. Day 11 took me two weeks (I actually just finished it yesterday, without using the blog post everyone's been linking to but with my own measurement that involves deltaX, deltaY and deltaZ) but I had fun. If you're going for speed, like many leaderboard contenders, figuring out the trick is just not as good as having known it, and climbing the gap in skill difference really just means having more tricks in your pockets and keep digging for interesting problems for their tricks."
        result = "ev2y t2k h2e has a tr2k l4d to it. s2e of wh2h are s4e, l2e un10g how to use y2r t2l to do what you w2t, but s2e are a m7e of pr5s and an6g the pr4m for the r3t tr3s t3s w2k. The r5s are st12d, once you know the tr2k, you know the tr2k f5r. If you w2t to en2y the pr4s, f4e out the tr2k. Day 11 t2k me two w3s (I ac5y j2t f6d it y7y, w5t us2g the blog p2t ev5e's b2n l5g to but w2h my own m9t that in5s d4x, d4y and d4z) but I had fun. If you're g3g for sp2d, l2e m2y l9d c8s, f6g out the tr2k is j2t not as g2d as h4g kn2n it, and cl5g the gap in sk2l d8e r4y j2t m3s h4g m2e tr3s in y2r p5s and k2p d5g for in8g pr5s for th2r tr3s."
        self.assertEqual(result, n7m(sentence))

    def test_05(self):
        sentence = "On the other hand, we denounce with righteous indignation and dislike men who are so beguiled and demoralized by the charms of pleasure of the moment, so blinded by desire, that they cannot foresee the pain and trouble that are bound to ensue; and equal blame belongs to those who fail in their duty through weakness of will, which is the same as saying through shrinking from toil and pain. These cases are perfectly simple and easy to distinguish. In a free hour, when our power of choice is untrammeled and when nothing prevents our being able to do what we like best, every pleasure is to be welcomed and every pain avoided. But in certain circumstances and owing to the claims of duty or the obligations of business it will frequently occur that pleasures have to be repudiated and annoyances accepted. The wise man therefore always holds in these matters to this principle of selection: he rejects pleasures to secure other greater pleasures, or else he endures pains to avoid worse."
        result = "On the ot2r h2d, we d6e w2h r7s in8n and d5e men who are so b6d and d9d by the ch3s of pl5e of the m4t, so bl4d by d4e, that they c4t f5e the p2n and tr4e that are b3d to en2e; and eq2l bl2e b5s to th2e who f2l in th2r d2y th4h w6s of w2l, wh2h is the s2e as s4g th4h sh6g from t2l and p2n. th2e c3s are p7y s4e and e2y to d9h. In a free h2r, when our p3r of ch3e is un8d and when n5g pr5s our b3g able to do what we l2e b2t, ev2y pl5e is to be w6d and ev2y p2n av4d. But in c5n c11s and ow2g to the cl3s of d2y or the ob8s of b6s it w2l fr7y oc2r that pl6s h2e to be r8d and an7s ac5d. The w2e man th6e al3s h3s in th2e m5s to this pr6e of s7n: he r5s pl6s to s4e ot2r gr4r pl6s, or else he en4s p3s to av2d w3e."
        self.assertEqual(result, n7m(sentence))

if __name__ == '__main__':
    unittest.main()
