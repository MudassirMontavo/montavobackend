from azure.servicebus import ServiceBusService


service_namespace = 'dev-montavo'
account_key = '3me4sCOHDWBK8PkjkznLnFkksQ0H/aWL3FU/JlzF5d0='
sbs = ServiceBusService(service_namespace, account_key, 'owner')
[q.name for q in sbs.list_queues()]
q = sbs.list_queues()[0]
m = sbs.receive_queue_message(q.name)
m.body
m.custom_properties