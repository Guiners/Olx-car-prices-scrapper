
class Calculate_statistic():
    @staticmethod
    def count_average(data: list) -> int:
        return round(sum(data) / len(data), 2)

    @staticmethod
    def count_min(data: list) -> int:
        return min(data)

    @staticmethod
    def count_max(data: list) -> int:
        return max(data)
