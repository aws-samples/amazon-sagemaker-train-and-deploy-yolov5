## Label and prepare your dataset with Amazon SageMaker Ground Truth

In this section you will focus on preparing your dataset needed to train a custom YOLOv5 model.

There are two available notebooks you can use to create your dataset:

**A. Label and prepare your own dataset** : In this notebook, you will use Amazon SageMaker Ground Truth to create a labelling job and label your training images. After you have finished labelling your images you will download them to the local environment, split them into training and validation datasets, convert the label format to COCO and upload to S3 the resulting datasets, needed to train your custom model. 

**B. Label and prepare your own dataset with SM Processing** : In this notebook, you will use Amazon SageMaker Ground Truth to create a labelling job and label your training images. After you have finished labelling your images you will use an Amazon SageMaker Processing Job to split them into training and validation datasets, convert the label format to COCO and upload to S3 the resulting datasets, needed to train your custom model. 
