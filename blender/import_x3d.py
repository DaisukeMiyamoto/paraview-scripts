# # # # # # # # # # # # # # # # # # # # # # # # # # # #
# Blender python script for rendering x3d scenes
# Tobias Holzmann
# February 2016
# Tobias.Holzmann@Holzmann-cfd.de
# # # # # # # # # # # # # # # # # # # # # # # # # # # #

import bpy

# Loop through all x3d files
# Change the number 500 to the timesteps you have
for num in range(500):

    # Open the file
    # Your file locations
    file = '/home/shorty/OpenFOAM/shorty-2.3.1/run/multiphase/blendMe/x3d/blenderX3D_%d.x3d' % num
    #file = '/home/shorty/OpenFOAM/shorty-2.3.1/run/multiphase/blendMe/x3d/blenderX3D_350.x3d'
    print('Render %s' % file)
    bpy.ops.import_scene.x3d(filepath=file, axis_forward='X', axis_up='Z')

    # Deselect everything
    bpy.ops.object.select_all(action='TOGGLE')

    # Delete not necessary stuff
    for item in bpy.data.objects:
        if item.type != "MESH":
            bpy.data.objects[item.name].select = True
            bpy.ops.object.delete()
        else:
            if ( item.name == "ShapeIndexedFaceSet.003" or item.name == "ShapeIndexedFaceSet.004" or item.name == "ShapeIndexedFaceSet.005" ):
                bpy.data.objects[item.name].select = True
                bpy.ops.object.delete()

    # Rename the left data
    bpy.data.objects["ShapeIndexedFaceSet"].data.name = 'WasserMesh'
    bpy.data.objects["ShapeIndexedFaceSet.001"].data.name = 'GroundMesh'
    bpy.data.objects["ShapeIndexedFaceSet.002"].data.name = 'WandMesh'

    for obj in bpy.context.scene.objects:
        if obj.name == 'ShapeIndexedFaceSet':
            obj.name = 'Wasser'
        if obj.name == 'ShapeIndexedFaceSet.001':
            obj.name = 'Ground'
        if obj.name == 'ShapeIndexedFaceSet.002':
            obj.name = 'Wand'

    # Create a new plane (groundplane) and scale
    bpy.ops.mesh.primitive_plane_add(radius=1, view_align=False, location=(0, 0, 0))
    bpy.ops.transform.resize(value=(8,8,8))
    bpy.ops.transform.translate(value=(0,0,-0.001))

    # Create a new plane (light) move and rotate
    bpy.ops.mesh.primitive_plane_add(radius=1, view_align=False, location=(0, 0, 0))
    bpy.ops.transform.translate(value=(1.5,0.4,3.0))
    bpy.ops.transform.rotate(value=0.523599, axis=(0,1,1))
    bpy.ops.transform.resize(value=(1.2,1.2,1.2))
    bpy.ops.transform.translate(value=(-1.2, 0,0))

    # Deselect everything
    bpy.ops.object.select_all(action='TOGGLE')


    # Materials
    #-------------------------------------------------------------
    ####################
    ### Activate Wasser
    ####################

    # Select Wasser
    bpy.data.objects['Wasser'].select = True
    bpy.ops.object.shade_smooth()

    bpy.context.scene.objects.active = None
    bpy.context.scene.objects.active =bpy.data.objects["Wasser"]

    ob = bpy.context.active_object

    # Create material
    mat = bpy.data.materials.new(name="MaterialWasser")

    # Assign it to object
    if len(ob.data.materials):
        # assign to 1st material slot
        ob.data.materials[0] = mat
    else:
        # no slots
        ob.data.materials.append(mat)

    # Activated material -> cmat
    cmat=ob.active_material
    cmat.use_nodes=True
    TreeNodes=cmat.node_tree
    links = TreeNodes.links

    # Remove nodes (clean it)
    for node in TreeNodes.nodes:
        TreeNodes.nodes.remove(node)

    # Add the guy to the node view
    # Output node
    node_out = TreeNodes.nodes.new(type='ShaderNodeOutputMaterial')
    node_out.location = 200,0

    # Glossy BSDF
    #    node_glossy = TreeNodes.nodes.new(type='ShaderNodeBsdfGlossy')
    #    node_glossy.location =0,180
    #    node_glossy.inputs['Color'].default_value= (0.3,0.5,0.8,1)
    #    node_glossy.inputs['Roughness'].default_value=0.34

    # Glass BSDF
    node_glass = TreeNodes.nodes.new(type='ShaderNodeBsdfGlass')
    node_glass.location =0,180
    node_glass.distribution = 'GGX'
    node_glass.inputs['Color'].default_value= (0.619,0.727,0.8,1)
    node_glass.inputs['Roughness'].default_value=0.34

    # Connect the guys
    links.new(node_glass.outputs[0], node_out.inputs[0])

    ######################
    ### Activate Plane.001
    ######################
    bpy.context.scene.objects.active = None
    bpy.context.scene.objects.active =bpy.data.objects["Plane.001"]

    ob = bpy.context.active_object

    # Create material
    mat = bpy.data.materials.new(name="MaterialLight")

    # Assign it to object
    if len(ob.data.materials):
        # assign to 1st material slot
        ob.data.materials[0] = mat
    else:
        # no slots
        ob.data.materials.append(mat)

    # Activated material -> cmat
    cmat=ob.active_material
    cmat.use_nodes=True
    TreeNodes=cmat.node_tree
    links = TreeNodes.links

    # Remove nodes (clean it)
    for node in TreeNodes.nodes:
        TreeNodes.nodes.remove(node)

    # Add the guy to the node view
    # Output node
    node_out = TreeNodes.nodes.new(type='ShaderNodeOutputMaterial')
    node_out.location = 200,0

    # Emission
    node_emission = TreeNodes.nodes.new(type='ShaderNodeEmission')
    node_emission.location = 0,0
    node_emission.inputs[0].default_value = (1,0.86,0.63,1)  # green RGBA
    node_emission.inputs[1].default_value = 9.0 # strength

    # Connect the guys
    links.new(node_emission.outputs[0], node_out.inputs[0])

    ######################
    ### Activate Plane
    ######################
    bpy.context.scene.objects.active = None
    bpy.context.scene.objects.active =bpy.data.objects["Plane"]

    ob = bpy.context.active_object

    # Create material
    mat = bpy.data.materials.new(name="MaterialGround")

    # Assign it to object
    if len(ob.data.materials):
        # assign to 1st material slot
        ob.data.materials[0] = mat
    else:
        # no slots
        ob.data.materials.append(mat)

    # Activated material -> cmat
    cmat=ob.active_material
    cmat.use_nodes=True
    TreeNodes=cmat.node_tree
    links = TreeNodes.links

    # Remove nodes (clean it)
    for node in TreeNodes.nodes:
        TreeNodes.nodes.remove(node)

    # Add the guy to the node view
    # Output node
    node_out = TreeNodes.nodes.new(type='ShaderNodeOutputMaterial')
    node_out.location = 200,0

    # Toon
    node_Toon = TreeNodes.nodes.new(type='ShaderNodeBsdfDiffuse')
    node_Toon.location = 0,0
    node_Toon.inputs[0].default_value = (0.8,0.7,0.6,1)  # green RGBA
    #node_Toon.component = 'GLOSSY'
    #node_Toon.inputs['Smooth'].default_value = 0.187 # strength

    # Connect the guys
    links.new(node_Toon.outputs[0], node_out.inputs[0])


    ######################
    ### Activate Wand
    ######################
    bpy.context.scene.objects.active = None
    bpy.context.scene.objects.active =bpy.data.objects["Wand"]

    ob = bpy.context.active_object

    bpy.ops.transform.resize(value=(1.001, 1.001, 1.001))


    # Create material
    mat = bpy.data.materials.new(name="MaterialGround")

    # Assign it to object
    if len(ob.data.materials):
        # assign to 1st material slot
        ob.data.materials[0] = mat
    else:
        # no slots
        ob.data.materials.append(mat)

    # Activated material -> cmat
    cmat=ob.active_material
    cmat.use_nodes=True
    TreeNodes=cmat.node_tree
    links = TreeNodes.links

    # Remove nodes (clean it)
    for node in TreeNodes.nodes:
        TreeNodes.nodes.remove(node)

    # Add the guy to the node view
    # Output node
    node_out = TreeNodes.nodes.new(type='ShaderNodeOutputMaterial')
    node_out.location = 200,0

    # Toon
    node_Toon = TreeNodes.nodes.new(type='ShaderNodeBsdfTransparent')
    node_Toon.location = 0,0
    node_Toon.inputs[0].default_value = (0.488,0.66,0.58,1)  # green RGBA

    # Connect the guys
    links.new(node_Toon.outputs[0], node_out.inputs[0])


    ######################
    ### Add a camera
    ######################

    bpy.ops.object.camera_add(location=(0,0,0))

    o = bpy.ops
    o.transform.translate(value=(2.2,0.6,0.9))
    o.transform.rotate(value=1.5708, axis=(0,0,1))
    o.transform.rotate(value=1.3400, axis=(0,1,0))
    o.transform.rotate(value=0.216889, axis=(0,0,1))
    o.transform.rotate(value=0.0872664, axis=(0,0,1))
    bpy.data.objects["Camera"].rotation_euler[0] = 1.18682

    o.transform.translate(value=(-1,0,0))
    o.transform.rotate(value=0.785398, axis=(0,0,1))
    o.transform.translate(value=(0,0.4,0))
    o.transform.translate(value=(0,0,0.4))
    bpy.data.objects["Camera"].rotation_euler[0] = 0.890118
    bpy.data.objects["Camera"].rotation_euler[2] = 2.44346


    ############
    # For saving
    ############

    cam = bpy.data.objects['Camera']
    bpy.context.scene.camera = cam

    bpy.context.scene.cycles.samples = 120

    bpy.data.scenes['Scene'].render.filepath = '/home/shorty/blender/CFD/blended_%d.png' % num
    bpy.ops.render.render( write_still = True )


    ###################
    # Delete everything
    ###################

    bpy.ops.object.select_all(action='TOGGLE')
    bpy.ops.object.select_all(action='TOGGLE')
    bpy.ops.object.delete()
