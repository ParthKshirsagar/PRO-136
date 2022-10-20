import pandas as pd

df = pd.read_csv('final.csv')

stars_data = df.to_numpy().tolist()

final_list = []
for star_data in stars_data:
    temp_list = {
        'star_name': star_data[0],
        'star_distance': star_data[1],
        'star_mass': star_data[2],
        'star_radius': star_data[3]
    }
    final_list.append(temp_list)