SELECT TOP 80000 s.specObjID,p.z,p.objid,p.ra,p.dec,p.u,p.g,p.r,p.i,s.z as redshift
FROM PhotoObj AS p
JOIN SpecObj AS s ON s.bestobjid = p.objid
WHERE 
  p.u BETWEEN 0 AND 19.6
  AND p.g BETWEEN 0 AND 20 AND s.class = 'QSO'
