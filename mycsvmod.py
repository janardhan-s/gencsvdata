file_csv_columns = {
	"s.no":{"position": 0},
	"Issuekey":{"position": 1, "gen_col":{"ncol_name":"STORY ID", "npos":3}},
	"Issueid":{"position": 2},
	"custom field(epic link)":{"position": 3, "gen_col":{"ncol_name":"EPIC ID", "npos":1}},
	"Ename":{"position": 4},
	"Esdate":{"position": 5, "gen_col":{"ncol_name":"STORY\nPLANNED\nSTART", "npos":7}},
	"ETdate":{"position": 6, "gen_col":{"ncol_name":"STORY\nPLANNED\nEND", "npos":8}},
	"EASdate":{"position": 7, "gen_col":{"ncol_name":"STORY\nACTUAL\nSTART", "npos":13}},
	"EAEdate":{"position": 8, "gen_col":{"ncol_name":"STORY\nACTUAL\nEND", "npos":14}},
	"Assignee":{"position": 9, "gen_col":{"ncol_name": "ASSIGNED TO", "npos":5}},
	"progrss":{"position": 10, "gen_col":{"nclo_name":"STROY\nEFFORT\nCOMPLETION %", "npos":15}},
	"custom field(story points)":{"position": 11, "gen_col":{"ncol_name":"ESTIMATED\nSTORY\nPOINTS", "npos":6}},
	"Original Estimate":{"position": 12, "gen_col":{"ncol_name":"TIME SPENT\n(in SEC'S)", "npos":10}},
	"Time spent":{"position": 13},
	"remaining Estimate":{"position": 15},
	"original hours":{"position": 14, "gen_col":{"ncol_name":"EFFORT\nCONSUMED\n(inHOURS)", "npos":11}},
	"spenthours":{"position": 17, "gen_col":{"ncol_name":"ESTIMATED\nEFFORT\n(inHOURS)", "npos":9}},
	"remaining hours":{"position": 16, "gen_col":{"ncol_name":"PENDING\nEFFORT\n(inHOURS)", "npos":12}},
	"sprint":{"position": 18, "gen_col":{"ncol_name":"SPRINT ID", "npos":2}},
	"sprint2":{"position": 19},
	"sprint3":{"position": 20},
	"summary":{"position": 21, "gen_col":{"nclo_name":"STORY DISCRIPTION", "npos":4}},
    "story_schedule_progress":{"gen_col": {"ncol_name" : "STORY\nSCHEDULE\nPROGRESS % ","npos": 22}},
    "story_schedule_overrun":{"gen_col": {"ncol_name": "STORY\nSCHEDULE\nOVERRUN %", "npos": 23}}
}

epics_of_columns = {
	"s.num": {"position":0},
	"Custom field (Epic Link)": {"position": 1},
	"Ename": {"position": 2},
	"ESdate": {"position":3},
	"ETdate":{"position":4},
	"EASDate": {"position":5},
	"EAEDate": {"position": 6}
}
def get_stry_sch_progress():
    return file_csv_columns["story_schedule_progress"]["gen_col"]["ncol_name"]
def get_stry_sch_progress_pos():
    return file_csv_columns["story_schedule_progress"]["gen_col"]["npos"]    
def get_stry_sch_progress_run():
    return file_csv_columns["story_schedule_overrun"]["gen_col"]["ncol_name"]
def get_stry_sch_progress_run_pos():
    return file_csv_columns["story_schedule_overrun"]["gen_col"]["npos"]    
    
def get_new_sprint_name():
    return file_csv_columns["sprint"]["gen_col"]["ncol_name"]
def get_new_sprint_pos():
    return file_csv_columns["sprint"]["gen_col"]["npos"]    
def get_new_epcid_col_name():
    return file_csv_columns["custom field(epic link)"]["gen_col"]["ncol_name"]
def get_new_epcid_pos():
    return file_csv_columns["custom field(epic link)"]["gen_col"]["npos"]
