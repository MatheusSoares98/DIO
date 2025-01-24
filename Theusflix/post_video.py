def main(req):
    body = req.get_json()
    video_data = {
        "id": body["title"],
        "path": body["path"],
        "title": body["title"],
        "genre": body["genre"]
    }
    cosmos_client = CosmosClient("<cosmos-endpoint>", {'masterKey': "<cosmos-key>"})
    database = cosmos_client.get_database_client("Theusflix")
    container = database.get_container_client("Movies")
    container.create_item(video_data)
    return func.HttpResponse("Video details added successfully!", status_code=201)