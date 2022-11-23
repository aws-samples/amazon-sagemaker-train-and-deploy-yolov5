import os
import numpy
import json
import shutil
import boto3
from sklearn.model_selection import train_test_split

envs = dict(os.environ)
groundtruth_job_name = envs.get('gt_job_name')
region = envs.get('region')
print("Region: ",region)

sm_client = boto3.client('sagemaker', region_name=region)
s3_resource = boto3.resource('s3', region_name=region)

response = sm_client.describe_labeling_job(
    LabelingJobName=groundtruth_job_name
)

labelingJobStatus = response["LabelingJobStatus"]
manifestUri = response["LabelingJobOutput"]["OutputDatasetS3Uri"]
labelsListUri = response["LabelCategoryConfigS3Uri"]

print("Manifest Uri: ", manifestUri)
print("Labels Uri: ", labelsListUri)

def split_s3_path(s3_path):
    path_parts=s3_path.replace("s3://","").split("/")
    bucket=path_parts.pop(0)
    key="/".join(path_parts)
    return bucket, key

def get_labels_list(labels_uri):
    labels = []
    bucket, key = split_s3_path(labels_uri)
    s3_resource.meta.client.download_file(bucket, key, 'labels.json')
    with open('labels.json') as f:
        data = json.load(f)
    for label in data["labels"]:
        labels.append(label["label"])
    return labels

labels = get_labels_list(labelsListUri)
print("Labels: ",labels)

def get_manifest_file(manifest_uri):
    bucket, key = split_s3_path(manifest_uri)
    s3_resource.meta.client.download_file(bucket, key, 'output.manifest')
    return "output.manifest"

manifest = get_manifest_file(manifestUri)

with open(manifest) as file:
    lines = file.readlines()
    data = numpy.array(lines)
    train_data, validation_data = train_test_split(data, test_size=0.2)
    
print("The manifest contains {} annotations.".format(len(data)))
print("{} will be used for training.".format(len(train_data)))
print("{} will be used for validation.".format(len(validation_data)))

os.makedirs("/opt/ml/processing/output/train/training_data")
os.makedirs("/opt/ml/processing/output/train/training_data/images")
os.makedirs("/opt/ml/processing/output/train/training_data/labels")
os.makedirs("/opt/ml/processing/output/train/training_data/images/train")
os.makedirs("/opt/ml/processing/output/train/training_data/labels/train")
os.makedirs("/opt/ml/processing/output/train/training_data/images/validation")
os.makedirs("/opt/ml/processing/output/train/training_data/labels/validation")


def ground_truth_to_yolo(dataset, dataset_category):
    print("Downloading images and creating labels for the {} dataset".format(dataset_category))
    for line in dataset:
        line = json.loads(line)     
        # Variables
        object_s3_uri = line["source-ref"]
        bucket, key = split_s3_path(object_s3_uri)
        image_filename = object_s3_uri.split("/")[-1]
        txt_filename = '.'.join(image_filename.split(".")[:-1]) + ".txt"
        txt_path = "/opt/ml/processing/output/train/training_data/labels/{}/{}".format(dataset_category, txt_filename)
        
        # Download image
        s3_resource.meta.client.download_file(bucket, key, "/opt/ml/processing/output/train/training_data/images/{}/{}".format(dataset_category,image_filename))
        
        # Create txt with annotations
        with open(txt_path, 'w') as target:
            for annotation in line[groundtruth_job_name]["annotations"]:
                class_id = annotation["class_id"]
                center_x = (annotation["left"] + (annotation["width"]/2)) / line[groundtruth_job_name]["image_size"][0]["width"]
                center_y = (annotation["top"] + (annotation["height"]/2)) / line[groundtruth_job_name]["image_size"][0]["height"]
                w = annotation["width"] / line[groundtruth_job_name]["image_size"][0]["width"]
                h = annotation["height"] / line[groundtruth_job_name]["image_size"][0]["height"]
                data = "{} {} {} {} {}\n".format(class_id, center_x, center_y, w, h)
                target.write(data)
                
ground_truth_to_yolo(train_data, "train")
ground_truth_to_yolo(validation_data, "validation")                

print("Completed running the processing job")