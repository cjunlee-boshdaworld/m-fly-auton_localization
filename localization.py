import numpy as np
import cv2

def pixel_to_ray(pixel, K, plane_z=0.0, cam_pose_R=np.eye(3), cam_pose_t=np.zeros((3,1))):
    """
    Backproject a pixel px=(u,v) to a 3D point on a horizontal plane (z=plane_z) in world coordinates.

    Arguments:
      px: (u,v) pixel coordinates (tuple or 1x2 array)
      K: 3x3 camera intrinsic matrix
      plane_z: z coordinate of the plane in WORLD frame (meters)
      cam_pose_R, cam_pose_t: camera-to-world rotation (3x3) and translation (3x1).
                           (i.e., world_point = R_cam_to_world @ cam_point + t_cam_to_world)

    Returns:
      X_world (3,) 3D point in world coordinates lying on plane_z (if intersection exists)
    """
    return

def triangulate_two_rays(pt1, pt2, K1, K2, R1=np.eye(3), t1=np.zeros((3,1)), R2=np.eye(3), t2=np.zeros((3,1)), dist1=None, dist2=None):
    """
    Backproject a pixel px=(u,v) to a 3D point on a horizontal plane (z=plane_z) in world coordinates.

    Arguments:
      px: (u,v) pixel coordinates (tuple or 1x2 array)
      K: 3x3 camera intrinsic matrix
      dist: distortion coeffs (None if none)
      plane_z: z coordinate of the plane in WORLD frame (meters)
      cam_pose_R, cam_pose_t: camera-to-world rotation (3x3) and translation (3x1).
                           (i.e., world_point = R_cam_to_world @ cam_point + t_cam_to_world)

    Returns:
      X_world (3,) 3D point in world coordinates lying on plane_z (if intersection exists)
    """
    return