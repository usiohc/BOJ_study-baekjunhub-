SELECT MEMBER_ID, MEMBER_NAME, GENDER, date_format(date_of_birth, "%Y-%m-%d") as date_for_birth
from member_profile
where tlno is not null and date_of_birth like '_____03%' and gender = 'W'
order by member_id;