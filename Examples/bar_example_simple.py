from sjvisualizer import Canvas
from sjvisualizer import DataHandler
from sjvisualizer import BarRace
import time
import json


def main(fps=60, duration=0.35):

    number_of_frames = duration*60*fps

    # load colors
    with open('colors/colors.json') as f:
        colors = json.load(f)

    df = DataHandler.DataHandler(
        excel_file="data/Insta.xlsx", number_of_frames=number_of_frames).df

    canvas = Canvas.canvas()

    # add bar chart
    bar_chart = BarRace.bar_race(
        canvas=canvas.canvas, df=df, colors=colors, height=800)
    canvas.add_sub_plot(bar_chart)

    # add static text
    canvas.add_title("MOST FOLLOWED INSTAGRAM ACCOUNTS", color=(0, 132, 255))
    canvas.add_sub_title(
        "By Number of Followers in Millions", color=(0, 132, 255))

    # add time indication
    canvas.add_time(df=df, time_indicator="month")

    # save colors for next run
    with open("colors/colors.json", "w") as file:
        json.dump(colors, file, indent=4)

    canvas.play(fps=fps)


if __name__ == "__main__":
    main()
