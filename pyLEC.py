#!/usr/bin/env python
# coding: utf-8

import numpy as np
from scipy import spatial
from matplotlib import path


def pyLEC(points):
    '''
    LEC: Largest Empty Circle between Points in a flat plane
    also know as Pole of Inaccessibility problem.
    

    see: https://en.wikipedia.org/wiki/Largest_empty_sphere
    The largest empty circle problem is the problem of finding
    a circle of largest radius in the plane whose interior
    does not overlap with any given point and whose center
    is lying in the convex hull of the points.
    
    Hint: The LEC is centered at the internal Voronoi vertices
    with the largest shortest distance to the polygon

    Parameters
    ----------
    points : 2d numpy array with x, y coordinate of the points
             on the Concave Hull

    Returns
    -------
    LEC_Radius: scalar
    LEC_Centroid: (x, y)
    '''
    
    # Error handling
    if points.shape[0] < 3:
        print('less than 3 Points: ')
        return np.nan, (np.nan, np.nan)

    # Step 1: get Voronoi vertices (scipy.spatial)
    vor_Verts = spatial.Voronoi(points).vertices
 
    # Step 2: select Voronoi vertices inside the convex hull (mpl)
    polygon = path.Path(points)
    selector = polygon.contains_points(vor_Verts)
    vor_Verts = vor_Verts[selector]  # Verts inside Polygon Verts inside Polygon

    # Step 3: Get nearest neighbors as well as radius und centroid of LEC
    tree = spatial.KDTree(points)
    neighbores = tree.query(vor_Verts)
    idx = np.argmax(neighbores[0])
    LEC_Radius = neighbores[0][idx]
    LEC_Centroid = vor_Verts[idx]
    
    return LEC_Radius, LEC_Centroid





