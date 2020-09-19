# new = DrugClass(name=name, )


first_generation_antihistamine = ["<br /><b>Avoid</b><br />"\
                  "<br />Highly anticholinergic; clearance reduced with advanced age,and tolerance develops when used as "\
                  "hypnotic; risk of confusion, dry mouth, constipation, "\
                  "and other anticholinergic effects or toxicity.<br />"\
                  "Use of diphenhydramine in situations such as acute treatment of "\
                  "severe allergic reaction may be appropriate."\
                  "<br /><br /><b>QE = Moderate; SR = Strong</b>", 
                  "<br />Stop if prolonged use (longer than 1 week) due to risk of sedation and anti-cholinergic side effects<br /><br />"\
                  "<b>Anticholinergic Drug Burden (ADB) score: 3</b>", 1]

antiparkinsonian_agents = ["<br /><b>Avoid</b><br />"\
"<br />Not recommended for prevention of extrapyramidal symptoms with antipsychotics; more-effective agents available for treatment of Parkinson disease."\
"<br /><br /><QE = Moderate; SR = Strong", "</br>No recommendation", 2]                  






antispasmodics = ["<br /><b>Avoid</b><br />"\
"<br />Highly anticholinergic, uncertain effectiveness."\
"<br /><br />QE = Moderate; SR = Strong", "<br />Anticholinergic Drug Burden (ADB) score: 3", 3]

alpha_1_blockers = ["<br /><b>Avoid use as an antihypertensive</b><br /><br />"\
"High risk of orthostatic hypotension; not recommended as routine treatment"\
" for hypertension; alternative agents have superior risk/benefit profile"\
"<br /><br />Avoid in older women who is also taking loop diuretic unless conditions warrant both drugs<br /><br />Increased risk of urinary incontinence "
"in older women<br /><br /><b>QE = Moderate; SR = Strong</b>", "STOP in patients with symptomatic"\
" orthostatic hypotension or micturition syncope (risk of precipitating recurrent syncope)."\
"<br /><br />START in patients with symptomatic prostatism, where prostatectomy is"\
"not considered necessary.", 4]

central_alpha_agonists = ["<br /><b>Avoid clonidine as first-line antihypertensive.</b> "\
"Avoid others as listed<br /><br />High risk of adverse CNS effects; may cause bradycardia "\
"and orthostatic hypotension; not recommended as routine treatment for hypertension"\
"<br /><br />QE = Low; SR = Strong", "<br /><b>STOP unless clear intolerance of, or lack of "\
"efficacy with, other classes of antihypertensives</b> (centrally-active "\
"antihypertensives are generally less well tolerated by older people than younger people).", 5]

antiarrhythmic = ["<br />See medication list", "<br />See medication list", 6]

dig = ["<br /><b>Avoid as first-line therapy for atrial fibrillation. Avoid"\
" as first line therapy for heart failure. </b>If used for atrial fibrillation or"\
" heart failure, avoid dosages > 0.125 mg/d"\
"<br /><br />Use in atrial fibrillation: should not be used as a first-line agent"\
"in atrial fibrillation, because more-effective alternatives exist"\
" and it may be associated with increased mortality"\
"<br /><br />Use in heart failure: questionable effects on risk of hospitalization"\
" and may be associated with increased mortality in older adults "\
"with additional benefit and may increase risk of toxicity<br /><br />"\
"Decreased renal clearance of digoxin may lead to increased risk of toxic "\
"effects; further dose reduction may be necessary in those with Stage 4 "\
"or 5 chronic kidney disease.<br /><br />"\
"QE = Atrial fibrillation: moderate. Heart failure: low.<br /><br />"\
"Dosage > 0.125 mg/d: moderate; SR = Atrial fibrillation: strong.<br /><br />"\
"Heart failure: strong. Dosage >0.125 mg/d: strong", 
"<br /><b>STOP:<br /><br />-for heart failure with normal systolic ventricular function</b>"\
"(no clear evidence of benefit)<br /><br />-for left systolic ventricular dysfunction, "\
"where key interventions have not previously been tried<br /><br />-at a long-term dose "\
"greater than 125 micrograms per day if eGFR less than 30 ml/min/1.73m2 "\
"(risk of toxicity if digoxin plasma levels not measured as eGFR may not be an "\
"accurate indicator of clearance).<br /><br />"\
"Anticholinergic Drug Burden (ACB) score: 1", 6]
####
ami = ["<br /><b>Avoid amiodarone as first-line therapy for atrial fibrillation unless "\
"the patient has heart failure or substantial left ventricular hypertrophy</b><br /><br />"\
"Amiodarone is effective for maintaining sinus rhythm but has greater toxicities "\
"than other antiarrhythmics used in atrial fibrillation; it may be reasonable "\
"first-line therapy in patients with concomitant heart failure or substantial "\
"left ventricular hypertrophy if rhythm control is preferred over rate control<br /><br />"\
"QE = High; SR = Strong", "<br /><b>STOP as first-line antiarrhythmic therapy in supraventricular"\
" tachyarrhythmias</b> (higher risk of side-effects than beta-blockers, digoxin, verapamil"\
" or diltiazem), following review and recommendation by specialist team.", 6]

PDE5Is = ["<br />No recommendation", "<br />STOP Phosphodiesterase type-5 inhibitors (e.g. "
"sildenafil, tadalafil) in severe heart failure characterised by hypotension "
"i.e. systolic BP below 90 mmHg, or concurrent nitrate therapy for angina "
"(risk of cardiovascular collapse)", 7]

