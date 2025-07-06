from pathlib import Path
import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from arrowetc import ArrowETC

def main():
    base_path = Path(__file__).resolve().parent.parent / 'resources'

    # basic arrow with head
    path = [(0, 0), (0, 4)]
    arrow = ArrowETC(path, arrow_width=0.5, arrow_head=True)
    arrow.save_arrow(base_path / "basic_arrow_with_head.png")

    # multi segmented arrows
    path = [(0, 0), (0, 4), (5, 4), (5, -2)]
    arrow = ArrowETC(path, arrow_width=0.5, arrow_head=True)
    arrow.save_arrow(base_path / "multi_segment_arrow_with_head.png", fc="magenta", lw=1)

    # obtuse angles
    path = [(0, 0), (4, 0), (8, 2)]
    arrow = ArrowETC(path, arrow_width=0.5, arrow_head=True)
    arrow.save_arrow(base_path / "obtuse_arrow_with_head.png", fc="orange", ec="cyan", lw=1.2)

    # acute angles
    path = [(0, 0), (4, 0), (1, 4)]
    arrow = ArrowETC(path, arrow_width=0.5, arrow_head=True)
    arrow.save_arrow(base_path / "acute_arrow_with_head.png")

    # basic segments without head
    path = [(0, 0), (0, -10), (10, -10), (10, 0)]
    arrow = ArrowETC(path, arrow_width=1, arrow_head=False)
    arrow.save_arrow(base_path / "multi_segment_no_head.png")

    # basic bezier
    path = [(0, 0), (4, 0), (8, 2)]
    arrow = ArrowETC(path, arrow_width=0.5, arrow_head=True, bezier=True)
    arrow.save_arrow(base_path / "basic_bezier_with_head.png", fc="orange", ec="cyan", lw=1.2)

    # crazier bezier (bezier_n too low, skews arrowhead)
    path = [(0, 0), (4, -5), (8, 2), (16, -8)]
    arrow = ArrowETC(path, arrow_width=1, arrow_head=True, bezier=True)
    arrow.save_arrow(base_path / "crazier_bezier_with_head-low_n.png", lw=1.2)

    # crazier bezier (bezier_n now appropritate value)
    path = [(0, 0), (4, -5), (8, 2), (14, -8)]
    arrow = ArrowETC(path, arrow_width=1, arrow_head=True, bezier=True, bezier_n=800)
    arrow.save_arrow(base_path / "crazier_bezier_with_head-high_n.png", lw=1.2)

    # many segments
    path = [(0, 0), (1, 2), (2, -1), (4, -2), (5, 0), (7, 0)]
    arrow = ArrowETC(path, arrow_head=True, arrow_width=0.2)
    arrow.save_arrow(base_path / "many_segments_with_head.png", lw=1.2)

if __name__ == "__main__":
    main()
