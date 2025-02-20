import json
import os
from google.cloud import bigquery, storage
from google.oauth2 import service_account


DATA_FOLDER = "data"
BUSINESS_DOMAIN = "greenery"
location = "asia-southeast1"

# Prepare and Load Credentials to Connect to GCP Services
keyfile_gcs = "deb-200024-load-data-to-gcs.json"
service_account_info_gcs = json.load(open(keyfile_gcs))
credentials_gcs = service_account.Credentials.from_service_account_info(
    service_account_info_gcs
)

keyfile_bigquery = "deb-200024-load-data-to-gcs-then-bq.json"
service_account_info_bigquery = json.load(open(keyfile_bigquery))
credentials_bigquery = service_account.Credentials.from_service_account_info(
    service_account_info_bigquery
)

project_id = "deb-200024"

# Load data from Local to GCS
bucket_name = "deb2-bootcamp-200024"
storage_client = storage.Client(
    project = project_id,
    credentials = credentials_gcs,
)
bucket = storage_client.bucket(bucket_name)

# -----------------------------------------------------------
# addresses

data = "addresses"
file_path = f"{DATA_FOLDER}/{data}.csv"
destination_blob_name = f"{BUSINESS_DOMAIN}/{data}/{data}.csv"

# YOUR CODE HERE TO LOAD DATA TO GCS
blob = bucket.blob(destination_blob_name)
blob.upload_from_filename(file_path)

# Load data from GCS to BigQuery
bigquery_client = bigquery.Client(
    project=project_id,
    credentials=credentials_bigquery,
    location=location,
)
table_id = f"{project_id}.my_deb_bootcamp.{data}"
job_config = bigquery.LoadJobConfig(
    skip_leading_rows=1,
    write_disposition=bigquery.WriteDisposition.WRITE_TRUNCATE,
    source_format=bigquery.SourceFormat.CSV,
    autodetect=True,
)
job = bigquery_client.load_table_from_uri(
    f"gs://{bucket_name}/{destination_blob_name}",
    table_id,
    job_config=job_config,
    location=location,
)
job.result()

table = bigquery_client.get_table(table_id)
print(f"Loaded {table.num_rows} rows and {len(table.schema)} columns to {table_id}")

# -----------------------------------------------------------
# products

data = "products"
file_path = f"{DATA_FOLDER}/{data}.csv"
destination_blob_name = f"{BUSINESS_DOMAIN}/{data}/{data}.csv"

# LOAD DATA TO GCS
blob = bucket.blob(destination_blob_name)
blob.upload_from_filename(file_path)

# Load data from GCS to BigQuery
bigquery_client = bigquery.Client(
    project=project_id,
    credentials=credentials_bigquery,
    location=location,
)
table_id = f"{project_id}.my_deb_bootcamp.{data}"
job_config = bigquery.LoadJobConfig(
    skip_leading_rows=1,
    write_disposition=bigquery.WriteDisposition.WRITE_TRUNCATE,
    source_format=bigquery.SourceFormat.CSV,
    autodetect=True,
)
job = bigquery_client.load_table_from_uri(
    f"gs://{bucket_name}/{destination_blob_name}",
    table_id,
    job_config=job_config,
    location=location,
)
job.result()

table = bigquery_client.get_table(table_id)
print(f"Loaded {table.num_rows} rows and {len(table.schema)} columns to {table_id}")

# -----------------------------------------------------------
# order_items
data = "order_items"
file_path = f"{DATA_FOLDER}/{data}.csv"
destination_blob_name = f"{BUSINESS_DOMAIN}/{data}/{data}.csv"

# load data to gcs
blob = bucket.blob(destination_blob_name)
blob.upload_from_filename(file_path)

# load data from gcs to bigquery
bigquery_client = bigquery.Client(
    project = project_id,
    credentials = credentials_bigquery,
    location = location
)

table_id = f"{project_id}.my_deb_bootcamp.{data}"
job_config = bigquery.LoadJobConfig(
    skip_leading_rows = 1,
    write_disposition = bigquery.WriteDisposition.WRITE_TRUNCATE,
    source_format = bigquery.SourceFormat.CSV,
    autodetect = True
)
job = bigquery_client.load_table_from_uri(
    f"gs://{bucket_name}/{destination_blob_name}",
    table_id,
    job_config = job_config,
    location = location
)
job.result()

table = bigquery_client.get_table(table_id)
print(f"Loaded {table.num_rows} rows and {len(table.schema)} columns to {table_id}")

# -----------------------------------------------------------
# promos
data = "promos"
file_path = f"{DATA_FOLDER}/{data}.csv"
destination_blob_name = f"{BUSINESS_DOMAIN}/{data}/{data}.csv"

# load data to gcs
blob = bucket.blob(destination_blob_name)
blob.upload_from_filename(file_path)

