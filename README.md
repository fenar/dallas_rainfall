# dallas_rainfall

**Use Case**: Automates live Dallas Rainfall data collection and flows it into Google BigQuery for interactive real-time analysis.

**Technical Concept**: Schedules a CronJob over AppEngine (GCP Docker Container RunTime) to append OpenData API pulled data into BigQuery.

**Setup Prerequisites**:
A. Enable BigQuery API, Stackdriver API, Google Cloud Deployment Manager V2 API, Google Compute Engine API

**Deploy Instructions**:
1. Git Clone this repo <br>
2. To deploy App Engine app, run: gcloud app deploy app.yaml
3. To deploy App Engine CRON, run: gcloud app deploy cron.yaml

**NOTES**:<br>
i. If you download the historical data as .csv and import in to BigQuery the schema will not match with the data pulled over soda api as csv uses clear field names but api uses shortned abbrevations. Instead you can delete the table and re-run cron job to pull all data with correct field names. <br>
ii. There is a ready to use DataLab Notebook Sample, in order to use follow the steps @ [https://cloud.google.com/datalab/docs/quickstart] to setup DataLabs 1st and then import the notebook.<br>
NOTE: If you loose connection to datalab vm you can reconnect with: <br>
$ datalab connect --zone us-central1-a --port 8081 project-slave-datalab
