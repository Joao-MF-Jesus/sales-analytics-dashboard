 Sobre o Projeto
Este projeto tem como objetivo analisar dados de um e-commerce brasileiro, com foco em vendas, comportamento regional e eficiência logística.
A solução envolve a construção de um pipeline de dados com Python para tratamento e modelagem, seguido da criação de um dashboard interativo no Power BI.


Objetivos
Analisar a evolução do faturamento ao longo do tempo
Identificar os estados com maior volume de vendas
Avaliar o ticket médio dos pedidos
Investigar a eficiência logística (tempo de entrega e custo de frete)

Tecnologias Utilizadas
Python (Pandas) → tratamento e transformação dos dados
SQL (conceitos) → estruturação lógica dos dados
Power BI → criação do dashboard interativo

Pipeline de Dados
Extração
Dados provenientes do dataset público Olist
Transformação (Python)
Filtragem de pedidos entregues
Tratamento de valores nulos
Cálculo de métricas:
Faturamento
Ticket médio
Tempo de entrega
Proporção de frete (freight_ratio)
Carga
Exportação para CSV tratado (dataset_tratado.csv)
Importação no Power BI

 Dashboard
O dashboard foi estruturado para responder perguntas de negócio de forma clara e objetiva.
 KPIs principais
Faturamento total
Ticket médio
Total de pedidos
Tempo médio de entrega

 Análises
Evolução do faturamento
Crescimento consistente ao longo de 2017
Estabilização no período seguinte
Faturamento por estado
Forte concentração em São Paulo
RJ e MG como principais mercados secundários
Pedidos por estado
Distribuição semelhante ao faturamento
Indício de concentração regional de clientes
Logística
Frete Médio (% do pedido)
Varia significativamente entre estados
Indica impacto logístico relevante em algumas regiões
Tempo médio de entrega por estado
Diferenças claras entre regiões
Possível influência de distância e infraestrutura

Principais Insights
O estado de São Paulo concentra a maior parte do faturamento e volume de pedidos
Existe uma forte concentração regional nas vendas
O custo de frete pode representar uma parcela relevante do pedido em alguns estados
A eficiência logística varia significativamente entre regiões

Conclusão
O projeto demonstra a capacidade de:
Construir pipelines de dados com Python
Modelar e tratar dados para análise
Criar dashboards claros e orientados a negócio
Extrair insights relevantes para tomada de decisão

📎 Autor
João marcelo ferreira de jesus

