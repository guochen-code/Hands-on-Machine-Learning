fit, (ax_before,ax_after)=plt.subplot(1,2,figsize=(10,5))
df[field].hist(ax=ax_before)
df[field].apply(np.log1p).hist(ax=ax_after)
ax_before.set(title='title',ylabel='ylabel',xlabel='xlabel')
ax_after.set(title='title',ylabel='ylabel',xlabel='xlabel')
fig.suptitle('suptitle')

# fig - ax - all plots on one figure
def automate_plot(df, variable, target):
    
    fig = plt.figure()
    ax = fig.add_subplot(111)
    
    for category in df[variable].unique():
        df[df[variable]==category][target].plot(kind='kde', ax=ax)
    
    # add the legend
    lines, labels = ax.get_legend_handles_labels()
    labels = df[variable].unique()
    ax.legend(lines, labels, loc='best')
    
    plt.show()
