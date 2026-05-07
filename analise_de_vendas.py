import pandas as pd

# ==============================
# 1. EXTRAÇÃO
# ==============================

def load_df(file):
    return pd.read_csv(f"dataset/{file}")

orders = load_df("olist_orders_dataset.csv")
order_items = load_df("olist_order_items_dataset.csv")
payments = load_df("olist_order_payments_dataset.csv")
customers = load_df("olist_customers_dataset.csv")
reviews = load_df("olist_order_reviews_dataset.csv")

# ==============================
# 2. VALIDAÇÃO INICIAL
# ==============================

print("Orders:", orders.shape)
print("Items:", order_items.shape)
print("Payments:", payments.shape)

# ==============================
# 3. FILTRO DE PEDIDOS VÁLIDOS
# ==============================

orders = orders[orders['order_status'] == 'delivered']

# ==============================
# 4. AGREGAÇÕES (EVITAR DUPLICIDADE)
# ==============================

# pagamentos por pedido
payments_agg = payments.groupby('order_id')['payment_value'].sum().reset_index()

# itens por pedido (VALOR + FRETE CORRETO)
items_agg = order_items.groupby('order_id').agg({
    'price': 'sum',
    'freight_value': 'sum'
}).reset_index()

items_agg['total_order_value'] = items_agg['price'] + items_agg['freight_value']

# ==============================
# 5. MERGE FINAL
# ==============================

reviews_agg = reviews.groupby('order_id')['review_score'].mean().reset_index()

df = orders.merge(payments_agg, on='order_id', how='left') \
           .merge(items_agg, on='order_id', how='left') \
           .merge(customers, on='customer_id', how='left') \
           .merge(reviews_agg, on='order_id', how='left')

# ==============================
# 6. TRATAMENTO
# ==============================

df['order_purchase_timestamp'] = pd.to_datetime(df['order_purchase_timestamp'])
df['order_delivered_customer_date'] = pd.to_datetime(df['order_delivered_customer_date'])

# tempo
df['year_month'] = df['order_purchase_timestamp'].dt.strftime('%Y-%m')

df['delivery_time'] = (
    df['order_delivered_customer_date'] - df['order_purchase_timestamp']
).dt.days

df.loc[df['delivery_time'] < 0, 'delivery_time'] = None

# tratar nulos importantes
df['delivery_time'] = df['delivery_time'].fillna(df['delivery_time'].median())

# ==============================
# 7. MÉTRICAS
# ==============================

# faturamento total
faturamento = df['payment_value'].sum()

# ticket médio (forma robusta)
ticket_medio = df.groupby('order_id')['payment_value'].sum().mean()

# total de pedidos
total_pedidos = df['order_id'].nunique()

# faturamento mensal
faturamento_mensal = df.groupby('year_month')['payment_value'].sum().reset_index()

# ==============================
# 8. FEATURE ENGINEERING
# ==============================

# proporção de frete
df['freight_ratio'] = df['freight_value'] / df['payment_value']

df.loc[df['payment_value'] <= 0, 'freight_ratio'] = None
df.loc[df['freight_ratio'] > 2, 'freight_ratio'] = None
# ==============================
# 9. INSIGHTS BASE
# ==============================

insight_entrega = df.groupby('review_score')['delivery_time'].mean()

analise_estado = df.groupby('customer_state').agg({
    'payment_value': 'sum',
    'order_id': 'count',
    'freight_value': 'mean'
}).sort_values(by='payment_value', ascending=False)

clientes_recorrentes = df.groupby('customer_id')['order_id'].nunique()

# ==============================
# 10. DATASET FINAL PARA BI
# ==============================

df_final = df[[
    'order_id',
    'customer_state',
    'year_month',
    'payment_value',
    'total_order_value',
    'freight_value',
    'freight_ratio',
    'delivery_time',
    'review_score'
]]

df_final.to_csv("dataset_tratado.csv", index=False)

# ==============================
# 11. OUTPUT RESUMO
# ==============================

print("\n=== KPIs ===")
print("Faturamento:", faturamento)
print("Ticket médio:", ticket_medio)
print("Total pedidos:", total_pedidos)

print("\n=== Entrega x Avaliação ===")
print(insight_entrega.head())

print("\n=== Top Estados ===")
print(analise_estado.head())
print(df['freight_ratio'].describe())