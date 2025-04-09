# glue-etl-project

Deploy etl job

Install & Configure AWS CLI:
aws configure

and enter

AWS Access Key ID

AWS Secret Access Key

Region (us-east-1 or as needed)

Upload Code to S3:

aws s3 cp glue-job.py s3://your-script-bucket/scripts/glue-job.py



to create job:

aws glue create-job --name my-etl-job --role AWSGlueServiceRoleDefault --command "{\"Name\":\"glueetl\",\"ScriptLocation\":\"s3://script-glue-etl/glue-job.py\",\"PythonVersion\":\"3\"}" --glue-version "3.0"

Run the Glue Job (Optional):
aws glue start-job-run --job-name my-etl-job

Now update your Glue job to use this new role:

aws glue update-job --job-name my-etl-job --job-update '{"Role": "MyGlueETLRole"}'

Create a file called job-update.json in your folder (e.g., C:\Users\Keert\Downloads\ETL\glue-etl-project\job-update.json):

{
  "Role": "arn:aws:iam::588738603076:role/MyGlueETLRole",
  "Command": {
    "Name": "glueetl",
    "ScriptLocation": "s3://script-glue-etl/glue-job.py",
    "PythonVersion": "3"
  },
  "GlueVersion": "3.0"
}

run:

aws glue update-job --job-name my-etl-job --job-update file://job-update.json



Then re-run the job:
aws glue start-job-run --job-name my-etl-job


Push Your Code to GitHub:
git add .
git commit -m "Initial Glue ETL Job"
git push origin main
