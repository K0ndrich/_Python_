-- В етом файле храняться ограничения для колонок

-- можно передавать занчение NULL
my_column INT NULL

-- нельзя перевавать NULL
my_column INT NOT NULL 

-- может ханить только уникальныне значения
my_column INT UNIQUE 

-- если не указываее значение, тогда вставляеться значение по умолчанию
мy_column INT DEFAULT 3 

-- вписыват значение, если условие TRUE
my_column INT CHECK my_value > 5 