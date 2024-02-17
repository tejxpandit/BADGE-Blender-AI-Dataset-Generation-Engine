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

