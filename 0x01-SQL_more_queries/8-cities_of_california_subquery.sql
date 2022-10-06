-- Lists all the cities of California found in db hbtn_0d_usa
SELECT cities.id, cities.name FROM cities, states WHERE states.name = 'California' AND state.id ORDER BY cities.id
