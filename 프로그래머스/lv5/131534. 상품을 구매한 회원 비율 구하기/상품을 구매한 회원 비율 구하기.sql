SELECT to_char(sales_date,'YYYY') as year, 
       to_number(to_char(sales_date,'MM')) as month,
       count(distinct os.user_id) as puchased_users,
       round(count(distinct os.user_id)/(select count(distinct user_id) 
                                        from user_info 
                                        where to_char(joined, 'yyyy') like '2021'), 1) as puchased_ratio
from online_sale os JOIN user_info ui on os.user_id = ui.user_id
where to_char(ui.joined, 'yyyy') like '2021'
GROUP BY to_char(sales_date,'YYYY'), to_number(to_char(sales_date,'MM'))
ORDER BY year, month