'''4.1 Объединить таблицы'''
SELECT *
FROM customer
FULL JOIN city
ON city_code = city_id
'''4,2 Объединить таблицы по таблице Заказчики'''
SELECT *
FROM customer
RIGHT JOIN city
ON city_code = city_id
'''4.3 Объединить таблицы по таблицк Города'''
SELECT *
FROM city
RIGHT JOIN customer
ON city_code = city_id