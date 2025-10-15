import json
import pandas as pd
import numpy as np
from pandas.core.interchange.dataframe_protocol import DataFrame

genres = set()
with open("data/animes.json", "r", encoding="utf-8") as f:
    data = json.load(f)

    genres = sorted({g  for anime in data for g in anime['genre']})


print(len(genres), genres)


df = pd.DataFrame(data, columns=["uid", "title","aired", "link", "img_url", "synopsis",
                                 "score", "ranked", "popularity", "members", "episodes", "genre",
                                 ])

df.drop(columns = ["aired", "img_url"], inplace = True)

#One hot encoding version
df2 = pd.DataFrame(data)[['uid', 'score', 'ranked', 'popularity', 'genre']]
for g in genres:
    df2[g] = df2["genre"].apply(lambda x: 1 if g in x else 0)

df2.drop(columns = ["genre"], inplace = True)
# for anime in data:
#     tmp = []
#     for x in genres:
#         tmp.append(1 if x in anime['genre'] else 0)
#     genres_binary.append(tmp)


df.to_csv("data/list_of_animes.csv", index = False, encoding = "utf-8-sig")
df2.to_csv("data/anime_genre_binary.csv", index=False, encoding="utf-8-sig")


#user dataset making
num_users = 250
list_users = []
for _ in range (num_users):
    a_user = np.round(np.random.normal(loc = np.random.randint(7, 9),
                    scale = np.random.uniform(0.4, 1.9),       #uniform for float
                    size = len(genres)), 2)

    zero_indices = np.random.choice(len(genres), size = int(np.random.uniform(0.4, 0.8) * len(genres)), replace = True)

    a_user[zero_indices] = 0

    list_users.append(a_user)

list_users = np.clip(list_users, 0, 10)   #limit the list

user_df = pd.DataFrame(list_users, columns = genres)
user_df.insert(0, "user_id", range(1, num_users + 1))

user_df.to_csv("data/list_of_users.csv", index = False, encoding = "utf-8-sig")


#MAKING TRAINING DATASET

num_sample = 10000
num_genre = list_users.shape[1]
anime_feature = df2.iloc[:, 4: ].to_numpy()

training_data = []

for i in range (num_sample):
    user_idx = np.random.randint(0, num_users)
    anime_idx = np.random.randint(1, len(data))

    user_vec = list_users[user_idx]
    anime_vec = df2.iloc[anime_idx, 4:].to_numpy()

    #Ground truth

    score = ((np.dot(user_vec, anime_vec) / (np.sum(anime_vec) + 1e-6) ) + np.random.uniform(-0.5, 1))
    score = np.clip(score, 0, 10)
    score = round(score)

    training_data.append([user_idx + 1, df2.iloc[anime_idx]['uid'], score])



df3 = pd.DataFrame(training_data, columns = ['user_id', 'anime_id', 'score'])
df3.to_csv("data/training_data.csv", index = False, encoding  = "utf-8-sig")

training_users = []
training_animes = []

user_idx = df3['user_id']
anime_idx = df3['anime_id']
for i in range (num_sample):
    training_users.append(list_users[user_idx[i] - 1])
    training_animes.append(df2.loc[df2['uid'] == anime_idx[i]].iloc[:, 1:].to_numpy()[0])

df4 = pd.DataFrame(training_users, columns = genres)
df4.to_csv("data/training_users.csv", index = False, encoding  = "utf-8-sig")

df5 = pd.DataFrame(training_animes, columns = ['score','ranked','popularity'] + genres)
df5.to_csv("data/training_animes.csv", index = False, encoding  = "utf-8-sig")
