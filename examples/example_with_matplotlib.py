from pathlib import Path
import os
import sys

import matplotlib.pyplot as plt
import numpy as np

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from arrowetc import ArrowETC

def get_bbox_center_bottom(fig, ax, text, vertical_offset=0.07):
    """
    Get the center-bottom coordinate of the text's bounding box,
    with optional vertical offset downwards.
    """
    fig.canvas.draw()
    bbox = text.get_window_extent(renderer=fig.canvas.get_renderer())
    bbox_data = bbox.transformed(ax.transData.inverted())
    x_center = (bbox_data.x0 + bbox_data.x1) / 2
    y_bottom = bbox_data.ymin - vertical_offset
    return x_center, y_bottom, bbox_data

def add_annotation(ax, x, y, text_str, fontsize=10, ha='left', va='center'):
    """
    Add an annotation text box to the axes.
    """
    return ax.text(
        x, y, text_str, fontsize=fontsize,
        bbox=dict(boxstyle="round", fc="white", ec="black"),
        horizontalalignment=ha, verticalalignment=va
    )

def draw_arrow(ax, path, width, color, bezier=False, bezier_n=300):
    """
    Create and draw an ArrowETC polygon.
    """
    arrow = ArrowETC(path, arrow_width=width, arrow_head=True, bezier=bezier, bezier_n=bezier_n)
    ax.fill(arrow.x_vertices, arrow.y_vertices, color=color, alpha=1, ec="black", zorder=100)
    return arrow

def main():
    base_path = Path(__file__).resolve().parent.parent / 'resources'

    # plot sparse sample data
    x = np.array([0, 1.5, 3, 5, 7])
    y = np.array([0, 0.5, -0.3, 0.7, -0.2])
    fig, ax = plt.subplots(figsize=(12, 4))
    ax.plot(x, y, 'o-', label='Sample Data')
    ax.set_title("Using ArrowETC with Matplotlib")

    # first annotation: Interesting Point
    point_idx = 2
    point_x, point_y = x[point_idx], y[point_idx]
    text1 = add_annotation(ax, point_x, point_y + 1, "Interesting Point", fontsize=12, ha='center', va='bottom')
    x_center1, y_bottom1, bbox1 = get_bbox_center_bottom(fig, ax, text1)
    arrow1 = draw_arrow(ax, [(x_center1, y_bottom1), (point_x, point_y + 0.05)], width=0.15, color='magenta')

    # second annotation: I have access to each vertex
    vertex1_x, vertex1_y = arrow1.vertices[2]
    text2 = add_annotation(ax, vertex1_x + 1.3, vertex1_y + 0.1, "I have access to each vertex")
    x_center2, y_center2, bbox2 = get_bbox_center_bottom(fig, ax, text2, vertical_offset=-0.02)
    arrow2 = draw_arrow(ax, [(bbox2.xmin - 0.07, y_center2), (vertex1_x, vertex1_y)], width=0.1, color='cyan')

    # third annotation: We can easily add more complex arrows
    text3 = add_annotation(ax, -0.5, -0.8, "We can easily add more complex arrows")
    x_center3, y_center3, bbox3 = get_bbox_center_bottom(fig, ax, text3, vertical_offset=0)
    x_right3, y_center3 = bbox3.x1 + 0.59, (bbox3.y0 + bbox3.y1) / 2

    # path for segmented arrow from text2 to text3
    x_center2 = (bbox2.x0 + bbox2.x1) / 2 + 0.14
    path3 = [
        (x_center2, bbox2.y0 - 0.11),  # below second text
        (x_center2, y_center3),       # straight down
        (x_right3, y_center3)         # left to third text
    ]
    arrow3 = draw_arrow(ax, path3, width=0.1, color='teal')

    # path for Bezier arrow from below text3 to second vertex of arrow3
    vertex3_x, vertex3_y = arrow3.vertices[1]
    bezier_path = [
        (x_center3 + 0.25, bbox3.ymin - 0.11), 
        (x_center3 + 0.25, vertex3_y - 0.15),
        (x_center3 + 1.1, vertex3_y - 0.5),
        (vertex3_x + 0.8, vertex3_y - 0.3),
        (vertex3_x, vertex3_y)
    ]
    draw_arrow(ax, bezier_path, width=0.09, color='orange', bezier=True, bezier_n=800)

    # final plot adjustments
    ax.grid(True)
    ax.set_xlim(-1.5, 8)
    ax.set_ylim(-1.55, 1.5)
    ax.set_aspect('equal')
    fig.savefig(base_path / "example_with_matplotlib.png")

if __name__ == "__main__":
    main()
