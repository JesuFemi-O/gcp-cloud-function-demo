from cf_utils import load_to_biquery

def file_processor(event, context):
    """Triggered by a change to a Cloud Storage bucket.
    Args:
         event (dict): Event payload.
         context (google.cloud.functions.Context): Metadata for the event.
    """
    bucket_name = event["bucket"]
    file_name = event["name"]

    gcs_uri = f"gs://{bucket_name}/{file_name}"
    load_to_biquery(file_uri=gcs_uri, dataset_id="alt_school_commerce", table_id="customer_orders")