-- SELECT ('/home/grep/src/' || board_id || '/' || file_id || file_name) as FILE_PATH
-- from USED_GOODS_FILE ugf join USED_GOODS_BOARD ugb on ugf.BOARD_ID = ugb.BOARD_ID;

SELECT ('/home/grep/src/' || board_id || '/' || file_id || file_name || file_ext) as FILE_PATH
from used_goods_file natural join used_goods_board
where views = (select max(views) from used_goods_board)
order by file_id desc;