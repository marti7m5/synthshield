import bpy
import random
import os

# Clear scene
bpy.ops.object.select_all(action='SELECT')
bpy.ops.object.delete()

# Create output directory
script_dir = os.path.dirname(os.path.abspath(__file__))
output_dir = os.path.join(script_dir, "output")
annotations_dir = os.path.join(script_dir, "annotations")
os.makedirs(annotations_dir, exist_ok=True)
os.makedirs(output_dir, exist_ok=True)

# Add camera
bpy.ops.object.camera_add(location=(0, -8, 5), rotation=(1.1, 0, 0))
camera = bpy.context.object
bpy.context.scene.camera = camera

# Add lighting
bpy.ops.object.light_add(type='SUN', location=(5, 5, 10))

# Add ground
bpy.ops.mesh.primitive_plane_add(size=15)

# Generate multiple scenes
for i in range(5):
    cubes = []
    labels = []

    for j in range(random.randint(3, 8)):
        x = random.uniform(-5, 5)
        y = random.uniform(-5, 5)

        bpy.ops.mesh.primitive_cube_add(location=(x, y, 0.5))
        obj = bpy.context.object
        cubes.append(obj)

        # Convert to YOLO-style normalized coordinates
        x_center = 0.5 + (x / 20)
        y_center = 0.5 + (y / 20)
        width = 0.1
        height = 0.1

        label = f"0 {x_center} {y_center} {width} {height}"
        labels.append(label)

    # Render image
    image_path = os.path.join(output_dir, f"scene_{i}.png")
    bpy.context.scene.render.filepath = image_path
    bpy.ops.render.render(write_still=True)

    # Save annotation file
    label_path = os.path.join(annotations_dir, f"scene_{i}.txt")
    with open(label_path, "w") as f:
        f.write("\n".join(labels))

    # Cleanup
    for obj in cubes:
        bpy.data.objects.remove(obj, do_unlink=True)

print("Dataset generation complete.")
