-- Lists all cities contained in db hbtn_0d_usa
SELECT cities.id, cities.name, states.name
    FROM cities
    LEFT JOIN states
    ON states_id = states.id
    ORDER BY cities.id ASC
     