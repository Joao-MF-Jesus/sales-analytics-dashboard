import kagglehub
from kagglehub import KaggleDatasetAdapter

df = kagglehub.load_dataset(
    KaggleDatasetAdapter.PANDAS,
    "olistbr/brazilian-ecommerce",
    "olist_orders_dataset.csv"
)

print(df.head())