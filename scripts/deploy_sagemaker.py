import sagemaker
from sagemaker.sklearn.model import SKLearnModel

role = "arn:aws:iam::232932848445:role/service-role/AmazonSageMaker-ExecutionRole-20260504T141657"

model = SKLearnModel(
    model_data="s3://mlops-project-churn-customer-bucket-prod/model/model.tar.gz",
    role=role,
    entry_point="inference.py",
    framework_version="1.2-1",
    py_version="py3"
)

predictor = model.deploy(
    instance_type="ml.t2.medium",
    initial_instance_count=1
)

print("✅ Endpoint deployed")
print(predictor.endpoint_name)