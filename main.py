import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

# Descargar los datos históricos del ETF QQQ y algunas acciones representativas del Nasdaq
symbols = ['AAPL', 'MSFT', 'GOOGL', 'AMZN', 'FB', 'QQQ']  # Puedes añadir más acciones si lo deseas
data = yf.download(symbols, start='2020-01-01', end='2024-01-01')['Adj Close']

# Calcular los retornos diarios
returns = data.pct_change()

# Definir parámetros
momentum_period = 60  # 3 meses (aprox. 60 días)
top_n = 5  # Seleccionamos las 5 mejores empresas

# Definir un DataFrame para almacenar las señales de rotación
rotation_signals = pd.DataFrame(index=returns.index, columns=symbols[:-1])

# Calcular rendimiento de momentum
for i in range(momentum_period, len(returns)):
    # Promedio de retornos en los últimos 3 meses
    momentum_scores = returns.iloc[i-momentum_period:i].mean()
    # Seleccionar los top N performers
    top_performers = momentum_scores.nlargest(top_n).index
    # Señal de compra para los mejores performers
    rotation_signals.iloc[i][top_performers] = 1

# Asumimos que QQQ es mantenido sin rotación
qqq_returns = returns['QQQ']

# Estrategia: Si el rendimiento promedio de las acciones seleccionadas es menor que el QQQ, se invierte en QQQ
rotated_portfolio_returns = (rotation_signals.shift(1) * returns[symbols[:-1]]).sum(axis=1) / top_n  # Promediamos top_n
comparison_returns = rotated_portfolio_returns.copy()
comparison_returns[rotated_portfolio_returns < qqq_returns] = qqq_returns[rotated_portfolio_returns < qqq_returns]  # Transferir al QQQ si el rendimiento es menor

# Graficamos el rendimiento acumulado de ambas estrategias
cumulative_rotated = (1 + comparison_returns).cumprod()
cumulative_qqq = (1 + qqq_returns).cumprod()

plt.figure(figsize=(10, 6))
plt.plot(cumulative_rotated, label='Cartera Rotada vs QQQ')
plt.plot(cumulative_qqq, label='QQQ (Nasdaq ETF)', linestyle='--')
plt.title('Comparación de Rendimiento: Cartera Rotada vs QQQ')
plt.legend()
plt.ylabel('Retorno acumulado')
plt.xlabel('Fecha')
plt.grid(True)
plt.show()
