
## Create Docker Image
1. Use command `docker build -t streamlitapp:latest -f Dockerfile .`
2. To run use `docker run -p 8501:8501 streamlitapp:latest`
3. Sample Dockerfile 
```
FROM python:3.7
WORKDIR /app
COPY requirements.txt ./requirements.txt
RUN pip3 install -r requirements.txt
EXPOSE 8501
COPY . /app
ENTRYPOINT ["streamlit", "run"]
CMD ["app.py"]

```
Folder Structure
```
.
├── app.py
├── Dockerfile
├── README.md
├── requirements.txt
```

## Saving and Loading Docker Image

### Method 1
1. To save use `docker save -o <path for generated tar file> <image name>`
2. Then copy your image to a new system with regular file transfer tools such as cp, scp or rsync(preferred for big files). After that you will have to load the image into Docker:
`docker load -i <path to image tar file>`. For example:`docker save -o /home/masuri/Downloads/test/data-analysis-moh-vaccination-death/streamlitapp.tar streamlitapp:latest`

### Method 2
1. Transferring a Docker image via SSH, bzipping the content on the fly. `docker save <image> | bzip2 | ssh user@host docker load`. _Note that docker load automatically decompresses images for you. It supports gzip, bzip2 and xz._
2. It's also a good idea to put pv in the middle of the pipe to see how the transfer is going. `docker save <image> | bzip2 | pv | ssh user@host docker load`

### Method 3
1. First save the Docker image to a compressed archive. `docker save <docker image name> | gzip > <docker image name>.tar.gz`
2. Then load the exported image to Docker using the command. `zcat <docker image name>.tar.gz | docker load`
