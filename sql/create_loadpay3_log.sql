CREATE TABLE ps_loadpay3_log (
    ps_date_pay timestamp NOT NULL DEFAULT current_timestamp,
    ps_abonent_kod varchar(24) NOT NULL,
    ps_service_kod varchar(24) NOT NULL,
    ps_sum numeric(10,2) NOT NULL,
    ps_lsp varchar(8) NOT NULL DEFAULT '',
    ps_date_load timestamp NOT NULL DEFAULT current_timestamp,
    ps_error varchar(100) NOT NULL DEFAULT '',
    ps_ok int NOT NULL DEFAULT 0
);


--- Для таблицы ps_loadpay3_log ---
CREATE INDEX ps_loadpay3_log_i0 ON ps_loadpay3_log USING btree (ps_date_pay,ps_abonent_kod,ps_service_kod,ps_sum);
CREATE INDEX ps_loadpay3_log_i1 ON ps_loadpay3_log USING btree (ps_date_load);
CREATE INDEX ps_loadpay3_log_i2 ON ps_loadpay3_log USING btree (ps_ok);
CREATE INDEX ps_loadpay3_log_i3 ON ps_loadpay3_log USING btree (ps_date_pay);
CREATE INDEX ps_loadpay3_log_i4 ON ps_loadpay3_log USING btree (ps_abonent_kod);
CREATE INDEX ps_loadpay3_log_i5 ON ps_loadpay3_log USING btree (ps_service_kod);


CREATE OR REPLACE VIEW ps_show_loadpay3 AS
SELECT
ps_date_pay AS date_pay,
ps_date_load AS date_load,
to_char(ps_date_pay,'DD.MM.YYYY') AS date_pay_str,
to_char(ps_date_load,'DD.MM.YYYY') AS date_load_str,
ps_lsp AS lsp,
CASE 
WHEN ps_service_kod='' THEN ''
ELSE (SELECT ps_services_name FROM ps_services WHERE ps_rec_id=ps_service_kod)
END AS service_name,
CASE WHEN ps_sum IS NULL THEN 0
ELSE ps_sum
END AS sum_pay,
btrim(to_char(ps_sum,'99999999.00')) AS sum_pay_str,
ps_error AS load_error,
ps_ok AS load_ok 
FROM
ps_loadpay3_log
ORDER BY ps_date_pay,ps_lsp;


GRANT SELECT,UPDATE,INSERT ON ps_loadpay3_log TO petrovich;
GRANT SELECT ON ps_show_loadpay3 TO petrovich;
