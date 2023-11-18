-- Consulta 1: Todos os posts, ordenados pela data, sendo o mais recente primeiro
SELECT * FROM oblog_post ORDER BY data_publicada DESC;

-- Consulta 2: Para um post com comentários, todos os seus comentários
SELECT * FROM oblog_comment WHERE post_id = 16;

-- Consulta 3: Para um post com comentários, todos os seus comentários, incluindo todas as colunas da tabela comentários (exceto o post_id), o título do post e sua data de publicação, renomeada para post_date
SELECT p.titulo AS post_title, p.data_publicada AS post_date, c.*
FROM oblog_post p 
INNER JOIN oblog_comment c ON p.id = c.post_id 
WHERE p.id = 16;

-- Consulta 4: Para uma categoria, todos os posts pertencentes a ela, incluindo as colunas da tabela de categoria e da tabela de posts
SELECT categ.nome AS nome_categoria, p.*
FROM oblog_post_categorias pc
INNER JOIN oblog_post p ON pc.post_id = p.id
INNER JOIN oblog_category categ ON pc.category_id = categ.id
WHERE pc.category_id = 1;

-- Consulta 5: Todas as categorias que possuem dois ou mais posts
SELECT categ.nome AS category_name, COUNT(pc.post_id) AS total_posts
FROM oblog_post_categorias pc
INNER JOIN oblog_category categ ON pc.category_id = categ.id
GROUP BY categ.nome
HAVING COUNT(pc.post_id) >= 2;