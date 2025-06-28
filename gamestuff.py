import streamlit as st
import requests
from streamlit_extras.let_it_rain import rain

API_KEY = st.secrets["gamekey"]



# use apis to organize games IN ORDER idbg thing
#chat can do api stuff NOT knn

# setting up model
platforms= {
    "pc": 4,
    "playstation 5": 187,
    "playstation 4": 18,
    "playstation 3": 16,
    "playstation 2": 15,
    "playstation 1": 27,
    "xbox series s/x": 186,
    "xbox one": 1,
    "xbox 360": 14,
    "xbox": 80,
    "nintendo switch": 7,
    "wii u": 10,
    "wii": 11,
    "gamecube": 105,
    "nintendo 3ds": 8,
    "nintendo ds": 9,
    "macos": 5,
    "linux": 6,
    "ios": 3,
    "android": 21,
    "web": 171,
    "ps vita": 19,
    "psp": 17
}
genres = {
    "action": "action",
    "indie": "indie",
    "adventure": "adventure",
    "rpg": "role-playing-games-rpg",
    "strategy": "strategy",
    "shooter": "shooter",
    "casual": "casual",
    "simulation": "simulation",
    "puzzle": "puzzle",
    "arcade": "arcade",
    "platformer": "platformer",
    "racing": "racing",
    "sports": "sports",
    "fighting": "fighting",
    "family": "family",
    "board games": "board-games",
    "educational": "educational",
    "card": "card"
}
tagdict = {
    "first person": "first-person",
    "third person": "third-person",
    "top down": "top-down",
    "side view": "side-view",
    "isometric": "isometric",
    "singleplayer": "singleplayer",
    "multiplayer": "multiplayer",
    "co-op": "co-op",
    "local co-op": "local-co-op",
    "split screen": "split-screen",
    "mmo": "massively-multiplayer",
    "battle royale": "battle-royale",
    "memes": "memes",
    "funny": "funny",
    "pixel graphics": "pixel-graphics",
    "retro": "retro",
    "anime": "anime",
    "atmospheric": "atmospheric"
}


#gameTypes = {"adventure","indie","arcade","visual novel", "fighting", "shooter", "music", "platform", "puzzle", "racing", "RPG", "simulator", "sport", "strategy", "tactical", "quiz/trivia"}
#genres = ["action", "fantasy", "sci-fi", "horror", "thriller", "survival", "historical", "comedy", "drama", "warfare", "mystery", "romance"]
#modes = ["battle royale", "co-op", "MMO", "multiplayer", "singleplayer", "bird view", "first person", "third person", "VR", "side view"]


st.title("G A M E F I N D E R")
st.subheader("a kinda helpful quiz to see what video games you might like")
st.text("made by betty!!")
st.markdown("---")
st.subheader("quiz")
platform = st.selectbox("whats the platform u use most?", platforms)
#gameType = st.selectbox("whats ur fav game type?", gameTypes)
genre = st.selectbox("whats ur fav genre?", genres)
tag = st.multiselect("select some tags to narrow your search!", tagdict)
#gameMode = st.selectbox("whats ur fav gamemode?", modes)

tags = ",".join(tag)

if st.button("FIND GAMES"):
    if tags!="":
        url = f"https://api.rawg.io/api/games?key={API_KEY}&platforms={platforms[platform]}&genres={genres[genre]}&tags={tags}&page_size=10"
    else:
        url = f"https://api.rawg.io/api/games?key={API_KEY}&platforms={platforms[platform]}&genres={genres[genre]}&page_size=15"

    response = requests.get(url)
    games = response.json()['results']

    if len(games)>0:
        st.subheader("GAMES FOUND:")
        for i in range(10):
            if i % 3 == 0:
                col1, col2,col3 = st.columns(3)

            game = games[i]
            detail_url = f"https://api.rawg.io/api/games/{game['slug']}?key={API_KEY}"
            detail_response = requests.get(detail_url)
            detail_data = detail_response.json()

            #description = detail_data.get("description_raw", "No description available.")
            image_url = detail_data.get("background_image", "no image available.")

            if i % 3 == 0:
                with col1:
                    st.image(image_url, width=200)
                    st.write(game['name'].lower())
                    st.subheader("")
            elif i % 3 == 1:
                with col2:
                    st.image(image_url, width=200)
                    st.write(game['name'].lower())
                    st.subheader("")
            else:
                with col3:
                    st.image(image_url, width=200)
                    st.write(game['name'].lower())
                    st.subheader("")

            #st.write(f"{description.lower()[:200]}...")

    else:
        st.subheader("NO GAMES FOUND :((")


st.markdown("---")
st.subheader("give me feedback!")
st.write("is this gas?")
feedback = st.feedback("faces")
if feedback is not None:
    if feedback>=3:
        st.success("yay!")
        st.balloons()
        rain(emoji=">7<", falling_speed=2, font_size=30, animation_length=1)
    if feedback==2:
        st.warning("i'll try to improve ts 🙏🙏")
    elif feedback<2:
        st.error("pmo")
        rain(emoji=">:C️", falling_speed=2, font_size=70, animation_length=1)



