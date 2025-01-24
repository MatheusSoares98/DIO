def main(req):
    data = req.get_json()
    video_title = data["title"]
    thumbnail_url = data["thumbnail_path"]
    cosmos_client = CosmosClient("<cosmos-endpoint>", {'masterKey': "<cosmos-key>"})
    database = cosmos_client.get_database_client("Theusflix")
    container = database.get_container_client("Movies")
    video_item = container.read_item(video_title, partition_key=video_title)
    video_item["thumbnail"] = thumbnail_url
    container.replace_item(video_item["id"], video_item)
    return func.HttpResponse("Thumbnail updated successfully!", status_code=200)