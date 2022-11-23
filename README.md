![banner-image](src/images/banner-1.png)
## Train and deploy custom YOLOv5 Object Detection models on Amazon SageMaker.

Object detection allows us to identify and locate objects in images or videos. You may want to detect your company brand in pictures, find objects in an shelf, count the number of people in a shop and many other detection use cases which need to be fullfilled everyday. **You only look once (YOLO)** is a state-of-the-art, real-time object detection system [presented in 2015](https://arxiv.org/abs/1506.02640). Nowadays YOLO has become a very popular algorithm to use when focusing on object detection.

**[Amazon SageMaker](https://aws.amazon.com/sagemaker/)** is a fully managed service to build, train, and deploy machine learning (ML) models for any use case with fully managed infrastructure, tools, and workflows.

In this workshop you will learn how to use different Amazon Sagemaker features to train and deploy custom [YOLOv5 models](https://github.com/ultralytics/yolov5).

Here are the different sections you can find:

  **0. Label and prepare your dataset:** Before we start creating a custom model, we need data, which has to be labelled and organized in the expected format. For this task we will make use of [Amazon SageMaker Ground Truth](https://aws.amazon.com/sagemaker/data-labeling/?sagemaker-data-wrangler-whats-new.sort-by=item.additionalFields.postDateTime&sagemaker-data-wrangler-whats-new.sort-order=desc), a feature that helps you build and manage your own data labeling workflows and data labeling workforce. Once you have labeled your dataset, you can choose to convert it to the expected format locally or using [Amazon SageMaker Processing Jobs](https://docs.aws.amazon.com/sagemaker/latest/dg/processing-job.html).
  
  **1. Train and test on Amazon SageMaker Studio:** Once we have prepared the dataset we can train the custom YOLOv5 model. In this section you will download your dataset to train and test the model locally on [Amazon SageMaker Studio](https://aws.amazon.com/sagemaker/studio/). 
  
  **2. Train and deploy with Amazon SageMaker:** Training and testing locally is good to quickly test out your model, but for production you will probably want to train your models with more powerfull instances and deploy your model to an endpoint (having to manage the least infrastructure as possible). In this section you will learn how to make use of [Amazon SageMaker Training Jobs](https://docs.aws.amazon.com/sagemaker/latest/dg/how-it-works-training.html) and [Amazon SageMaker Endpoints](https://docs.aws.amazon.com/sagemaker/latest/dg/deploy-model.html) to train and deploy your custom model.


---

This package depends on and may incorporate or retrieve a number of third-party
software packages (such as open source packages) at install-time or build-time
or run-time ("External Dependencies"). The External Dependencies are subject to
license terms that you must accept in order to use this package. If you do not
accept all of the applicable license terms, you should not use this package. We
recommend that you consult your company’s open source approval policy before
proceeding.

Provided below is a list of External Dependencies and the applicable license
identification as indicated by the documentation associated with the External
Dependencies as of Amazon's most recent review.

THIS INFORMATION IS PROVIDED FOR CONVENIENCE ONLY. AMAZON DOES NOT PROMISE THAT
THE LIST OR THE APPLICABLE TERMS AND CONDITIONS ARE COMPLETE, ACCURATE, OR
UP-TO-DATE, AND AMAZON WILL HAVE NO LIABILITY FOR ANY INACCURACIES. YOU SHOULD
CONSULT THE DOWNLOAD SITES FOR THE EXTERNAL DEPENDENCIES FOR THE MOST COMPLETE
AND UP-TO-DATE LICENSING INFORMATION.

YOUR USE OF THE EXTERNAL DEPENDENCIES IS AT YOUR SOLE RISK. IN NO EVENT WILL
AMAZON BE LIABLE FOR ANY DAMAGES, INCLUDING WITHOUT LIMITATION ANY DIRECT,
INDIRECT, CONSEQUENTIAL, SPECIAL, INCIDENTAL, OR PUNITIVE DAMAGES (INCLUDING
FOR ANY LOSS OF GOODWILL, BUSINESS INTERRUPTION, LOST PROFITS OR DATA, OR
COMPUTER FAILURE OR MALFUNCTION) ARISING FROM OR RELATING TO THE EXTERNAL
DEPENDENCIES, HOWEVER CAUSED AND REGARDLESS OF THE THEORY OF LIABILITY, EVEN
IF AMAZON HAS BEEN ADVISED OF THE POSSIBILITY OF SUCH DAMAGES. THESE LIMITATIONS
AND DISCLAIMERS APPLY EXCEPT TO THE EXTENT PROHIBITED BY APPLICABLE LAW.

{YOLOv5 (https://github.com/ultralytics/yolov5) - GNU General Public License v3.0 or later}

