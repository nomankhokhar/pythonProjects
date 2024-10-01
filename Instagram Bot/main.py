from instabot import Bot

bot = Bot()

# Login to Instagram
def login(username, password):
    try:
        bot.login(username=username, password=password)
        print("Login successful.")
    except Exception as e:
        print(f"Error during login: {e}")
        exit()

# Logout from Instagram
def logout():
    try:
        bot.logout()
        print("Logged out successfully.")
    except Exception as e:
        print(f"Error during logout: {e}")

# Follow a user
def follow_user(username):
    try:
        bot.follow(username)
        print(f"Followed {username}")
    except Exception as e:
        print(f"Error following {username}: {e}")

# Unfollow a user
def unfollow_user(username):
    try:
        bot.unfollow(username)
        print(f"Unfollowed {username}")
    except Exception as e:
        print(f"Error unfollowing {username}: {e}")

# Upload a photo with or without caption
def upload_photo(photo_path, caption=None):
    try:
        if caption:
            bot.upload_photo(photo_path, caption=caption)
            print(f"Photo uploaded with caption: {caption}")
        else:
            bot.upload_photo(photo_path)
            print("Photo uploaded without caption.")
    except Exception as e:
        print(f"Error uploading photo: {e}")

# Upload a video with or without caption
def upload_video(video_path, caption=None):
    try:
        if caption:
            bot.upload_video(video_path, caption=caption)
            print(f"Video uploaded with caption: {caption}")
        else:
            bot.upload_video(video_path)
            print("Video uploaded without caption.")
    except Exception as e:
        print(f"Error uploading video: {e}")

# Like a media (photo or video)
def like_media(media_id):
    try:
        bot.like(media_id)
        print(f"Liked media with ID: {media_id}")
    except Exception as e:
        print(f"Error liking media: {e}")

# Unlike a media (photo or video)
def unlike_media(media_id):
    try:
        bot.unlike(media_id)
        print(f"Unliked media with ID: {media_id}")
    except Exception as e:
        print(f"Error unliking media: {e}")

# Main process
if __name__ == "__main__":
    username = "your_instagram_username"
    password = "your_instagram_password"

    # Login
    login(username, password)

    # Follow a user
    follow_user("wscubetechindia")

    # Unfollow a user
    unfollow_user("wscubetechindia")

    # Upload a photo (replace with your image path)
    upload_photo("path_to_your_photo.jpg", "This is a caption for the photo")

    # Upload a photo without a caption
    upload_photo("path_to_your_photo.jpg")

    # Upload a video (replace with your video path)
    upload_video("path_to_your_video.mp4", "This is a caption for the video")

    # Upload a video without a caption
    upload_video("path_to_your_video.mp4")

    # Like a media (use media ID)
    like_media("media_id_to_like")

    # Unlike a media (use media ID)
    unlike_media("media_id_to_unlike")

    # Logout
    logout()
