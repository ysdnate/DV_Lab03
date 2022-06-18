import pandas as pd
# create a dataframe
df = pd.DataFrame({
    'Address': ['4860 Sunset Boulevard,San Francisco,California',
                '3055 Paradise Lane,Salt Lake City,Utah',
                '682 Main Street,Detroit,Michigan',
                '9001 Cascade Road,Kansas City,Missouri']
})
# display the dataframe
print(df)
df[['Street', 'City', 'State']] = df['Address'].str.split(',', expand=True)
# display the dataframe
df
print(df)