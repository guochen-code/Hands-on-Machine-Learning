# DO NOT delete a row(s) that one, two, three, or four of those logs have null values. It must all 5 columns should be missing in that row.
df_dropped=df.dropna(how='all',subset=['DTC','PEF','NPHI','RHOB','lithology_name'],axis=0)

# Find the outliers for DTC, PEF, and NPHI. How many outliers are there for each feature? Which Well has the least outliers?
df_dtc_out=df_dropped[(df_dropped['DTC']>250)|(df_dropped['DTC']<25)]
df_pef_out=df_dropped[(df_dropped['PEF']>15)|(df_dropped['PEF']<1)]
df_nphi_out=df_dropped[(df_dropped['NPHI']>0.65)|(df_dropped['NPHI']<-0.15)]

df_new=df_dtc_out.append([df_pef_out,df_nphi_out])

df_new['WELL'].value_counts()
print('DTC:',len(df_dtc_out))
print('PEF:',len(df_pef_out))
print('NPHI:',len(df_nphi_out))


# group by
df_dropped.groupby(['GROUP']).agg({'FORMATION':'nunique'})
