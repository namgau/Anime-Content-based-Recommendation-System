import tabulate
import numpy as np
import pandas as pd

def print_pred_animes(y_p, sorted_animes, anime_dict, maxcount=10):
    """In bảng anime gợi ý với điểm dự đoán cao nhất."""
    disp = [["Pred_Score", "Anime_ID", "Score", "Title", "Genres"]]

    for i in range(min(maxcount, len(sorted_animes))):
        # Lấy Anime_ID (uid)
        anime_id = int(sorted_animes.iloc[i]['uid']) if 'uid' in sorted_animes.columns else i

        # Lấy thông tin từ dict
        anime_info = anime_dict.get(anime_id, {"titl.e": "Unknown", "genres": "N/A"})

        # Lấy Score gốc (nếu có cột score)
        score = float(sorted_animes.iloc[i]['score']) if 'score' in sorted_animes.columns else 'N/A'

        disp.append([
            np.around(y_p[i, 0], 2),  # Pred_Score
            anime_id,
            score,
            anime_info["title"],
            anime_info["genres"]
        ])

    table = tabulate.tabulate(disp, tablefmt='html', headers="firstrow")
    return table


def gen_tmp_users(tmp_user, n_items):
    if tmp_user.ndim == 1:
        tmp_user = tmp_user.reshape(1, -1)
    tmp_users = np.repeat(tmp_user, n_items, axis=0)
    return tmp_users

