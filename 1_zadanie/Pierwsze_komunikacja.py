
# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import pandas as pd
import os


def main():
    plt.figure(figsize=(3, 3))
    plt.plot([100, 200, 300, 400], [0.1, 0.2, 0.8, 0.9])
    plt.savefig('myplot.pdf')
    plt.close()

    folder_path = r'C:\Users\barte\Desktop\Komunikacja\1_zadanie\pliki'
    files = os.listdir(folder_path)
    dataframes = []
    names = []
    for file in files:
        file_path = os.path.join(folder_path, file)
        df = pd.read_csv(file_path)
        dataframes.append(df)
        names.append(file)
    print(names)

    fig, ax = plt.subplots(figsize=(8, 6))

    for i, df in enumerate(dataframes):
        selected_data = df.iloc[1:, 2:]
        games_count = df.iloc[1:, 1]
        row_averages = selected_data.mean(axis=1)

        ax.plot(games_count, row_averages,
                label=names[i])

    ax.set_xlabel('Rozegranych gier')
    ax.set_ylabel('Odsetek wygranych gier')
    ax.set_title('PLOT')
    plt.tight_layout()

    ax.legend(loc='lower right')
    plt.show()


if __name__ == '__main__':
    main()
