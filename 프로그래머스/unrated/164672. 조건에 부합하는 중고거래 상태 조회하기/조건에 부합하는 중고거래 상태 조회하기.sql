SELECT board_id, writer_id, title, price, case when STATUS = 'SALE' then '판매중'
                                               when STATUS = 'DONE' then '거래완료'
                                               when STATUS = 'RESERVED' then '예약중'
                                               end as STATUS
from used_goods_board
where CREATED_DATE like '2022-10-05'
order by board_id Desc