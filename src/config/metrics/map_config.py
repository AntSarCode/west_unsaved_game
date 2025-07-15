from src.config.metrics.map_loader import MAP_NODES, MAP_WIDTH, MAP_HEIGHT, TERRAIN_TYPES

def find_node_by_name(name):
    return next((node for node in MAP_NODES if node['name'] == name), None)

def get_capture_zones():
    return [node for node in MAP_NODES if node.get('capture_zone')]

def is_within_bounds(x, y):
    return 0 <= x <= MAP_WIDTH and 0 <= y <= MAP_HEIGHT

def terrain_multiplier(terrain_type):
    return TERRAIN_TYPES.get(terrain_type, 1.0)

def node_distance(node1, node2):
    dx = node2['x'] - node1['x']
    dy = node2['y'] - node1['y']
    return (dx ** 2 + dy ** 2) ** 0.5
