import database_functions as db  #db is an alias


group1 = [
    ['Tammy Spencer', '42022 Daniel Forest Apt. 201', 'Lake Amyhaven', 'Louisiana', '54479', 'Runner, broadcasting/film/video'],
    ['Amy Meyer', '5558 Brown Street Apt. 718', 'Calebport', 'Wyoming', '96398', 'Administrator, charities/voluntary organisations'],
    ['Michael Gutierrez', '560 Rhonda Isle Apt. 851', 'West Dakotaside', 'South Carolina', '92315', 'Location manager'],
    ['Victoria Zhang', '9007 Rivera Highway Apt. 726', 'Andreafurt', 'Connecticut', '08533', 'Lecturer, further education'],
    ['Dorothy Acevedo', '43878 Deleon Ranch Apt. 191', 'Emilystad', 'Vermont', '05721', 'Social worker'],
    ['Richard Haley', '482 Robertson Plaza', 'West Kelly', 'Alabama', '65044', 'Fashion designer'],
    ['Christopher Jimenez MD', '5679 Pamela Wall Apt. 023', 'West Nathan', 'Delaware', '63181', 'Naval architect'],
    ['Paul Peterson', '415 Hernandez Islands Suite 379', 'Port Matthew', 'Utah', '99271', 'Publishing rights manager'],
    ['Christine Lambert DDS', '043 Wright Key Suite 737', 'Port Lisa', 'Vermont', '84484', 'Technical author'],
    ['Robert Jones', '0816 Tyler Inlet', 'Courtneyberg', 'Nevada', '05095', 'Clinical psychologist']
]