# load data from gcs to bigquery
bigquery_client = bigquery.Client(
    project = project_id,
    credentials = credentials_bigquery,
    location = location
)
table_id = f"{project_id}.my_deb_bootcamp.{data}"
job_config = bigquery.LoadJobConfig(
    skip_leading_rows = 1,
    write_disposition = bigquery.WriteDisposition.WRITE_TRUNCATE,
    source_format = bigquery.SourceFormat.CSV,
    autodetect = True
)
job = bigquery_client.load_table_from_uri(
    f"gs://{bucket_name}/{destination_blob_name}",
    table_id,
    job_config = job_config,
    location = location
)
job.result()
table = bigquery_client.get_table(table_id)

print(f"loaded {table.num_rows} rows and {len(table.schema)} columns to {table_id}")

# -----------------------------------------------------------
# events

data = "events"
file_path = f"{DATA_FOLDER}/{data}.csv"
dt = "2021-02-10"
partition = dt.replace("-","")
destination_blob_name = f"{BUSINESS_DOMAIN}/{data}/{dt}/{data}.csv"

# load data to gcs
blob = bucket.blob(destination_blob_name)
blob.upload_from_filename(file_path)

# load data from gcs to bigquery
bigquery_client = bigquery.Client(
    project = project_id,
    credentials = credentials_bigquery,
    location = location
)
table_id = f"{project_id}.my_deb_bootcamp.{data}${partition}"
job_config = bigquery.LoadJobConfig(
    skip_leading_rows = 1,
    write_disposition = bigquery.WriteDisposition.WRITE_TRUNCATE,
    source_format = bigquery.SourceFormat.CSV,
    autodetect = True,
    time_partitioning = bigquery.TimePartitioning(
        type_ = bigquery.TimePartitioningType.DAY,
        field = "created_at"
    )
)
job = bigquery_client.load_table_from_uri(
    f"gs://{bucket_name}/{destination_blob_name}",
    table_id,
    job_config = job_config,
    location = location
)
job.result()
table = bigquery_client.get_table(table_id)

print(f"loaded {table.num_rows} rows and {len(table.schema)} columns to {table_id}")

# -----------------------------------------------------------
# users

data = "users"
file_path = f"{DATA_FOLDER}/{data}.csv"
dt = "2020-10-23"
partition = dt.replace("-","")
destination_blob_name = f"{BUSINESS_DOMAIN}/{data}/{dt}/{data}.csv"

# load data to gcs
blob = bucket.blob(destination_blob_name)
blob.upload_from_filename(file_path)

# load data from gcs to bigquery
bigquery_client = bigquery.Client(
    project = project_id,
    credentials = credentials_bigquery,
    location = location
)
table_id = f"{project_id}.my_deb_bootcamp.{data}${partition}"
job_config = bigquery.LoadJobConfig(
    skip_leading_rows = 1,
    write_disposition = bigquery.WriteDisposition.WRITE_TRUNCATE,
    source_format = bigquery.SourceFormat.CSV,
    autodetect = True,
    time_partitioning = bigquery.TimePartitioning(
        type_ = bigquery.TimePartitioningType.DAY,
        field = "created_at"
    )
)
job = bigquery_client.load_table_from_uri(
    f"gs://{bucket_name}/{destination_blob_name}",
    table_id,
    job_config = job_config,
    location = location
)
job.result()
table = bigquery_client.get_table(table_id)

print(f"loaded {table.num_rows} rows and {len(table.schema)} columns to {table_id}")

# -----------------------------------------------------------
# orders

data = "orders"
file_path = f"{DATA_FOLDER}/{data}.csv"
dt = "2021-02-10"
partition = dt.replace("-","")
destination_blob_name = f"{BUSINESS_DOMAIN}/{data}/{dt}/{data}.csv"

# load data to gcs
blob = bucket.blob(destination_blob_name)
blob.upload_from_filename(file_path)

# load data from gcs to bigquery
bigquery_client = bigquery.Client(
    project = project_id,
    credentials = credentials_bigquery,
    location = location
)
table_id = f"{project_id}.my_deb_bootcamp.{data}${partition}"
job_config = bigquery.LoadJobConfig(
    skip_leading_rows = 1,
    write_disposition = bigquery.WriteDisposition.WRITE_TRUNCATE,
    source_format = bigquery.SourceFormat.CSV,
    autodetect = True,
    time_partitioning = bigquery.TimePartitioning(
        type_ = bigquery.TimePartitioningType.DAY,
        field = "created_at"
    )
)
job = bigquery_client.load_table_from_uri(
    f"gs://{bucket_name}/{destination_blob_name}",
    table_id,
    job_config = job_config,
    location = location
)
job.result()
table = bigquery_client.get_table(table_id)

print(f"loaded {table.num_rows} rows and {len(table.schema)} columns to {table_id}")
