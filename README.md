    LEC: Largest Empty Circle between Points in a flat plane
    also know as Toxic Waste Dump problem
    

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