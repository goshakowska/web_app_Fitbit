import database_models.models as models

def get_all_clients():
    clients = models.Client.objects.all()
    clients = [[client.client_id, client.name, client.surname] for client in clients]
    return clients
