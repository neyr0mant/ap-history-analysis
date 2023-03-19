from start_analysis import StartАnalysis

class AnalysisAP(StartАnalysis):
    print()

    def get_distance(self, lat1, lon1, lat2, lon2):
        import math
        def to_radians(degrees):
            return degrees * math.pi / 180
        r = 6371  # Радиус Земли в километрах
        # Переводим градусы в радианы
        lat1 = to_radians(lat1)
        lon1 = to_radians(lon1)
        lat2 = to_radians(lat2)
        lon2 = to_radians(lon2)
        # Вычисляем разницу широт и долгот
        delta_lat = lat2 - lat1
        delta_lon = lon2 - lon1
        # Вычисляем расстояние по формуле гаверсинуса
        a = math.sin(delta_lat / 2) ** 2 + math.cos(lat1) * math.cos(lat2) * math.sin(delta_lon / 2) ** 2
        c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
        return r * c