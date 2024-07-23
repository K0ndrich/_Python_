--   JOIN == INNER JOIN   -------------------------------------------------------------------------------

-- ON нужно указывать колонки в обеих таблицах, по которым связываються таблици 
-- JOIN == INNER JOIN включаем в виборку только те данные, только когда условие ON совпадает
-- Если условние ON c одной из любих стронок, тогда запись не попадает в выборку
SELECT my_table1.my_column1 , my_column , my.my_table2.my_column2 FROM my_table1
JOIN my_table2 ON my_table2.my_column2 = my_table1.my_column1

-- Все соединения ->
--  INNER JOIN == JOIN
--  LEFT JOIN
--  RIGHT JOIN
--  FULL JOIN
