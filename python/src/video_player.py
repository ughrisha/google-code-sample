"""A video player class."""
import random
from .video_library import VideoLibrary


class VideoPlayer:
    """A class used to represent a Video Player."""

    def __init__(self):
        self._video_library = VideoLibrary()

    def number_of_videos(self):
        num_videos = len(self._video_library.get_all_videos())
        print(str(num_videos)+" videos in the library")

    def show_all_videos(self):
        """Returns all videos."""
        videos = (self._video_library.get_all_videos()) 
        list = []
        tag = ""
        print("Here's a list of all available videos:")
        for i in videos:
            if(i.tags):
                tags = "["
                for j in i.tags:
                    tags += j + " "
                tags = tags.strip()
                tags+="]"
            else:
                tags = "[]"
            list += [f"{i.title} ({i.video_id}) {tags}"]
        list.sort()
        for i in list:
            print(i)
            

    def play_video(self, video_id):
        """Plays the respective video.

        Args:
            video_id: The video_id to be played.
        """
        global is_playing 
        global current_video
        global current_id
        videos = (self._video_library.get_all_videos()) 
        flag = False
        for i in videos:
            if(i.video_id == video_id):
                if(is_playing == False):
                    flag = True
                    is_playing = True
                    print("Playing video: "+f"{i.title}")
                    current_video = i.title
                    current_id = i.video_id
                else:
                    flag = True
                    print("Stopping video: "+current_video)
                    print("Playing video: "+f"{i.title}")
                    current_video = i.title
                    current_id = i.video_id
        if(flag == False):
            print("Cannot play video: Video does not exist")   


    def stop_video(self):
        """Stops the current video."""
        global current_video
        global is_playing
        global current_id
        if(is_playing == True):
            print("Stopping video: "+f"{current_video}")
            current_video = ""
            current_id = ""
            is_playing = False
        else:
            print("Cannot stop video: No video is currently playing")

    def play_random_video(self):
        """Plays a random video from the video library."""
        n = random.randint(0,len(self._video_library.get_all_videos())-1)
        global current_video
        global is_playing
        global current_id
        videos = (self._video_library.get_all_videos()) 
        if(is_playing == True):
            print("Stopping Video: "+f"{current_video}")
            current_video = videos[n].title
            current_id = videos[n].video_id
            print("Playing video: "+f"{current_video}")
        else:
            current_video = videos[n].title
            current_id = videos[n].video_id
            is_playing = True
            print("Playing video: "+f"{current_video}")

    def pause_video(self):
        """Pauses the current video."""
        global pause
        global is_playing
        global current_video
        if(pause == False and current_video!=""):
            print("Pausing Video: "+f"{current_video}")
            pause = True
        elif(current_video!=""):
            print("Video already paused: "+f"{current_video}")
        else:
            print("Cannot pause video: No video playing")

    def continue_video(self):
        global pause
        global is_playing
        global current_video
        if(pause == True and current_video!=""):
            print("Continuing Video: "+f"{current_video}")
            pause = False
        elif(current_video!=""):
            print("Video already continuing: "+f"{current_video}")
        else:
            print("Cannot continue video: No video playing")

    def show_playing(self):
        """Displays video currently playing."""
        global current_id
        global current_video
        global is_playing
        global pause
        if(is_playing and pause):
            i = self._video_library.get_video(current_id)
            if(i.tags):
                tags = "["
                for j in i.tags:
                    tags += j + " "
                tags = tags.strip()
                tags+="]"
            else:
                tags = "[]"
            print("Currently playing: "+f"{i.title} ({i.video_id}) {tags}"+" - PAUSED")
        elif(is_playing):
            i = self._video_library.get_video(current_id)
            if(i.tags):
                tags = "["
                for j in i.tags:
                    tags += j + " "
                tags = tags.strip()
                tags+="]"
            else:
                tags = "[]"
            print("Currently playing: "+f"{i.title} ({i.video_id}) {tags}")
        else:
            print("No video is currently playing")


    def create_playlist(self, playlist_name):
        """Creates a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        print("create_playlist needs implementation")

    def add_to_playlist(self, playlist_name, video_id):
        """Adds a video to a playlist with a given name.

        Args:
            playlist_name: The playlist name.
            video_id: The video_id to be added.
        """
        print("add_to_playlist needs implementation")

    def show_all_playlists(self):
        """Display all playlists."""

        print("show_all_playlists needs implementation")

    def show_playlist(self, playlist_name):
        """Display all videos in a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        print("show_playlist needs implementation")

    def remove_from_playlist(self, playlist_name, video_id):
        """Removes a video to a playlist with a given name.

        Args:
            playlist_name: The playlist name.
            video_id: The video_id to be removed.
        """
        print("remove_from_playlist needs implementation")

    def clear_playlist(self, playlist_name):
        """Removes all videos from a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        print("clears_playlist needs implementation")

    def delete_playlist(self, playlist_name):
        """Deletes a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        print("deletes_playlist needs implementation")

    def search_videos(self, search_term):
        """Display all the videos whose titles contain the search_term.

        Args:
            search_term: The query to be used in search.
        """
        print("search_videos needs implementation")

    def search_videos_tag(self, video_tag):
        """Display all videos whose tags contains the provided tag.

        Args:
            video_tag: The video tag to be used in search.
        """
        print("search_videos_tag needs implementation")

    def flag_video(self, video_id, flag_reason=""):
        """Mark a video as flagged.

        Args:
            video_id: The video_id to be flagged.
            flag_reason: Reason for flagging the video.
        """
        print("flag_video needs implementation")

    def allow_video(self, video_id):
        """Removes a flag from a video.

        Args:
            video_id: The video_id to be allowed again.
        """
        print("allow_video needs implementation")

is_playing = False
current_video = ""
pause = False
current_id = ""