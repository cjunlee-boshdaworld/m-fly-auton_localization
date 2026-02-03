# main.py
import numpy as np
from localization import triangulate_two_rays



def main():
    Fx=float(input("cam fx: ")) #Focal lengths #Calibrate these with opencv calibrate camera function
    Fy=float(input("cam fy: "))
    Cx=float(input("cam cx: ")) #This is center of the image in terms of pixels
    Cy=float(input("cam cy: ")) 
    K1 = np.array([
        [Fx, 0, Cx],
        [0, Fy, Cy],
        [0, 0, 1]
    ])
    t1 = np.zeros((3, 1))
    R1 = np.eye(3)
    tx = float(input("Camera translation tx (meters): ")) # position of camera 2 relative to camera 1 in meters
    ty = float(input("Camera translation ty (meters): "))
    tz = float(input("Camera translation tz (meters): "))

    

    t2 = np.array([[tx], [ty], [tz]])


    R2 = np.eye(3)
    K2= K1.copy()
    

    print("Press Ctrl+C to stop.")
    while True:
        
        # take point inputs
        x1 = float(input("x1: ")) #points on the image
        y1 = float(input("y1: "))
        x2 = float(input("x2: "))
        y2 = float(input("y2: ")) 

        pt1 = np.array([x1, y1]) 
        pt2 = np.array([x2, y2])

        X = triangulate_two_rays(pt1,pt2,K1,K2,R1,t1,R2,t2)

        print("3D point:", X) #returns the point but its relative coords to camera 1


if __name__ == "__main__": # makes sure it only runs if called directly
    main()
