import bpy

class OBJECT_OT_AddSphere(bpy.types.Operator):
    bl_idname = "object.add_sphere"
    bl_label = "Add Dock"
    
    def execute(self, context):
        bpy.ops.mesh.primitive_uv_sphere_add(location = (-2, 0, 2))
        bpy.ops.mesh.primitive_uv_sphere_add(location = (2, 0, 2))
        bpy.ops.mesh.primitive_uv_sphere_add(location = (0, 0, 2))
        bpy.ops.mesh.primitive_cylinder_add(enter_editmode=False, align='WORLD', location=(2, 0, 0), scale=(1, 1, 2))
        bpy.ops.mesh.primitive_cylinder_add(enter_editmode=False, align='WORLD', location=(-2, 0, 0), scale=(1, 1, 2))
        bpy.ops.mesh.primitive_cylinder_add(enter_editmode=False, align='WORLD', location=(0, 0, 1.5), scale=(1, 1, 0.5))

        return {'FINISHED'}
    
    
class TestPanel(bpy.types.Panel):
    bl_label = "Test Panel"
    bl_idname = "PT_TestPanel"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'The Best Add-on'
    
    def draw(self, context):
        layout = self.layout
        row = layout.row()
        row.label(text = "Docking Station", icon = 'COLOR_RED')
        row.operator("object.add_sphere")


def register():
    bpy.utils.register_class(TestPanel)
    bpy.utils.register_class(OBJECT_OT_AddSphere)
   

def unregister():
    bpy.utils.register_class(TestPanel)
    bpy.utils.register_class(OBJECT_OT_AddSphere)

if __name__ == "__main__":
    register()