antidepressants = ["<br /><b>Avoid</b><br /><br />Highly anticholinergic, sedating, and cause orthostatic "\
"hypotension; safety profile of low-dose doxepin (<6mg/d) comparable with that of placebo"\
"<br /><br />QE = High; SR = Strong<br /><br />Avoid total of 3 or more CNS-active drugs "
"; minimize number of CNS active drugs<br /><br />Increased risk of falls and fractures"
"<br /><br />QE = Moderate; SR = Strong", "<br />STOP Tricyclic antidepressants (TCA) (particularly Dosulepin) in patients: "\
"<br /><br />-with dementia (risk of worsening cognitive impairment)."\
"<br />-with glaucoma (likely to exacerbate glaucoma)."\
"<br />-with cardiac conductive abnormalities (pro-arrhythmic effects)."\
"<br />-with constipation or medication likely to exacerbate constipation, following review (likely to worsen constipation)."\
"<br />-with prostatism or prior history of urinary retention (risk of urinary retention)."\
"<br /><br />START (non TCA) antidepressant in the presence of moderate-severe depressive "\
"symptoms lasting at least three months (higher risk of adverse drug reactions with TCAs than with SSRIs or SNRIs)."\
"<br /><br />START SSRI (or SNRI if SSRI is contra-indicated) for persistent severe anxiety that "\
"interferes with independent functioning, or for social anxiety disorder where "\
"patient declines cognitive behavioural therapy", 8]

antipsychotics = ["<br /><b>Avoid for both typical and atypical antipsychotics "\
"except for schizophrenia, bipolar disorder, or short-term use as antiemetic during chemotherapy</b>"\
"<br /><br />Increased risk of cerebrovascular accident (stroke) and greater "\
"rate of cognitive decline and mortality in persons with dementia"\
"<br /><br />Avoid antipsychotics for behavioral problems of dementia and or delirium "\
"unless nonpharmacological options (e.g., behavioral interventions) have failed "\
"or are not possible and the older adult is threatening substantial harm to self or others"\
"<br /><br />QE = Moderate; SR = Strong<br /><br />Avoid total of 3 or more CNS-active drugs "
"; minimize number of CNS active drugs<br /><br />Increased risk of falls and fractures"
"<br /><br />QE = Moderate; SR = Strong", "<br />STOP if"
"<br /><br />-long-term (beyond 1 month) as hypnotics (risk of confusion, hypotension, "
"extra-pyramidal side effects, falls)."
"<br /><br />-long-term (beyond 1 month) in those with Parkinsonism or Lewy Body Disease "
"(likely to worsen extra-pyramidal symptoms)."
"<br /><br />-if fallen in past 3 months (may cause gait dyspraxia, Parkinsonism)."
"<br /><br />-With moderate marked antimuscarinic/anticholinergic effects. "
"(chlorpromazine, clozapine, flupenthixol, flupenzine, pipothiazine, promazine, zuclopenthixol) "
"<br /><br />-with a history of prostatism or previous urinary retention (high risk of "
"urinary retention)."
"<br /><br />-In patients with behavioural and psychological symptoms of dementia (BPSD) "
"unless symptoms are severe and other non-pharmacological treatments have failed "
"(increased risk of stroke)."
"<br /><br />-As hypnotics, unless sleep disorder is due to psychosis or dementia (risk of "
"confusion, hypotension, extra-pyramidal side effects, falls).", 9]

barbiturates = ["<br /><b>Avoid</b><br /><br />High rate of physical dependence, tolerance to sleep benefits, "\
"greater risk of overdose at low dosages<br /><br />QE = High; SR = Strong", "<br />No recommendation", 10]



benzos = ["<br /><b>Avoid</b><br /><br />Older adults have increased sensitivity to benzodiazepines "\
"and decreased metabolism of long-acting agents; in general, all benzodiazepines "\
"increase risk of cognitive impairment, delirium, falls, fractures, and motor "\
"vehicle crashes in older adults<br /><br />May be appropriate for seizure disorders, "\
"rapid eye movement sleep disorders, benzodiazepine withdrawal, ethanol withdrawal, "\
"severe generalized anxiety disorder, and periprocedural anesthesia"\
"<br /><br />QE = Moderate; SR = Strong<br /><br />Avoid total of 3 or more CNS-active drugs "
"; minimize number of CNS active drugs<br /><br />Increased risk of falls and fractures"
"<br /><br />QE = High; SR = Strong", "<br />STOP for patients:<br /><br />-with acute or chronic "\
"respiratory failure i.e. pO2 less than 8.0 kPa and/ or pCO2 greater than 6.5 kPa "\
"(risk of exacerbation of respiratory failure)."\
"<br /><br />-if fallen in past 3 months."\
"<br /><br />-for longer than 4 weeks (no indication for longer treatment; risk of prolonged "\
"sedation, confusion, impaired balance, falls, road traffic accidents; all "\
"benzodiazepines/hypnotics should be withdrawn gradually if taken for more "\
"than 4 weeks as there is a risk of causing a withdrawal syndrome if stopped abruptly).", 11]

nbd = ["<br /><b>Avoid</b><br /><br />Benzodiazepine-receptor agonists have adverse events similar "\
"to those of benzodiazepines in older adults (e.g., delirium, falls, fractures); "\
"increased emergency room visits/hospitalizations; motor vehicle crashes; "\
"minimal improvement in sleep latency and duration<br /><br />QE = Moderate; SR = Strong",
"<br />No recommendation", 12]

androgens = ["<br /><b>Avoid unless indicated for confi rmed hypogonadism with clinical symptoms<b>"\
"<br /><br />Potential for cardiac problems; contraindicated in men with prostate cancer"\
"<br /><br />QE = Moderate; SR = Weak", "<br />STOP in the absence of primary or secondary "\
"hypogonadism (risk of androgen toxicity; no proven benefit outside of the hypogonadism indication).", 13]

