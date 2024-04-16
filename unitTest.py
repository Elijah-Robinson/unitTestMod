import unittest

class TestProject3Inputs(unittest.TestCase):

    def test_symbol(self):
        symbol = 'AAPL'  # Example symbol
        self.assertTrue(symbol.isalpha() and symbol.isupper() and len(symbol) >= 1 and len(symbol) <= 7)

    def test_chart_type(self):
        chart_type = '1'  # Example chart type
        self.assertTrue(chart_type.isdigit() and (chart_type == '1' or chart_type == '2'))

    def test_time_series(self):
        time_series = '1'  # Example time series
        self.assertTrue(time_series.isdigit() and int(time_series) >= 1 and int(time_series) <= 4)

    def test_start_date(self):
        start_date = '2024-01-01'  # Example start date
        self.assertTrue(len(start_date) == 10 and start_date.count('-') == 2)

    def test_end_date(self):
        end_date = '2024-12-31'  # Example end date
        self.assertTrue(len(end_date) == 10 and end_date.count('-') == 2)

if __name__ == '__main__':
    unittest.main()
