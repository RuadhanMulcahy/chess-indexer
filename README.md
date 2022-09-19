# Chess Video Indexer
Application to convert chess videos into time stamped PGN (Portable Game Notation).

# Tasks
- [X] Download Youtube video from URL and convert to individual frames.
- [X] Train YOLOV5 computer vision model to detect chess pieces and boards.
- [X] Run an image through YOLOV5 model.
- [X] Convert YOLOV5 output into 2D Array representing chess board.
- [X] Process multiple YOLOV5 outputs and detect valid chess moves.
- [ ] Detect reverse moves and catch up moves ie. If chess game in video starts traversing game backwards.
- [X] Combine chess moves into valid chess games in PGN (Portable Game Notation) format.
- [X] Flask server to allow for interaction with the system.

## Run
sudo docker build -t dockerfile .
sudo docker run -p 5000:5000 -d dockerfile

## Sample Output





