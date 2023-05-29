from bertopic import BERTopic


docs = [
    "LIST OF TABLES\n\nTable 1. Investigator’s Global Assessment (IGA) Score 62\n\nTable 2. Clinical Sign Severity Scoring Criteria for the Eczema Area and Severity Index (EASI) 63\n\nTable 3. Handprint Determination of Body Surface Area (BSA) 64\n\nTable 4. Eczema Area and Severity Index (EASI) Area Score Criteria 65\n\nTable 5. Eczema Area and Severity Index (EASI) Body Region Weighting 65\n\nTable 6. Protocol-Required Safety Laboratory Assessments 98",
    "LIST OF TABLES\n\nTable 1. Summary of Studies Demonstrating Benefit of Dose-Dense Frontline Chemotherapy and Related Studies 29\n\nTable 2. Most Frequently Reported (Incidence ≥ 2%) Treatment-Related TEAEs in the Pooled Expansion Cohorts and in the Ovarian Cancer Expansion Cohort (Any Grade) 33\n\nTable 3. Most Frequently Reported (in ≥ 2 Patients) Grade ≥ 3 Treatment-Related TEAEs in the Pooled Expansion Cohorts and in the Ovarian Cancer Expansion Cohort 34\n\nTable 4. Unconfirmed Tumor Response Observed in Ovarian Cancer Expansion Cohort 38\n\nTable 5. Dose Modification Levels for Paclitaxel and Carboplatin 65\n\nTable 6. Treatment Modification for Symptoms of Avelumab Infusion-Related Reactions 67\n\nTable 7. Avelumab: Management of Immune-Related Adverse Events 71\n\nTable 8. Modification Instructions for Hematologic Toxicity: Q3W Chemotherapy Regimen 76\n\nTable 9. Modification Instructions for Hematologic Toxicity: Weekly Chemotherapy Regimen 76\n\nTable 10. Avelumab in Combination with Chemotherapy (Arm C) Toxicity Management 79\n\nTable 11. Required Laboratory Tests 90\n\nTable 12. Objective Response Status at each Evaluation 140\n\nTable 13. Objective Response Status at each Evaluation for Patients with Non Target Disease Only 141\n\nTable 14. Overall Response Derived from Changes in Index, Non-index and New Lesions 143\n\nTable 15. Criteria for Chemotherapy Response Score 145",
    "LIST OF TABLES\n\nTable 1. Phase 1b Combination A 1L SCCHN Avelumab + Bempegaldesleukin (NKTR-214) Dose Levels 27\n\nTable 2.  Phase 1b Combination B mCRPC Avelumab, Bempegaldesleukin (NKTR-214), and Talazoparib Dose levels 28\n\nTable 3. Phase 1b Combination C mCRPC Avelumab, Bempegaldesleukin (NKTR-214) and Enzalutamide Dose levels 28\n\nTable 4. SoA for SCCHN Phase 1b and Phase 2 (Combination A): Screening, Cycle 1 and Cycle 2 34\n\nTable 5. SoA for SCCHN Phase 1b and Phase 2 (Combination A): Cycle ≥ 3 and Post-Treatment 41\n\nTable 6. SoA for mCRPC Phase 1b and Phase 2 (Combinations B and C): Screening, Cycle 1 and Cycle 2 47\n\nTable 7. SoA for mCRPC Phase 1b and Phase 2 (Combinations B and C): Cycle ≥ 3 and Post-Treatment 56\n\nTable 8. Phase 1b Combination A 1L SCCHN Avelumab + Bempegaldesleukin (NKTR-214)  Dose Levels 87\n\nTable 9. Phase 1b Combination B mCRPC Avelumab, Bempegaldesleukin (NKTR-214), and Talazoparib Dose levels 87\n\nTable 10. Phase 1b Combination C mCRPC Avelumab, Bempegaldesleukin (NKTR-214), and Enzalutamide Dose levels 89\n\nTable 11. Treatment Modification for Symptoms of Infusion related Reactions Associated with Avelumab 118\n\nTable 12. Treatment Modification for Symptoms of Infusion related Reactions Associated with Bempegaldesleukin (NKTR-214) 119\n\nTable 13. Cerebrovascular Accident Adverse Event Management Algorithm 121\n\nTable 14. Avelumab and Bempegaldesleukin (NKTR-214) Treatment Modifications for Drug Related Toxicity (Excluding Infusion Related Reactions and Immune Related AEs) 123\n\nTable 15. Avelumab + Bempegaldesleukin (NKTR-214) + Talazoparib Triplet Treatment Modifications for Drug Related Toxicity (Excluding Infusion Related Reactions and Immune Related AEs) 126\n\nTable 16. Avelumab + Bempegaldesleukin (NKTR-214) + Enzalutamide Triplet Treatment Modifications for Drug Related Toxicity (Excluding Infusion Related Reactions and Immune Related AEs) 132\n\nTable 17. Management of Immune Related Adverse Events for Avelumab and Bempegaldesleukin (NKTR-214) 136\n\nTable 18. B9991040 Sample Size and Exact 95% Confidence Interval for ORR/PSA Response Rate 171",
    "LIST OF TABLES\n\nTable 1. Recommended Regimen for Oral Corticosteroids 64\n\nTable 2. Recommended Regimen for Combination Intravenous and Oral Corticosteroids 65",
    "LIST OF FIGURES\n\nFigure 1. Study Schematic 16\n\n\n",
    "LIST OF TABLES\n\nTable 1. Efficacy Results from Trials in Similar Patient Population 31\n\nTable 2. Study C1071001: Enrollment Summary 32\n\nTable 3. Study C1071001: TEAEs Occurring in >15% of SC Participants (All Causalities by MedDRA PT and Maximum CTCAE b  Grade in Descending Order of Frequency by Part 1 SC Cohorts; Safety Analysis Set) 35\n\nTable 4. Dose Modifications for Elranatamab-Related Toxicity and for Peripheral Sensory or Motor Neuropathy  a  56\n\nTable 5. Dose Levels for Elranatamab 58\n\nTable 6. Staging Systems for Multiple Myeloma 67\n\nTable 7. Eastern Cooperative Oncology Group (ECOG) Performance Status Scale 70\n\nTable 8. Minimum Number of Participants With Identified Events That Would Prompt Temporary Enrollment Hold (CRS, ICANS, Non-hematologic treatment-related AEs) 92\n\nTable 9. Minimum Number of Participants With Identified Treatment-Related Events That Would Prompt Temporary Enrollment Hold (GBS/GB-like AEs, Peripheral Neuropathy/IR Neurologic AEs) 93\n\nTable 10. Protocol Required Safety Laboratory Assessments 103\n\nTable 11. ASTCT CRS Grading 127\n\nTable 12. Immune Effector Cell-Associated Encephalopathy (ICE) Score 129\n\nTable 13. ASTCT ICANS Grading 129",
    "LIST OF TABLES\n\nTable 1. Study Schedule of Assessments: Part 1 Safety Lead-in 26\n\nTable 2. Study Schedule of Assessments: Part 2 35\n\nTable 3. Efficacy Results from Trials in Similar Patient Population 49\n\nTable 4. Demographic Breakdown of Multiple Myeloma in the US 71\n\nTable 5. Hematological and Non-hematological Treatment-related Dose-limiting Toxicities 74\n\nTable 6. Dose Modifications for Elranatamab-Related Toxicity and for Peripheral Sensory or Motor Neuropathy 91\n\nTable 7. Dose Levels for Elranatamab 93\n\nTable 8. Dose Modifications for Daratumumab-related Toxicity 94\n\nTable 9. Eastern Cooperative Oncology Group (ECOG) Performance Status Scale 111\n\nTable 10. Minimum Number of Participants With Identified Events That Would Prompt Temporary Enrollment Hold (CRS, ICANS, Non-hematologic treatment-related AEs) 139\n\nTable 11. Minimum Number of Participants With Identified Treatment-Related Events That Would Prompt Temporary Enrollment Hold (GBS/GB-like AEs, Peripheral Neuropathy/IR Neurologic AEs) 140\n\nTable 12. Planned Stopping Boundaries for PFS by BICR at Interim Analyses and Final Analysis 141\n\nTable 13. Planned Stopping Boundaries for Overall Survival at Interim Analyses and Final Analysis 142\n\nTable 14. Protocol Required Safety Laboratory Assessments 153\n\nTable 15. ASTCT CRS Grading 180\n\nTable 16. Immune Effector Cell-Associated Encephalopathy (ICE) Score 183\n\nTable 17. ASTCT ICANS Grading 183\n\nTable 18. Staging Systems for Multiple Myeloma 191",
    "LIST OF TABLES\n\nTable 1. Relevant Population Metrics for Multiple Myeloma – US 57\n\nTable 2. Dose Modifications for Elranatamab-Related Toxicity and for Peripheral Sensory or Motor Neuropathy 72\n\nTable 3. Lenalidomide Dose Adjustment for Thrombocytopenia 73\n\nTable 4. Lenalidomide Dose Adjustment for Neutropenia 73\n\nTable 5. Dose Reduction Steps 74\n\nTable 6. Staging Systems for Multiple Myeloma 88\n\nTable 7. ECOG Performance Status Scale 92\n\nTable 8. Safety QTcF Assessment 113\n\nTable 9. Planned Stopping Boundaries for PFS by BICR at Interim Analysis and Final Analysis 114\n\nTable 10. Protocol Required Safety Laboratory Assessments 124\n\nTable 11. ASTCT CRS Grading 152\n\nTable 12. Immune Effector Cell-Associated Encephalopathy (ICE) Score 155\n\nTable 13. ASTCT ICANS Grading 155",
    "LIST OF TABLES\n\nTable 1. Primary and Secondary Endpoint Events and Definitions 78\n\nTable 2. Grading Scale for Local Reactions 93\n\nTable 3. Grading Scale for Systemic Events 94\n\nTable 4. Ranges for Fever 95",
    "LIST OF TABLES\n\nTable 1. Local Reaction Grading Scale 113\n\nTable 2. Systemic Event Grading Scale 114\n\nTable 3. Scale for Fever 115\n\nTable 4. Power Analysis for Noninferiority Assessment 185\n\nTable 5. Probability of Observing at Least 1 AE by Assumed True Event Rates With Different Sample Sizes 187\n\nTable 6. Interim Analysis Plan and Boundaries for Efficacy and Futility 209\n\nTable 7. Statistical Design Operating Characteristics: Probability of Success or Failure for Interim Analyses 210\n\nTable 8. Statistical Design Operating Characteristics: Probability of Success for Final Analysis and Overall 211\n\nTable 9. Laboratory Abnormality Grading Scale 222\n\nTable 10. Stopping Rule: Enrollment Is Stopped if the Number of Severe Cases in the Vaccine Group Is Greater Than or Equal to the Prespecified Stopping Rule Value (S) 242\n\nTable 11. Alert Rule: Further Action Is Taken if the Number of Severe Cases in the Vaccine Group Is Greater Than or Equal to the Prespecified Alert Rule Value (A) 243",
]


topic_model = BERTopic(embedding_model="emilyalsentzer/Bio_ClinicalBERT")
# "microsoft/BiomedNLP-PubMedBERT-base-uncased-abstract-fulltext"
# "emilyalsentzer/Bio_ClinicalBERT"

topics, probs = topic_model.fit_transform(docs)

df = topic_model.get_topic_info()
print(df)

# Write DataFrame to a CSV file
df.to_csv("topics.csv", index=False)