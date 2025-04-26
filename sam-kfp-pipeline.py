import kfp
from kfp import compiler, dsl
from kfp.dsl import component
from google.cloud import aiplatform
from google_cloud_pipeline_components.v1.custom_job import utils
from dotenv import load_dotenv
import os

load_dotenv()  # take environment variables

project_id =            os.getenv("PROJECT_ID")
location =              os.getenv("LOCATION")
bucket_name =           os.getenv("BUCKET_NAME")
BASE_IMAGE_PATH=        os.getenv("BASE_IMAGE_PATH")
BUCKET_URI =            os.getenv("BUCKET_URI")
PIPELINE_ROOT =         os.getenv("PIPELINE_ROOT")
PIPELINE_PACKAGE_PATH = os.getenv("PIPELINE_PACKAGE_PATH")
DISPLAY_NAME=           os.getenv("DISPLAY_NAME")
IMAGE_PATH=             os.getenv("IMAGE_PATH")

aiplatform.init(project=project_id, location=location, staging_bucket=BUCKET_URI)     

@component(
    base_image=BASE_IMAGE_PATH,
    packages_to_install=["scikit-learn==1.5.1","opencv-python"],
)
def custom_sam_job(image_path: str):

    import torch
    import torchvision
    import cv2
    print("PyTorch version:", torch.__version__)
    print("Torchvision version:", torchvision.__version__)
    print("CUDA is available:", torch.cuda.is_available())
    # from segment_anything import sam_model_registry
    print("image_path:",image_path)
    from segment_anything import sam_model_registry, SamAutomaticMaskGenerator, SamPredictor

    print("loading checkpoint...")
    sam = sam_model_registry["default"](checkpoint="/checkpoint/sam_vit_h_4b8939.pth")
    print("loaded")
    _ = sam.to(device="cuda")
    print("loaded to cuda")

    mask_generator = SamAutomaticMaskGenerator(sam)
    image = cv2.imread('/images/dog.jpg')
    masks = mask_generator.generate(image)

    print(len(masks))
    print(masks[0].keys())
    print(masks[0])

custom_sam_job_op = utils.create_custom_training_job_op_from_component(
    custom_sam_job, 
    replica_count=1,
    machine_type = 'n1-standard-4',
    accelerator_type='NVIDIA_TESLA_T4',
    accelerator_count='1'
)

# Define the workflow of the pipeline.
@kfp.dsl.pipeline(
    name="custom-sam-pipeline",
    pipeline_root=PIPELINE_ROOT)
def pipeline(project_id: str, image_path: str):

    custom_sam_job_task = custom_sam_job_op(
        project=project_id,
        image_path=image_path
    )

compiler.Compiler().compile(
    pipeline_func=pipeline, package_path=PIPELINE_PACKAGE_PATH
)

if __name__ == "__main__":

    DISPLAY_NAME = "custom-sam-pipeline"

    job = aiplatform.PipelineJob(
        display_name=DISPLAY_NAME,
        template_path=PIPELINE_PACKAGE_PATH,
        pipeline_root=PIPELINE_ROOT,
        parameter_values={
            'project_id': project_id,
            'image_path': IMAGE_PATH
        }
    )

    # job.submit()
