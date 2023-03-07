-- select a.ANIMAL_ID, a.ANIMAL_TYPE, a.NAME
-- from animal_ins a, animal_outs b
-- where a.animal_id = b.animal_id and
--     a.sex_upon_intake like 'Intact%' and
--     REGEXP_LIKE(b.sex_upon_outcome, '^Spayed|^Neutered')
-- order by a.animal_id

select a.ANIMAL_ID, a.ANIMAL_TYPE, a.NAME
from animal_ins a, animal_outs b
where a.animal_id = b.animal_id and
    a.sex_upon_intake != b.sex_upon_outcome
order by a.animal_id