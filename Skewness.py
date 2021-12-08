mask=data.dtypes==np.float
float_cols = data.columns[mask]
skew_limit=skew_limit
skew_vals=data[float_cols].skew()

skew_cols=(skew_vals.sort_values(ascending=False).to_frame().rename(columns={0:'Skew'}).query('abs(Skew)>{}'.format(skew_limit)))
skew_cols
