"""A video player class."""

from .video_library import VideoLibrary as video
import random

class VideoPlayer:
    """A class used to represent a Video Player."""
   
    def __init__(self):
        self._video = video()
        self.play="" 
        self.link=""
        self.pause=""
        self.playlist=""
        self.curr_video=""
        self.list_ofvids=""
        self.once="once"
        self.play, self.curr_video = False, ""
        self.list_ofvids=[]
        self.once, self.pause= True, False
        self.playlist=[]

        

    def number_of_videos(self):
        num_videos = len(self._video.get_all_videos())
        print(f"{num_videos} videos in the library")

    def show_all_videos(self):
        print("Here is a list of all available videos:")
        # list in alphabetical order 
        new_list=self._video.get_all_videos()
        new_list.sort(key=lambda x: x.title, reverse=False)
        
        for i in range(0, len(new_list)):
            if (len(new_list[i].tags)!=0 ):
                    s=new_list[i].tags[0]+" "+new_list[i].tags[1]
            else:
                    s=""
            print(
                new_list[i].title,"("+new_list[i].video_id+")","["+s+"]"
                )

    def play_video(self, video_id):
        try:
            if (self.play == False):
                if (self.curr_video== ""):
                    self.play= True
                    self.curr_video= self._video.get_video(video_id).title
                    print("Playing video: "+self.curr_video)
            # self.curr_video playing
            elif (self.play == True ): 
                if (self.curr_video!= ""):
                    print("Stopping video: "+self.curr_video)
                    self.curr_video= self._video.get_video(video_id).title
                    print("Playing video: "+self.curr_video)
                    self.pause= False
        except AttributeError:
            print("Cannot play video: Video does not exist")


    def stop_video(self):
        if self.curr_video=="":
            print("Cannot stop video: No video is currently playing")
        else:
            print("Stopping video: "+ self.curr_video)
            self.curr_video=""
            self.pause, self.play=False, False

    def play_random_video(self):
        if self==None:
            print("No videos available")
            return
        else:
            new_list=self._video.get_all_videos()
            if self.once== True:
                for i in range(0, len(new_list)):
                    self.list_ofvids.append(new_list[i].title)
                self.once=False

            if len(self.list_ofvids)!=0:
                r = random.randint(0, len(self.list_ofvids)-1)
                if self.play == False:
                    self.play=True
                else:
                    print("Stopping video: ", self.curr_video)

                self.curr_video= self.list_ofvids[r]
                print("Playing video:",self.curr_video)
                self.list_ofvids.remove(self.curr_video)
            else:
                print("No videos available")



    def pause_video(self):
        if self.play== False:
            print("Cannot pause video: No video is currently playing")
            return
        elif self.pause== False:
            print("Pausing video:", self.curr_video)
            self.pause= True
        else:
            print("Video already paused:", self.curr_video)


    def continue_video(self):
        if self.play==False:
            print("Cannot continue video: No video is currently playing")
        elif self.pause==False:
            print("Cannot continue video: Video is not paused")
        else:
            print("Continuing video:", self.curr_video)
            self.pause=False
            self.play=True


    def show_playing(self):
        # global  pause
        if self.play==False:
            print("No video is currently playing")
            return
        # call method to recover id and tags knowing title
        id_vid, tags_vid=self.find_id(self.curr_video)
        vid=self._video.get_video(id_vid)
# play funny_dogs_video_id
        if self.pause==True: 
            print(
                "Currently playing:", self.curr_video, "("+id_vid+")", "["+tags_vid[0], tags_vid[1]+']', 
                "-", "PAUSED"
            )
        else:
            print(
                "Currently playing:", self.curr_video, "("+id_vid+")", "["+tags_vid[0], tags_vid[1]+']'
            )

    def find_id(self, title):
        vid=self._video.get_all_videos()
        for i in range(0, len(vid)):
            if vid[i].title == self.curr_video:
                return vid[i].video_id, vid[i].tags
        

# ------------------ part 2

# A list called playlist has multiple playlists that are also lists. 
# Name of playlist is on first position of each playlist

    def create_playlist(self, playlist_name):

        # given that all IS SAVED IN LIST is in small letters
        if len(self.playlist)==0 or self.playlist_name.lower() not in self.playlist:
            new_playlist=[playlist_name.lower()]
            self.playlist.append(new_playlist)
            print("Successfully created a new playlist:", playlist_name)
        else:
            print("Cannot create a playlist: A playlist with the same name already exists")


    def add_to_playlist(self, playlist_name, video_id):
        try:
            if  playlist_name not in self.playlist:
                print("Cannot add video to", playlist_name+ ": Playlist does not exist")
                return
        except AttributeError:
            print("Cannot add video to", playlist_name+ ": Video does not exist")     
        # PROBLEM: CANT READ WHATS INSIDE PLAYLISTS IF U DO IT LIKE THIS
        

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


# --------------------------------------
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
