# Adnan Akbas

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime
from matplotlib.animation import FuncAnimation


def animate_movement_plot(df, interval=10, frames=1000):
    df['nr'] = np.arange(len(df))

    def update_graph(num):
        row = df[df['nr'] == num]
        ax.scatter(row['pal_accX'], row['pal_accY'], row['pal_accZ'])

        return ax

    fig = plt.figure()
    ax = fig.add_subplot(projection='3d')

    init_row = df[df['nr'] == 0]
    ax.scatter(init_row['pal_accX'], init_row['pal_accY'], init_row['pal_accZ'])

    ax.set_title('3D accelerometer movement')
    ax.set_ylabel('Y')
    ax.set_xlabel('X')
    ax.set_zlabel('Z')

    ani = FuncAnimation(fig, update_graph, frames=frames, interval=interval)

    plt.show()


def timestamp_to_date(timestamp):
    return datetime.fromtimestamp(float(timestamp.split(',')[0]))


activepal = pd.read_csv('../../BMR002/activpal20.csv', delimiter=';', header=0, index_col=0, parse_dates=True,
                        date_parser=timestamp_to_date, nrows=1000000)
activity = pd.read_csv('../../BMR002/activiteiten.csv', delimiter=';', index_col=0, header=0, parse_dates=True)

activity_jump = activity.loc['traplopen']

date_filter = (activepal.index >= activity_jump['start']) & (activepal.index <= activity_jump['stop'])

activepal = activepal[date_filter].resample('S').mean()

animate_movement_plot(activepal, interval=1, frames=100000)
