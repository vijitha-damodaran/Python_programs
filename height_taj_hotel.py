"""
Like everyone I too enjoyed watching Taj Hotel from Mumbai’s Gateway of India. 
When I stood at the Gateway of India, I saw that the 
top of Taj Hotel’s tower was at an angle of elevation of 25 degrees.
I then walked to the security guard near the gate of Taj Hotel and 
noticed that the top of the tower was at an angle of elevation of 65 degrees. 
The security guard informed me that the Tower was about 100 yards from the gate.

Write a program to find the height of Taj Hotel’s tower and 
the distance between Gateway of India and Taj Hotel’s entrance.
"""

def taj_height(dist,ang):
    res=dist*math.tan(math.radians(ang))
    return res

def dist_goi_and_entrance(hght,dist,ang):
    res=(hght/math.tan(math.radians(ang)))-dist
    return res

#main starts from here
if __name__ == "__main__":
    import math
    dist_security_tower=100
    angle_elev_security=65
    angle_elev_goi=25
    height=taj_height(dist_security_tower,angle_elev_security)
    distance_goi_entrance=dist_goi_and_entrance(height,dist_security_tower,angle_elev_goi)
    print('Height of taj hotel=',height)
    print('Distance between gateway and security personal=',distance_goi_entrance)
