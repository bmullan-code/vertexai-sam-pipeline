# VertexAI Segment Anything Pipeline
Run a segment anything model job as a vertexai pipeline with scheduling

## Requirements
- python develoment environment

- gcloud cli [installation](https://cloud.google.com/sdk/docs/install)


## Setup
```console
python -m venv .venv
. .venv/bin/activate
pip install -r requirements.txt
```

## Build the custom container

- Create or retrieve Artifact Registry information
    - Go to [Artifact Registry](https://console.cloud.google.com/artifacts)
    - Select an existing Docker Repository or Create One and select it
    - Select "Setup Instructions" for the command to configure your local docker command eg. 
```console
    gcloud auth configure-docker us-central1-docker.pkg.dev
```    
- 
    - Copy the path to your repository (use the copy tool next to repository name) eg.
```console
    us-central1-docker.pkg.dev/(project)/vertexai
```

- Build the docker image
```console
    cd docker
```
```console
    docker build -t <repo-path-from-previous-step>/pytorch-sam:latest .
```
```console
    docker push <repo-path-from-previous-step>/pytorch-sam:latest
```
    


## Create the pipeline

Edit the environment variables values in template.txt 
run
```console
mv template.txt .env
```
Create the pipeline
```console
python sam-kfp-pipeline.py
```
This will create the file 'sam-kfp-pipeline.yaml' in the current directory

## Run the pipeline

You can run the pipeline job in a couple of ways. 

- Python API
    - Uncomment the line 'job.submit()' in sam-kfp-pipeline.py and re-run it. 

- Using Google Cloud Console
    - Using the file 'sam-kfp-pipeline.yaml'.
    - Goto [VertexAI Pipelines](https://console.cloud.google.com/vertex-ai/pipelines)
    - Select Create Run
    - Select Upload File, Select File, Click Submit

- Scheduled Runs
    - Using the file 'sam-kfp-pipeline.yaml'.
    - Goto [VertexAI Pipelines](https://console.cloud.google.com/vertex-ai/pipelines)
    - Select Create Run
    - Select Upload File, Select File, Click Submit
    - Select Recurring and complete Schedule Information
    - <img src="https://raw.githubusercontent.com/bmullan-code/vertexai-sam-pipeline/refs/heads/main/images/pipeline-schedule.png" alt="schedule" height="300"/>




- See this [link](https://cloud.google.com/vertex-ai/docs/pipelines/run-pipeline) for more options. 


