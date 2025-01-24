def main(req):
    cosmos_client = CosmosClient("<cosmos-endpoint>", {'masterKey': "<cosmos-key>"})
    database = cosmos_client.get_database_client("Theusflix")
    container = database.get_container_client("Movies")
    movie_list = list(container.read_all_items())
    return func.HttpResponse(json.dumps(movie_list), status_code=200, mimetype="application/json")