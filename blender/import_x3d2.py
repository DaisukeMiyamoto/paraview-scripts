import bpy

##################################################################

path_tox3d='C:/Users/xxx/Documents/blender/'
path_toimage='C:/Users/xxx/Documents/blender/'
filename_ofx3d='projectname_'
filename_ofimage='newimage_'
startframe_ofx3d=0
endframe_ofx3d=10



##################################################################
#---------------------------------------------------------------#
##  Delete everything from scene before importing              ##

#bpy.ops.object.select_all(action='TOGGLE')
#bpy.ops.object.delete()

#---------------------------------------------------------------#
##  Add a text                                                  #
#bpy.ops.object.text_add()
#bpy.ops.object.editmode_toggle()
#bpy.ops.font.delete()
#bpy.ops.font.text_insert(text="Frame: ")
#bpy.ops.object.editmode_toggle()
#bpy.ops.object.select_all(action='TOGGLE')
#bpy.data.objects['Text'].name="Frametext"

#---------------------------------------------------------------#
#bpy.context.scene.frame_set(currentframe)
bpy.ops.object.add()
bpy.data.objects['Empty'].select=True
bpy.data.objects['Empty'].name="Aux_Empty"
#bpy.ops.anim.keyframe_insert(type='Location', confirm_success=True)
bpy.context.active_object.location =(0.0, 0.0, 0.0)
bpy.data.objects['Aux_Empty'].select=False


for currentframe in range(startframe_ofx3d,endframe_ofx3d):
    bpy.context.scene.frame_set(currentframe)
    #bpy.ops.object.add()
    bpy.data.objects['Aux_Empty'].select=True
    bpy.context.scene.objects.active = bpy.data.objects['Aux_Empty']
    #bpy.data.objects['Empty'].name="MyEmpty"
    obj = bpy.context.object
    obj.location[2] = 0.0
    #obj.keyframe_insert()
    obj.keyframe_insert(data_path='location')
    #bpy.context.active_object.location =(0.0, 0.0, 0.0)
    bpy.data.objects['Aux_Empty'].select=False

    #---------------------------------------------------------------#
    ## import the x3d file
    bpy.ops.import_scene.x3d(filepath=path_tox3d+filename_ofx3d+str(currentframe)+'.x3d', filter_glob="*.x3d;*.wrl", axis_forward='Z', axis_up='Y')
    #---------------------------------------------------------------#
    ## add the frame number to the text
    #bpy.data.objects["Frametext"].select=True
    #bpy.ops.object.editmode_toggle()
    #bpy.ops.font.delete()
    #bpy.ops.font.text_insert(text="Frame: "+str(currentframe))
    #bpy.ops.object.editmode_toggle()
    #bpy.data.objects["Frametext"].select=False

    #---------------------------------------------------------------#
    ## rename the geometry to "imported geometry"
    bpy.data.objects['ShapeIndexedFaceSet'].name="imported_geometry"
    bpy.data.objects['imported_geometry'].select=True
    bpy.context.scene.objects.active = bpy.data.objects['imported_geometry']
    bpy.context.active_object.material_slots[0].material.use_vertex_color_paint=True
    #bpy.ops.anim.keyframe_insert(type='Location', confirm_success=True)
    bpy.data.objects['imported_geometry'].select=False
    ## rename the default lamp to imported_lamp and delete right away
    bpy.data.objects['TODO'].name="imported_lamp"
    bpy.data.objects['imported_lamp'].select=True
    bpy.ops.object.delete()
    ## rename the default camera to imported_camera and delete right away
    bpy.data.objects['Viewpoint'].name="imported_camera"
    bpy.data.objects['imported_camera'].select=True
    bpy.ops.object.delete()

    #bpy.context.active_object.location = position





    #for object_name in candidate_list:
    #      bpy.data.objects[object_name].select = True
    #     bpy.context.active_object.location = position
    #  bpy.ops.anim.keyframe_insert(type='Location', confirm_success=True)


    bpy.data.scenes['Scene'].render.resolution_percentage=100

    bpy.ops.render.render(write_still=True)

    bpy.data.images['Render Result'].file_format='PNG'
    bpy.data.images['Render Result'].save_render(filepath=path_toimage+filename_ofimage+str(currentframe)+'.png')
    bpy.data.objects['imported_geometry'].select=True
    bpy.ops.object.delete()


bpy.data.objects['Aux_Empty'].select=True
bpy.ops.object.delete()