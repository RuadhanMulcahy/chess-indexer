import os
import datetime
from video_handler import download_youtube_video
from yolov5.detect import run
from file_handler import read_label_file, remove_old_label_file
from convert import Convert
from game_handler import GameHandler
from misc import extract_integer_from_file_name


# video_url = 'https://www.youtube.com/watch?v=MuWCNb9TYqU&ab_channel=GothamChess'
# video_url = 'https://www.youtube.com/watch?v=zFViSKSOgs0'
def indexer(video_url):
    video_file_name = 'video'

    if download_youtube_video(video_url, video_file_name):
        remove_old_label_file()
        run(weights='./files/model/best.pt', source=f'./files/videos/{video_file_name}.mp4', name='../../../files/results/result', conf_thres=0.2 ,save_txt=True ,imgsz=(400,400), save_conf=True)

        file_names = sorted(os.listdir('./files/results/result/labels'), key=extract_integer_from_file_name)
        game_handler = GameHandler()

        for file_name in file_names:
            board = Convert(read_label_file(f"./files/results/result/labels/{file_name}")).to_board()
            if board:
                seconds = extract_integer_from_file_name(file_name) / 30
                if game_handler.read_board(board, datetime.timedelta(seconds=seconds)) == False:
                    break

        game_handler.games.append(game_handler.game)
        
        return game_handler.get_games()
    else:
        return "Video failed to download"