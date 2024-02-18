# Title : Calculate Bounding Box for Target
# Project : BADGE : Blender AI Dataset Generation Engine
# Author : Tej Pandit
# Date : Feb 2024

import bpy

# Get the active object
obj = bpy.context.active_object

# Get object's bounding box corners in world space
bbox_corners = [obj.matrix_world @ corner for corner in obj.bound_box]

# Calculate minimum and maximum coordinates
min_x, min_y, min_z = min(coord.x for coord in bbox_corners), min(coord.y for coord in bbox_corners), min(coord.z for coord in bbox_corners)
max_x, max_y, max_z = max(coord.x for coord in bbox_corners), max(coord.y for coord in bbox_corners), max(coord.z for coord in bbox_corners)

