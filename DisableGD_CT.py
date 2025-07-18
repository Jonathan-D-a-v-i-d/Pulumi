import boto3

## Accepts a previously initialized boto3 session and executes the function below

def disable_guardduty(session, guardduty_id):
    """Disables a specific GuardDuty detector."""
    try:
        guardduty_client = session.client('guardduty')

        print("Disabling GuardDuty Detector...")
        if guardduty_id:
            guardduty_client.update_detector(DetectorId=guardduty_id, Enable=False)
            print(f"Disabled GuardDuty Detector: {guardduty_id}")
        else:
            print("No valid GuardDuty Detector ID provided.")

    except Exception as e:
        print(f"ERROR: Failed to disable GuardDuty: {e}")


def stop_cloudtrail_logging(session, cloudtrail_name):
    """Stops logging for a specific CloudTrail instance."""
    try:
        cloudtrail_client = session.client('cloudtrail')

        print("Stopping CloudTrail Logging...")
        if cloudtrail_name:
            cloudtrail_client.stop_logging(Name=cloudtrail_name)
            print(f"Stopped logging for CloudTrail: {cloudtrail_name}")
        else:
            print("No valid CloudTrail name provided.")

    except Exception as e:
        print(f"ERROR: Failed to stop CloudTrail logging: {e}")


def delete_guardduty(session, guardduty_id):
    """Deletes a specific GuardDuty detector."""
    try:
        guardduty_client = session.client('guardduty')

        print("Deleting GuardDuty Detector...")
        if guardduty_id:
            guardduty_client.delete_detector(DetectorId=guardduty_id)
            print(f"Deleted GuardDuty Detector: {guardduty_id}")
        else:
            print("No valid GuardDuty Detector ID provided.")

    except Exception as e:
        print(f"ERROR: Failed to delete GuardDuty: {e}")


def delete_cloudtrail(session, cloudtrail_name):
    """Deletes a specific CloudTrail instance."""
    try:
        cloudtrail_client = session.client('cloudtrail')

        print("Deleting CloudTrail...")
        if cloudtrail_name:
            cloudtrail_client.delete_trail(Name=cloudtrail_name)
            print(f"Deleted CloudTrail: {cloudtrail_name}")
        else:
            print("No valid CloudTrail name provided.")

    except Exception as e:
        print(f"ERROR: Failed to delete CloudTrail: {e}")

