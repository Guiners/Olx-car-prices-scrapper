from numpy import percentile


# napisac testy
class Format_data():

    @staticmethod
    def remove_outliers(data: list) -> list:
        q25 = percentile(data, 25)
        q75 = percentile(data, 75)
        iqr = q75 - q25
        cut_off = iqr * 1.5
        lower, upper = q25 - cut_off, q75 + cut_off
        outliers = [x for x in data if x < lower or x > upper]
        if len(outliers) == 0:
            return data
        else:
            outliers_removed = [x for x in data if x >= lower and x <= upper]
            return outliers_removed

    # testy
    @staticmethod
    def format_price(price: str) -> str:
        return int(price.replace(' ', '').strip('zł'))

    @staticmethod
    def format_number(list: list) -> int:
        number = str(list).replace(r'\n', '')
        return  int(number)
