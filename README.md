# FoundationPose_IS

Follow these steps to run FoundationPose on the IndustryShapes dataset.

### Apply some minor modifications to the FoundationPose repo:

  ```
  cd FoundationPose
  git apply ../diff.patch
  ```

## Data preparation & Docker container setup

Follow the Data Preparation steps in the FoundationPose directory.


Download the IndustryShapes dataset from ___ and place it in the `FoundationPose/BOP` dir

### For the model-based setup:

Run:

  ```
  export BOP_DIR = /path/to/FoundationPose/BOP
  ```

And then:

  ```
  python run_linemod.py --dataset_dir /path/to/FoundationPose/BOP/IndustryShapes --use_reconstructed_mesh 0
  ```

### For the model-free setup:

You can run [BundleSDF](https://github.com/NVlabs/BundleSDF), as the authors of FoundationPose suggest, on the IndustryShapes onboarding sequences (up)
to get the object pose relative to the camera for each frame. These can then be used by FoundationPose as reference views to reconstruct the mesh. 

Run:

  ```
  python bundlesdf/run_nerf.py --ref_view_dir /path/to/ref_views --dataset lmo
  ```

And then:

  ```
  python run_linemod.py --dataset_dir /path/to/FoundationPose/BOP/IndustryShapes --use_reconstructed_mesh 1 --ref_view_dir /path/to/ref_views
  ```


## Evaluation

FoundationPose creates a yml file in the /debug dir. You can run 

  ```
  cd ..
  python eval_bop.py
  ```

to get a BOP format prediction csv. You can then use bop_toolkit for the evaluation. 
