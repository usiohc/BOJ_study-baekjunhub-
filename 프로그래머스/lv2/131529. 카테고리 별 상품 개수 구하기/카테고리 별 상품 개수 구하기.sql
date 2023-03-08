SELECT substr(PRODUCT_CODE, 0, 2) as category, count(*)
from product
group by substr(PRODUCT_CODE, 0, 2)
order by category