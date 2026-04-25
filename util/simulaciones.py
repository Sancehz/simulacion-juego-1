from random import random

# Esta funcion simula un juego dadas las especificas tiradas de moneda y minimo para ganar
# Retorna datos relevantes al resultado como un dict
def simular_juego_moneda(tiradas: int, min_ganar: int) -> dict:
	escalon_actual: int = 0;
	tirada_ganadora: int = -1;

	for tirada in range(tiradas):
		resultado: bool = random() < 0.5; # 50% probabilidad

		if resultado:
			escalon_actual += 1;

		if (escalon_actual >= min_ganar) and (tirada_ganadora == -1):
			tirada_ganadora = tirada;

	return {
		"ganado": (tirada_ganadora != -1),
		"tirada_ganadora": tirada_ganadora,
		"escalon_final": escalon_actual,
	};

def simular_multiples_juegos(csv_path: str, simulaciones: int, tiradas_por_juego: int = 10, min_ganar_por_juego: int = 5) -> dict:
	total_ganadas: int = 0;
	suma_tiradas_ganadoras: int = 0;
	suma_escalones_finales: int = 0;

	with open(csv_path, "w") as f:
		f.write("num_partida, ganado, tirada_ganadora, escalon_final\n")
		for simulacion in range(simulaciones):
			resul: dict = simular_juego_moneda(tiradas_por_juego, min_ganar_por_juego);

			if resul["ganado"]:
				total_ganadas += 1;
				suma_tiradas_ganadoras += resul["tirada_ganadora"];

			suma_escalones_finales += resul["escalon_final"];

			f.write(f'{simulacion}, {("SI" if resul["ganado"] else "NO")}, {resul["tirada_ganadora"] if (resul["tirada_ganadora"] != -1) else ""}, {resul["escalon_final"]}\n');

	return {
		"total_ganadas": total_ganadas,
		"porcentaje_ganadas": float(total_ganadas) / float(simulaciones),
		"promedio_tirada_ganadora": float(suma_tiradas_ganadoras) / float(total_ganadas),
		"promedio_escalon_final": float(suma_escalones_finales) / float(simulaciones),
	};