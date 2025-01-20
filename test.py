import open3d as o3d
import random
import numpy as np

def parse_obj(file_path):
    vertices = []
    lines = []
    with open(file_path, 'r') as file:
        for line in file:
            if line.startswith('v '):
                parts = line.strip().split()
                x, y, z = float(parts[1]), float(parts[2]), float(parts[3])
                vertices.append([x, y, z])
            elif line.startswith('l '):
                parts = line.strip().split()
                start, end = int(parts[1]) - 1, int(parts[2]) - 1
                lines.append([start, end])
    return vertices, lines

def create_cylinder(start_point, end_point, radius=0.03, resolution=20):
    start_point = np.array(start_point)
    end_point = np.array(end_point)
    direction = end_point - start_point
    length = np.linalg.norm(direction)
    direction /= length

    cylinder = o3d.geometry.TriangleMesh.create_cylinder(radius, length, resolution=resolution)
    cylinder.paint_uniform_color([random.random(), random.random(), random.random()])

    # Align cylinder with the direction vector
    z_axis = np.array([0, 0, 1])
    rotation_matrix = np.eye(3)
    if not np.allclose(direction, z_axis):
        axis = np.cross(z_axis, direction)
        angle = np.arccos(np.dot(z_axis, direction))
        rotation_matrix = o3d.geometry.get_rotation_matrix_from_axis_angle(axis * angle)

    cylinder.rotate(rotation_matrix, center=(0, 0, 0))
    cylinder.translate(start_point)

    return cylinder

def create_cylinders(vertices, lines):
    cylinders = []
    for line in lines:
        start_point = vertices[line[0]]
        end_point = vertices[line[1]]
        cylinder = create_cylinder(start_point, end_point)
        cylinders.append(cylinder)
    return cylinders

def parse_txt(file_path):
    points = []
    with open(file_path, 'r') as file:
        for line in file:
            parts = line.strip().split()
            x, y, z = float(parts[0]), float(parts[1]), float(parts[2])
            points.append([x, y, z])
    return points

def visualize_lines_and_planes(lines_obj_path, txt_path):
    lines_vertices, lines_lines = parse_obj(lines_obj_path)
    points = parse_txt(txt_path)

    cylinders = create_cylinders(lines_vertices, lines_lines)

    point_cloud = o3d.geometry.PointCloud()
    point_cloud.points = o3d.utility.Vector3dVector(points)
    point_cloud.paint_uniform_color([0.45, 0.45, 0.45])

    o3d.visualization.draw_geometries(cylinders + [point_cloud])

if __name__ == "__main__":
    lines_obj_path = r"C:\Users\Milo\OneDrive - Universiteit Utrecht\Scriptie\Data\dutch_data\Test\individual_lines\cluster_3_3-lines.obj"
    txt_path = r"C:\Users\Milo\OneDrive - Universiteit Utrecht\Scriptie\Data\dutch_data\Test\individual_lines\cluster_3_3.txt"

    visualize_lines_and_planes(lines_obj_path, txt_path)