estrogens = ["<br /><b>Avoid oral and topical patch.</b> Vaginal cream or tablets: acceptable "\
"to use low-dose intravaginal estrogen for management of dyspareunia, lower "\
"urinary tract infections, and other vaginal symptoms"\
"<br /><br />Evidence of carcinogenic potential (breast and endometrium); lack of "\
"cardioprotective effect and cognitive protection in older women."\
"<br /><br />Evidence indicates that vaginal estrogens for the treatment of vaginal "\
"dryness are safe and effective; women with a history of breast cancer who do "\
"not respond to nonhormonal therapies are advised to discuss the risk and "\
"benefits of low-dose vaginal estrogen (dosages of estradiol <25 mcg twice weekly) "\
"with their health care provider<br /><br />QE = Oral and patch: high. Vaginal cream or tablets: moderate."\
"<br /><br />SR = Oral and patch: strong. Topical vaginal cream or tablets: weak", 
"<br />STOP in patients:<br /><br />-with a history of breast cancer or venous thromboembolism (increased risk of recurrence)."\
"<br /><br />-without progestogen in patients with intact uterus (risk of endometrial cancer)"\
"<br /><br />START Topical vaginal oestrogen or vaginal oestrogen pessary for symptomatic atrophic vaginitis", 14]

insulin = ["<br />See insulin", "<br />See insulin", 15]

ppi = ["<br /><b>Avoid scheduled use for >8 weeks unless for high-risk patients</b>"
"(e.g. oral corticosteroids or chronic NSAID use), erosive esophagitis, "
"Barretts esophagitis, pathological hypersecretory condition, or demonstrated "
"need for maintenance treatment(e.g. due to failure of drug discontinuation trial "
"or H2 blockers)<br /><br />Increased risk of C difficile infection and bone loss and fractures"
"<br /><br />QE = High; SR = Strong", "<br />STOP for uncomplicated peptic ulcer disease at "
"full therapeutic dosage after 1-2 months (if healed, offer low dose maintenance "
"treatment, possibly on an as required basis - review at least annually)."
"<br /><br />START:<br /><br />-at full dose, long term (initially 8 weeks, if symptoms resolve "
"consider full dose maintenance, review annually) with severe grade oesophagitis "
"or oesophageal stricture requiring dilation."
"<br /><br />-for patients on medication with risk of gastric bleeding eg. "
"antiplatelets, SSRIs, venlafaxine, corticosteroids, NSAIDs (particularly if "
"in combination where unavoidable).", 16]

nsaids = ["<br /><b>Avoid chronic use, unless other alternatives are not effective</b> "
"and patient can take gastroprotective agent (proton-pump inhibitor or misoprostol)"
"<br /><br />Increased risk of gastrointestinal bleeding or peptic ulcer "
"disease in high-risk groups, including those aged >75 or "
"taking oral or parenteral corticosteroids, anticoagulants, or "
"antiplatelet agents; use of proton-pump inhibitor or misoprostol "
"reduces but does not eliminate risk. Upper gastrointestinal "
"ulcers, gross bleeding, or perforation caused by NSAIDs occur "
"in approximately 1 percent of patients treated for 3 to 6 months and in "
"2 to 4 percent of patients treated for 1 year, these trends continue with longer duration of use"
"<br /><br />QE = Moderate; SR = Strong", "<br />STOP in patients:"
"<br /><br />-with history of peptic ulcer disease or gastrointestinal bleeding, unless with "
"concurrent, appropriate gastroprotection (risk of peptic ulcer relapse)."
"<br /><br />-with concurrent oral corticosteroid, antiplatelet (especially Aspirin) or "
"antidepressant (SSRI, Venlafaxine) without concurrent, appropriate "
"gastroprotection (increased risk of peptic ulcer disease)."
"<br /><br />-with severe or uncontrolled hypertension (risk of exacerbation of hypertension)"
"<br /><br />-with moderate-severe heart failure (risk of exacerbation of heart failure). Do "
"not use Diclofenac or a COX-2 selective agent at any stage of heart failure."
"<br /><br />-long-term (beyond 3 months) for symptom relief of musculoskeletal pain "
"where simple analgesia and/ or topical NSAID (where appropriate) has not "
"been tried (may be as effective for pain relief)."
"<br /><br />-if eGFR less than 50 ml/min/1.73m2 (risk of deterioration in renal function)."
"<br /><br />-with warfarin or NOAC (risk of gastrointestinal bleeding).", 17]

muscle_relaxants = ["<br /><b>Avoid</b><br /><br />Most muscle relaxants poorly tolerated by older "
"adults because some have anticholinergic adverse effects, sedation, increased "
"risk of fractures; effectiveness at dosages tolerated by older adults questionable"
"<br /><br />QE = Moderate; SR = Strong", "<br />No recommendation", 18]

acei = ["<br />When administered with amiloride or triamterene:<br /><br />Avoid routine use, "
"reserve for patients with demonstrated hypokalemia while taking an ACEI"
"<br /><br />Increased risk of hyperkalemia<br /><br />QE = Moderate; SR = Strong", 
"<br />STOP:<br /><br />-in patients with hyperkalaemia<br /><br />-in combination "
"with other ACEIs or AIIRAs (limited evidence of benefit) unless under "
"specialist review and recommendation."
"<br /><br />START:<br /><br />-with systolic heart failure and/or documented coronary artery disease.", 19]

anticholinergic = ["<br /><b>Avoid combination with other anticholinergic or minimize "
"number of anticholinergic drugs</b><br /><br />Increased risk of cognitive decline"
"<br /><br />QE = Moderate; SR = Strong", "<br />STOP:<br /><br />-to treat extra-pyramidal side-effects "
"of antipsychotic medications (risk of anticholinergic toxicity)"
"<br /><br />-In patients with delirium or dementia (risk of exacerbation of cognitive "
"impairment<br /><br />-patients with dementia, or chronic cognitive impairment "
"(risk of increased confusion, agitation)<br /><br />-In patients with narrow-angle "
"glaucoma (risk of acute exacerbation of glaucoma)"
"<br /><br />-In patients with chronic prostatism (risk of urinary retention).", 20]

