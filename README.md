# VertexAI Segment Anything Pipeline
Run a segment anything model job as a vertexai pipeline with scheduling

## Setup
```console
python -m venv .venv
. .venv/bin/activate
pip install -r requirements.txt
```

## Build the custom container


## Create the pipeline

edit the environment variables values in template.txt 
run
```console
mv template.txt .env
```
create the pipeline
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
    - ![schedule information](https://raw.githubusercontent.com/bmullan-code/vertexai-sam-pipeline/refs/heads/main/images/pipeline-schedule.png =x250)




- See this [link](https://cloud.google.com/vertex-ai/docs/pipelines/run-pipeline) for more options. 


