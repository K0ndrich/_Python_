
-- Вывод значений указаных колонок из указаной таблици , выводяться все записи из базы
SELECT my_column1 , my_column2 FROM my_table


-- Вывод значений всех колонок из указаной таблции
SELECT * FROM my_table


-- as дает новое имя(псевдоним) для колонки, теперь нужно ображаться к етой колонке по новому имени только внутри выборки
SELECT my_column as new_name FROM my_table


-- DISTINCT выводит только уникальные значения из указаной колонки
SELECT DISTINCT my_column FROM my_table


-- Возвращает только те записи со всеми колонками, где WHERE возвращает True
SELECT * FROM my_table
WHERE id = 2


-- GROUP BY групирует сума значений указаной колонки для каждой записи по колонке ID 
SELECT SUM(my_column) FROM my_table
GROUP BY my_table.my_column_id


-- HAVING тоже самое что WHERE только используеться для GROUP BY
-- HAVING не работает с псевдонимами колонок, только с оригинальными названиями
SELECT SUM(my_column) FROM my_table
GROUP BY my_table.my_column_id
HAVING SUM(my_column)


-- ORDER BY удет выводить записи по возростанию или убыванию значений в указаной колонке  my_column
SELECT my_column FROM my_table
ORDER BY my_column DESC   -- от большего к меньшему
-- ORDER BY my_column ASC -- от меньшего к большему


-- LIMIT указывает количество записей в виборке
SELECT my_column FROM my_table
LIMIT 5 
-- LIMIT 5 OFFSET 3 -- OFFSET пропускает 3 превые записи из начальной выборки