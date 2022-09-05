FROM nvcr.io/nvidia/pytorch:22.04-py3
RUN rm -rf /opt/pytorch 

RUN apt-get update
RUN DEBIAN_FRONTEND=noninteractive TZ=Etc/UTC apt-get -y install tzdata
RUN apt-get install ffmpeg libsm6 libxext6  -y

RUN mkdir /app
COPY app /app
WORKDIR /app
RUN git clone https://github.com/ultralytics/yolov5.git
RUN python3 -m venv venv
RUN source ./venv/bin/activate
RUN python3 -m pip install --upgrade pip
RUN python3 -m pip install -r ../requirements.txt
ENTRYPOINT ["python3"]
CMD ["server.py"]

