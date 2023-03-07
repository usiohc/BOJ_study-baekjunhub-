-- SELECT product_code, (price*sales_amount) as sales
-- from product natural join (select product_id, sum(sales_amount)
--                            from offline_sale
--                            group by product_id having sum(sales_amount))
-- order by sales desc, product_code

select product_code, price*s_a as sales
from product natural join (select product_id, sum(sales_amount) as s_a
                           from offline_sale
                           group by product_id)
order by sales desc, product_code 