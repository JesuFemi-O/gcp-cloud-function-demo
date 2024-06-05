from google.cloud import bigquery

def load_to_biquery(file_uri, dataset_id,  table_id):
    bigquery_client = bigquery.Client()
    dataset_ref = bigquery_client.dataset(dataset_id)
    table_ref = dataset_ref.table(table_id)

    # => project_id.dataset_id.table_id

    job_config = bigquery.LoadJobConfig(
        autodetect=True,
        skip_leading_rows=1,
        source_format=bigquery.SourceFormat.CSV,
    )

    load_job = bigquery_client.load_table_from_uri(file_uri, table_ref, job_config=job_config)
    load_job.result()

    print(f"successfully wrote {file_uri} to {table_id}")