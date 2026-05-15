import boto3

s3 = boto3.client("s3")

s3.upload_file(
    "model.tar.gz",
    "mlops-project-churn-customer-bucket-prod",
    "model/model.tar.gz"
)

print("✅ Uploaded tar.gz to S3")