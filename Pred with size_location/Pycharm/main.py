import matplotlib
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt

df1 = pd.read_csv("Participants_Data_HPP/Train.csv")
df2 = pd.read_csv("Participants_Data_HPP/Test.csv")

df1.rename(columns={'POSTED_BY': 'posted_by',
                    'UNDER_CONSTRUCTION': 'under_construction',
                    'RERA': 'rera_approved',
                    'BHK_NO.': 'no_of_rooms',
                    'BHK_OR_RK': 'property_type',
                    'SQUARE_FT': 'area_sqft',
                    'READY_TO_MOVE': 'ready_to_move',
                    'RESALE': 'resale',
                    'ADDRESS': 'address',
                    'LONGITUDE': 'lon',
                    'LATITUDE': 'lat',
                    'TARGET(PRICE_IN_LACS)': 'price_lakh'}, inplace=True)
df1["city"] = df1["address"].str.split(",", expand=True)[1]
df1.drop(columns=["address"], inplace=True)
df1 = df1.iloc[:, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 10]]


df2.rename(columns={'POSTED_BY': 'posted_by',
                    'UNDER_CONSTRUCTION': 'under_construction',
                    'RERA': 'rera_approved',
                    'BHK_NO.': 'no_of_rooms',
                    'BHK_OR_RK': 'property_type',
                    'SQUARE_FT': 'area_sqft',
                    'READY_TO_MOVE': 'ready_to_move',
                    'RESALE': 'resale',
                    'ADDRESS': 'address',
                    'LONGITUDE': 'lon',
                    'LATITUDE': 'lat'}, inplace=True)
df2["city"] = df2["address"].str.split(",", expand=True)[1]
df2.drop(columns=["address"], inplace=True)

# df1.to_csv("Participants_Data_HPP/Train1.csv", index=False)


df = pd.read_csv("Participants_Data_HPP/Train1.csv")

fig = px.scatter_mapbox(
    df,
    lat="lat",
    lon="lon",
    center={"lat": 20.5937, "lon": 78.9629},
    width=625,
    height=825,
    hover_data=['price_lakh'],
)
fig.update_layout(mapbox_style="open-street-map")
fig.show()

print(df.city.unique().size)


# print(df[["area_sqft", "price_lakh"]].describe())
#
# mean_price_by_city = df.groupby("city")["price_lakh"].mean().sort_values(ascending=False)
# print(mean_price_by_city.head())
# mean_price_by_city.plot(
#     kind="bar",
#     xlabel="City",
#     ylabel="Mean Price [Lakh]",
#     title="Mean House Price by City"
# )
# plt.show()
#
# print(df[0:1000])
# pudulayam = df.loc[26047, 'city'] = 'Tamil Nadu'
# print(pudulayam)

