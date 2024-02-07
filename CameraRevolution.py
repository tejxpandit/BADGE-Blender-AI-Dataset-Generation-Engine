# Title : Camera Revolving around Target
# Project : BADGE : Blender AI Dataset Generation Engine
# Author : Tej Pandit
# Date : Feb 2024

import bpy
import math

# Get the camera and object objects
camera = bpy.data.objects['Camera']
object_to_orbit = bpy.data.objects['Object_Name']  # Replace 'Object_Name' with the actual object's name

# Set initial camera position and rotation
distance = 5  # Adjust this to control the distance from the object
angle = 0  # Initial angle
camera.location = (distance * math.cos(angle), distance * math.sin(angle), 0)
camera.rotation_euler = (0, 0, 0)

# Function to update camera position and rotation
def update_camera(frame):
    global angle
    angle = frame * 0.05  # Change 0.05 to control rotation speed
    camera.location = (distance * math.cos(angle), distance * math.sin(angle), 0)
    camera.rotation_euler = (0, 0, angle)

# Add a handler to update the camera on every frame change
bpy.app.handlers.frame_change_post.append(update_camera)