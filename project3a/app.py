from flask import Flask, render_template, request, jsonify
import webQuery
import json

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/result', methods=['POST'])
def result():
    symbol = request.form['symbol']
    chartType = request.form['chartType']
    timeSeries = request.form['timeSeries']
    startDate = request.form['startDate']
    endDate = request.form['endDate']
    
    # Process the form data as needed
    # For example, you can pass these values to a function that generates the chart data
    chart_data = webQuery.get_stock_data(symbol, chartType, timeSeries, startDate, endDate)
    if chart_data is None:
        return "No data available for the selected stock symbol."
    dates = chart_data['dates']
    prices = chart_data['prices']
    return render_template('result.html', symbol=symbol, dates=json.dumps(dates), prices=json.dumps(prices))

if __name__ == '__main__':
    app.run(debug=True)
