"""
A melting furnace converts a hollow sphere into a solid cylinder
of 3cm diameter with a 5% loss. 
Write a program that finds out the length of the solid cylinder when
 the inner and external radii of the hollow sphere are known

Volume of sphere = 4/3 * pi * r * r * r
Volume of cylinder = pi * r * r * height
"""

def volume_sphere(r_ext,r_int):
    res=4*math.pi*(r_ext**3-r_int**3)/3
    return res

def volume_sphere_with_loss(vol,loss):
    res=vol*95/100
    return res

def height_cylinder(vol,radi):
    res=vol/(math.pi*(radi**2))
    return res

#main pgm starts from here
if __name__ == "__main__":
    import sys
    import math
    radii_cyl=3
    loss_perc=5
    radii_ext=int(sys.argv[1])
    radii_int=int(sys.argv[2])
    vol_sphere=volume_sphere(radii_ext,radii_int)
    vol_sphere_with_loss=volume_sphere_with_loss(vol_sphere,loss_perc)
    height_cyl=height_cylinder(vol_sphere_with_loss,radii_cyl)
    print('Height of cylinder=',height_cyl)
