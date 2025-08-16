import os
import sys

# Add parent directory to sys.path to allow importing instabot
sys.path.append(os.path.join(sys.path[0], "../"))
from instabot import Bot  # noqa: E402


# -----------------------------
# Login credentials (HARD-CODED)
# -----------------------------
USERNAME = "my_user"
PASSWORD = "my_pass"
PROXY = None  # Example: "http://127.0.0.1:8080" or leave None if not using


# -----------------------------
# Bot initialization & login
# -----------------------------
bot = Bot()
bot.login(username=USERNAME, password=PASSWORD, proxy=PROXY)

# 1. Follow a user
bot.follow("target_user")

# 2. Unfollow a user
bot.unfollow("target_user")

# 3. Like a user’s recent posts (3 posts here)
bot.like_user("target_user", amount=3, filtration=False)

# 4. Like posts under a hashtag
bot.like_hashtag("python", amount=5)

# 5. Comment on a post
bot.comment("post_id", "Awesome post! 🚀")

# 6. Send direct message
bot.send_message("Hello from bot!", ["friend_user", "another_friend"])

# 7. Get followers of a user
followers = bot.get_user_followers("target_user")
print("Followers:", followers)

# 8. Get following list
following = bot.get_user_following("my_user")
print("Following:", following)

# 9. Get user info
info = bot.get_user_info("target_user")
print("User Info:", info)

# 10. Upload a photo
bot.upload_photo("photo.jpg", caption="Automated upload via bot")

# 11. Unfollow everyone
bot.unfollow_everyone()

# 12. Block/Unblock a user
bot.block("annoying_user")
bot.unblock("annoying_user")
