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