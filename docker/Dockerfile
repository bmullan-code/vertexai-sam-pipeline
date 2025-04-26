# first create a docker repository [repo name] in Google Cloud Artifact Registry
# Build image with (eg)
# docker build -t us-central1-docker.pkg.dev/[project-id]/[repo name]/pytorch-sam .
# push to registry with 
# docker push us-central1-docker.pkg.dev/[project-id]/[repo name]/pytorch-sam .

from us-docker.pkg.dev/vertex-ai/training/pytorch-gpu.2-4.py310

RUN apt-get update && apt-get install -y \ 
    git

# download the sam checkpoint
RUN mkdir checkpoint && wget -P checkpoint https://dl.fbaipublicfiles.com/segment_anything/sam_vit_h_4b8939.pth

# clone and install segment-anything
RUN git clone https://github.com/facebookresearch/segment-anything && cd segment-anything  && pip install -e . 

# download a sample image used for testing
RUN mkdir images && wget -P images https://raw.githubusercontent.com/facebookresearch/segment-anything/main/notebooks/images/dog.jpg




