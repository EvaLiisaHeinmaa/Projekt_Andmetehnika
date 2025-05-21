
### Juhised

### Superset build
```bash
# Build the image (Uses the Dockerfile in this directory)
docker build -t superset-build .

# Secret key should be changed and kept secret, not published to GitHub :)
docker run -d -v ${PWD}:/data:rw -p 8080:8088 -e "SUPERSET_SECRET_KEY=oiuetrjbgjruwet" --name superset superset-build

# Explanation for the -v ${PWD}:/data:rw flag:
# This flag mounts the current working directory (${PWD}) on the host machine to the /data directory inside the container.
# You should replace ${PWD} with the absolute path to the folder where their data files will be stored.
# For example: -v /Users/yourname/superset_data:/data:rw
# Or if you are in the folder where the data files are located, you can use -v $(pwd):/data:rw
# The :rw option allows read and write access to the mounted directory.
# This ensures that the container has access to the necessary data files.

# Update user, firstname, lastname, email and password as you see fit
docker exec -it superset superset fab create-admin --username admin --firstname Admin --lastname Superset --email admin@example.com --password admin
docker exec -it superset superset db upgrade
docker exec -it superset superset init

If you need to rebuild the image (e.g., after making changes to the Dockerfile or other configuration files), you can use the following commands:

```bash
# Remove the existing container (if running)
docker stop superset
docker rm superset

# Rebuild the image
docker build -t superset-build .

# Run the container again with the updated image
docker run -d -v ${PWD}:/data:rw -p 8080:8088 -e "SUPERSET_SECRET_KEY=your_new_secret_key" --name superset superset-build

# Update user, firstname, lastname, email and password as you see fit
docker exec -it superset superset fab create-admin --username admin --firstname Admin --lastname Superset --email admin@example.com --password admin 
docker exec -it superset superset db upgrade
docker exec -it superset superset init
### Removing Dangling Images

Dangling images are unused Docker images that can take up unnecessary space. To remove them, use the following command:

```bash
docker image prune -f

## Important Notes

- **Host Machine Execution**: All the commands in this README should be executed on the host machine where Docker is installed. While the project includes a `devcontainer`, these commands are not intended to be run inside the development container.
- **Data Directory**: Ensure that the directory you mount with the `-v` flag contains the data files you want to use with Superset. This directory will be accessible inside the container at `/data`.

Additional up-to-date documentation about Superset can be found at [https://superset.apache.org/docs/intro](https://superset.apache.org/docs/intro).
```
### Requirements

All the requirements can be found in the requirements.txt.

### Apache Superset

Here's how to get started with visualizing kalad data in Apache Superset:

Open your web browser and navigate to localhost:8080. This will take you to the Apache Superset login page.
Enter the credentials (admin/admin) you set up during the initialization process to log in.
Once logged in, follow these steps to connect to your data source:

Click on the '+' icon, then select 'Connect Database'.
In the 'Connect Database' screen, you'll see a 'Supported databases' dropdown menu. Select DuckDB from this list.
For the URI, you need to specify the location of your database. Enter duckdb:////data/kalad.db into the URI field.
By connecting to the DuckDB database, you're setting up Superset to directly query and visualize the data you've transformed and stored. DuckDB is an in-process SQL OLAP Database Management System, perfect for analytical queries on large datasets, like the air quality data we're working with.

To start visualizing the kalad data, we first need to create a dataset within Apache Superset. This dataset will be the foundation for our explorations and visualizations. Follow the steps below to create a dataset from the Parquet files we prepared earlier:

From the top navigation bar, select SQL and then SQL Lab from the dropdown menu. SQL Lab is a flexible tool within Superset that allows for executing SQL queries on your connected databases.
Within SQL Lab, you'll see an option to select your database. Choose the database connection you set up previously (the one connected to DuckDB).
In the SQL query editor that appears, you'll enter a SQL query to load your data. Type or copy the following SQL command into the editor:
SELECT * FROM read_parquet('/data/*.parquet')
This SQL command tells Superset to read all Parquet files (just one in kalad case). Using the `read_parquet` function allows us to directly query and work with the Parquet files as if they were tables in a database.
After entering the query, execute it by pressing the "Run selection" button. This action will load the data and display the results within SQL Lab. After confirming that the query works, save the dataset using "Save" -> "Save dataset" button.

**Sharing Apache Superset dashboard**


- Export your dashboard as a zip file from Superset

- Commit the file to Github 

- Clone the repository/or download it directly from Github repository

- Open Superset

- Import Superset Dashboard zip-file (no need to unzip it)



# Share Superset Running in Your Docker Container 

NB! sharing your local Superset dashboard using an IP address like http://192.168.x.x:8080 only works if both users are on the same network (e.g., same Wi-Fi or hotspot). duckdb /app/superset_home/mydb.duckdb



Create different users. (Alpha for editing, Gamma for viewing)
- Editor user (Alpha)

docker exec -it superset superset fab create-user --username editor --firstname Editor --lastname User --email editor@example.com --password editor --role Alpha


- Viewer user (Gamma)

docker exec -it superset superset fab create-user --username viewer --firstname Viewer --lastname User --email viewer@example.com --password viewer --role Gamma

 Share the Superset Link 
 http://<your-ip-address>:8080

 Others can enter the superset via shared link by entering the assigned username and password. 
