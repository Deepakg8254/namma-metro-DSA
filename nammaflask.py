from flask import Flask, render_template, request
from flask22 import *
app = Flask(__name__)

# Define the stations for the Purple Line
purple_line_stations = [
    'Majestic', 'Sir M. Visvesvaraya Station, Central College', 'Dr. B.R. Ambedkar Station, Vidhana Soudha',
    'Cubbon Park', 'Mahatma Gandhi Road', 'Trinity', 'Halasuru', 'Indiranagar', 'Swami Vivekananda Road',
    'Baiyappanahalli', 'Benniganahalli', 'K.R Pura', 'Singayyanapalya', 'Garudacharapalya', 'Hoodi', 'Seetharampalya',
    'Kundalahalli', 'Nallur Halli', 'Sri Sathya Sai Hospital', 'Pattandur Agrahara', 'Kadugodi Tree Park',
    'Hopefarm Channasandra', 'Whitefield(Kadugodi)', 'Krantivira Sangolli Rayanna Railway Station', 'Magadi Road', 'Balagangadaranatha Swamiji Station, Hosahalli',
    'Vijayanagar', 'Attiguppe', 'Deepanjali Nagar', 'Mysuru Road', 'Pantharapalya - Nayandahalli',
    'Rajarajeshwari Nagar', 'Jnanabharathi', 'Pattanagere', 'Kengeri Bus Terminal', 'Kengeri', 'Challaghatta'
]

# Define the stations for the Green Line
green_line_stations = [
    'Majestic', 'Mantri Square Sampige Road', 'Srirampura', 'Mahakavi Kuvempu Road', 'Rajajinagar', 'Mahalakshmi', 'Sandal Soap Factory', 'Yeshwanthpur', 'Goragunte Palya', 'Peenya', 'Peenya Industry', 'Jalahalli', 'Dasarahalli', 'Nagasandra'
    'Chickpet', 'Krishna Rajendra Market', 'National College', 'Lalbagh', 'South End Circle', 'Jayanagar', 'Rashtreeya Vidyalaya Road', 'Banashankari', 'Jaya Prakash Nagar', 'Yelachenahalli', 'Konanakunte Cross', 'Doddakallasandra', 'Vajarahalli', 'Thalaghattapura', 'Silk Institute'
]


@app.route('/', methods=['GET', 'POST'])
def index():
    global calculate_stops
    if request.method == 'POST':
        boarding_station = request.form['boarding_station']
        destination_station = request.form['destination_station']

        stops, ticket_price = calculate_stops(
            boarding_station, destination_station)

        return render_template('result.html', stops=stops, ticket_price=ticket_price)

    return render_template('index.html', purple_line_stations=purple_line_stations, green_line_stations=green_line_stations)


if __name__ == '__main__':
    app.run(debug=True)
