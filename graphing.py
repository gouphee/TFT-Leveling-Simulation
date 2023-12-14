from collections import Counter 
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
from simulator import simulation

def create_joint_grid(df):
    sns.set_theme(style="ticks")

    g = sns.JointGrid(data=df, x="Total Rounds", y="Gold Left", marginal_ticks=True)

    cax = g.figure.add_axes([.15, .55, .02, .2])

    # Add the joint and marginal histogram plots
    g.plot_joint(
        sns.histplot, 
        discrete=(True, True),
        cmap="light:#19002D", 
        pmax=.8, 
        cbar=True, 
        cbar_ax=cax,
        cbar_kws={"shrink": 0.75}
    )
    g.plot_marginals(sns.histplot, element="step", color="#19002D")  

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
    results = []
    simulation(0, 0, True, 8, 128, results)
    df = pd.DataFrame(results, columns = ['Total Rounds', 'Gold Left'])

    create_joint_grid(df)
    create_binned_joint_grid(df)

if __name__ == "__main__":
    main()