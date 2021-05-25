-- Changelog for version 01
-- INDEX


-- TABLE COMMUNITY RLS POLICY UPDATE
DROP POLICY IF EXISTS community_rls_technician ON community;
CREATE POLICY community_rls_technician ON community
 	FOR SELECT
	USING ((community.id = (SELECT user_community.community_id FROM user_community WHERE current_user = user_name)) 
		   OR (current_user = 'reader'));
		   
-- TABLE FEATURE BASE UPDATE
ALTER TABLE feature_base ADD COLUMN inspection_date DATE;
ALTER TABLE feature_base RENAME COLUMN structure_id TO parent_feature_id;

