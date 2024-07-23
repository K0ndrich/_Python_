--   INSERT   ----------------------------------------------------------------------------------------------------------------------------
-- Добавление новой записи в нашу таблицу my_table. 
-- Последовательность колонок и значений очень важна
INSERT INTO my_table
VALUES ('my_value1' , 'my_value2')

-- Вставка значений только по указаными колонкам
INSERT INTO my_table (my_column1 , my_column2)
VALUES ('my_value1' , 'my_value2')

-- Добавление сразу несколько запись в базу данных
INSERT INTO my_table 
VALUES
('my_value1' , 'my_value2'),
('my_value1' , 'my_value2'),
('my_value1' , 'my_value2'),
('my_value1' , 'my_value2');


--   UPDATE   ------------------------------------------------------------------------------------------------------------------------------------
-- Изменение всех существующий значений колонки my_column на новое значений new_value
UPDATE my_table 
SET my_column = "new_value"

-- Изменение значения указаной колонки только для для той записи где WHERE возвращает True
UPDATE my_table 
SET my_column1 = "new_value" -- new_value новое значение только для етой колонки етой записи
WHERE my_column1 = "value"


UPDATE my_table 
SET my_column2 = "new_value"
WHERE my_column1 = "value"


--   DELETE   -------------------------------------------------------------------------------------------------------------------------------------------
-- Удаление Записей из базы
-- Удаляет только те записи , где WHERE возвращает True
DELETE FROM my_table
WHERE id = 2

DELETE FROM my_table
WHERE id = 2 OR WHERE id = 3
