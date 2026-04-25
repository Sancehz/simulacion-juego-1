from util.simulaciones import simular_multiples_juegos

SIMULACIONES = 100;
TIRADAS_POR_PARTIDA = 10;
MINIMO_PARA_GANAR = 5;

print(
	simular_multiples_juegos("resultados.csv", SIMULACIONES, TIRADAS_POR_PARTIDA, MINIMO_PARA_GANAR)
);