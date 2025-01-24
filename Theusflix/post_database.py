def main(req):
    request_data = req.get_json()
    cosmos_client = CosmosClient("<cosmos-endpoint>", {'masterKey': "<cosmos-key>"})
    database = cosmos_client.get_database_client("Theusflix")
    container = database.get_container_client("Movies")
    for movie in request_data["movies"]:
        container.create_item(movie)
    return func.HttpResponse("Movies added to Cosmos DB!", status_code=201)