--- selections

-- descending list of names and part numbers where name contains 'hair'
SELECT name, part_num FROM parts WHERE name LIKE '%Hair%' ORDER BY part_num DESC;

-- list of sets between 1990 and 2015 where the name contains 'showdown'
SELECT * FROM sets WHERE set_name LIKE '%showdown%' AND year BETWEEN 1990 AND 2015;

-- list of part ids and names of parts containing the term 'bricks'
SELECT p.id, p.name FROM part_categories AS p WHERE p.name LIKE '%bricks%';


--- subqueries

-- list of sets where the theme id matches 'pirates' or 'star wars'
SELECT set_name FROM sets WHERE theme_id IN (SELECT id FROM themes WHERE name LIKE '%Pirates%' OR name LIKE '%Star Wars%');

-- full inventory parts table that only lists parts with more than one version
SELECT * FROM inventory_parts WHERE inventory_id IN (SELECT id FROM inventories WHERE version > 1);


--- manipulate values

-- list all sets where set name contains batman, concatenate '!!!' and uppercase names
SELECT CONCAT(UPPER(set_name), '!!!'), year FROM sets as s WHERE set_name LIKE '%Batman%';

-- descending list of top 20 quantity x 2 of parts where quantity is greater than one. 
SELECT quantity * 2 FROM inventory_parts WHERE quantity > 1 ORDER BY quantity DESC LIMIT 20;


--- dates

--list of set names with year and date corresponding to Jan 1st of the year 
SELECT set_name, year, MAKEDATE(year, 1) FROM sets;


---aggregates

-- total number of transparent colors
SELECT COUNT(is_trans) FROM colors WHERE is_trans = 1;

-- sum, average of all the parts from all sets since 2000
SELECT SUM(NUM_PARTS) FROM sets WHERE year >= 2000;
SELECT ROUND(AVG(NUM_PARTS), 2) FROM sets WHERE year >= 2000;

-- list average number of parts for each theme_id in sets
SELECT ROUND(AVG(NUM_PARTS), 2) as avg_num_parts, theme_id FROM sets GROUP BY theme_id;


---joins

-- join parts and part_categories on category id, display parts where name contains 'werewolf'
SELECT * FROM parts
JOIN part_categories
ON part_cat_id = id
WHERE parts.name LIKE '%Werewolf%';

-- inner join using aliasing 
SELECT p.part_num, p.name as part_name, p.part_cat_id, pc.name as part_cat_name FROM parts AS p
INNER JOIN part_categories AS pc
ON p.part_cat_id = pc.id
WHERE p.name LIKE '%Werewolf%';

-- counts number of rows for inner join (580,251)
SELECT COUNT(*) FROM colors as c
INNER JOIN inventory_parts as ip
ON c.id = ip.color_id;

-- counts number of rows for left join (580,255)
SELECT COUNT(*) FROM colors as c
LEFT JOIN inventory_parts as ip
ON c.id = ip.color_id;

-- counts number of rows for right join (580,251)
SELECT COUNT(*) FROM colors as c
RIGHT JOIN inventory_parts as ip
ON c.id = ip.color_id;

--- The above joins return two values, one for both the inner and right join, and the other for the left join. 
--- The difference tells us that the colors table contains values that don't exist in the inventories table, 
--- or that there are four colors that we do not have any inventory of. 