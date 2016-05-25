CREATE OR REPLACE FUNCTION in_acctradiususer()
  RETURNS "trigger" AS
'

/*

	пЮЯВЕР НОКЮРШ ГЮ ОНРПЕАКЕММШИ РПЮТХЙ, НТНПЛКЕМХЕ СДЕПФЮМХИ,
 	НРЙКЧВЕМХЕ Б ЯКСВЮЕ ДНЯРХФЕМХЪ НРПХЖЮРЕКЭМНЦН АЮКЮМЯЮ

*/



DECLARE

---- оЕПЕЛЕММШЕ -----

--- йНД СВЕРМНИ ГЮОХЯХ ЮАНМЕМРЮ ---
user_kod varchar(24);

--- яРНХЛНЯРЭ 1ла РПЮТХЙЮ ---
cost_1mb numeric(8,2);

--- яСЛЛЮ СДЕПФЮМХЪ ГЮ РПЮТХЙ ГЮ ЩРС ЯЕЯЯХЧ ---
sum_ses numeric(10,2);

--- йНД Internet СЯКСЦХ ---
internet_kod varchar(24);

--- йНД ГЮОХЯХ КХЖЕБНЦН ЯВЕРЮ INTERNET СЯКСЦХ ЮАНМЕМРЮ ---
kod_ls varchar(24);

--- йНД РЮПХТЮ РЮПТХЙЮ, ОН ЙНРНПНЛС ПЮАНРЮЕР ЮАНМЕМР ---
kod_tarif int4;

--- яСЛЛЮ МЮ КХЖЕБНЛ ЯВЕРЕ ДН СДЕПФЮМХЪ ---
sum_before numeric(10,2);

--- яСЛЛЮ МЮ КХЖЕБНЛ ЯВЕРЕ ОНЯКЕ СДЕПФЮМХЪ ---
sum_after numeric(10,2);

--- яСЛЛЮ НАЫЕЦН АЮКЮМЯЮ ---
balans numeric(10,2);



BEGIN 

--- еЯКХ ЯЕЯЯХЪ ГЮБЕПЬЕМЮ Х ЙНКХВЕЯРБН НЙРЕРНБ ОПХЯСРЯРБСЕР ---
IF (NEW.acctstoptime IS NOT NULL) AND (NEW.acctoutputoctets IS NOT NULL) THEN

	--- нОПЕДЕКЕМХЕ ЙНДЮ INTERNET СЯКСЦХ ---
	SELECT INTO internet_kod ps_rec_id FROM ps_services WHERE btrim(ps_services_name)=\'INTERNET\';

	--- нОПЕДЕКЕМХЕ ЙНДЮ СВЕРМНИ ГЮОХЯХ ЮАНМЕМРЮ, ЙНДЮ РЮПХТЮ ---
	SELECT INTO user_kod,kod_tarif in_rec_id,in_cost_kod FROM in_account WHERE btrim(in_user_login)=btrim(NEW.username);

	--- нОПЕДЕКЕМХЕ ЙНДЮ ГЮОХЯХ КХЖЕБНЦН ЯВЕРЮ ЮАНМЕМРЮ ---
	SELECT INTO kod_ls ps_rec_id FROM ps_ls WHERE ps_abonent_kod=user_kod AND ps_service_kod=internet_kod;

	--- нОПЕДЕКЕМХЕ ЯРНХЛНЯРХ 1ла ДКЪ ЩРНЦН ЙНМЙПЕРМНЦН ЮАНМЕМРЮ ---
	SELECT INTO cost_1mb t.in_cost_1mb FROM in_traf_cost t, in_account u WHERE u.in_cost_kod=t.in_rec_id AND u.in_rec_id=user_kod;
	
	--- нОПЕДЕКЕМХЕ ЯСЛЛШ СДЕПФЮМХЪ ГЮ РПЮТХЙ ГЮ ЩРС ЯЕЯЯХЧ ---
	sum_ses := NEW.acctoutputoctets/1024/1024*cost_1mb+0.1;

	--- яСЛЛЮ МЮ КХЖЕБНЛ ЯВЕРЕ ДН СДЕПФЮМХЪ ---
	SELECT INTO sum_before ps_ls_sum FROM ps_ls WHERE ps_rec_id=kod_ls;

	--- яСЛЛЮ МЮ КХЖЕБНЛ ЯВЕРЕ, ЙНРНПЮЪ ДНКФМЮ АШРЭ ОНЯКЕ СДЕПФЮМХЪ ---
	sum_after := sum_before - sum_ses;

	--- тХЙЯЮЖХЪ ХГЛЕМЕМХИ Б РЮАКХЖЮУ ---
	UPDATE ps_ls SET ps_ls_sum=sum_after WHERE ps_rec_id=kod_ls;
	SELECT INTO balans sum(ps_ls_sum) FROM ps_ls WHERE ps_abonent_kod=user_kod;
	UPDATE ps_abonent_list SET ps_balans_total=balans WHERE ps_rec_id=user_kod;
	INSERT INTO in_pay_traf (in_rec_abonent,in_sum,in_sum_before,in_sum_after,in_traf,in_traf_cost) VALUES(user_kod,sum_ses,sum_before,sum_after,NEW.acctoutputoctets/1024/1024,kod_tarif);
	UPDATE in_account SET in_ip_client=NEW.callingstationid,in_last_time=NEW.acctstarttime WHERE in_rec_id=user_kod;

	--- еЯКХ КХЖЕБНИ ЯВЕР НРПХЖЮРЕКЭМШИ МЕНАУНДХЛН ГЮАКНЙХПНБЮРЭ СВЕРМСЧ ГЮОХЯЭ ---
	IF sum_after<0 THEN
		UPDATE in_account SET in_rec_delete=\'delete\' WHERE in_rec_id=user_kod;
	END IF;

END IF;

RETURN NEW;

END;'
  LANGUAGE 'plpgsql';
