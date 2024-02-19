# Title : Highlight Selected Objects in Render
# Project : BADGE : Blender AI Dataset Generation Engine
# Author : Tej Pandit
# Date : Feb 2024

import bpy

# Get selected and non-selected objects
selected_objs = bpy.context.selected_objects
non_selected_objs = [obj for obj in bpy.context.scene.objects if obj not in selected_objs]

# Define pink color
pink = (1, 0.75, 0.75, 1)  # (red, green, blue, alpha)

# Create a new pink material (optional)
pink_material = bpy.data.materials.new(name="Pink Material")
pink_material.diffuse_color = pink

# Assign pink material to selected objects
for obj in selected_objs:
    if obj.data.materials:
        # Replace existing material with pink material
        obj.data.materials[0] = pink_material
    else:
        # Add pink material to object
        obj.data.materials.append(pink_material)

