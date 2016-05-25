CREATE TRIGGER in_acctradiususertrigger
  AFTER INSERT OR UPDATE
  ON radacct
  FOR EACH ROW
  EXECUTE PROCEDURE in_acctradiususer();
