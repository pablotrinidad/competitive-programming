"""Solution.

HackerRank > Algorithms > Implementation > Designer PDF Viewer.
"""


def designerPdfViewer(h, word):
    """Problem solution."""
    heights = [h[ord(c) - 97] for c in word]
    return len(word) * max(heights)
