import bpy

class OBJECT_OT_BryanSize(bpy.types.Operator):
    
    bl_idname = "object.add_bryan"
    bl_label = "Bryan Size"
    
    def execute(self, context):
        bpy.ops.object.select_all(action='SELECT')
        bpy.ops.object.delete(use_global=False)
        bpy.ops.mesh.primitive_cylinder_add(enter_editmode=False, align='WORLD', location=(0, 0, 1), scale=(0.5, 0.5, 1))
        bpy.ops.mesh.primitive_uv_sphere_add(location = (.5,0,0), scale = (.7, .7, .7))
        bpy.ops.mesh.primitive_uv_sphere_add(location = (-.5,0,0), scale = (.7, .7, .7))
        bpy.ops.mesh.primitive_uv_sphere_add(location = (0,0,2), scale = (.5, .5, .5))
        bpy.ops.object.select_all(action='SELECT')
        bpy.ops.object.shade_smooth()
        
        return {'FINISHED'}

class OBJECT_OT_MrgSize(bpy.types.Operator):
    
    bl_idname = "object.add_cylinder"
    bl_label = "Mr. G Size"
    
    def execute(self, context):
        bpy.ops.object.select_all(action='SELECT')
        bpy.ops.object.delete(use_global=False)
        bpy.ops.mesh.primitive_cylinder_add(enter_editmode=False, align='WORLD', location=(0, 0, 6), scale=(2, 2, 6))
        bpy.ops.mesh.primitive_uv_sphere_add(location = (1,0,0), scale = (2.5, 2.5, 2.5))
        bpy.ops.mesh.primitive_uv_sphere_add(location = (-1,0,0), scale = (2.5, 2.5, 2.5))
        bpy.ops.mesh.primitive_uv_sphere_add(location = (0,0,12), scale = (2, 2, 2))
        bpy.ops.object.select_all(action='SELECT')
        bpy.ops.object.shade_smooth()
        
        return {'FINISHED'}
    
    
class OBJECT_OT_AddSphere(bpy.types.Operator):
    bl_idname = "object.add_sphere"
    bl_label = "Add Rocket"
    
    def execute(self, context):
        bpy.ops.object.select_all(action='SELECT')
        bpy.ops.object.delete(use_global=False)
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
        row = layout.row()
        row.label(text = "Mr. G Size", icon = 'EVENT_G')
        row.operator("object.add_cylinder")
        row = layout.row()
        row.label(text = "Bryan Size", icon = 'EVENT_B')
        row.operator("object.add_bryan")

        
        
def register():
    bpy.utils.register_class(TestPanel)
    bpy.utils.register_class(OBJECT_OT_AddSphere)
    bpy.utils.register_class(OBJECT_OT_Clear)
    bpy.utils.register_class(OBJECT_OT_MrgSize)
    bpy.utils.register_class(OBJECT_OT_BryanSize)
    
def unregister():
    bpy.utils.unregister_class(TestPanel)
    bpy.utils.unregister_class(OBJECT_OT_AddSphere)
    bpy.utils.unregister_class(OBJECT_OT_Clear)
    bpy.utils.unregister_class(OBJECT_OT_MrgSize)
    bpy.utils.unregister_class(OBJECT_OT_BryanSize)
    
if __name__ == "__main__":
    register()
    
    