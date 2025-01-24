def main(req):
    title = req.params.get("title")
    cosmos_client = CosmosClient("<cosmos-endpoint>", {'masterKey': "<cosmos-key>"})
    database = cosmos_client.get_database_client("Theusflix")
    container = database.get_container_client("Movies")
    movie = container.read_item(title, partition_key=title)
    return func.HttpResponse(json.dumps(movie), status_code=200, mimetype="application/json")