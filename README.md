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



so I did:


so I have pushed in github as well
so I created repo in githib to store and version
and written code in vscode
and using Aws cli
i h=confighured Aws configure by giving cred
clone repo 
written code
save the cript in s3
upload the glue job

added I am role 
updated it
run it 
fixed it
re run it
then deploy it in githib


Created GitHub Repo – version control like a boss 👩‍💻

Written Code in VS Code – clean and local dev setup 🧹

Configured AWS CLI – securely connected with your AWS account 🔐

Cloned the Repo – Git best practices 💯

Saved Script to S3 – storage game strong 📦

Created Glue Job from CLI – infra-as-code vibes 🛠️

Created & Updated IAM Role – got your permissions right 🔐

Ran & Debugged the Glue Job – didn’t give up till it ran 🧠

Deployed Final Version to GitHub – all clean and tracked 📁

