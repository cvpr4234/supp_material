import glob
import os
import point_cloud_utils as pcu

base = 'shapenet_reconstruction'

methods = glob.glob(base + '/*/')


for method in methods: 
    scenes = glob.glob(method + '/*/')

    for scene in scenes:
        files = glob.glob(scene + '/*.ply')
        for file in files:
            save_name = file[:-4] + '.obj'
            v, f, n = pcu.load_mesh_vfn(file)
            pcu.save_mesh_vfn(save_name, v, f, n)
            os.remove(file)