import numpy as np
import cv2
from localization import triangulate_two_rays   

def project_point(K, R, t, X):
    """Project 3D point X (world) into camera image."""
    X_cam = R @ X.reshape(3,1) + t
    x = K @ X_cam
    return (x[0]/x[2], x[1]/x[2])  # pixel coords

def main():
    # ---------- Camera intrinsics ----------
    fx = fy = 800
    cx = cy = 320
    K = np.array([[fx, 0, cx],
                  [0, fy, cy],
                  [0,  0,  1]])

    # ---------- Camera extrinsics ----------
    R1 = np.eye(3)
    t1 = np.zeros((3,1))

    R2 = np.eye(3)
    t2 = np.array([[1.0],[0],[0]])  # second cam 1m to the right

    # ---------- Ground truth 3D point ----------
    X_gt = np.array([0.5, 0.2, 4.0])

    # ---------- Project to both images ----------
    u1,v1 = project_point(K, R1, t1, X_gt)
    u2,v2 = project_point(K, R2, t2, X_gt)

    pt1 = (float(u1), float(v1))
    pt2 = (float(u2), float(v2))

    print("Pixel in cam1:", pt1)
    print("Pixel in cam2:", pt2)

    # ---------- Triangulate ----------
    X_est = triangulate_two_rays(pt1, pt2, K, K, R1, t1, R2, t2)

    print("\nGround truth:", X_gt)
    print("Triangulated:", X_est.reshape(3))

if __name__ == "__main__":
    main()