corticosteroid = ["<br />When administered with NSAIDs:<br /><br />Avoid; if not possible, provide "
"gastrointestinal protection<br /><br />Increased risk of peptic ulcer disease or "
"gastrointestinal bleeding<br /><br />QE = Moderate; SR = Strong", "<br />-STOP Systemic "
"corticosteroids instead of inhaled corticosteroids for maintenance therapy "
"in moderate-severe COPD (unnecessary exposure to long-term side effects of "
"systemic corticosteroids and effective inhaled therapies are available)"
"<br /><br />-STOP long-term corticosteroids (longer than 3 months) as monotherapy for "
"rheumatoid arthritis (risk of systemic corticosteroid side-effects)."
"<br /><br />-STOP corticosteroids (other than periodic intra-articular injections for "
"mono-articular pain) for osteoarthritis (risk of systemic corticosteroid "
"side-effects).", 21]

lithium = ["<br />See lithium", "<br />See lithium", 22]

theophylline = ["<br />When adminstered with Cimetidine:<br /><br />Avoid<br /><br />Increased risk "
"of theophylline toxicity<br /><br />QE = Moderate; SR = Strong", "<br />STOP Theophylline as "
"monotherapy for Asthma or COPD (safer, more effective alternative; risk of "
"adverse effects due to narrow therapeutic index).", 23]

anticoagulants = ["<br />See medication list", "<br />See medication list", 24]

warfarin = ["<br />When administered with amiodarone: Avoid when possible; monitor "
"INR closely<br /><br />Increased risk of bleeding<br /><br />QE = Moderate; SR = Strong"
"<br /><br />When administered with NSAIDs: Avoid when possible; if used together, monitor "
"for bleeding closely<br /><br />Increased risk of bleeding<br /><br />QE = High; SR = Strong",
"<br />STOP in patients:<br /><br />-for first deep vein thrombosis without continuing "
"provoking risk factors (e.g.thrombophilia) for longer than 6 months "
"(no proven added benefit)<br /><br />-for first pulmonary embolus without continuing "
"provoking risk factors (e.g.thrombophilia) for longer than 12 months "
"(no proven added benefit).", 24]

loop_diuretic = ["<br />No recommendation", "<br />STOP:<br /><br />-as treatment for hypertension "
"(safer, more effective alternatives available)."
"<br /><br />-for dependent ankle oedema without clinical, biochemical evidence or "
"radiological evidence of heart failure, liver failure, nephrotic syndrome or "
"renal failure (leg elevation and/ or compression hosiery usually more appropriate)", 25]

thiazide_diuretic = ["<br />No recommendation", "<br />STOP Thiazide diuretic in patients with "
"current significant hypokalaemia (i.e. serum K+ less than 3.0 mmol/L), "
"hyponatraemia (i.e. serum Na+ less than 130 mmol/L) hypercalcaemia (i.e. corrected "
"serum calcium greater than 2.65 mmol/L) or with recent/ concurrent gout "
"(hypokalaemia, hyponatraemia, hypercalcaemia and gout can be precipitated "
"by thiazide diuretic)", 26]

aldosterone_antagonists = ["<br />No recommendation", 
"<br />STOP Aldosterone antagonists (e.g. spironolactone, eplerenone), AIIRAs "
"particularly if coprescribed with potassium-conserving drugs (e.g. ACEIs, "
"amiloride, triamterene) without "
"monitoring of serum potassium (risk of dangerous hyperkalaemia i.e. greater "
"than 6 mmol/L, serum K should be monitored regularly, i.e. at least every 6 months).", 27]

beta_blockers = ["<br />No recommendation", "<br />STOP non-selective beta-blocker with a "
"recent history of bradycardia, heart block or uncontrolled heart failure; or "
"asthma requiring treatment (risk of increased bronchospasm)."
"<br /><br />STOP non-selective beta-blocker (whether oral or topical for glaucoma) "
"with a recent history of bradycardia, heart block or uncontrolled heart "
"failure; or asthma requiring treatment (risk of increased bronchospasm)."
"<br /><br />START appropriate beta-blocker with stable systolic heart failure.", 28]

ams = ["<br />No recommendation", "<br />STOP anti-muscarinic "
"bronchodilators (e.g. ipratropium, tiotropium) in patients with a history of narrow angle "
"glaucoma (may exacerbate glaucoma) or bladder outflow obstruction"
"(may cause urinary retention).", 29]

phenothiazines = ["<br /><b>Avoid in patients with chronic seizures or epilepsy"
"</b><br /><br />Lowers seizure threshold; may be acceptable in individuals with well "
"controlled seizures in whom alternative agents have not been effective"
"<br /><br />QE = Low; SR = Strong", "<br />STOP:<br /><br />-in patients with epilepsy (may lower "
"seizure threshold)."
"<br /><br />-As first-line treatment, since safer and more efficacious alternatives exist "
"(phenothiazines are sedative, have significant anti-muscarinic toxicity in older "
"people), with the exception of prochloprerazine for nausea/vomiting/vertigo, "
"chlorpromazine for relief of persistent hiccoughs and levomepromazine as an "
"anti-emetic in palliative care).", 30]

opioids = ["<br /><b>Avoid use of total of 3 or more CNS-active drugs; minimize number of "
"CNS drugs</b><br /><br />Increased risk of falls<br /><br />QE = High; SR = Strong", "<br />STOP:"
"<br /><br />-Use of long-term strong opioids as first line therapy for mild-moderate pain "
"(WHO analgesic ladder not observed)."
"<br /><br />-Regular opioids for more than 2 weeks in those with chronic constipation "
"without concurrent use of laxatives (risk of severe constipation)."
"<br /><br />-Long-term in those with dementia unless for palliative care or management "
"of chronic pain syndrome (exacerbation of cognitive impairment)."
"<br /><br />-Long-term in those with recurrent falls (risk of drowsiness, postural "
"hypotension, vertigo)."
"<br /><br />-Slow-release opioids in severe pain without short-acting opioids for "
"breakthrough pain (risk of persistence of severe pain)."
"<br /><br />START strong opioids in moderate-severe pain, where paracetamol, NSAIDs "
"or weak opioids are not appropriate to the pain severity or have been "
"ineffective. Use morphine first line.", 31]