def get_new_srtyid_name():
    return file_csv_columns["Issuekey"]["gen_col"]["ncol_name"]
def get_new_stryid_pos():
    return file_csv_columns["Issuekey"]["gen_col"]["npos"]
def get_new_stry_plan_strt_name():
    return file_csv_columns["Esdate"]["gen_col"]["ncol_name"]
def get_new_stry_plan_strt_pos():
    return file_csv_columns["Esdate"]["gen_col"]["npos"]    
def get_new_stry_plan_end_name():
    return file_csv_columns["ETdate"]["gen_col"]["ncol_name"]
def get_new_stry_plan_end_pos():
    return file_csv_columns["ETdate"]["gen_col"]["npos"]    
def get_new_stry_act_strt_name():
    return file_csv_columns["EASdate"]["gen_col"]["ncol_name"]
def get_new_stry_act_strt_pos():    
    return file_csv_columns["EASdate"]["gen_col"]["npos"]
def get_new_stry_act_end_name():
    return file_csv_columns["EAEdate"]["gen_col"]["ncol_name"]
def get_new_stry_act_end_pos():    
    return file_csv_columns["EAEdate"]["gen_col"]["npos"]
def get_new_assign_name():
    return file_csv_columns["Assignee"]["gen_col"]["ncol_name"]
def get_new_assign_pos():
    return file_csv_columns["Assignee"]["gen_col"]["npos"]    
def get_new_stry_effort_comp_name():
    return file_csv_columns["progrss"]["gen_col"]["nclo_name"]
def get_new_stry_effort_comp_pos():
    return file_csv_columns["progrss"]["gen_col"]["npos"]    
def get_new_est_stry_pnts_name():
    return file_csv_columns["custom field(story points)"]["gen_col"]["ncol_name"]
def get_new_est_stry_pnts_pos():
    return file_csv_columns["custom field(story points)"]["gen_col"]["npos"] 
def get_new_time_spnt_name():
    return file_csv_columns["Original Estimate"]["gen_col"]["ncol_name"]
def get_new_time_spnt_pos():
    return file_csv_columns["Original Estimate"]["gen_col"]["npos"]   
def get_new_effort_cons_hrs_name():
    return file_csv_columns["original hours"]["gen_col"]["ncol_name"]
def get_new_effort_cons_hrs_pos():
    return file_csv_columns["original hours"]["gen_col"]["npos"]    
def get_new_est_effrt_name():
    return file_csv_columns["spenthours"]["gen_col"]["ncol_name"]
def get_new_est_effrt_pos():
    return file_csv_columns["spenthours"]["gen_col"]["npos"]    
def get_new_pending_effrt_name():
    return file_csv_columns["remaining hours"]["gen_col"]["ncol_name"]
def get_new_pending_effrt_pos():
    return file_csv_columns["remaining hours"]["gen_col"]["npos"]  
def get_new_stry_discrpt_name():
    return file_csv_columns["summary"]["gen_col"]["nclo_name"]
def get_new_stry_discrpt_pos():
    return file_csv_columns["summary"]["gen_col"]["npos"]    
    
    


def get_serial_num_pos():
	return file_csv_columns["s.no"]["position"]

def get_issukey_pos():
	return file_csv_columns["Issuekey"]["position"]

def get_isid_pos():
	return file_csv_columns["Issueid"]["position"]
    
def get_custom_epic():
    return file_csv_columns["custom field(epic link)"]["position"]

def get_ename_pos():
    return file_csv_columns["Ename"]["position"]
    
def get_est_starting_date_pos():
    return file_csv_columns["Esdate"]["position"]
    
def get_est_target_date_pos():
    return file_csv_columns["ETdate"]["position"]
    
def get_est_actual_strt_date_pos():
    return file_csv_columns["EASdate"]["position"]
    
def get_est_actual_end_date_pos():
    return file_csv_columns["EAEdate"]["position"]
    
def get_assignee_pos():
    return file_csv_columns["Assignee"]["position"]
    
