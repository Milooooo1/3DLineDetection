import open3d as o3d

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

def create_line_set(vertices, lines, color):
    line_set = o3d.geometry.LineSet()
    line_set.points = o3d.utility.Vector3dVector(vertices)
    line_set.lines = o3d.utility.Vector2iVector(lines)
    colors = [color for _ in range(len(lines))]
    line_set.colors = o3d.utility.Vector3dVector(colors)
    return line_set

def parse_txt(file_path):
    points = []
    with open(file_path, 'r') as file:
        for line in file:
            parts = line.strip().split()
            x, y, z = float(parts[0]), float(parts[1]), float(parts[2])
            points.append([x, y, z])
    return points

def visualize_lines_and_planes(planes_obj_path, lines_obj_path, txt_path):
    # Parse planes and lines from .obj files
    planes_vertices, planes_lines = parse_obj(planes_obj_path)
    lines_vertices, lines_lines = parse_obj(lines_obj_path)

    # Parse points from .txt file
    points = parse_txt(txt_path)

    # Create line sets for visualization
    # planes_line_set = create_line_set(planes_vertices, planes_lines, [1, 0, 0])  # Red for planes
    lines_line_set = create_line_set(lines_vertices, lines_lines, [0, 1, 0])    # Green for lines

    # Create point cloud for visualization
    point_cloud = o3d.geometry.PointCloud()
    point_cloud.points = o3d.utility.Vector3dVector(points)
    point_cloud.paint_uniform_color([0.45, 0.45, 0.45])

    # Visualize
    o3d.visualization.draw_geometries([lines_line_set])

if __name__ == "__main__":
    planes_obj_path = r"C:\Users\Milo\OneDrive - Universiteit Utrecht\Scriptie\Data\dutch_data\Test\individual_lines\cluster_4_0-planes.obj"
    lines_obj_path = r"C:\Users\Milo\OneDrive - Universiteit Utrecht\Scriptie\Data\dutch_data\Test\individual_lines\cluster_4_0-lines.obj"
    txt_path = r"C:\Users\Milo\OneDrive - Universiteit Utrecht\Scriptie\Data\dutch_data\Test\individual_lines\cluster_4_0.txt"

    visualize_lines_and_planes(planes_obj_path, lines_obj_path, txt_path)