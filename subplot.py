fit, (ax_before,ax_after)=plt.subplot(1,2,figsize=(10,5))
df[field].hist(ax=ax_before)
df[field].apply(np.log1p).hist(ax=ax_after)
ax_before.set(title='title',ylabel='ylabel',xlabel='xlabel')
ax_after.set(title='title',ylabel='ylabel',xlabel='xlabel')
fig.suptitle('suptitle')
