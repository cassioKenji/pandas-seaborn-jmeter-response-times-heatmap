import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

dataframe = pd.read_csv("result.csv", index_col=False)

# encontrei esse esquema no stackoverflow, pq o timestamp do jmeter dava zika com o to_datetime() do pandas. dava no ano de 1970
dataframe["timeStamp"] = (dataframe["timeStamp"].astype(np.int64)) // 10**3
dataframe["timeStamp"] = pd.to_datetime(dataframe["timeStamp"], unit='s')

balance_df = dataframe[dataframe["label"] == "balance"].copy()

balance_response_times = balance_df["elapsed"]
balance_timestamps = balance_df["timeStamp"]

response_times_timestamps_df = pd.concat([balance_timestamps, balance_response_times, balance_df["label"]], axis=1)
response_times_timestamps_df = response_times_timestamps_df.pivot_table(index="timeStamp", columns="label", values="elapsed", aggfunc="sum")

heatmap = sns.heatmap(response_times_timestamps_df)
plt.show()
