SELECT to_number(to_char(datetime, 'HH24')) as hour, count(datetime)
from animal_outs
where to_number(to_char(datetime, 'HH24')) between 9 and 19
group by to_number(to_char(datetime, 'HH24'))
order by hour

-- select to_char(datetime, 'HH24')
-- from animal_outs