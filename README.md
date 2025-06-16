# EV HW3: PhysGaussian

R13922191  
Lu, Ting-Yang  
young91319@cmlab.csie.ntu.edu.tw

## Visualization
|jelly|plasticine|sand|metal|
|-|-|-|-|
|[jelly](https://youtube.com/shorts/k9Oj12-BwoA?feature=share)|[plasticine](https://youtube.com/shorts/ZeHWRDi0fQQ?feature=share)|[sand](https://youtube.com/shorts/5JX7gF-tQcs?feature=share)|[metal](https://youtube.com/shorts/_ZBQdMK21P4?feature=share)|

## Ablation:
#### baseline:  
    softening: 0.1  
    grid_v_damping_scale: 0.9999 
    n_grid: 50 
    substeps: 1e-4


| Test ID | Parameter             | Value    | Expected                | Avg. PSNR (dB) |Video link|
|---------|------------------------|----------|------------------------------------|-|----------------|
| S1      | softening              | 0.01     | More aggressive collapse           | 41.96         |[softening 0.01](https://youtube.com/shorts/YwEANOVN21s?feature=share)
| S2      | softening              | 1.0      | Softer force, less concentration   | 41.90           |[softening 1.0](https://youtube.com/shorts/4Z7smSWs2Jc?feature=share)
| D1      | grid_v_damping_scale  | 0.9      | Stronger damping                   | 22.23           |[damping 0.9](https://youtube.com/shorts/q4vFIw3LMPI?feature=share)
| D2      | grid_v_damping_scale  | 1.0      | No damping, more oscillation       | 20.29           |[damping 1.0](https://youtube.com/shorts/9d-4vgv42tE?feature=share)
| T1     | substeps               | 1e-3| -|-
| T2      | substeps               | 1e-5     | Slow but stable                    | 31.6           |[subset_dt 1e-5](https://youtube.com/shorts/fQ-CQ8Q3iPI?feature=share)
| G1      | n_grid                 | 45       | Coarse resolution                  | 23.63           |[n_grid 45](https://youtube.com/shorts/x-jg5yf6vU0?feature=share)
| G2      | n_grid                 | 55      | High resolution                    | 22.21           |[n_grid 55](https://youtube.com/shorts/YIiB3ZcUgU0?feature=share)


### Observation:

Lowering grid_v_damping_scale reduced oscillations, while increasing it caused more visible shaking. For other parameters (softening, substeps, n_grid), visual differences were minimal in the output videos. Notably, increasing substeps too much caused the simulation to crash, likely due to numerical instability.

[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/SdXSjEmH)
# EV-HW3: PhysGaussian

This homework is based on the recent CVPR 2024 paper [PhysGaussian](https://github.com/XPandora/PhysGaussian/tree/main), which introduces a novel framework that integrates physical constraints into 3D Gaussian representations for modeling generative dynamics.

You are **not required** to implement training from scratch. Instead, your task is to set up the environment as specified in the official repository and run the simulation scripts to observe and analyze the results.


## Getting the Code from the Official PhysGaussian GitHub Repository
Download the official codebase using the following command:
```
git clone https://github.com/XPandora/PhysGaussian.git
```


## Environment Setup
Navigate to the "PhysGaussian" directory and follow the instructions under the "Python Environment" section in the official README to set up the environment.


## Running the Simulation
Follow the "Quick Start" section and execute the simulation scripts as instructed. Make sure to verify your outputs and understand the role of physics constraints in the generated dynamics.


## Homework Instructions
Please complete Part 1–2 as described in the [Google Slides](https://docs.google.com/presentation/d/13JcQC12pI8Wb9ZuaVV400HVZr9eUeZvf7gB7Le8FRV4/edit?usp=sharing).


# Reference
```bibtex
@inproceedings{xie2024physgaussian,
    title     = {Physgaussian: Physics-integrated 3d gaussians for generative dynamics},
    author    = {Xie, Tianyi and Zong, Zeshun and Qiu, Yuxing and Li, Xuan and Feng, Yutao and Yang, Yin and Jiang, Chenfanfu},
    booktitle = {Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition},
    year      = {2024}
}
```
