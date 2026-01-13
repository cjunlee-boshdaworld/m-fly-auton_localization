# main.py
import numpy as np
from localization import triangulate_two_rays



def main():
    Fx=float(input("cam fx: "))
    Fy=float(input("cam fy: "))
    Cx=float(input("cam cx: "))
    Cy=float(input("cam cy: "))
    K1 = np.array([
        [Fx, 0, Cx],
        [0, Fy, Cy],
        [0, 0, 1]
    ])
    R1 = np.eye(3)
    t1 = np.zeros((3, 1))

    R2 = np.eye(3)
    t2 = np.zeros((3,1))
    K2= K1.copy()
    

    print("Press Ctrl+C to stop.")
    while True:
        
        # take point inputs

        X = #do something

        print("3D point:", X)


if __name__ == "__main__": # makes sure it only runs if called directly
    main()
