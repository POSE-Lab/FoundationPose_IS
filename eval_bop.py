import yaml
import numpy as np
from typing import Dict

def arr2str(x: np.ndarray):
    return ' '.join(map(str, x.reshape(-1).tolist()))

x: Dict[str, Dict[str, Dict[str, list]]] = yaml.safe_load(open("debug/industryshapes.yml.yml"))

with open("fp_industryshapes-test.csv", "w") as fo:
    fo.write("scene_id,im_id,obj_id,score,R,t,time\n")
    for video_id, frames in x.items():
        for frame_id, objs in frames.items():
            for obj_id, pose_list in objs.items():
                for inst_idx, mat in enumerate(pose_list):
                    pose_np = np.array(mat)              
                    R       = pose_np[:3, :3]            
                    t       = pose_np[:3,  3] * 1000.0
                    fo.write(
                        f"{int(video_id)},{int(frame_id)},{int(obj_id)},1.0,"
                        f"{arr2str(R)},{arr2str(t)},1.0\n"
                    )
