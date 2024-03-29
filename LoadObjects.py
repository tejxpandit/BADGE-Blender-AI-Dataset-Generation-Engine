# Title : Import and Load 3D Objects from Folder
# Project : BADGE : Blender AI Dataset Generation Engine
# Author : Tej Pandit
# Date : Feb 2024

import bpy
import os

# Specify the folder containing the 3D objects
folder_path = "/path/to/your/folder"  # Replace with the actual path

# Import all .obj files from the folder
for filename in os.listdir(folder_path):
   if filename.endswith(".obj"):
       filepath = os.path.join(folder_path, filename)
       bpy.ops.import_scene.obj(filepath=filepath)

# Position all imported objects at the origin
for obj in bpy.context.scene.objects:
   if obj.type == "MESH":
       obj.location = (0, 0, 0)

# Hide all objects except the first one
for obj in bpy.context.scene.objects[1:]:
   obj.hide_viewport = True
   obj.hide_render = True
   