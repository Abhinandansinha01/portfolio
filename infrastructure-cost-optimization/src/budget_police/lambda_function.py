import json
import boto3
import logging
from datetime import datetime, time

# Setup Logging
logger = logging.getLogger()
logger.setLevel(logging.INFO)

# Unique Feature: "Budget Police" - Intelligent Scaling
# Instead of just stopping all instances, it checks for specific "SafeToStop" tags
# and sends a mock "Slack Notification" of savings.

def lambda_handler(event, context):
    ec2 = boto3.client('ec2')
    
    # Define Off-Hours (e.g., 7 PM to 7 AM)
    current_time = datetime.now().time()
    off_hours_start = time(19, 0)
    off_hours_end = time(7, 0)
    
    is_off_hours = current_time >= off_hours_start or current_time <= off_hours_end
    
    if is_off_hours:
        logger.info("🕵️ Budget Police Active: Patroling for cost leakage...")
        
        # Filter for running instances that are NOT critical
        filters = [
            {'Name': 'instance-state-name', 'Values': ['running']},
            {'Name': 'tag:Environment', 'Values': ['Dev', 'Staging', 'Test']}
        ]
        
        instances = ec2.describe_instances(Filters=filters)
        to_stop = []
        saved_cost = 0.0
        
        for reservation in instances['Reservations']:
            for instance in reservation['Instances']:
                logger.info(f"Checking Instance: {instance['InstanceId']}")
                # Unique Check: Don't stop if "Overtime" tag is present
                tags = {t['Key']: t['Value'] for t in instance.get('Tags', [])}
                
                if tags.get('Overtime') == 'True':
                    logger.info(f"⚠️ Skipping {instance['InstanceId']} - Dev working overtime!")
                    continue
                    
                to_stop.append(instance['InstanceId'])
                # Mock cost calculation ($0.10/hr)
                saved_cost += 0.10
        
        if to_stop:
            logger.info(f"🛑 Stopping {len(to_stop)} instances: {to_stop}")
            # Uncomment in real AWS environment:
            # ec2.stop_instances(InstanceIds=to_stop)
            
            # Simulated Slack Notification
            message = {
                "channel": "#devops-alerts",
                "username": "Budget Police Bot",
                "text": f"💰 **Savings Alert**: Stopped {len(to_stop)} dev instances. Estimated nightly savings: ${saved_cost * 12:.2f}",
                "icon_emoji": ":moneybag:"
            }
            print(f"SLACK_WEBHOOK_MOCK: Sending {json.dumps(message)}")
            
            return {
                'statusCode': 200,
                'body': json.dumps('Budget Police patrol complete. Savings secured.')
            }
        else:
            return {
                'statusCode': 200,
                'body': json.dumps('No instances needed stopping.')
            }
            
    else:
        logger.info("☀️ Day shift. Budget Police standing down.")
        return {'statusCode': 200, 'body': 'Business hours active.'}