acetylcholinesterase_inhibitors = ["<br /><b>Avoid in patients with syncope</b><br /><br />"
"Increases risk of orthostatic hypotension or bradycardia<br /><br />"
"QE = moderate; SR = strong", "<br />STOP acetylcholinesterase inhibitors with a "
"known history of persistent bradycardia(below 60 beats/min.), heart block or "
"recurrent unexplained syncope or concurrent treatment with drugs that reduce "
"heart rate such as beta-blockers, digoxin, diltiazem, verapamil "
"(risk of cardiac conduction failure, syncope and injury)."
"<br /><br />START acetylcholinesterase inhibitor (e.g. donepezil, rivastigmine, "
"galantamine or Memantine if others not tolerated) for mild-moderate "
"Alzheimers dementia or Lewy Body dementia (rivastigmine) following review "
"and recommendation by specialist team. Use donepezil first line", 32]

bisphosphonates = ["<br />No recommendation", "<br />STOP Bisphosphonates:"
"<br /><br />-if greater than 5 years treatment duration (for drug holiday), after "
"discussion of risks and benefits."
"<br /><br />-if unexplained thigh, hip or groin pain is reported, after discussion "
"of risks and benefits."
"<br /><br />-given orally in patients with a current or recent history of upper "
"gastrointestinal disease i.e. dysphagia, oesophagitis, gastritis, duodenitis, "
"or peptic ulcer disease, or upper gastrointestinal bleeding (risk "
"of relapse/exacerbation of oesophagitis, oesophageal ulcer, oesophageal stricture)."
"<br /><br />-in patients considered at low fracture risk(FRAX assessment tool)."
"<br /><br />START bisphosphonates and vitamin D and calcium (where dietary calcium is"
"intake inadequate) in patients taking long-term systemic glucocorticosteroid "
"therapy(greater than or equal to 7.5 mg prednisolone per day (or equivalent) "
"for 3 months or more)", 33]

antiplatelets = ["<br />See medication list", "<br />See medication list", 34]

antibiotics = ["<br />See medication list", "<br />See medication list", 35]

ccb = ["<br />See medication list", "<br />See medication list", 36]


tranquilizers = ["<br /><b>Avoid</b><br /><br />High rate of physical dependence; very sedating<br /><br />QE = Moderate; SR = Strong",
                     "<br />No recommendation", 37]

Antineoplastics = ["<br />See medication list", "<br />See medication list", 38]

sulfonylureas = ["<br />See medication list", "<br />See medication list", 39]

prokinetic = ["<br />See medication list", "<br />See medication list", 40]

mineral_oil = ["<br /><b>Avoid</b><br /><br />Potential for aspiration and adverse effects; "
"safer alternatives available<br /><br />QE = Moderate; SR = Strong", "<br />No recommendation", 41]

antacids = ["<br />No recommendation", "<br />STOP Simple antacids for long term, "
"frequent dose, continuous prescribing of simple antacids (relieves symptoms "
"in the short term rather than preventing them).", 42]

biguanides = ["<br />See Metformin", "<br />See Metformin", 43]

RANK_ligand_inhibitors = ["<br />See denosumab", "<br />See denosumab", 44]

anti_gout_agents = ["<br />See medication list", "<br />See medication list", 45]


   
    
    
    
  


drug_classes = {'H1 antihistamine': first_generation_antihistamine,
'Antiparkinsonian_agents': antiparkinsonian_agents,
'Antispasmodics': antispasmodics,
"Alpha 1 Blockers": alpha_1_blockers,
"Central Alpha Agonists": central_alpha_agonists,
"Antiarrhythmic": antiarrhythmic,
"PDE5 Inhibitors": PDE5Is,
"Antidepressants": antidepressants,
"Antipsychotics": antipsychotics,
"Barbiturates": barbiturates,

"Benzodiazepines": benzos,
"Benzodiazepine-receptor agonists": nbd,
"Androgens": androgens,
"Estrogens": estrogens,
"Insulin": insulin,
"Proton Pump Inhibitors": ppi,
"NSAIDs": nsaids,
"Muscle Relaxants": muscle_relaxants,
"ACE Inhibitors": acei,
"Anticholinergics": anticholinergic,

"Corticosteroid": corticosteroid,
"Lithium": lithium,
"Theophylline": theophylline,
"Anticoagulants": anticoagulants,
"Loop Diuretic": loop_diuretic,
"Thiazide Diuretic": thiazide_diuretic,
"Aldosterone antagonists": aldosterone_antagonists,
"Beta Blockers": beta_blockers,
"Muscarinic antagonist": ams,
"Phenothiazines": phenothiazines,

"Opioids": opioids,
"Acetylcholinesterase inhibitors": acetylcholinesterase_inhibitors,
"Bisphosphonates": bisphosphonates,
"Antiplatelets": antiplatelets,
"Antibiotics": antibiotics,
"Calcium channel blockers": ccb,
"Tranquilizers": tranquilizers,
"Antineoplastics": Antineoplastics,
"Sulfonylureas": sulfonylureas,
"Prokinetic agents": prokinetic,

"Mineral oil": mineral_oil,
"Antacids": antacids,
"Biguanides": biguanides,
"RANK ligand inhibitors": RANK_ligand_inhibitors,
"Anti-Gout agents": anti_gout_agents

}

