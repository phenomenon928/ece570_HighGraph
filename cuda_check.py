import torch
print("cuda avail", torch.cuda.is_available())
print("cuda version", torch.version.cuda)

# nvcc: NVIDIA (R) Cuda compiler driver
# Copyright (c) 2005-2023 NVIDIA Corporation
# Built on Tue_Aug_15_22:02:13_PDT_2023
# Cuda compilation tools, release 12.2, V12.2.140
# Build cuda_12.2.r12.2/compiler.33191640_0