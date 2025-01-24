### `README.md`

Theusflix Azure Functions

Welcome to Theusflix! This repository includes Azure Functions that manage the movie data for your streaming service, interacting with an Azure Cosmos DB.

Prerequisites:

- Azure Account
- Azure Functions Core Tools
- Python 3.x
- Cosmos DB Account

Function Overview:

Post Video:
HTTP Method: POST
Endpoint: /api/post_video

Post Thumbnail to Video:
HTTP Method: POST
Endpoint: /api/post_thumbnail

Post Database to Cosmos DB:
HTTP Method: POST
Endpoint: /api/post_database

Get All Movies from Cosmos DB:
HTTP Method: GET
Endpoint: /api/get_all_movies

Get Movie Detail from Cosmos DB:
HTTP Method: GET
Endpoint: /api/get_movie_detail?title=Movie Title

Local Development:

1. Clone this repository
2. Install dependencies
3. Set your Cosmos DB credentials
4. Run the functions locally
