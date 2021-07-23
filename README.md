
## Project Punch

Punch is an User-item Embedding Based Recommendation Engine with the primary focus being proactively explore and
exploit the Most Relevant Content for user community.

#### Author: joe.xing.ai@gmail.com

### Design

The main idea behind this learning framework is to 

#### The Model Architecture:

#### The System Architecture:

### Setup

Main dependencies: conda 4.10.1, CUDA 10.1(2), cuDNN 7.6.4 (works with CUDA 10.2 as well), tensorflow-gpu 2.3.0,
torch 1.7.1

    - conda env create --file environment_ubuntu.yaml (environment_windows.yml)

For now we only support Ubuntu and Windows 10 OS.

    - conda activate punch

These initialization procedures will start to download Tensorflow standard datasets.

### Experimental Setup

### Deployment

Docker-based micro-service, TBD

