# Title : Scatter Objects Randomly on a Plane
# Project : BADGE : Blender AI Dataset Generation Engine
# Author : Tej Pandit
# Date : Feb 2024

import bpy
import random

# Get the plane object and collection
plane_obj = bpy.data.objects['Plane']
collection = bpy.data.collections['Objects']

# Function to create a random location within the plane's bounds
def random_location_within_bounds(obj):
    min_x, min_y, min_z = obj.bound_box[0]
    max_x, max_y, max_z = obj.bound_box[6]
    return (random.uniform(min_x, max_x), random.uniform(min_y, max_y), min_z)

# Scatter objects from the collection
for obj in collection.objects:
    # Create a copy of the object
    new_obj = obj.copy()
    new_obj.location = random_location_within_bounds(plane_obj)

    # Link the copied object to the current scene
    scene = bpy.context.scene
    scene.collection.objects.link(new_obj)