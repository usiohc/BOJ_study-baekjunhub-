SELECT animal_id, name
from animal_ins
where lower(name) like '%el%' and animal_type like 'Dog'
order by name;