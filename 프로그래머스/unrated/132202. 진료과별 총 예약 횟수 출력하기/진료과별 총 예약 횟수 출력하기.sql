SELECT MCDP_CD as "진료과코드", count(*) as "5월예약건수"
from appointment
where to_char(apnt_ymd, 'YYYY-MM') like '2022-05'
group by mcdp_cd
order by "5월예약건수", "진료과코드"
