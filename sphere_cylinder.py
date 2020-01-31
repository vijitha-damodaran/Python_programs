"""
A melting furnace converts a hollow sphere into a solid cylinder of 3cm diameter with a 5% loss. 
Write a program that finds out the length of the solid cylinder when
 the inner and external radii of the hollow sphere are known

Volume of sphere = 4/3 * pi * r * r * r
Volume of cylinder = pi * r * r * height
"""
def get_radius_ext():
    res=int(sys.argv[1])
    return res

def get_radius_inner():
    res=int(sys.argv[2])
    return res

def height_cylindr(r_ext,r_int,r_cyl):
    res=4*(r_ext**3-r_int**3)/(3*r_cyl**2)
    return res

#main pgm starts from here
if __name__ == "__main__":
    import sys
    radii_cyl=3
    radii_ext=get_radius_ext()
    radii_int=get_radius_inner()
    height=height_cylindr(radii_ext,radii_int,radii_cyl)
    print('Height of cylinder=',height)
