from math import radians, sin, cos, sqrt, atan2
from typing import Tuple, List, Dict, Union
from dataclasses import dataclass

@dataclass
class LogisticsResult:
    distancia: float
    tiempo_estimado: float
    litros_usados: float
    costo_combustible: float

class LogisticsCalculator:
    def __init__(self):
        self.R = 6371  # Radio de la Tierra en kilómetros

    def calcular_distancia(self, coord1: Tuple[float, float], coord2: Tuple[float, float]) -> float:
        """
        Calcula la distancia entre dos puntos geográficos usando la fórmula de Haversine.
        
        Args:
            coord1: Tupla con (latitud, longitud) del punto origen
            coord2: Tupla con (latitud, longitud) del punto destino
            
        Returns:
            float: Distancia en kilómetros
        """
        lat1, lon1 = radians(coord1[0]), radians(coord1[1])
        lat2, lon2 = radians(coord2[0]), radians(coord2[1])
        
        dlat = lat2 - lat1
        dlon = lon2 - lon1
        
        a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
        c = 2 * atan2(sqrt(a), sqrt(1-a))
        
        return self.R * c

    def calcular_viaje(
        self,
        origen: Tuple[float, float],
        destino: Tuple[float, float],
        carga: float,
        litros_km: float,
        precio_litro: float,
        velocidad: float
    ) -> LogisticsResult:
        """
        Calcula todos los parámetros de un viaje logístico.
        
        Args:
            origen: Tupla con (latitud, longitud) del punto origen
            destino: Tupla con (latitud, longitud) del punto destino
            carga: Peso de la carga en toneladas
            litros_km: Consumo de combustible en litros por kilómetro
            precio_litro: Precio del combustible por litro
            velocidad: Velocidad promedio en km/h
            
        Returns:
            LogisticsResult: Objeto con todos los resultados del cálculo
        """
        distancia = self.calcular_distancia(origen, destino)
        tiempo = distancia / velocidad
        litros_usados = distancia * litros_km
        costo_combustible = litros_usados * precio_litro
        
        return LogisticsResult(
            distancia=distancia,
            tiempo_estimado=tiempo,
            litros_usados=litros_usados,
            costo_combustible=costo_combustible
        )

    def parse_coordenadas(self, coord_str: str) -> Tuple[float, float]:
        """
        Convierte una cadena de coordenadas en formato "lat,lon" a una tupla de floats.
        
        Args:
            coord_str: String con coordenadas en formato "lat,lon"
            
        Returns:
            Tuple[float, float]: Tupla con (latitud, longitud)
        """
        try:
            lat, lon = map(float, coord_str.strip().split(","))
            return (lat, lon)
        except Exception as e:
            raise ValueError(f"Formato de coordenadas inválido: {coord_str}. Use formato 'lat,lon'") from e 