from airflow.hooks.base import BaseHook

SLACK_WEBHOOK_CONNECTION_ID = 'slack'
SLACK_WEBHOOK_TOKEN = BaseHook.get_connection(
    SLACK_WEBHOOK_CONNECTION_ID).password