medications = {
    "Brompheniramine" : first_generation_antihistamine,
    "Carbinoxamine" : first_generation_antihistamine,
    "Clemastine" : first_generation_antihistamine,
    "Cyproheptadine" : first_generation_antihistamine,
    "Dexbrompheniramine" : first_generation_antihistamine,
    "Dexchlorpheniramine" : first_generation_antihistamine,
    "Dimenhydrinate" : first_generation_antihistamine,
    "Diphenhydramine" : first_generation_antihistamine,
    "Doxylamine" : first_generation_antihistamine,
    "Hydroxyzine" : first_generation_antihistamine,
    "Meclizine" : first_generation_antihistamine,
    "Promethazine" : first_generation_antihistamine,
    "Triprolidine" : first_generation_antihistamine,
    "Benztropine" : antiparkinsonian_agents,
    "Trihexyphenidyl" : antiparkinsonian_agents,
    "Atropine" : ["<br /><b>Avoid (excludes opthalmic)</b><br />"\
"<br />Highly anticholinergic, uncertain effectiveness."\
"<br /><br />QE = Moderate; SR = Strong", "<br />Anticholinergic Drug Burden (ADB) score: 3", 20],
    "Belladonna" : antispasmodics,
    "Clidinium " : antispasmodics,
    "Dicyclomine" : antispasmodics,
    "Hyoscyamine" : antispasmodics,
    "Propantheline" : antispasmodics,
    "Scopolamine" : antispasmodics,
    "Dipyridamole" : ["<br />Only applies to oral short-acting (does not apply to the extended release combination with aspirin)"\
"<br /><br />Avoid<br /><br />May cause orthostatic hypotension; more effective alternatives available;"\
"IV form acceptable for use in cardiac stress testing"\
"<br /><br />QE = Moderate; SR = Strong", "<br />STOP if patient presents with concurrent"\
"significant bleeding risk, i.e. uncontrolled severe hypertension,"\
" bleeding diathesis, recent non-trivial spontaneous bleeding (high risk of bleeding).", 34],

    "Ticlopidine" : ["<br /><b>Avoid</b><br /><br />Safer, effective alternatives available"\
"<br /><br />QE = Moderate; SR = Strong", "<br />No recommendation", 34],

    "Nitrofurantoin" : ["<br /><b>Avoid in individuals with creatinine clearance <30 mL/min"\
" or for long-term suppression of bacteria.</b><br /><br />"\
"Potential for pulmonary toxicity, hepatoxicity, and peripheral"\
"neuropathy, especially with long-term use; safer alternatives available"\
"<br /><br />QE = Low; SR = Strong", "<br />No recommendation", 35],

    "Doxazosin" : alpha_1_blockers,
    "Prazosin" : alpha_1_blockers,
    "Terazosin" : alpha_1_blockers,
    "Clonidine" : central_alpha_agonists,
    "Guanabenz" : central_alpha_agonists,
    "Guanfacine" : central_alpha_agonists,
    "Methyldopa" : central_alpha_agonists,
    "Reserpine" : central_alpha_agonists,
    "Disopyramide" : ["<br /><b>Avoid</b><br /><br />Disopyramide is a potent negative inotrope and "\
"therefore may induce heart failure in older adults; strongly anticholinergic; "\
"other antiarrhythmic drugs preferred<br /><br />QE = Low; SR = Strong", "<br />No recommendation", 6],

    "Dronedarone" : ["<br /><b>Avoid in individuals with permanent atrial fibrillation "\
"or severe or recently decompensated heart failure</b><br /><br />Worse outcomes have been "\
"reported in patients taking dronedarone who have permanent atrial fibrillation "\
"or severe or recently decompensated heart failure<br /><br />QE = High; SR = Strong",
"<br />No recommendation", 6],
    "Digoxin" : dig,
    "Nifedipine" : ["<br /><b>For immediate release: Avoid</b><br /><br />Potential for hypotension; "\
"risk of precipitating myocardial ischemia<br /><br />QE = High; SR = Strong", "<br />No recommendation", 36],
    "Amiodarone": ami,
    "Amitriptyline": antidepressants,
    "Amoxapine" : antidepressants,
    "Clomipramine" : antidepressants,
    "Desipramine" : antidepressants,
    "Doxepin" : antidepressants,
    "Imipramine" : antidepressants,
    "Nortriptyline" : antidepressants,
    "Paroxetine" : antidepressants,
    "Protriptyline" : antidepressants,
    "Trimipramine" : antidepressants,
    "Aripiprazole" : antipsychotics,
    "Asenapine" : antipsychotics,
    "Cariprazine" : antipsychotics,
    "Clozapine" : antipsychotics,
    "Lurasidone": antipsychotics,
    "Olanzapine": antipsychotics, 
    "Quetiapine": antipsychotics, 
    "Risperidone": antipsychotics, 
    "Ziprasidone": antipsychotics,   
    "Amobarbital" : barbiturates,
    "Butabarbital" : barbiturates,
    "Butalbital" : barbiturates,
    "Mephobarbital" : barbiturates,
    "Pentobarbital" : barbiturates,
    "Phenobarbital" : barbiturates,
    "Secobarbital" : barbiturates,
    "Alprazolam" : benzos,
    "Estazolam" : benzos,
    "Lorazepam" : benzos,
    "Oxazepam" : benzos,
    "Temazepam" : benzos,
    "Triazolam" : benzos,
    "Clorazepate" : benzos,
    "Chlordiazepoxide" : benzos,
    "Clonazepam" : benzos,
    "Diazepam" : benzos,
    "Flurazepam" : benzos,
    "Quazepam" : benzos,
    "Eszopiclone" : nbd,
    "Zolpidem" : nbd,
    "Zaleplon" : nbd,
    "Methyltestosterone" : androgens,
    "Testosterone" : androgens,
    "Insulin" : ["<br /><b>Avoid</b><br /><br />Higher risk of hypoglycemia without improvement in "\
"hyperglycemia management regardless of care setting; refers "
"to sole use of short- or rapid-acting insulins to manage or avoid "
"hyperglycemia in absence of basal or long-acting insulin; does "
"not apply to titration of basal insulin or use of additional short- or "
"rapid-acting insulin in conjunction with scheduled insulin (ie, "
"correction insulin)<br /><br />QE = Moderate; SR = Strong", "<br />No recommendation", 15],
    "Megestrol" : ["<br /><b>Avoid</b><br /><br />Minimal effect on weight; increases risk of thrombotic events "
"and possibly death in older adults<br /><br />QE = Moderate; SR = Strong", "<br />No recommendation", 38],
    "Glyburide" : ["<br /><b>Avoid</b><br /><br />Higher risk of severe prolonged hypoglycemia in older adults"
"<br /><br />QE = High; SR = Strong", "<br />STOP Sulfonylureas with a long duration of action "
"(e.g. glibenclamide, chlorpropamide, glimepiride) with type 2 diabetes mellitus "
"(risk of prolonged hypoglycaemia).", 39],
    "Chlorpropamide" : ["<br /><b>Avoid</b><br /><br />Prolonged half-life in older adults; can cause "
"prolonged hypoglycemia; causes SIADH<br /><br />QE = High; SR = Strong", "<br /><b>Avoid</b><br /><br /> "
"higher risk of severe prolonged hypoglycemia in older adults"
"<br /><br />QE = High; SR = Strong", "STOP Sulfonylureas with a long duration of action "
"(e.g. glibenclamide, chlorpropamide, glimepiride) with type 2 diabetes mellitus "
"(risk of prolonged hypoglycaemia).", 39],

    "Metoclopramide" : ["<br /><b>Avoid, unless for gastroparesis</b><br /><br />"
"Can cause extrapyramidal effects, including tardive dyskinesia; "
"risk may be greater in frail older adults<br /><br />QE = Moderate; SR = Strong",
"<br />STOP in patients:<br /><br />-with Parkinsonism (risk of exacerbating symptoms)."
"<br /><br />-after maximum treatment time of 5 days", 40],
    "Meprazole" : ppi,
    "Omeprazole" : ppi,
    "Lansoprazole" : ppi,
    "Dexlansoprazole" : ppi,
    "Rabeprazole" : ppi,
    "Pantoprazole" : ppi,
    "Esomeprazole" : ppi,
    "Meperidine": ["<br /><b>Avoid, especially in those with chronic kidney disease</b>"
"<br /><br />Not effective oral analgesic in dosages commonly used; may "
"have higher risk of neurotoxicity, including delirium, than other "
"opioids; safer alternatives available<br /><br />QE = Moderate; SR = Strong", "<br />No recommendation", 31],

    "Aspirin": ["<br /><b>Use with caution in adults >80 years old</b><br /><br />"
"Lack of evidence of benefit versus risk in adults >80 years old"
"<br /><br />QE = Low; SR = Strong", "<br />STOP Aspirin if:"
"<br /><br />-Long-term aspirin at doses greater than 160 mg per day (increased risk of "
"bleeding, no evidence for increased efficacy)."
"<br /><br />-with a past history of peptic ulcer disease without concomitant PPI (risk of "
"recurrent peptic ulcer)."
"<br /><br />-in combination with warfarin or NOACs in patients with chronic atrial "
"fibrillation (no added benefit from aspirin)."
"<br /><br />-as monotherapy for stroke prevention in atrial fibrillation."
"<br /><br />-Stop the combination of aspirin plus clopidogrel as secondary stroke "
"prevention, unless the patient has a coronary stent(s) inserted in the "
"previous 12 months or concurrent acute coronary syndrome or has a high grade "
"symptomatic carotid arterial stenosis (no evidence of added benefit over clopidogrel monotherapy).", 34],
    "Diclofenac": nsaids,
    "Diflunisal": nsaids,
    "Etodolac": nsaids,
    "Fenoprofen": nsaids,
    "Ibuprofen": nsaids,
    "Ketoprofen": nsaids,
    "Meclofenamate": nsaids,
    "Mefenamic acid": nsaids,
    "Meloxicam": nsaids,
    "Nabumetone": nsaids,
    "Naproxen": nsaids,
    "Oxaprozin": nsaids,
    "Piroxicam": nsaids,
    "Sulindac": nsaids,
    "Tolmetin": nsaids,
    "Ketorolac": nsaids,
    "Indomethacin": ["<br /><b>Avoid</b><br /><br />Indomethacin is more likely than other NSAIDs to "
"have adverse CNS effects. Of all the NSAIDs, indomethacin has the most adverse effects."
"<br /><br />Increased risk of gastrointestinal bleeding/peptic ulcer disease, "
"and acute kidney injury in older adults<br /><br />QE = Moderate; SR = Strong","<br />STOP in patients:"
"<br /><br />-with history of peptic ulcer disease or gastrointestinal bleeding, unless with "
"concurrent, appropriate gastroprotection (risk of peptic ulcer relapse)."
"<br /><br />-with concurrent oral corticosteroid, antiplatelet (especially Aspirin) or "
"antidepressant (SSRI, Venlafaxine) without concurrent, appropriate "
"gastroprotection (increased risk of peptic ulcer disease)."
"<br /><br />-with severe or uncontrolled hypertension (risk of exacerbation of hypertension)"
"<br /><br />-with moderate-severe heart failure (risk of exacerbation of heart failure). Do "
"not use Diclofenac or a COX-2 selective agent at any stage of heart failure."
"<br /><br />-long-term (beyond 3 months) for symptom relief of musculoskeletal pain "
"where simple analgesia and/ or topical NSAID (where appropriate) has not "
"been tried (may be as effective for pain relief)."
"<br /><br />-if eGFR less than 50 ml/min/1.73m2 (risk of deterioration in renal function)."
"<br /><br />-with warfarin or NOAC (risk of gastrointestinal bleeding).", 17],
    "Carisoprodol": muscle_relaxants,
    "Chlorzoxazone": muscle_relaxants,
    "Cyclobenzaprine": muscle_relaxants,
    "Metaxalone": muscle_relaxants,
    "Methocarbamol": muscle_relaxants,
    "Orphenadrine": muscle_relaxants,
    "Dabigatran": ["<br /><b>Use with caution in adults >75 years old and in patients "
"with CrCl <30 mL/min</b><br /><br />Increased risk of gastrointestinal bleeding compared "
"with warfarin and reported rates with other target-specific oral anticoagulants "
"in adults>75 years old; lack of evidence of effi cacy and safety in "
"individuals with CrCl <30 mL/m<br /><br />QE = Moderate; SR = Strong", "<br />STOP if eGFR "
"less than 30 ml/min/1.73m2 (risk of bleeding).", 24],
    "Prasugrel": ["<br /><b>Use with caution in adults aged >75</b><br /><br />"
"Increased risk of bleeding in older adults; benefit in highest-risk older "
"adults (e.g., those with prior myocardial infarction or diabetes mellitus) may offset risk"
"<br /><br />QE = Moderate; SR = Weak", "<br />START antiplatelet therapy (one of aspirin, "
"clopidogrel, prasugrel or ticagrelor) with a documented history of coronary, "
"cerebral or peripheral vascular disease.", 34],
    "Benazepril": acei,
    "Captopril": acei,
    "Enalapril" : acei, 
    "Fosinopril" : acei,
    "Lisinopril" : acei,
    "Moexipril" : acei,
    "Perindopril" : acei,
    "Quinapril" : acei,
    "Ramipril" : acei,
    "Trandolapril" : acei,
    "Prednisone": corticosteroid,
    "Lithium" : ["<br />When administered with ACEIs or Loop diuretics:<br /><br />Avoid, "
"monitor lithium concentrations<br /><br />Increased risk of lithium toxicity"
"<br /><br />QE = Moderate; SR = Strong", "<br />No recommendation", 22],
    "Theophylline" : theophylline,
    "Domperidone" : ["<br />No recommendation", "<br />STOP in patients:<br /><br />-for treatment "
"other than nausea and vomiting."
"<br /><br />-after maximum treatment time of one week."
"<br /><br />-in patients with serious underlying heart conditions."
"<br /><br />-if receiving other medications known to prolong QT interval or potent "
"CYP3A4 inhibitors.", 20],

    "Chlorothiazide" : thiazide_diuretic,
    "Chlorthalidone" : thiazide_diuretic,
    "Hydrochlorothiazide" : thiazide_diuretic,
    "Indapamide" : thiazide_diuretic,
    "Metolazone" : thiazide_diuretic,
    "Bumetanide" : loop_diuretic,
    "Ethacrynic acid" : loop_diuretic,
    "Furosemide" : loop_diuretic,
    "Torsemide" : loop_diuretic,
    "Spironolactone" : aldosterone_antagonists,
    "Eplerenone" : aldosterone_antagonists,
    "Verapamil" : ["<br /><b>Avoid in Heart failure patients</b><br /><br />Potential to promote "
"fluid retention and exacerbate heart failure<br /><br />QE = Moderate SR = Strong", "<br />STOP in patients with heart failure (may worsen heart failure).", 36],
    "Diltiazem" : ["<br /><b>Avoid in Heart failure patients</b><br /><br />Potential to promote "
"fluid retention and exacerbate heart failure<br /><br />QE = Moderate SR = Strong", "STOP in patients with heart failure (may worsen heart failure).", 36],
    "Acebutolol" : beta_blockers,
    "Atenolol": beta_blockers,
    "Bisoprolol": beta_blockers,
    "Metoprolol": beta_blockers,
    "Nadolol": beta_blockers,
    "Nebivolol": beta_blockers,
    "Propranolol" : beta_blockers,   
    "Ipratropium" : ams,
    "Tiotropium" : ams,
    "Prochlorperazine": phenothiazines,
    "Chlorpromazine": phenothiazines,
    "Fluphenazine": phenothiazines,
    "Perphenazine": phenothiazines,
    "Trifluoperazine": phenothiazines,
    "Thioridazine": phenothiazines,
    "Mesoridazine" : phenothiazines,
    "Codeine": opioids,
    "Hydrocodone": opioids,
    "Morphine" : opioids,
    "Oxycodone" : opioids,
    "Hydromorphone": opioids,
    "Fentanyl" : opioids,  
    "Donepezil": acetylcholinesterase_inhibitors,
    "Tacrine": acetylcholinesterase_inhibitors,
    "Rivastigmine" : acetylcholinesterase_inhibitors,
    "Galantamine": acetylcholinesterase_inhibitors,
    "Memantine": acetylcholinesterase_inhibitors,
    "Ambenonium": acetylcholinesterase_inhibitors,
    "Neostigmine": acetylcholinesterase_inhibitors,  
    "Metformin" : ["<br />No recommendation", "<br />STOP Metformin if eGFR below "
"30 ml/min/1.73m2 (risk of lactic acidosis)", 43],
    "Alendronate": bisphosphonates,
    "Risedronate": bisphosphonates,
    "Ibandronate": bisphosphonates,
    "Zoledronic acid": bisphosphonates,
    "Denosumab" : ["<br />No recommendation", "<br />STOP denosumab in patients:<br /><br />-considered at low "
"fracture risk(FRAX assessment tool)."
"<br /><br />-if patient is unable to have regular dental check ups.", 44],
    "Sildenafil": PDE5Is,
    "Tadalafil": PDE5Is,
    "Warfarin": warfarin,
    "Colchicine" : ["<br />If CrCl < 30, Reduce dose; monitor for adverse effects"
"<br /><br />Gastrointestinal, neuromuscular, bone marrow toxicity"
"<br /><br />QE = Moderate; SR = Strong", "<br />STOP Colchicine (beyond 3 months) for chronic "
"treatment of gout where there is no contraindication to Allopurinol "
"(xanthine-oxidase inhibitors are first choice prophylactic drugs in gout)"
"<br /><br />STOP if eGFR less than 10 ml/min/1.73m2(risk of colchicine toxicity).", 45]}