def get_progress_pos():
    return file_csv_columns["progrss"]["position"]
    
def get_custom_fld_stry_pos():
    return file_csv_columns["custom field(story points)"]["position"]
    
def get_org_est_pos():
    return file_csv_columns["Original Estimate"]["position"]
    
def get_spented_time_pos():
    return file_csv_columns["Time spent"]["position"]
    
def get_remain_est_pos():
    return file_csv_columns["remaining Estimate"]["position"]
    
def get_original_hours():
    return file_csv_columns["original hours"]["position"]
    
def get_spent_hours():
    return file_csv_columns["spenthours"]["position"]
    
def get_rem_hours_pos():
    return file_csv_columns["remaining hours"]["position"]
    
def get_sprnt_pos():
    return file_csv_columns["sprint"]["position"]
    
def get_sprntt_pos():
    return file_csv_columns["sprint2"]["position"]
    
def get_sprrnt_pos():
    return file_csv_columns["sprint3"]["position"]
    
def get_smry_csv():
    return file_csv_columns["summary"]["position"]
def get_epic_snum_pos():
    return epics_of_columns["s.num"]["position"]
def get_epic_custom_field_link():
    return epics_of_columns["Custom field (Epic Link)"]["position"]
def get_epic_Ename():
    return epics_of_columns["Ename"]["position"]
def get_epic_esdate():
    return epics_of_columns["ESdate"]["position"]
def get_epic_etdate():
    return epics_of_columns["ETdate"]["position"]
def get_epic_easdate():
    return epics_of_columns["EASDate"]["position"]
def get_epic_eaedate():
    return epics_of_columns["EAEDate"]["position"]




def main():    
    get_epic_custom_field_link()
    get_epic_Ename()
    get_epic_esdate()
    get_epic_etdate()
    get_epic_easdate()
    get_epic_eaedate()
    get_epic_snum_pos()
    
    get_serial_num_pos()
    get_issukey_pos()
    get_isid_pos()
    get_custom_epic()
    get_ename_pos()
    get_est_starting_date_pos()
    get_est_target_date_pos()
    get_est_actual_strt_date_pos()
    get_est_actual_end_date_pos()
    get_assignee_pos()
    get_progress_pos()
    get_custom_fld_stry_pos()
    get_org_est_pos()
    get_spented_time_pos()
    get_remain_est_pos()
    get_original_hours()
    get_spent_hours()
    get_rem_hours_pos()
    get_sprnt_pos()
    get_sprntt_pos()
    get_sprrnt_pos()
    get_smry_csv()


    get_new_epcid_col_name()
    get_new_epcid_pos()
    get_new_srtyid_name()
    get_new_stryid_pos()
    get_new_stry_plan_strt_name()
    get_new_stry_plan_strt_pos()
    get_new_stry_plan_end_name()
    get_new_stry_plan_end_pos()
    get_new_stry_act_strt_name()
    get_new_stry_act_strt_pos()
    get_new_stry_act_end_name()
    get_new_stry_act_end_pos()
    get_new_assign_name()
    get_new_assign_pos()
    get_new_stry_effort_comp_name()
    get_new_stry_effort_comp_pos()
    get_new_est_stry_pnts_name()
    get_new_est_stry_pnts_pos()
    get_new_time_spnt_name()
    get_new_time_spnt_pos()
    get_new_effort_cons_hrs_name()
    get_new_effort_cons_hrs_pos()
    get_new_est_effrt_name()
    get_new_est_effrt_pos()
    get_new_pending_effrt_name()
    get_new_pending_effrt_pos()
    get_new_stry_discrpt_name()
    get_new_stry_discrpt_pos()
    get_new_sprint_name()
    get_new_sprint_pos()
    get_stry_sch_progress()
    get_stry_sch_progress_pos()
    get_stry_sch_progress_run()
    get_stry_sch_progress_run_pos()
    
    
if (__name__=="__main__"):
    main()