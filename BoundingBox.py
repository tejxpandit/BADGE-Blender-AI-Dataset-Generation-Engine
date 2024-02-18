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

# Create a new mesh for the bounding box
mesh = bpy.data.meshes.new("BoundingBox")
mesh.from_pydata([min_x, min_y, min_z, max_x, min_y, min_z, max_x, max_y, min_z, min_x, max_y, min_z], [], [(0, 0, 1), (0, 0, 1), (0, 0, 1), (0, 0, 1)])

# Create a new object from the mesh and link it to the scene
bbox_obj = bpy.data.objects.new("BoundingBox", mesh)
bpy.context.collection.objects.link(bbox_obj)

# Set object origin to the center of the bounding box
bbox_obj.location = (min_x + max_x) / 2, (min_y + max_y) / 2, (min_z + max_z) / 2

# Set the bounding box object's draw type to "Wire" for better visualization
bbox_obj.data.display.draw_type = 'WIRE'