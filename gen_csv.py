import csv

from mycsvmod import (get_serial_num_pos,
    get_issukey_pos,
    get_isid_pos,
    get_custom_epic,
    get_ename_pos,
    get_est_starting_date_pos,
    get_est_target_date_pos,
    get_est_actual_strt_date_pos,
    get_est_actual_end_date_pos,
    get_assignee_pos,
    get_progress_pos,
    get_custom_fld_stry_pos,
    get_org_est_pos,
    get_spented_time_pos,
    get_remain_est_pos,
    get_original_hours,
    get_spent_hours,
    get_rem_hours_pos,
    get_sprnt_pos,
    get_sprntt_pos,
    get_sprrnt_pos,
    get_smry_csv,
    
    get_epic_custom_field_link,
    get_epic_Ename,
    get_epic_esdate,
    get_epic_etdate,
    get_epic_easdate,
    get_epic_eaedate,
    get_epic_snum_pos,
    get_new_epcid_col_name,
    get_new_epcid_pos,
    
    get_new_srtyid_name,
    get_new_stryid_pos,
    get_new_stry_plan_strt_name,
    get_new_stry_plan_strt_pos,
    get_new_stry_plan_end_name,
    get_new_stry_plan_end_pos,
    get_new_stry_act_strt_name,
    get_new_stry_act_strt_pos,
    get_new_stry_act_end_name,
    get_new_stry_act_end_pos,
    get_new_assign_name,
    get_new_assign_pos,
    get_new_stry_effort_comp_name,
    get_new_stry_effort_comp_pos,
    get_new_est_stry_pnts_name,
    get_new_est_stry_pnts_pos,
    get_new_time_spnt_name,
    get_new_time_spnt_pos,
    get_new_effort_cons_hrs_name,
    get_new_effort_cons_hrs_pos,
    get_new_est_effrt_name,
    get_new_est_effrt_pos,
    get_new_pending_effrt_name,
    get_new_pending_effrt_pos,
    get_new_stry_discrpt_name,
    get_new_stry_discrpt_pos,
    get_new_sprint_name,
    get_new_sprint_pos,
    get_stry_sch_progress,
    get_stry_sch_progress_pos,
    get_stry_sch_progress_run,
    get_stry_sch_progress_run_pos,
)
cus_l = get_epic_custom_field_link()
epic_en = get_epic_Ename()
epic_es = get_epic_esdate()
epic_et = get_epic_etdate()
epic_ea = get_epic_easdate()
epc_eae = get_epic_eaedate()
ep_sno = get_epic_snum_pos()

ser = get_serial_num_pos()
isu_k = get_issukey_pos()
isu_id = get_isid_pos()
cust = get_custom_epic()
ename = get_ename_pos()
est_s = get_est_starting_date_pos()
est_t = get_est_target_date_pos()
est_a = get_est_actual_strt_date_pos()
est_ae = get_est_actual_end_date_pos()
ass = get_assignee_pos()
pro = get_progress_pos()
cus = get_custom_fld_stry_pos()
org_p = get_org_est_pos()
spn_t = get_spented_time_pos()
rem_t = get_remain_est_pos()
orig_h = get_original_hours()
spe_h = get_spent_hours()
rem_h = get_rem_hours_pos()
sprn_n = get_sprnt_pos()
sprt = get_sprntt_pos()
sp_t = get_sprrnt_pos()
smr_y = get_smry_csv()


ep_c = get_new_epcid_col_name()
ep_p = get_new_epcid_pos()
str_n = get_new_srtyid_name()
str_p = get_new_stryid_pos()
psrt_n = get_new_stry_plan_strt_name()
pstr_p = get_new_stry_plan_strt_pos()
p_endn = get_new_stry_plan_end_name()
p_endp = get_new_stry_plan_end_pos()
act_n = get_new_stry_act_strt_name()
act_po = get_new_stry_act_strt_pos()
end_n = get_new_stry_act_end_name()
end_p = get_new_stry_act_end_pos()
ass_n = get_new_assign_name()
ass_p = get_new_assign_pos()
eff_cn = get_new_stry_effort_comp_name()
eff_cp = get_new_stry_effort_comp_pos()
est_n = get_new_est_stry_pnts_name()
est_p = get_new_est_stry_pnts_pos()
spn_n = get_new_time_spnt_name()
spn_p = get_new_time_spnt_pos()
cons_n = get_new_effort_cons_hrs_name()
cons_p = get_new_effort_cons_hrs_pos()
efrt_n = get_new_est_effrt_name()
efrt_p = get_new_est_effrt_pos()
pen_n = get_new_pending_effrt_name()
pen_p = get_new_pending_effrt_pos()
dis_n = get_new_stry_discrpt_name()
disc_p = get_new_stry_discrpt_pos()
spr_n = get_new_sprint_name()
sprint_p = get_new_sprint_pos()
sch_pr = get_stry_sch_progress()
sch_po = get_stry_sch_progress_pos()
sch_r = get_stry_sch_progress_run()
sch_rpos = get_stry_sch_progress_run_pos()

