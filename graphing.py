from collections import Counter 
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from simulator import simulation

def create_joint_grid(df):
    sns.set_theme(style="ticks")

    g = sns.JointGrid(data=df, x="Total Rounds", y="Gold Left", marginal_ticks=True)

    cax = g.figure.add_axes([.15, .55, .02, .2])

    # Define bins for the x-axis
    x_bins = np.arange(df["Total Rounds"].min() - 0.5, df["Total Rounds"].max() + 1.5, 1)
    # Define bins for the y-axis
    y_bins = np.arange(df["Gold Left"].min() - 0.5, df["Gold Left"].max() + 1.5, 1)

    # Add the joint and marginal histogram plots
    g.plot_joint(
        sns.histplot, 
        discrete=(True, True),
        cmap="light:#19002D", 
        pmax=.8, 
        cbar=True, 
        cbar_ax=cax,
        cbar_kws={"shrink": 0.75},
        binwidth=(1, 1),  # Assuming that the bin width for both x and y is 1
        bins=(x_bins, y_bins)
    )
    
    g.plot_marginals(sns.histplot, element="step", color="#19002D", bins=x_bins, common_norm=False, common_bins=False)
    g.plot_marginals(sns.histplot, element="step", color="#19002D", bins=y_bins, common_norm=False, common_bins=False, fill=True, multiple="dodge")

    # Explicitly set the limits of the x and y axes
    g.ax_joint.set_xlim(df["Total Rounds"].min() - 0.5, df["Total Rounds"].max() + 0.5)
    g.ax_joint.set_ylim(df["Gold Left"].min() - 0.5, df["Gold Left"].max() + 0.5)

    # Set the ticks for x and y axis
    g.ax_joint.set_xticks(np.arange(df["Total Rounds"].min() - 0.5, df["Total Rounds"].max() + 1.5, 1))
    g.ax_joint.set_yticks(np.arange(df["Gold Left"].min() - 0.5, df["Gold Left"].max() + 1.5, 1))

    # Setting the ticks for the marginal axes can be done similarly, if needed
    g.ax_marg_x.set_xlim(df["Total Rounds"].min() - 0.5, df["Total Rounds"].max() + 0.5)
    g.ax_marg_y.set_ylim(df["Gold Left"].min() - 0.5, df["Gold Left"].max() + 0.5)

    # Adjust x and y axis to only show whole numbers
    g.ax_joint.xaxis.set_major_locator(plt.MultipleLocator(1))
    g.ax_joint.yaxis.set_major_locator(plt.MultipleLocator(1))

    # Showing the plot
    plt.show()

def create_binned_joint_grid(df):
    # Bin 'Gold Left' into bins of 2
    df['Binned Gold Left'] = (df['Gold Left'] // 2) * 2

    sns.set_theme(style="ticks")

    g = sns.JointGrid(data=df, x="Total Rounds", y="Binned Gold Left", marginal_ticks=True)

    cax = g.figure.add_axes([.15, .55, .02, .2])

    # Add the joint and marginal histogram plots
    g.plot_joint(
        sns.histplot, 
        discrete=(True, True), 
        binwidth=2,
        cmap="light:#19002D", 
        pmax=.8, 
        cbar=True, 
        cbar_ax=cax,
        cbar_kws={"shrink": 0.75}
    )
    g.plot_marginals(sns.histplot, element="step", color="#19002D", binwidth=2)  

    # Adjust x and y axis to only show whole numbers
    g.ax_joint.xaxis.set_major_locator(plt.MultipleLocator(1))
    g.ax_joint.yaxis.set_major_locator(plt.MultipleLocator(2))  # Adjust for the binning of 2

    # Showing the plot
    plt.show()

def main():
    # results = []
    # simulation(0, 0, True, 8, 128, results)
    # df = pd.DataFrame(results, columns = ['Total Rounds', 'Gold Left'])

    # create_joint_grid(df)
    # # create_binned_joint_grid(df)
    
    # overlapping densities plot for this

    # different_starts = {}
    # start_averages = []
    # for i in range(5, 15):
    #     results = []
    #     simulation(0,0,True,i,128,results)
    #     df = pd.DataFrame(results, columns = ['Total Rounds', 'Gold Left'])
    #     start_averages.append(df["Total Rounds"].mean())
    #     different_starts[i] = df
    
    # print(start_averages)

    # another overlapping densities plot for this

    # Level+Gold   8+0  8+10 8+20 8+30 8+30 8+30 9+0  9+10
    breakpoints = [108, 118, 128, 138, 148, 158, 188, 208]
    # different_goals = {}
    # goal_averages = []
    # for breakpoint in breakpoints:
    #     results=[]
    #     simulation(0, 0, True, 8, breakpoint, results)
    #     df = pd.DataFrame(results, columns = ['Total Rounds', 'Gold Left'])
    #     goal_averages.append(df["Total Rounds"].mean())
    #     different_goals[breakpoint] = df

    # print(goal_averages)

    # combo graph of breakpoints and gold starts, make a surface plot with y axis = rounds

    combo_averages = []
    for breakpoint in breakpoints:
        starts = []
        for i in range(5, 15):
            results = []
            simulation(0,0,True,i,breakpoint,results)
            df = pd.DataFrame(results, columns = ['Total Rounds', 'Gold Left'])
            starts.append(df["Total Rounds"].mean())
        combo_averages.append(starts)
    
    combos = pd.DataFrame(combo_averages, index= breakpoints, columns=range(5,15))
    print(combos)




if __name__ == "__main__":
    main()