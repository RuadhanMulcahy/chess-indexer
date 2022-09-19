# Chess Video Indexer
Application to convert chess videos into time stamped PGN (Portable Game Notation).

## Tasks
&emsp;&emsp;:heavy_check_mark:&emsp; Download Youtube video from URL and convert to individual frames.</br></br>
&emsp;&emsp;:heavy_check_mark:&emsp;Train YOLOV5 computer vision model to detect chess pieces and boards.</br></br>
&emsp;&emsp;:heavy_check_mark:&emsp; Run an image through YOLOV5 model.</br></br>
&emsp;&emsp;:heavy_check_mark:&emsp; Convert YOLOV5 output into 2D Array representing chess board.</br></br>
&emsp;&emsp;:heavy_check_mark:&emsp; Process multiple YOLOV5 outputs and detect valid chess moves.</br></br>
&emsp;&emsp;❌&emsp; Detect reverse moves and catch up moves ie. If chess game in video starts traversing game backwards.</br></br>
&emsp;&emsp;:heavy_check_mark:&emsp; Combine chess moves into valid chess games in PGN (Portable Game Notation) format.</br></br>
&emsp;&emsp;:heavy_check_mark:&emsp; Flask server to allow for interaction with the system.</br></br>

## Run
```
sudo docker build -t dockerfile . 
sudo docker run -p 5000:5000 -d dockerfile
```

## Sample Output





