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
sudo docker build -t chess_indexer . 
sudo docker run -p 5000:5000 -d chess_indexer
```

## Sample Input
Service takes in Youtube URL as a GET request. </br>
- GET Request: </br>http://0.0.0.0:5000?video_url=https://www.youtube.com/watch?v=VT5W8ZXYTAo%26list=LL%26index=4%26ab_channel=Bigguy

## Sample Output
Returned JSON object below shows the result for a video containing a single chess game.
 - The games object contains all moves for each game contained in the video.
 - The time_stamps object contains the corresponding timestamps for each move in the games object.
```
{
    "games": {
        "0": "1. g4 2. e5 3. f3 4. Qh4"
    },
    "time_stamps": {
        "0": "1. 0:00:06.933333 2. 0:00:10.366667 3. 0:00:16.833333 4. 0:00:20.100000"
    }
}
```