group2 = [
    ['Lawrence Krause', '7116 Jose Garden Apt. 442', 'Amandaside', 'North Carolina', '87377', 'Pharmacist, community'],
    ['David Kennedy', '306 Mitchell Shores', 'Port Rachel', 'South Dakota', '94249', 'Patent attorney'],
    ['Ethan Johnson', '0611 Smith Burg Apt. 670', 'East Danielle', 'Delaware', '03419', 'Surveyor, insurance'],
    ['Kevin Clark', '659 Lawrence Village Suite 220', 'Priceport', 'Mississippi', '90864', 'Planning and development surveyor'],
    ['Adam Marshall', '160 Angela Track', 'Laurenmouth', 'Arkansas', '72136', 'Market researcher'],
    ['Daniel Torres', '645 Kaitlyn Hills', 'Lake Paulside', 'Kansas', '50552', 'Plant breeder/geneticist'],
    ['Becky Payne', '391 Burns Street', 'Jordanmouth', 'Utah', '33100', 'Environmental consultant'],
    ['Charles Bishop', '44108 Thomas Drive', 'Christopherland', 'New Jersey', '26513', 'Pathologist'],
    ['Alex Scott', '7569 Rodriguez Pine', 'Bernardville', 'South Carolina', '91675', 'Ecologist'],
    ['Heidi King DVM', '03002 Jones Locks Apt. 559', 'East Matthew', 'Montana', '16824', 'Ergonomist'],
    ['Madison Hamilton', '1384 Hunter Well Apt. 810', 'East Mark', 'Indiana', '51355', 'Sports development officer'],
    ['Teresa Jones', '541 Sparks Islands', 'West Ronaldbury', 'Alabama', '74946', 'Chief Operating Officer'],
    ['Francisco Moore', '335 Katherine Tunnel Suite 850', 'Candaceville', 'Alabama', '89782', 'Clinical molecular geneticist'],
    ['Joseph Mitchell', '232 Alexander Causeway Suite 515', 'North Laurenborough', 'Pennsylvania', '71416', 'Marine scientist'],
    ['Shannon Mccullough', '63303 Paul Falls Suite 920', 'East Melissa', 'New Hampshire', '58524', 'Learning mentor'],
    ['Michael Rodriguez', '1500 Davis Summit Suite 206', 'Lisaburgh', 'Idaho', '18406', 'Hydrographic surveyor'],
    ['Joshua Daniels', '81268 Michelle Dam Apt. 540', 'South Mary', 'Florida', '19795', 'Insurance risk surveyor'],
    ['Pamela Ramsey', '85890 Perez Glen', 'Smithhaven', 'Indiana', '77327', 'Operational researcher'],
    ['Kirsten Roberts', '5707 Nguyen Locks', 'Lake Paul', 'California', '37556', 'Designer, ceramics/pottery'],
    ['Kevin Warner', '8631 Garcia Isle', 'Port Matthew', 'New Hampshire', '52976', 'Field seismologist'],
    ['Sophia Jones', '7110 Kimberly Mountain', 'New Stacey', 'Pennsylvania', '88276', 'Surveyor, building control'],
    ['Alan Miller', '982 Anthony Plaza Apt. 595', 'East Janeshire', 'Georgia', '39710', 'Ranger/warden'],
    ['Sara Sullivan', '244 Jamie Common', 'South James', 'Kentucky', '47171', 'Herpetologist'],
    ['Elizabeth Smith', '112 Gary Parks', 'East Jerry', 'Texas', '71251', 'Conservator, museum/gallery'],
    ['Mark Myers', '35500 Tracy Mount Suite 145', 'West Garrettbury', 'Mississippi', '81807', 'Regulatory affairs officer']
]
group3 = [
    ['Ariel Randall', '2445 Amanda River Suite 354', 'New Shawnhaven', 'South Carolina', '06735', 'Health and safety inspector'],
    ['Thomas Miller', '1454 Scott Camp', 'South Andrew', 'Washington', '28790', 'Personal assistant'],
    ['Antonio Klein', '49232 Benjamin Glen', 'West Matthew', 'Texas', '31926', 'Naval architect'],
    ['Barbara Gonzales', '26531 Cabrera Roads', 'Tiffanyville', 'Vermont', '49919', 'Chief Technology Officer'],
    ['Holly Howard', '0854 Osborne Rue', 'Brendastad', 'New Mexico', '95412', 'Mechanical engineer'],
    ['Seth Walters', '641 Russell Estate', 'Edwardsmouth', 'Missouri', '58748', 'Tour manager'],
    ['James Delgado', '08384 Clark Road Suite 309', 'Sanchezburgh', 'Delaware', '16590', 'Academic librarian'],
    ['Gina Lewis', '748 Hayden Knoll', 'Hughesland', 'New York', '88637', 'Engineer, drilling'],
    ['Barry Payne', '78282 James Stravenue', 'Sanchezshire', 'California', '68417', 'Database administrator'],
    ['Dr. Melissa Mccoy', '113 John Corners Suite 995', 'South Keithland', 'New Mexico', '09288', 'Solicitor'],
    ['Erica Lambert', '14032 Billy Park Suite 423', 'Johnsonside', 'Ohio', '41058', 'Tax adviser'],
    ['Mary Johnson', '024 Antonio Terrace', 'Reevesland', 'South Dakota', '62582', 'Futures trader'],
    ['Kimberly Brown', '28409 Clark Isle', 'Crossfort', 'Maryland', '29159', 'Retail manager'],
    ['Nicholas Gibson', '6607 Brian Extensions Suite 370', 'Gonzalezchester', 'Florida', '47104', 'Designer, graphic'],
    ['Kimberly Harris', '728 Kristi Flats Suite 864', 'Port Carla', 'Tennessee', '27760', 'Dealer'],
    ['Elizabeth Hanson', '6172 Harvey Orchard', 'Lake Misty', 'Mississippi', '51275', 'Conservator, furniture'],
    ['Pamela Mendez', '278 Nancy Pines Suite 981', 'Ericview', 'Oklahoma', '26001', 'Glass blower/designer'],
    ['Nicole Shelton', '79681 Eric Flat', 'Vasquezburgh', 'Missouri', '59134', 'TEFL teacher'],
    ['Roger Perez', '805 Simon Walks Apt. 113', 'East Joseph', 'Nevada', '73988', 'Environmental education officer'],
    ['Seth Black', '42090 Latoya Cliffs', 'South Amytown', 'Kansas', '93679', 'Ceramics designer'],
    ['Tyler Gentry', '976 Landry Wall Apt. 198', 'Territown', 'Oregon', '07649', 'Museum/gallery conservator'],
    ['James Larson', '89696 Monica Hills', 'Theresaport', 'Massachusetts', '22308', 'Contractor'],
    ['Mathew Rogers', '2188 Lori Summit', 'Port Annette', 'Ohio', '05956', 'Geoscientist'],
    ['Roy Lopez', '558 Miller Stream Suite 182', 'Martinezland', 'Ohio', '97553', 'Scientist, clinical (histocompatibility and immunogenetics)'],
    ['Matthew Waller', '44777 Jonathan Burgs', 'Lake Garyport', 'Kansas', '38824', 'Medical laboratory scientific officer'],
    ['William Lane', '5873 Tammy Burgs', 'South John', 'Michigan', '03480', 'Water quality scientist'],
    ['Jose Arellano', '89831 Smith Avenue Apt. 608', 'Sethport', 'Kentucky', '28720', 'Acupuncturist'],
    ['Loretta Chavez', '50289 April Pine', 'Port Heather', 'West Virginia', '67952', 'Archivist'],
    ['Taylor Fields', '172 Green Stravenue Suite 665', 'East Christinefort', 'New Jersey', '52805', 'Naval architect'],
    ['Kenneth White', '8124 Terry Lodge', 'Johnville', 'Illinois', '72947', 'Biomedical scientist'],
    ['Jonathan Lopez', '219 Alexandra Oval Suite 531', 'Williamston', 'Mississippi', '76417', 'Clinical embryologist'],
    ['Tracy Saunders', '44861 White Lock Suite 713', 'East Cheryl', 'Washington', '75061', 'Community development worker'],
    ['Stephanie Solomon', '90921 Davis Islands Apt. 528', 'Lake Tiffany', 'Idaho', '69231', 'IT trainer'],
    ['Susan Colon', '8284 Amy Plains', 'North Laurenbury', 'New Hampshire', '25228', 'Cytogeneticist'],
    ['Bradley Miller', '54789 Duran Curve Apt. 397', 'Ashleyfort', 'Indiana', '04068', 'Psychologist, prison and probation services'],
    ['Katherine Stanton', '48870 Solis Ridges Apt. 093', 'Ginabury', 'Maine', '14504', 'Facilities manager'],
    ['Mr. Dustin Phillips', '28886 Brown Light', 'Deannafurt', 'Arizona', '75475', 'Pharmacist, community'],
    ['Deborah Smith', '74322 Jones Common Suite 868', 'Georgeborough', 'Maine', '95149', 'Designer, blown glass/stained glass'],
    ['Jamie Martinez', '17720 Tonya Viaduct Suite 547', 'South Lauriemouth', 'Montana', '39118', 'Scientist, audiological'],
    ['Victor Ortiz', '402 Ellis Gardens', 'South Jamiemouth', 'Arkansas', '91033', 'Commercial horticulturist'],
    ['Elizabeth Lara', '3402 Billy Course', 'South Kellychester', 'New Hampshire', '93042', 'Arts administrator'],
    ['Jackson Perry', '895 Johnson River Suite 896', 'East Mistyberg', 'Kentucky', '70147', 'Designer, furniture'],
    ['Natalie Reese', '96806 Ashley Forest', 'Petersonhaven', 'Idaho', '12698', 'Surveyor, minerals'],
    ['Ronald Wright', '057 Allen Ramp Suite 661', 'Stephaniebury', 'Illinois', '04807', 'Veterinary surgeon'],
    ['James Sanchez', '511 Watson Bridge', 'Gonzalezfort', 'Minnesota', '68734', 'Engineer, agricultural'],
    ['Bryan Gibson', '94496 Rodriguez Course', 'Bullockfort', 'Hawaii', '01631', 'Tree surgeon'],
    ['Jason Gregory', '41729 Brandon Falls', 'West Kevintown', 'South Dakota', '91445', 'Prison officer'],
    ['Courtney Thompson', '181 Heather Heights', 'Jillianside', 'Virginia', '12863', 'Writer'],
    ['Cassandra Parker', '751 Campbell Lodge', 'Hahntown', 'Mississippi', '55055', 'Academic librarian'],
    ['Brandon Cox', '1028 Jeffrey Mountain', 'Perrychester', 'Arkansas', '12580', 'Equities trader'],
    ['Justin Johnson', '0239 Torres Loop Apt. 999', 'Davidhaven', 'Nevada', '12767', "Politician's assistant"],
    ['Steven Golden', '64214 Alice Valley', 'New Roger', 'Pennsylvania', '62276', 'Magazine journalist'],
    ['Nicholas Mccarthy', '219 Melissa River', 'Lake Alexanderside', 'Wyoming', '83669', 'Event organiser'],
    ['Jamie Paul', '0726 Smith Fields Suite 595', 'North Matthew', 'Rhode Island', '33877', 'Editor, film/video'],
    ['Christopher Peters', '71666 Nelson Ports', 'Fordstad', 'Indiana', '44675', 'Fisheries officer'],
    ['Michael Freeman', '6227 Samantha Stream', 'Port Alicia', 'Florida', '99771', 'Designer, textile'],
    ['Elizabeth Dominguez', '5132 Jason Fall', 'Charleneland', 'South Dakota', '47605', 'Teacher, special educational needs'],
    ['Kevin Adams', '932 Thompson Prairie Suite 222', 'North Danielle', 'Missouri', '39915', 'Neurosurgeon'],
    ['Ashley Mitchell', '4118 Nelson Hollow Apt. 457', 'Port Adam', 'Vermont', '19514', 'Education officer, environmental'],
    ['Melody Silva', '4970 Lewis Lock', 'New Morganhaven', 'Louisiana', '75773', 'Retail banker'],
    ['Maria Singh', '530 Harper Streets', 'North Connie', 'Alabama', '63568', 'Set designer'],
    ['Allen Fischer', '48387 Conner Fields', 'East Alexandershire', 'California', '06913', 'Commercial horticulturist'],
    ['Rodney Horn', '2643 Carol Isle', 'Woodview', 'Oregon', '50523', 'Recycling officer'],
    ['Brandy Robertson', '254 Smith Ranch Suite 758', 'Michelleport', 'Tennessee', '50099', 'Higher education lecturer'],
    ['Jason Graves', '91399 Booker Road Apt. 091', 'South Jessica', 'Montana', '58042', 'Producer, radio']
]


print(db.filter_by_firefighter(group1))
print(db.filter_by_firefighter(group2))
print(db.filter_by_firefighter(group3))

##group1_zipcodes = db.get_zip_codes(group1)
##group2_zipcodes = db.get_zip_codes(group2)
##group3_zipcodes = db.get_zip_codes(group3)
##
##group1_names = db.get_names(group1)
##group2_names = db.get_names(group2)
##group3_names = db.get_names(group3)
##
##group1_occ = db.get_occupations(group1)
##group2_occ = db.get_occupations(group2)
##group3_occ = db.get_occupations(group3)

##print(group1_occ)
##print(group2_occ)
##print(group3_occ)

##print(group1_zipcodes)
##print(group2_zipcodes)
##print(group3_zipcodes)
##
##
##print(group1_names)
##print(group2_names)
##print(group3_names)











