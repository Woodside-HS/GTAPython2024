import bpy

class OBJECT_OT_AddSphere(bpy.types.Operator):
    bl_idname = "object.add_sphere"
    bl_label = "Add Rocket"
    
    def execute(self, context):
        bpy.ops.mesh.primitive_uv_sphere_add(location = (1,0,0), scale = (1.5, 1.5, 1.5))
        bpy.ops.mesh.primitive_uv_sphere_add(location = (-1,0,0), scale = (1.5, 1.5, 1.5))
        bpy.ops.mesh.primitive_cylinder_add(enter_editmode=False, align='WORLD', location=(0, 0, 2), scale=(1, 1, 2))
        bpy.ops.mesh.primitive_uv_sphere_add(location = (0,0,4))
        bpy.ops.object.select_all(action='SELECT')
        bpy.ops.object.shade_smooth()

        return {'FINISHED'}

class OBJECT_OT_Clear(bpy.types.Operator):
    bl_idname = "object.clear_scene"
    bl_label = "Clear"
    
    def execute(self, context):
        bpy.ops.object.select_all(action='SELECT')
        bpy.ops.object.delete(use_global=False)
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
        row.label(text = "Rocket Ship", icon = 'COLOR_RED')
        row.operator("object.add_sphere")
        row = layout.row()
        row.label(text = "Clear", icon = 'TRASH')
        row.operator("object.clear_scene")

        
        
def register():
    bpy.utils.register_class(TestPanel)
    bpy.utils.register_class(OBJECT_OT_AddSphere)
    bpy.utils.register_class(OBJECT_OT_Clear)
    
def unregister():
    bpy.utils.unregister_class(TestPanel)
    bpy.utils.unregister_class(OBJECT_OT_AddSphere)
    bpy.utils.unregister_class(OBJECT_OT_Clear)
    
if __name__ == "__main__":
    register()
    
    