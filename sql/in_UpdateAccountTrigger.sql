CREATE TRIGGER in_updateaccounttrigger
  AFTER UPDATE
  ON in_account
  FOR EACH ROW
  EXECUTE PROCEDURE in_changeuserlock();
