from collections import deque
from pathlib import Path

class playlist:
    def __init__(self):
        self.songs = deque()
    
    def add_song(self, song):
        self.songs.append(song)

    def display_all_playlist(self):
        for song in self.songs:
            return list(song)
    
    def load_songs(self, txt_file):
        PATH = Path(txt_file)
        if not PATH.is_file():
            raise FileNotFoundError(f"The file {txt_file} does not exist.")
        with open(txt_file, 'r') as file:
            for line in file:
                song = line.strip()
                if song:
                    self.add_song(song)
        return "Songs loaded successfully."

    def play_next_song(self):
        if self.songs:
            return self.songs.popleft()
        else:
            return "No songs in the playlist."
    
    def play_previous_song(self, song):
        self.songs.appendleft(song)
        return f"Re-added {song} to the front of the playlist."
    
    def clear_playlist(self):
        self.songs.clear()
        return "Playlist cleared."
    
    def shuffle_playlist(self):
        import random
        temp_list = list(self.songs)
        random.shuffle(temp_list)
        self.songs = deque(temp_list)
        return "Playlist shuffled."
    
    def save_playlist(self, txt_file):
        with open(txt_file, 'w') as file:
            for song in self.songs:
                file.write(f"{song}\n")
        return f"Playlist saved to {txt_file}."
    
    def get_playlist_length(self):
        return len(self.songs)
    
# if __name__ == "__main__":
#     my_playlist = playlist()
#     my_playlist.load_songs('songs.txt')
#     print(my_playlist.display_all_playlist())
#     print(my_playlist.play_next_song())
#     print(my_playlist.get_playlist_length())
#     my_playlist.shuffle_playlist()
#     print(my_playlist.display_all_playlist())
#     my_playlist.save_playlist('new_songs.txt')
