# from ophyd import Device
# from recordwhat.records import *
# 
# class Usercalcn_nodisable(Device):
#     ...
#     usercalc = Cpt(SwaitRecord, "userCalc")
# 
# 
# class Scalcout(Device):
#     ...
#     scalcout = Cpt(ScalcoutRecord, ":scalcout")
# 
# 
# class Blogioc(Device):
#     ...
#     info = Cpt(BlogRecord, ":info")
#     id_2 = Cpt(BiRecord, ":id_2")
#     newrun = Cpt(StrnoutRecord, ":newrun")
#     newseg = Cpt(StrnoutRecord, ":newseg")
#     endrun = Cpt(StrnoutRecord, ":endrun")
#     setgrp = Cpt(StrnoutRecord, ":setgrp")
#     setprj = Cpt(StrnoutRecord, ":setprj")
# 
#     
# class KandMeta(Device):
#     meta_key_0_sp = Cpt(VsoutRecord, ":META_KEY_0_SP")
#     meta_key_0_mon = Cpt(VsinRecord, ":META_KEY_0_MON")
#     meta_val_0_sp = Cpt(VsoutRecord, ":META_VAL_0_SP")
#     meta_val_0_mon = Cpt(VsinRecord, ":META_VAL_0_MON")
#     meta_key_1_sp = Cpt(VsoutRecord, ":META_KEY_1_SP")
#     meta_key_1_mon = Cpt(VsinRecord, ":META_KEY_1_MON")
#     meta_val_1_sp = Cpt(VsoutRecord, ":META_VAL_1_SP")
#     meta_val_1_mon = Cpt(VsinRecord, ":META_VAL_1_MON")
#     meta_key_2_sp = Cpt(VsoutRecord, ":META_KEY_2_SP")
#     meta_key_2_mon = Cpt(VsinRecord, ":META_KEY_2_MON")
#     meta_val_2_sp = Cpt(VsoutRecord, ":META_VAL_2_SP")
#     meta_val_2_mon = Cpt(VsinRecord, ":META_VAL_2_MON")
#     meta_key_3_sp = Cpt(VsoutRecord, ":META_KEY_3_SP")
#     meta_key_3_mon = Cpt(VsinRecord, ":META_KEY_3_MON")
#     meta_val_3_sp = Cpt(VsoutRecord, ":META_VAL_3_SP")
#     meta_val_3_mon = Cpt(VsinRecord, ":META_VAL_3_MON")
#     meta_key_4_sp = Cpt(VsoutRecord, ":META_KEY_4_SP")
#     meta_key_4_mon = Cpt(VsinRecord, ":META_KEY_4_MON")
#     meta_val_4_sp = Cpt(VsoutRecord, ":META_VAL_4_SP")
#     meta_val_4_mon = Cpt(VsinRecord, ":META_VAL_4_MON")
#     meta_key_5_sp = Cpt(VsoutRecord, ":META_KEY_5_SP")
#     meta_key_5_mon = Cpt(VsinRecord, ":META_KEY_5_MON")
#     meta_val_5_sp = Cpt(VsoutRecord, ":META_VAL_5_SP")
#     meta_val_5_mon = Cpt(VsinRecord, ":META_VAL_5_MON")
#     meta_key_6_sp = Cpt(VsoutRecord, ":META_KEY_6_SP")
#     meta_key_6_mon = Cpt(VsinRecord, ":META_KEY_6_MON")
#     meta_val_6_sp = Cpt(VsoutRecord, ":META_VAL_6_SP")
#     meta_val_6_mon = Cpt(VsinRecord, ":META_VAL_6_MON")
#     meta_key_7_sp = Cpt(VsoutRecord, ":META_KEY_7_SP")
#     meta_key_7_mon = Cpt(VsinRecord, ":META_KEY_7_MON")
#     meta_val_7_sp = Cpt(VsoutRecord, ":META_VAL_7_SP")
#     meta_val_7_mon = Cpt(VsinRecord, ":META_VAL_7_MON")
#     meta_key_8_sp = Cpt(VsoutRecord, ":META_KEY_8_SP")
#     meta_key_8_mon = Cpt(VsinRecord, ":META_KEY_8_MON")
#     meta_val_8_sp = Cpt(VsoutRecord, ":META_VAL_8_SP")
#     meta_val_8_mon = Cpt(VsinRecord, ":META_VAL_8_MON")
#     meta_key_9_sp = Cpt(VsoutRecord, ":META_KEY_9_SP")
#     meta_key_9_mon = Cpt(VsinRecord, ":META_KEY_9_MON")
#     meta_val_9_sp = Cpt(VsoutRecord, ":META_VAL_9_SP")
#     meta_val_9_mon = Cpt(VsinRecord, ":META_VAL_9_MON")
#     meta_key_10_sp = Cpt(VsoutRecord, ":META_KEY_10_SP")
#     meta_key_10_mon = Cpt(VsinRecord, ":META_KEY_10_MON")
#     meta_val_10_sp = Cpt(VsoutRecord, ":META_VAL_10_SP")
#     meta_val_10_mon = Cpt(VsinRecord, ":META_VAL_10_MON")
#     meta_key_11_sp = Cpt(VsoutRecord, ":META_KEY_11_SP")
#     meta_key_11_mon = Cpt(VsinRecord, ":META_KEY_11_MON")
#     meta_val_11_sp = Cpt(VsoutRecord, ":META_VAL_11_SP")
#     meta_val_11_mon = Cpt(VsinRecord, ":META_VAL_11_MON")
#     meta_key_12_sp = Cpt(VsoutRecord, ":META_KEY_12_SP")
#     meta_key_12_mon = Cpt(VsinRecord, ":META_KEY_12_MON")
#     meta_val_12_sp = Cpt(VsoutRecord, ":META_VAL_12_SP")
#     meta_val_12_mon = Cpt(VsinRecord, ":META_VAL_12_MON")
#     meta_key_13_sp = Cpt(VsoutRecord, ":META_KEY_13_SP")
#     meta_key_13_mon = Cpt(VsinRecord, ":META_KEY_13_MON")
#     meta_val_13_sp = Cpt(VsoutRecord, ":META_VAL_13_SP")
#     meta_val_13_mon = Cpt(VsinRecord, ":META_VAL_13_MON")
#     meta_key_14_sp = Cpt(VsoutRecord, ":META_KEY_14_SP")
#     meta_key_14_mon = Cpt(VsinRecord, ":META_KEY_14_MON")
#     meta_val_14_sp = Cpt(VsoutRecord, ":META_VAL_14_SP")
#     meta_val_14_mon = Cpt(VsinRecord, ":META_VAL_14_MON")
#     meta_key_15_sp = Cpt(VsoutRecord, ":META_KEY_15_SP")
#     meta_key_15_mon = Cpt(VsinRecord, ":META_KEY_15_MON")
#     meta_val_15_sp = Cpt(VsoutRecord, ":META_VAL_15_SP")
#     meta_val_15_mon = Cpt(VsinRecord, ":META_VAL_15_MON")
#     meta_key_16_sp = Cpt(VsoutRecord, ":META_KEY_16_SP")
#     meta_key_16_mon = Cpt(VsinRecord, ":META_KEY_16_MON")
#     meta_val_16_sp = Cpt(VsoutRecord, ":META_VAL_16_SP")
#     meta_val_16_mon = Cpt(VsinRecord, ":META_VAL_16_MON")
#     meta_key_17_sp = Cpt(VsoutRecord, ":META_KEY_17_SP")
#     meta_key_17_mon = Cpt(VsinRecord, ":META_KEY_17_MON")
#     meta_val_17_sp = Cpt(VsoutRecord, ":META_VAL_17_SP")
#     meta_val_17_mon = Cpt(VsinRecord, ":META_VAL_17_MON")
#     meta_key_18_sp = Cpt(VsoutRecord, ":META_KEY_18_SP")
#     meta_key_18_mon = Cpt(VsinRecord, ":META_KEY_18_MON")
#     meta_val_18_sp = Cpt(VsoutRecord, ":META_VAL_18_SP")
#     meta_val_18_mon = Cpt(VsinRecord, ":META_VAL_18_MON")
#     meta_key_19_sp = Cpt(VsoutRecord, ":META_KEY_19_SP")
#     meta_key_19_mon = Cpt(VsinRecord, ":META_KEY_19_MON")
#     meta_val_19_sp = Cpt(VsoutRecord, ":META_VAL_19_SP")
#     meta_val_19_mon = Cpt(VsinRecord, ":META_VAL_19_MON")
#     meta_key_20_sp = Cpt(VsoutRecord, ":META_KEY_20_SP")
#     meta_key_20_mon = Cpt(VsinRecord, ":META_KEY_20_MON")
#     meta_val_20_sp = Cpt(VsoutRecord, ":META_VAL_20_SP")
#     meta_val_20_mon = Cpt(VsinRecord, ":META_VAL_20_MON")
#     meta_key_21_sp = Cpt(VsoutRecord, ":META_KEY_21_SP")
#     meta_key_21_mon = Cpt(VsinRecord, ":META_KEY_21_MON")
#     meta_val_21_sp = Cpt(VsoutRecord, ":META_VAL_21_SP")
#     meta_val_21_mon = Cpt(VsinRecord, ":META_VAL_21_MON")
#     meta_key_22_sp = Cpt(VsoutRecord, ":META_KEY_22_SP")
#     meta_key_22_mon = Cpt(VsinRecord, ":META_KEY_22_MON")
#     meta_val_22_sp = Cpt(VsoutRecord, ":META_VAL_22_SP")
#     meta_val_22_mon = Cpt(VsinRecord, ":META_VAL_22_MON")
#     meta_key_23_sp = Cpt(VsoutRecord, ":META_KEY_23_SP")
#     meta_key_23_mon = Cpt(VsinRecord, ":META_KEY_23_MON")
#     meta_val_23_sp = Cpt(VsoutRecord, ":META_VAL_23_SP")
#     meta_val_23_mon = Cpt(VsinRecord, ":META_VAL_23_MON")
#     meta_key_24_sp = Cpt(VsoutRecord, ":META_KEY_24_SP")
#     meta_key_24_mon = Cpt(VsinRecord, ":META_KEY_24_MON")
#     meta_val_24_sp = Cpt(VsoutRecord, ":META_VAL_24_SP")
#     meta_val_24_mon = Cpt(VsinRecord, ":META_VAL_24_MON")
#     meta_key_25_sp = Cpt(VsoutRecord, ":META_KEY_25_SP")
#     meta_key_25_mon = Cpt(VsinRecord, ":META_KEY_25_MON")
#     meta_val_25_sp = Cpt(VsoutRecord, ":META_VAL_25_SP")
#     meta_val_25_mon = Cpt(VsinRecord, ":META_VAL_25_MON")
#     meta_key_26_sp = Cpt(VsoutRecord, ":META_KEY_26_SP")
#     meta_key_26_mon = Cpt(VsinRecord, ":META_KEY_26_MON")
#     meta_val_26_sp = Cpt(VsoutRecord, ":META_VAL_26_SP")
#     meta_val_26_mon = Cpt(VsinRecord, ":META_VAL_26_MON")
#     meta_key_27_sp = Cpt(VsoutRecord, ":META_KEY_27_SP")
#     meta_key_27_mon = Cpt(VsinRecord, ":META_KEY_27_MON")
#     meta_val_27_sp = Cpt(VsoutRecord, ":META_VAL_27_SP")
#     meta_val_27_mon = Cpt(VsinRecord, ":META_VAL_27_MON")
#     meta_key_28_sp = Cpt(VsoutRecord, ":META_KEY_28_SP")
#     meta_key_28_mon = Cpt(VsinRecord, ":META_KEY_28_MON")
#     meta_val_28_sp = Cpt(VsoutRecord, ":META_VAL_28_SP")
#     meta_val_28_mon = Cpt(VsinRecord, ":META_VAL_28_MON")
#     meta_key_29_sp = Cpt(VsoutRecord, ":META_KEY_29_SP")
#     meta_key_29_mon = Cpt(VsinRecord, ":META_KEY_29_MON")
#     meta_val_29_sp = Cpt(VsoutRecord, ":META_VAL_29_SP")
#     meta_val_29_mon = Cpt(VsinRecord, ":META_VAL_29_MON")
#     meta_key_30_sp = Cpt(VsoutRecord, ":META_KEY_30_SP")
#     meta_key_30_mon = Cpt(VsinRecord, ":META_KEY_30_MON")
#     meta_val_30_sp = Cpt(VsoutRecord, ":META_VAL_30_SP")
#     meta_val_30_mon = Cpt(VsinRecord, ":META_VAL_30_MON")
#     meta_key_31_sp = Cpt(VsoutRecord, ":META_KEY_31_SP")
#     meta_key_31_mon = Cpt(VsinRecord, ":META_KEY_31_MON")
#     meta_val_31_sp = Cpt(VsoutRecord, ":META_VAL_31_SP")
#     meta_val_31_mon = Cpt(VsinRecord, ":META_VAL_31_MON")
# 
# 
# class Kandinskivars(Device):
#     ...
# 
#     bias_volt_max = Cpt(AiRecord, ":BIAS_VOLT_MAX")
#     
#     blog = Cpt(Blogioc, '')
#     blog_conected_mon = Cpt(BiRecord, ":BLOG_CONECTED_MON")
#     blog_discard_mon = Cpt(BiRecord, ":BLOG_DISCARD_MON")
#     blog_enable_cmd = Cpt(BoRecord, ":BLOG_ENABLE_CMD")
#     blog_group_next_mon = Cpt(VsinRecord, ":BLOG_GROUP_NEXT_MON")
#     blog_group_next_sp = Cpt(VsoutRecord, ":BLOG_GROUP_NEXT_SP")
#     blog_project_next_mon = Cpt(VsinRecord, ":BLOG_PROJECT_NEXT_MON")
#     blog_project_next_sp = Cpt(VsoutRecord, ":BLOG_PROJECT_NEXT_SP")
#     blog_rate_mon = Cpt(LonginRecord, ":BLOG_RATE_MON")
#     blog_runno_mon = Cpt(LonginRecord, ":BLOG_RUNNO_MON")
#     blog_runsize_mon = Cpt(LonginRecord, ":BLOG_RUNSIZE_MON")
#     blog_runtime_mon = Cpt(LonginRecord, ":BLOG_RUNTIME_MON")
#     blog_segno_mon = Cpt(LonginRecord, ":BLOG_SEGNO_MON")
#     
#     bp_ilock_mon = Cpt(BiRecord, ":BP_ILOCK_MON")
# 
#     da_enable_cmd = Cpt(BoRecord, ":DA_ENABLE_CMD")
#     da_info_sp = Cpt(VsoutRecord, ":DA_INFO_SP")
# 
#     dam_ident = Cpt(VsinRecord, ":DAM_IDENT")
#     dam_revision = Cpt(LonginRecord, ":DAM_REVISION")
# 
#     deadtime_enable_cmd = Cpt(BoRecord, ":DEADTIME_ENABLE_CMD")
#     deadtime_info_sp = Cpt(VsoutRecord, ":DEADTIME_INFO_SP")
# 
#     det_bias_volt_mon = Cpt(AiRecord, ":DET_BIAS_VOLT_MON")
#     det_bias_volt_rate_sp = Cpt(AoRecord, ":DET_BIAS_VOLT_RATE_SP")
#     det_bias_volt_sp = Cpt(AoRecord, ":DET_BIAS_VOLT_SP")
#     det_leak_mon = Cpt(AiRecord, ":DET_LEAK_MON")
#     det_pelt_curr_rate_sp = Cpt(AoRecord, ":DET_PELT_CURR_RATE_SP")
#     det_pelt_curr_sp = Cpt(AoRecord, ":DET_PELT_CURR_SP")
#     det_pelt_mon = Cpt(AiRecord, ":DET_PELT_MON")
#     det_temp_mon = Cpt(AiRecord, ":DET_TEMP_MON")
# 
#     enc_axis_0_calib_count_sp = Cpt(LongoutRecord, ":ENC_AXIS_0_CALIB_COUNT_SP")
#     enc_axis_0_calib_pos_sp = Cpt(AoRecord, ":ENC_AXIS_0_CALIB_POS_SP")
#     enc_axis_0_calib_status = Cpt(VsinRecord, ":ENC_AXIS_0_CALIB_STATUS")
#     enc_axis_0_pos_mon = Cpt(AiRecord, ":ENC_AXIS_0_POS_MON")
#     enc_axis_0_pos_sp = Cpt(AoRecord, ":ENC_AXIS_0_POS_SP")
#     enc_axis_1_calib_count_sp = Cpt(LongoutRecord, ":ENC_AXIS_1_CALIB_COUNT_SP")
#     enc_axis_1_calib_pos_sp = Cpt(AoRecord, ":ENC_AXIS_1_CALIB_POS_SP")
#     enc_axis_1_calib_status = Cpt(VsinRecord, ":ENC_AXIS_1_CALIB_STATUS")
#     enc_axis_1_pos_mon = Cpt(AiRecord, ":ENC_AXIS_1_POS_MON")
#     enc_axis_1_pos_sp = Cpt(AoRecord, ":ENC_AXIS_1_POS_SP")
#     enc_axis_2_calib_count_sp = Cpt(LongoutRecord, ":ENC_AXIS_2_CALIB_COUNT_SP")
#     enc_axis_2_calib_pos_sp = Cpt(AoRecord, ":ENC_AXIS_2_CALIB_POS_SP")
#     enc_axis_2_calib_status = Cpt(VsinRecord, ":ENC_AXIS_2_CALIB_STATUS")
#     enc_axis_2_pos_mon = Cpt(AiRecord, ":ENC_AXIS_2_POS_MON")
#     enc_axis_2_pos_sp = Cpt(AoRecord, ":ENC_AXIS_2_POS_SP")
#     enc_axis_3_calib_count_sp = Cpt(LongoutRecord, ":ENC_AXIS_3_CALIB_COUNT_SP")
#     enc_axis_3_calib_pos_sp = Cpt(AoRecord, ":ENC_AXIS_3_CALIB_POS_SP")
#     enc_axis_3_calib_status = Cpt(VsinRecord, ":ENC_AXIS_3_CALIB_STATUS")
#     enc_axis_3_pos_mon = Cpt(AiRecord, ":ENC_AXIS_3_POS_MON")
#     enc_axis_3_pos_sp = Cpt(AoRecord, ":ENC_AXIS_3_POS_SP")
#     enc_axis_4_calib_count_sp = Cpt(LongoutRecord, ":ENC_AXIS_4_CALIB_COUNT_SP")
#     enc_axis_4_calib_pos_sp = Cpt(AoRecord, ":ENC_AXIS_4_CALIB_POS_SP")
#     enc_axis_4_calib_status = Cpt(VsinRecord, ":ENC_AXIS_4_CALIB_STATUS")
#     enc_axis_4_pos_mon = Cpt(AiRecord, ":ENC_AXIS_4_POS_MON")
#     enc_axis_4_pos_sp = Cpt(AoRecord, ":ENC_AXIS_4_POS_SP")
#     enc_axis_5_calib_count_sp = Cpt(LongoutRecord, ":ENC_AXIS_5_CALIB_COUNT_SP")
#     enc_axis_5_calib_pos_sp = Cpt(AoRecord, ":ENC_AXIS_5_CALIB_POS_SP")
#     enc_axis_5_calib_status = Cpt(VsinRecord, ":ENC_AXIS_5_CALIB_STATUS")
#     enc_axis_5_pos_mon = Cpt(AiRecord, ":ENC_AXIS_5_POS_MON")
#     enc_axis_5_pos_sp = Cpt(AoRecord, ":ENC_AXIS_5_POS_SP")
#     enc_axis_6_calib_count_sp = Cpt(LongoutRecord, ":ENC_AXIS_6_CALIB_COUNT_SP")
#     enc_axis_6_calib_pos_sp = Cpt(AoRecord, ":ENC_AXIS_6_CALIB_POS_SP")
#     enc_axis_6_calib_status = Cpt(VsinRecord, ":ENC_AXIS_6_CALIB_STATUS")
#     enc_axis_6_pos_mon = Cpt(AiRecord, ":ENC_AXIS_6_POS_MON")
#     enc_axis_6_pos_sp = Cpt(AoRecord, ":ENC_AXIS_6_POS_SP")
#     enc_axis_7_calib_count_sp = Cpt(LongoutRecord, ":ENC_AXIS_7_CALIB_COUNT_SP")
#     enc_axis_7_calib_pos_sp = Cpt(AoRecord, ":ENC_AXIS_7_CALIB_POS_SP")
#     enc_axis_7_calib_status = Cpt(VsinRecord, ":ENC_AXIS_7_CALIB_STATUS")
#     enc_axis_7_pos_mon = Cpt(AiRecord, ":ENC_AXIS_7_POS_MON")
#     enc_axis_7_pos_sp = Cpt(AoRecord, ":ENC_AXIS_7_POS_SP")
#     enc_axis_8_calib_count_sp = Cpt(LongoutRecord, ":ENC_AXIS_8_CALIB_COUNT_SP")
#     enc_axis_8_calib_pos_sp = Cpt(AoRecord, ":ENC_AXIS_8_CALIB_POS_SP")
#     enc_axis_8_calib_status = Cpt(VsinRecord, ":ENC_AXIS_8_CALIB_STATUS")
#     enc_axis_8_pos_mon = Cpt(AiRecord, ":ENC_AXIS_8_POS_MON")
#     enc_axis_8_pos_sp = Cpt(AoRecord, ":ENC_AXIS_8_POS_SP")
#     enc_axis_9_calib_count_sp = Cpt(LongoutRecord, ":ENC_AXIS_9_CALIB_COUNT_SP")
#     enc_axis_9_calib_pos_sp = Cpt(AoRecord, ":ENC_AXIS_9_CALIB_POS_SP")
#     enc_axis_9_calib_status = Cpt(VsinRecord, ":ENC_AXIS_9_CALIB_STATUS")
#     enc_axis_9_pos_mon = Cpt(AiRecord, ":ENC_AXIS_9_POS_MON")
#     enc_axis_9_pos_sp = Cpt(AoRecord, ":ENC_AXIS_9_POS_SP")
#     enc_axis_10_calib_count_sp = Cpt(LongoutRecord, ":ENC_AXIS_10_CALIB_COUNT_SP")
#     enc_axis_10_calib_pos_sp = Cpt(AoRecord, ":ENC_AXIS_10_CALIB_POS_SP")
#     enc_axis_10_calib_status = Cpt(VsinRecord, ":ENC_AXIS_10_CALIB_STATUS")
#     enc_axis_10_pos_mon = Cpt(AiRecord, ":ENC_AXIS_10_POS_MON")
#     enc_axis_10_pos_sp = Cpt(AoRecord, ":ENC_AXIS_10_POS_SP")
#     enc_axis_11_calib_count_sp = Cpt(LongoutRecord, ":ENC_AXIS_11_CALIB_COUNT_SP")
#     enc_axis_11_calib_pos_sp = Cpt(AoRecord, ":ENC_AXIS_11_CALIB_POS_SP")
#     enc_axis_11_calib_status = Cpt(VsinRecord, ":ENC_AXIS_11_CALIB_STATUS")
#     enc_axis_11_pos_mon = Cpt(AiRecord, ":ENC_AXIS_11_POS_MON")
#     enc_axis_11_pos_sp = Cpt(AoRecord, ":ENC_AXIS_11_POS_SP")
# 
#     enc_axis_calib_arm_0_cmd = Cpt(BoRecord, ":ENC_AXIS_CALIB_ARM_0_CMD")
#     enc_axis_calib_arm_1_cmd = Cpt(BoRecord, ":ENC_AXIS_CALIB_ARM_1_CMD")
#     enc_axis_calib_arm_2_cmd = Cpt(BoRecord, ":ENC_AXIS_CALIB_ARM_2_CMD")
#     enc_axis_calib_arm_3_cmd = Cpt(BoRecord, ":ENC_AXIS_CALIB_ARM_3_CMD")
#     enc_axis_calib_arm_4_cmd = Cpt(BoRecord, ":ENC_AXIS_CALIB_ARM_4_CMD")
#     enc_axis_calib_arm_5_cmd = Cpt(BoRecord, ":ENC_AXIS_CALIB_ARM_5_CMD")
#     enc_axis_calib_arm_6_cmd = Cpt(BoRecord, ":ENC_AXIS_CALIB_ARM_6_CMD")
#     enc_axis_calib_arm_7_cmd = Cpt(BoRecord, ":ENC_AXIS_CALIB_ARM_7_CMD")
#     enc_axis_calib_arm_8_cmd = Cpt(BoRecord, ":ENC_AXIS_CALIB_ARM_8_CMD")
#     enc_axis_calib_arm_9_cmd = Cpt(BoRecord, ":ENC_AXIS_CALIB_ARM_9_CMD")
#     enc_axis_calib_arm_10_cmd = Cpt(BoRecord, ":ENC_AXIS_CALIB_ARM_10_CMD")
#     enc_axis_calib_arm_11_cmd = Cpt(BoRecord, ":ENC_AXIS_CALIB_ARM_11_CMD")
# 
#     endrun_cmd = Cpt(BoRecord, ":ENDRUN_CMD")
# 
#     errstr = Cpt(StringinRecord, ":errstr")
# 
#     event_discard_rate_mon = Cpt(LonginRecord, ":EVENT_DISCARD_RATE_MON")
#     event_enable_mon = Cpt(BiRecord, ":EVENT_ENABLE_MON")
#     event_enable_sp = Cpt(BoRecord, ":EVENT_ENABLE_SP")
#     event_rate_mon = Cpt(LonginRecord, ":EVENT_RATE_MON")
# 
#     flux_chan_0_coeff_mon = Cpt(AiRecord, ":FLUX_CHAN_0_COEFF_MON")
#     flux_chan_0_coeff_sp = Cpt(AoRecord, ":FLUX_CHAN_0_COEFF_SP")
#     flux_chan_0_name_mon = Cpt(VsinRecord, ":FLUX_CHAN_0_NAME_MON")
#     flux_chan_0_name_sp = Cpt(VsoutRecord, ":FLUX_CHAN_0_NAME_SP")
#     flux_chan_0_source_mon = Cpt(VsinRecord, ":FLUX_CHAN_0_SOURCE_MON")
#     flux_chan_0_unit_mon = Cpt(VsinRecord, ":FLUX_CHAN_0_UNIT_MON")
#     flux_chan_0_unit_sp = Cpt(VsoutRecord, ":FLUX_CHAN_0_UNIT_SP")
#     flux_chan_1_coeff_mon = Cpt(AiRecord, ":FLUX_CHAN_1_COEFF_MON")
#     flux_chan_1_coeff_sp = Cpt(AoRecord, ":FLUX_CHAN_1_COEFF_SP")
#     flux_chan_1_name_mon = Cpt(VsinRecord, ":FLUX_CHAN_1_NAME_MON")
#     flux_chan_1_name_sp = Cpt(VsoutRecord, ":FLUX_CHAN_1_NAME_SP")
#     flux_chan_1_source_mon = Cpt(VsinRecord, ":FLUX_CHAN_1_SOURCE_MON")
#     flux_chan_1_unit_mon = Cpt(VsinRecord, ":FLUX_CHAN_1_UNIT_MON")
#     flux_chan_1_unit_sp = Cpt(VsoutRecord, ":FLUX_CHAN_1_UNIT_SP")
# 
#     gaintrim_enable_mon = Cpt(BiRecord, ":GAINTRIM_ENABLE_MON")
#     gaintrim_enable_sp = Cpt(BoRecord, ":GAINTRIM_ENABLE_SP")
#     gaintrim_info_sp = Cpt(VsoutRecord, ":GAINTRIM_INFO_SP")
# 
#     group_info_sp = Cpt(VsoutRecord, ":GROUP_INFO_SP")
# 
#     hermes_temp_mon = Cpt(AiRecord, ":HERMES_TEMP_MON")
# 
#     hymod_cpu_temp_mon = Cpt(AiRecord, ":HYMOD_CPU_TEMP_MON")
#     hymod_fpga_temp_mon = Cpt(AiRecord, ":HYMOD_FPGA_TEMP_MON")
# 
#     linearise_enable_mon = Cpt(BiRecord, ":LINEARISE_ENABLE_MON")
#     linearise_enable_sp = Cpt(BoRecord, ":LINEARISE_ENABLE_SP")
# 
#     link_mon = Cpt(BiRecord, ":LINK_MON")
#     link_rate_mon = Cpt(LonginRecord, ":LINK_RATE_MON")
# 
#     meta = Cpt(KandMeta, '')
#     meta_enable_mon = Cpt(BiRecord, ":META_ENABLE_MON")
#     meta_enable_sp = Cpt(BoRecord, ":META_ENABLE_SP")
#     meta_val_beam_energy_mon = Cpt(VsinRecord, ":META_VAL_BEAM_ENERGY_MON")
#     meta_val_beam_energy_sp = Cpt(VsoutRecord, ":META_VAL_BEAM_ENERGY_SP")
#     meta_val_beam_particle_mon = Cpt(VsinRecord, ":META_VAL_BEAM_PARTICLE_MON")
#     meta_val_beam_particle_sp = Cpt(VsoutRecord, ":META_VAL_BEAM_PARTICLE_SP")    
#     meta_val_sample_info_mon = Cpt(VsinRecord, ":META_VAL_SAMPLE_INFO_MON")
#     meta_val_sample_info_sp = Cpt(VsoutRecord, ":META_VAL_SAMPLE_INFO_SP")
#     meta_val_sample_name_mon = Cpt(VsinRecord, ":META_VAL_SAMPLE_NAME_MON")
#     meta_val_sample_name_sp = Cpt(VsoutRecord, ":META_VAL_SAMPLE_NAME_SP")
#     meta_val_sample_owner_mon = Cpt(VsinRecord, ":META_VAL_SAMPLE_OWNER_MON")
#     meta_val_sample_owner_sp = Cpt(VsoutRecord, ":META_VAL_SAMPLE_OWNER_SP")
#     meta_val_sample_serial_mon = Cpt(VsinRecord, ":META_VAL_SAMPLE_SERIAL_MON")
#     meta_val_sample_serial_sp = Cpt(VsoutRecord, ":META_VAL_SAMPLE_SERIAL_SP")
#     meta_val_sample_type_mon = Cpt(VsinRecord, ":META_VAL_SAMPLE_TYPE_MON")
#     meta_val_sample_type_sp = Cpt(VsoutRecord, ":META_VAL_SAMPLE_TYPE_SP")
#     meta_val_scan_crossref_mon = Cpt(VsinRecord, ":META_VAL_SCAN_CROSSREF_MON")
#     meta_val_scan_crossref_sp = Cpt(VsoutRecord, ":META_VAL_SCAN_CROSSREF_SP")
#     meta_val_scan_dwell = Cpt(VsoutRecord, ":META_VAL_SCAN_DWELL")
#     meta_val_scan_dwell_mon = Cpt(VsinRecord, ":META_VAL_SCAN_DWELL_MON")
#     meta_val_scan_info_mon = Cpt(VsinRecord, ":META_VAL_SCAN_INFO_MON")
#     meta_val_scan_info_sp = Cpt(VsoutRecord, ":META_VAL_SCAN_INFO_SP")
#     meta_val_scan_order_mon = Cpt(VsinRecord, ":META_VAL_SCAN_ORDER_MON")
#     meta_val_scan_order_sp = Cpt(VsoutRecord, ":META_VAL_SCAN_ORDER_SP")
#     meta_val_scan_region_mon = Cpt(VsinRecord, ":META_VAL_SCAN_REGION_MON")
#     meta_val_scan_region_sp = Cpt(VsoutRecord, ":META_VAL_SCAN_REGION_SP")
#     meta_val_scan_seq_num_mon = Cpt(VsinRecord, ":META_VAL_SCAN_SEQ_NUM_MON")
#     meta_val_scan_seq_num_sp = Cpt(VsoutRecord, ":META_VAL_SCAN_SEQ_NUM_SP")
#     meta_val_scan_seq_total_mon = Cpt(VsinRecord, ":META_VAL_SCAN_SEQ_TOTAL_MON")
#     meta_val_scan_seq_total_sp = Cpt(VsoutRecord, ":META_VAL_SCAN_SEQ_TOTAL_SP")
#     newrun_cmd = Cpt(BoRecord, ":NEWRUN_CMD")
#     newscan_cmd = Cpt(BoRecord, ":NEWSCAN_CMD")
#     newseg_cmd = Cpt(BoRecord, ":NEWSEG_CMD")
# 
#     pelt_curr_range_0 = Cpt(AiRecord, ":PELT_CURR_RANGE_0")
#     pelt_curr_range_1 = Cpt(AiRecord, ":PELT_CURR_RANGE_1")
# 
#     photon_enable_mon = Cpt(BiRecord, ":PHOTON_ENABLE_MON")
#     photon_enable_sp = Cpt(BoRecord, ":PHOTON_ENABLE_SP")
# 
#     pileup_enable_mon = Cpt(BiRecord, ":PILEUP_ENABLE_MON")
#     pileup_enable_sp = Cpt(BoRecord, ":PILEUP_ENABLE_SP")
#     pileup_info_sp = Cpt(VsoutRecord, ":PILEUP_INFO_SP")
# 
#     pixel_dwell = Cpt(AoRecord, ":PIXEL_DWELL")
#     pixel_enable_cmd = Cpt(BoRecord, ":PIXEL_ENABLE_CMD")
#     pixel_event_enable_cmd = Cpt(BoRecord, ":PIXEL_EVENT_ENABLE_CMD")
#     pixel_transit_sp = Cpt(AoRecord, ":PIXEL_TRANSIT_SP")
# 
#     pulser_enable_mon = Cpt(BiRecord, ":PULSER_ENABLE_MON")
#     pulser_enable_sp = Cpt(BoRecord, ":PULSER_ENABLE_SP")
#     pulser_rate_mon = Cpt(AiRecord, ":PULSER_RATE_MON")
#     pulser_rate_sp = Cpt(AoRecord, ":PULSER_RATE_SP")
#     pulser_voltage_mon = Cpt(AiRecord, ":PULSER_VOLTAGE_MON")
#     pulser_voltage_sp = Cpt(AoRecord, ":PULSER_VOLTAGE_SP")
#     scan_crossref_sp = Cpt(VsoutRecord, ":SCAN_CROSSREF_SP")
#     scan_info_0_sp = Cpt(VsoutRecord, ":SCAN_INFO_0_SP")
#     scan_info_1_sp = Cpt(VsoutRecord, ":SCAN_INFO_1_SP")
#     scan_info_2_sp = Cpt(VsoutRecord, ":SCAN_INFO_2_SP")
#     scan_info_3_sp = Cpt(VsoutRecord, ":SCAN_INFO_3_SP")
#     scan_info_4_sp = Cpt(VsoutRecord, ":SCAN_INFO_4_SP")
#     scan_info_5_sp = Cpt(VsoutRecord, ":SCAN_INFO_5_SP")
#     scan_info_6_sp = Cpt(VsoutRecord, ":SCAN_INFO_6_SP")
#     scan_info_7_sp = Cpt(VsoutRecord, ":SCAN_INFO_7_SP")
#     scan_info_array_sp = Cpt(WaveformRecord, ":SCAN_INFO_ARRAY_SP")
#     scan_number_sp = Cpt(LongoutRecord, ":SCAN_NUMBER_SP")
#     scan_order_int_sp = Cpt(LongoutRecord, ":SCAN_ORDER_INT_SP")
#     scan_order_sp = Cpt(VsoutRecord, ":SCAN_ORDER_SP")
#     throttle_enable_mon = Cpt(BiRecord, ":THROTTLE_ENABLE_MON")
#     throttle_enable_sp = Cpt(BoRecord, ":THROTTLE_ENABLE_SP")
#     throttle_info_sp = Cpt(VsoutRecord, ":THROTTLE_INFO_SP")
# 
#     water_temp_mon = Cpt(AiRecord, ":WATER_TEMP_MON")
# 
#     x_pixel_dim_coord = Cpt(LongoutRecord, ":X_PIXEL_DIM_COORD")
#     x_pixel_dim_coord_extent_sp = Cpt(LongoutRecord, ":X_PIXEL_DIM_COORD_EXTENT_SP")
#     x_pixel_dim_coord_modulus_mon = Cpt(LonginRecord, ":X_PIXEL_DIM_COORD_MODULUS_MON")
#     x_pixel_dim_coord_modulus_sp = Cpt(LongoutRecord, ":X_PIXEL_DIM_COORD_MODULUS_SP")
#     x_pixel_dim_hyst_sp = Cpt(AoRecord, ":X_PIXEL_DIM_HYST_SP")
#     x_pixel_dim_origin_sp = Cpt(AoRecord, ":X_PIXEL_DIM_ORIGIN_SP")
#     x_pixel_dim_pitch_range_0 = Cpt(AiRecord, ":X_PIXEL_DIM_PITCH_RANGE_0")
#     x_pixel_dim_pitch_range_1 = Cpt(AiRecord, ":X_PIXEL_DIM_PITCH_RANGE_1")
#     x_pixel_dim_pitch_sp = Cpt(AoRecord, ":X_PIXEL_DIM_PITCH_SP")
#     x_pixel_num_sp = Cpt(LongoutRecord, ":X_PIXEL_NUM_SP")
#     x_pos_dim_name = Cpt(VsinRecord, ":X_POS_DIM_NAME")
#     x_pos_dim_pos = Cpt(AiRecord, ":X_POS_DIM_POS")
#     x_pos_dim_source_sp = Cpt(VsoutRecord, ":X_POS_DIM_SOURCE_SP")
#     x_pos_dim_unit = Cpt(VsinRecord, ":X_POS_DIM_UNIT")
#     y_pixel_dim_coord = Cpt(LongoutRecord, ":Y_PIXEL_DIM_COORD")
#     y_pixel_dim_coord_extent_sp = Cpt(LongoutRecord, ":Y_PIXEL_DIM_COORD_EXTENT_SP")
#     y_pixel_dim_coord_modulus_mon = Cpt(LonginRecord, ":Y_PIXEL_DIM_COORD_MODULUS_MON")
#     y_pixel_dim_coord_modulus_sp = Cpt(LongoutRecord, ":Y_PIXEL_DIM_COORD_MODULUS_SP")
#     y_pixel_dim_hyst_sp = Cpt(AoRecord, ":Y_PIXEL_DIM_HYST_SP")
#     y_pixel_dim_origin_sp = Cpt(AoRecord, ":Y_PIXEL_DIM_ORIGIN_SP")
#     y_pixel_dim_pitch_range_0 = Cpt(AiRecord, ":Y_PIXEL_DIM_PITCH_RANGE_0")
#     y_pixel_dim_pitch_range_1 = Cpt(AiRecord, ":Y_PIXEL_DIM_PITCH_RANGE_1")
#     y_pixel_dim_pitch_sp = Cpt(AoRecord, ":Y_PIXEL_DIM_PITCH_SP")
#     y_pixel_num_sp = Cpt(LongoutRecord, ":Y_PIXEL_NUM_SP")
#     y_pos_dim_name = Cpt(VsinRecord, ":Y_POS_DIM_NAME")
#     y_pos_dim_pos = Cpt(AiRecord, ":Y_POS_DIM_POS")
#     y_pos_dim_source_sp = Cpt(VsoutRecord, ":Y_POS_DIM_SOURCE_SP")
#     y_pos_dim_unit = Cpt(VsinRecord, ":Y_POS_DIM_UNIT")
#     z_pixel_dim_coord = Cpt(LongoutRecord, ":Z_PIXEL_DIM_COORD")
#     z_pixel_dim_coord_extent_sp = Cpt(LongoutRecord, ":Z_PIXEL_DIM_COORD_EXTENT_SP")
#     z_pixel_dim_coord_modulus_mon = Cpt(LonginRecord, ":Z_PIXEL_DIM_COORD_MODULUS_MON")
#     z_pixel_dim_coord_modulus_sp = Cpt(LongoutRecord, ":Z_PIXEL_DIM_COORD_MODULUS_SP")
#     z_pixel_dim_hyst_sp = Cpt(AoRecord, ":Z_PIXEL_DIM_HYST_SP")
#     z_pixel_dim_origin_sp = Cpt(AoRecord, ":Z_PIXEL_DIM_ORIGIN_SP")
#     z_pixel_dim_pitch_range_0 = Cpt(AiRecord, ":Z_PIXEL_DIM_PITCH_RANGE_0")
#     z_pixel_dim_pitch_range_1 = Cpt(AiRecord, ":Z_PIXEL_DIM_PITCH_RANGE_1")
#     z_pixel_dim_pitch_sp = Cpt(AoRecord, ":Z_PIXEL_DIM_PITCH_SP")
#     z_pixel_num_sp = Cpt(LongoutRecord, ":Z_PIXEL_NUM_SP")
#     z_pos_dim_name = Cpt(VsinRecord, ":Z_POS_DIM_NAME")
#     z_pos_dim_pos = Cpt(AiRecord, ":Z_POS_DIM_POS")
#     z_pos_dim_source_sp = Cpt(VsoutRecord, ":Z_POS_DIM_SOURCE_SP")
#     z_pos_dim_unit = Cpt(VsinRecord, ":Z_POS_DIM_UNIT")
# 
#     
# class Scanparms2pos(Device):
#     ...
#     scanparms = Cpt(ScanparmRecord, ":scanParms")
#     scanparms_p2 = Cpt(ScanparmRecord, ":scanParms_p2")
