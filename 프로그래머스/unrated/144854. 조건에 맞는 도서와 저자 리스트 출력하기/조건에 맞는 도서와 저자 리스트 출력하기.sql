SELECT book_id, author_name, to_char(published_date, 'YYYY-MM-DD')
from book natural join author
where category like '경제'
order by published_date