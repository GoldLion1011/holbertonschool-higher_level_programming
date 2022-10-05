-- Lists all records in second_table (db hbtn_0c_0)
SELECT score, name
    FROM second_table
    WHERE name IS NOT NULL
    ORDER BY score DESC;
