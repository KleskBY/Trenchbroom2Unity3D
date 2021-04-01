bl_info = {
    "name": "Trenchbroom2Unity3D",
    "blender": (2, 80, 0),
    "category": "Object",
}

import bpy


class Trenchbroom2Unity3D(bpy.types.Operator):
    """Trenchbroom2Unity3D"""      # Use this as a tooltip for menu items and buttons.
    bl_idname = "object.trenchbroom2unity"        # Unique identifier for buttons and menu items to reference.
    bl_label = "Trenchbroom2Unity3D"         # Display name in the interface.
    bl_options = {'REGISTER', 'UNDO'}  # Enable undo for the operator.

    def execute(self, context):        # execute() is called when running the operator.

        # The original script
        lastName = ""
        scene = bpy.context.scene
        for obj in scene.objects:
                if obj.type == 'MESH':
                    temp = obj.name.split("_")
                    if(temp[0] == lastName):
                        print("Merge ", lastName, " with ", obj.name)
                        obj.select_set(True)
                        print(bpy.context.selected_objects)
                        bpy.ops.object.join()
                    else:
                        print("Now joining ", temp[0])
                        bpy.ops.object.select_all(action='DESELECT')
                        lastName = temp[0]
                        bpy.context.view_layer.objects.active = obj
                        obj.select_set(True)

        return {'FINISHED'}            # Lets Blender know the operator finished successfully.

def menu_func(self, context):
    self.layout.operator(Trenchbroom2Unity3D.bl_idname)

def register():
    bpy.utils.register_class(Trenchbroom2Unity3D)
    bpy.types.VIEW3D_MT_object.append(menu_func)

def unregister():
    bpy.utils.unregister_class(Trenchbroom2Unity3D)


# This allows you to run the script directly from Blender's Text editor
# to test the add-on without having to install it.
if __name__ == "__main__":
    register()