def read_csv_file(filename):
    data_list1 = []
    
    fd1 = open(filename, 'r')
    fdata = csv.reader(fd1)
    
    for row in fdata:
        
        data_list1.append(row)
  
    
    n1 = len(data_list1)
    fd1.close()
    return(data_list1)
    
def read_csv_file2(fname):

    data_list2 = []
    
    fd2 = open(fname, 'r')
    gdata = csv.reader(fd2)
    
    for row in gdata:
       
        data_list2.append(row)
    
    n2 = len(data_list2)
    fd2.close()
    return(data_list2)
def new_csv_column(data_list2):
    
    print(data_list2)
    data_list2[0].insert(est_t,"progress")
    
    data_list2[0].insert(cus,"spenthours")
    data_list2[0].insert(pro,"original hours")
    data_list2[0].insert(org_p,"remaining hours")
    for j in range(1, len(data_list2)):
        data_list2[j].insert(est_t,"0")
        data_list2[j].insert(cus,"0")
        data_list2[j].insert(pro,"0")
        data_list2[j].insert(org_p,"0")
        
    return data_list2
    
def gen_stories_of_csv_file(data_list1, data_list2):
    n1 = len(data_list1)
    n2 = len(data_list2)

    i = 1
    j = 1
    data_list2[0].insert(est_s,"ESdate")
    data_list2[0].insert(est_t,"ETdate")
    data_list2[0].insert(est_a,"EASdate")
    data_list2[0].insert(est_ae,"EAEdate")
    #print(data_list2)
    for i in range (1, n1):
        for j in range (1, n2):
        
            if (data_list1[i][cus_l] == data_list2[j][cust]):
                data_list2[j].insert(est_s,data_list1[i][epic_es])
                data_list2[j].insert(est_t,data_list1[i][epic_et])
                data_list2[j].insert(est_a,data_list1[i][epic_ea])
                data_list2[j].insert(est_ae,data_list1[i][epc_eae])
                
                data_list2[j][rem_t] = int(data_list2[j][org_p]) - int(data_list2[j][spn_t]) #rem time
                data_list2[j][orig_h] = int(data_list2[j][org_p])/3600 # original hours
                
                data_list2[j][spe_h] = int(data_list2[j][spn_t])/3600 # spent hours
                
                data_list2[j][rem_h] = int(data_list2[j][orig_h])-(data_list2[j][spe_h]) #rem hours
                data_list2[j][pro] = ((data_list2[j][spe_h])/(data_list2[j][orig_h]))*100 #progress
                
    return data_list2
def get_sort_to_sprint_cols(dlines):
    for i in range(1, len(dlines)):
        sp1 = dlines[i][sprn_n]
        sp2 = dlines[i][sprt]
        sp3 = dlines[i][sp_t]
        print(sp1)
        x = [sp1, sp2, sp3]
        x.sort(reverse = True)
        dlines[i][sprn_n] = x[sp1]
        dlines[i][sprt] = x[sp2]
        dlines[i][sp_t] = x[sp3]
        
    print(dlines)
    
def get_new_col_name(datalist):
    fdata = []
    datalist[0][isu_k] = str_n
    datalist[0][est_s] = psrt_n
    datalist[0][est_t] = p_endn
    datalist[0][est_a] = act_n
    datalist[0][est_ae] = end_n
    datalist[0][ass] = ass_n
    datalist[0][pro] = eff_cn
    datalist[0][cus] = est_n
    datalist[0][org_p] = spn_n
    datalist[0][orig_h] = cons_n 
    datalist[0][spe_h] = efrt_n
    datalist[0][rem_h] = pen_n
    datalist[0][smr_y] = dis_n
    datalist[0][cust] = ep_c
    datalist[0][sprn_n] = spr_n
    datalist[0].insert(sch_po, sch_pr)
    datalist[0].insert(sch_rpos, sch_r)
    for j in range (1, len(datalist)):
        datalist[j].insert(sch_po, "100%")
        datalist[j].insert(sch_rpos, "0%")
    for j in range(0, 1):
        
        for i in range(0, len(datalist)):
            list = [datalist[i][ser],datalist[i][cust],datalist[i][sprn_n],datalist[i][isu_k],datalist[i][smr_y],
                    datalist[i][ass],datalist[i][cus],datalist[i][est_s],datalist[i][est_t],datalist[i][spe_h],datalist[i][org_p],
                    datalist[i][orig_h],datalist[i][rem_h],datalist[i][est_a],
                    datalist[i][est_ae],datalist[i][pro],datalist[i][sch_po],datalist[i][sch_rpos],
                    ]
            fdata.append(list)
    return fdata
def main():
    filename = "01-epics.csv"
    fname = "02-stories.csv"
    
    data_list1 = read_csv_file(filename)
    
    data_list2 = read_csv_file2(fname)

    ncolumn = new_csv_column(data_list2)
    
    jlist = gen_stories_of_csv_file(data_list1, data_list2)
    
    a = get_new_col_name(jlist)
    
    with open("gen_datacsv_file.csv", "w") as csv_file:
        dd = csv.writer(csv_file)
        for line in a:
            dd.writerow(line)
      
if (__name__=="__main__"):
	main()