CREATE OR REPLACE FUNCTION ps_AddSer2TPlan(varchar(30),varchar(30),numeric(10,2)) RETURNS text

AS 
$BODY$

DECLARE


ser_ ALIAS FOR $1;

tp_ ALIAS FOR $2;

co_ ALIAS FOR $3;



kod_ser varchar(24);

kod_tp varchar(24);


a int4;

b int4;

n int4;

nn int4;


i int4;


row_data ps_abonent_list%ROWTYPE;


row_data2 ps_abonent_list%ROWTYPE;



BEGIN 


SELECT INTO a count(*) FROM ps_services WHERE btrim(ps_services_name)=btrim(ps_RusUpper(ser_));
IF a=1 THEN
SELECT INTO kod_ser ps_rec_id FROM ps_services WHERE btrim(ps_services_name)=btrim(ps_RusUpper(ser_));
ELSE
RETURN 'CANT FIND KOD THIS SERVICE';
END IF;


SELECT INTO b count(*) FROM ps_tarif_plan_name WHERE btrim(ps_tarif_plan_name)=btrim(ps_RusUpper(tp_));
IF b=1 THEN
SELECT INTO kod_tp ps_rec_id FROM ps_tarif_plan_name WHERE btrim(ps_tarif_plan_name)=btrim(ps_RusUpper(tp_));
ELSE
RETURN 'CANT FIND KOD THIS TARIF PLAN';
END IF;


SELECT INTO nn count(*) FROM ps_tarif_plan WHERE ps_tarif_plan_kod=kod_tp AND ps_service_kod=kod_ser AND ps_rec_delete='delete';

IF nn=1 THEN
UPDATE ps_tarif_plan SET ps_rec_delete='' WHERE ps_tarif_plan_kod=kod_tp AND ps_service_kod=kod_ser;

	IF btrim(ser_)='INTERNET' THEN

		FOR row_data2 IN SELECT * FROM ps_abonent_list WHERE ps_tarif_plan=kod_tp AND ps_rec_delete<>'delete' LOOP
		PERFORM in_CheckInternet(row_data2.ps_rec_id);
		END LOOP;
	END IF;


RETURN 'OK';
END IF;



SELECT INTO n count(*) FROM ps_tarif_plan WHERE ps_tarif_plan_kod=kod_tp AND ps_service_kod=kod_ser AND ps_rec_delete<>'delete';




IF n=0 THEN

	IF btrim(ser_)='INTERNET UNLIM' THEN
		INSERT INTO ps_tarif_plan(ps_rec_id,ps_tarif_plan_kod,ps_type_count,ps_cost,ps_service_kod) VALUES(ps_GenKeyCheck(2),kod_tp,'day_before',co_,kod_ser);
	ELSE
		INSERT INTO ps_tarif_plan(ps_rec_id,ps_tarif_plan_kod,ps_type_count,ps_cost,ps_service_kod) VALUES(ps_GenKeyCheck(2),kod_tp,'month_before',co_,kod_ser);
	END IF;

FOR row_data IN SELECT * FROM ps_abonent_list WHERE ps_tarif_plan=kod_tp LOOP

SELECT INTO i count(*) FROM ps_ls WHERE ps_abonent_kod=row_data.ps_rec_id AND ps_service_kod=kod_ser;

IF i=0 THEN
INSERT INTO ps_ls(ps_rec_id,ps_abonent_kod,ps_service_kod) VALUES(ps_GenKeyCheck(5),row_data.ps_rec_id,kod_ser);
END IF;
END LOOP;





--	IF btrim(ser_)='INTERNET' THEN
--		FOR row_data2 IN SELECT * FROM ps_abonent_list WHERE ps_tarif_plan=kod_tp AND ps_rec_delete<>'delete' LOOP
--		PERFORM in_CheckInternet(row_data2.ps_rec_id);
--		END LOOP;
--	END IF;







RETURN 'OK';

ELSE

RETURN 'CANT ADD THIS SERVICE';


END IF;






END;$BODY$

LANGUAGE 'plpgsql'






