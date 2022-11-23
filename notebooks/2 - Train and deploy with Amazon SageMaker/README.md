## Train and Deploy a Custom YOLOv5 Model with Amazon SageMaker Training Jobs and Endpoints

In the [Label your dataset with Amazon SageMaker GroundTruth notebooks](), you prepared your custom dataset to train a YOLOv5 model (If you don't have a labeled dataset in COCO format please go to that section an create your dataset).

In this section you will be using Amazon SageMaker features to train and test your Custom YOLOv5 model without having to worry about the infrastrucuture management.
You will first locate a labelled custom dataset to be used and pass it through to a SM Training Job. Once the training has finished, you will deploy the model to an endpoint on SageMaker and test it out.
