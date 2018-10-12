create or replace function SET_gdprjava_2040010  (I_SET_ID int)
returns int
as
$body$
declare
ERRORCODE	INT := 0;
begin
/* 
Set name SET_gdprjava_Collection

*/
 
  insert into SET_Contents (SetId, ObjectId)
   select distinct I_SET_ID, o.OBJECT_ID
  from CTT_OBJECT_APPLICATIONS o where o.OBJECT_TYPE in 
  		(select IdTyp from TypCat where IdCatParent in                   
  				(select IdCat from Cat where CatNam = 'GDPRViolation_CustomMetrics'));
  
return ERRORCODE;
end;
$body$
LANGUAGE plpgsql
/

