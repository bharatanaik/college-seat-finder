from django.db import models


pair = lambda x: ((i, i) for i in x)

class Cutoff(models.Model):
    _year = models.CharField(max_length = 1000, null = True, blank = True, verbose_name = 'Year')
    _round = models.CharField(max_length = 1000, null = True, blank = True, verbose_name = 'Round')
    _type = models.CharField(max_length = 1000, null = True, blank = True, verbose_name = 'Type')
    _college_code = models.CharField(max_length = 1000, null = True, blank = True, verbose_name = 'College Code')
    _college_name = models.CharField(max_length = 1000, null = True, blank = True, verbose_name = 'College Name')
    _course_code = models.CharField(max_length = 1000, null = True, blank = True, verbose_name = 'Course Code')
    _course_name = models.CharField(max_length = 1000, null = True, blank = True, verbose_name = 'Course Name')
    _1g = models.IntegerField(null = True, blank = True, verbose_name = '1G')
    _1k = models.IntegerField(null = True, blank = True, verbose_name = '1K')
    _1r = models.IntegerField(null = True, blank = True, verbose_name = '1R')
    _2ag = models.IntegerField(null = True, blank = True, verbose_name = '2AG')
    _2ak = models.IntegerField(null = True, blank = True, verbose_name = '2AK')
    _2ar = models.IntegerField(null = True, blank = True, verbose_name = '2AR')
    _2bg = models.IntegerField(null = True, blank = True, verbose_name = '2BG')
    _2bk = models.IntegerField(null = True, blank = True, verbose_name = '2BK')
    _2br = models.IntegerField(null = True, blank = True, verbose_name = '2BR')
    _3ag = models.IntegerField(null = True, blank = True, verbose_name = '3AG')
    _3ak = models.IntegerField(null = True, blank = True, verbose_name = '3AK')
    _3ar = models.IntegerField(null = True, blank = True, verbose_name = '3AR')
    _3bg = models.IntegerField(null = True, blank = True, verbose_name = '3BG')
    _3bk = models.IntegerField(null = True, blank = True, verbose_name = '3BK')
    _3br = models.IntegerField(null = True, blank = True, verbose_name = '3BR')
    _gm = models.IntegerField(null = True, blank = True, verbose_name = 'GM')
    _gmk = models.IntegerField(null = True, blank = True, verbose_name = 'GMK')
    _gmr = models.IntegerField(null = True, blank = True, verbose_name = 'GMR')
    _scg = models.IntegerField(null = True, blank = True, verbose_name = 'SCG')
    _sck = models.IntegerField(null = True, blank = True, verbose_name = 'SCK')
    _scr = models.IntegerField(null = True, blank = True, verbose_name = 'SCR')
    _stg = models.IntegerField(null = True, blank = True, verbose_name = 'STG')
    _stk = models.IntegerField(null = True, blank = True, verbose_name = 'STK')
    _str = models.IntegerField(null = True, blank = True, verbose_name = 'STR')
    _1h = models.IntegerField(null = True, blank = True, verbose_name = '1H')
    _1kh = models.IntegerField(null = True, blank = True, verbose_name = '1KH')
    _1rh = models.IntegerField(null = True, blank = True, verbose_name = '1RH')
    _2ah = models.IntegerField(null = True, blank = True, verbose_name = '2AH')
    _2akh = models.IntegerField(null = True, blank = True, verbose_name = '2AKH')
    _2arh = models.IntegerField(null = True, blank = True, verbose_name = '2ARH')
    _2bh = models.IntegerField(null = True, blank = True, verbose_name = '2BH')
    _2bkh = models.IntegerField(null = True, blank = True, verbose_name = '2BKH')
    _2brh = models.IntegerField(null = True, blank = True, verbose_name = '2BRH')
    _3ah = models.IntegerField(null = True, blank = True, verbose_name = '3AH')
    _3akh = models.IntegerField(null = True, blank = True, verbose_name = '3AKH')
    _3arh = models.IntegerField(null = True, blank = True, verbose_name = '3ARH')
    _3bh = models.IntegerField(null = True, blank = True, verbose_name = '3BH')
    _3bkh = models.IntegerField(null = True, blank = True, verbose_name = '3BKH')
    _3brh = models.IntegerField(null = True, blank = True, verbose_name = '3BRH')
    _gmh = models.IntegerField(null = True, blank = True, verbose_name = 'GMH')
    _gmkh = models.IntegerField(null = True, blank = True, verbose_name = 'GMKH')
    _gmrh = models.IntegerField(null = True, blank = True, verbose_name = 'GMRH')
    _sch = models.IntegerField(null = True, blank = True, verbose_name = 'SCH')
    _sckh = models.IntegerField(null = True, blank = True, verbose_name = 'SCKH')
    _scrh = models.IntegerField(null = True, blank = True, verbose_name = 'SCRH')
    _sth = models.IntegerField(null = True, blank = True, verbose_name = 'STH')
    _stkh = models.IntegerField(null = True, blank = True, verbose_name = 'STKH')
    _strh = models.IntegerField(null = True, blank = True, verbose_name = 'STRH')
    _gmp = models.IntegerField(null = True, blank = True, verbose_name = 'GMP')
    _gmph = models.IntegerField(null = True, blank = True, verbose_name = 'GMPH')
    _ma = models.IntegerField(null = True, blank = True, verbose_name = 'MA')
    _mc = models.IntegerField(null = True, blank = True, verbose_name = 'MC')
    _me = models.IntegerField(null = True, blank = True, verbose_name = 'ME')
    _meh = models.IntegerField(null = True, blank = True, verbose_name = 'MEH')
    _mk = models.IntegerField(null = True, blank = True, verbose_name = 'MK')
    _mm = models.IntegerField(null = True, blank = True, verbose_name = 'MM')
    _mmh = models.IntegerField(null = True, blank = True, verbose_name = 'MMH')
    _mu = models.IntegerField(null = True, blank = True, verbose_name = 'MU')
    _nri = models.IntegerField(null = True, blank = True, verbose_name = 'NRI')
    _opn = models.IntegerField(null = True, blank = True, verbose_name = 'OPN')
    _oth = models.IntegerField(null = True, blank = True, verbose_name = 'OTH')
    _rc2 = models.IntegerField(null = True, blank = True, verbose_name = 'RC2')
    _rc3 = models.IntegerField(null = True, blank = True, verbose_name = 'RC3')
    _rc4 = models.IntegerField(null = True, blank = True, verbose_name = 'RC4')
    _rc5 = models.IntegerField(null = True, blank = True, verbose_name = 'RC5')
    _rc6 = models.IntegerField(null = True, blank = True, verbose_name = 'RC6')
    _rc7 = models.IntegerField(null = True, blank = True, verbose_name = 'RC7')
    _rc8 = models.IntegerField(null = True, blank = True, verbose_name = 'RC8')
    

class SeatMatrix(models.Model):
    _year = models.CharField(max_length = 1000, null = True, blank = True, verbose_name = 'Year')
    _annexure = models.CharField(max_length = 1000, null = True, blank = True, verbose_name = 'Annexure')
    _seat_type = models.CharField(max_length = 1000, null = True, blank = True, verbose_name = 'Seat Type')
    _course_type = models.CharField(max_length = 1000, null = True, blank = True, verbose_name = 'Courese Type')
    _district = models.CharField(max_length = 1000, null = True, blank = True, verbose_name = 'District')
    _college_ownership_type = models.CharField(max_length = 1000, null = True, blank = True, verbose_name = 'College Ownership Type')
    _college_operation = models.CharField(max_length = 1000, null = True, blank = True, verbose_name = 'College Operation')
    _college_code = models.CharField(max_length = 1000, null = True, blank = True, verbose_name = 'College Code')
    _college_short_name = models.CharField(max_length = 1000, null = True, blank = True, verbose_name = 'College Short Name')
    _college_name = models.CharField(max_length = 1000, null = True, blank = True, verbose_name = 'College Name')
    _course_name = models.CharField(max_length = 1000, null = True, blank = True, verbose_name = 'Course Name')
    _affiliation = models.CharField(max_length = 1000, null = True, blank = True, verbose_name = 'Affiliation')
    _accreditation = models.CharField(max_length = 1000, null = True, blank = True, verbose_name = 'Accreditation')
    _govt_fees = models.CharField(max_length = 1000, null = True, blank = True, verbose_name = 'Govt Fees')
    _management_fees = models.CharField(max_length = 1000, null = True, blank = True, verbose_name = 'Management Fees')
    _email_i_d = models.CharField(max_length = 1000, null = True, blank = True, verbose_name = 'Email I D')
    _contact_number = models.CharField(max_length = 1000, null = True, blank = True, verbose_name = 'Contact Number')
    _1g = models.IntegerField(null = True, blank = True, verbose_name = '1G')
    _1k = models.IntegerField(null = True, blank = True, verbose_name = '1K')
    _1r = models.IntegerField(null = True, blank = True, verbose_name = '1R')
    _2ag = models.IntegerField(null = True, blank = True, verbose_name = '2AG')
    _2ak = models.IntegerField(null = True, blank = True, verbose_name = '2AK')
    _2ar = models.IntegerField(null = True, blank = True, verbose_name = '2AR')
    _2bg = models.IntegerField(null = True, blank = True, verbose_name = '2BG')
    _2bk = models.IntegerField(null = True, blank = True, verbose_name = '2BK')
    _2br = models.IntegerField(null = True, blank = True, verbose_name = '2BR')
    _3ag = models.IntegerField(null = True, blank = True, verbose_name = '3AG')
    _3ak = models.IntegerField(null = True, blank = True, verbose_name = '3AK')
    _3ar = models.IntegerField(null = True, blank = True, verbose_name = '3AR')
    _3bg = models.IntegerField(null = True, blank = True, verbose_name = '3BG')
    _3bk = models.IntegerField(null = True, blank = True, verbose_name = '3BK')
    _3br = models.IntegerField(null = True, blank = True, verbose_name = '3BR')
    _gm = models.IntegerField(null = True, blank = True, verbose_name = 'GM')
    _gmk = models.IntegerField(null = True, blank = True, verbose_name = 'GMK')
    _gmr = models.IntegerField(null = True, blank = True, verbose_name = 'GMR')
    _scg = models.IntegerField(null = True, blank = True, verbose_name = 'SCG')
    _sck = models.IntegerField(null = True, blank = True, verbose_name = 'SCK')
    _scr = models.IntegerField(null = True, blank = True, verbose_name = 'SCR')
    _stg = models.IntegerField(null = True, blank = True, verbose_name = 'STG')
    _stk = models.IntegerField(null = True, blank = True, verbose_name = 'STK')
    _str = models.IntegerField(null = True, blank = True, verbose_name = 'STR')
    _1gh = models.IntegerField(null = True, blank = True, verbose_name = '1GH')
    _1kh = models.IntegerField(null = True, blank = True, verbose_name = '1KH')
    _1rh = models.IntegerField(null = True, blank = True, verbose_name = '1RH')
    _2agh = models.IntegerField(null = True, blank = True, verbose_name = '2AGH')
    _2akh = models.IntegerField(null = True, blank = True, verbose_name = '2AKH')
    _2arh = models.IntegerField(null = True, blank = True, verbose_name = '2ARH')
    _2bgh = models.IntegerField(null = True, blank = True, verbose_name = '2BGH')
    _2bkh = models.IntegerField(null = True, blank = True, verbose_name = '2BKH')
    _2brh = models.IntegerField(null = True, blank = True, verbose_name = '2BRH')
    _3agh = models.IntegerField(null = True, blank = True, verbose_name = '3AGH')
    _3akh = models.IntegerField(null = True, blank = True, verbose_name = '3AKH')
    _3arh = models.IntegerField(null = True, blank = True, verbose_name = '3ARH')
    _3bgh = models.IntegerField(null = True, blank = True, verbose_name = '3BGH')
    _3bkh = models.IntegerField(null = True, blank = True, verbose_name = '3BKH')
    _3brh = models.IntegerField(null = True, blank = True, verbose_name = '3BRH')
    _gmh = models.IntegerField(null = True, blank = True, verbose_name = 'GMH')
    _gmkh = models.IntegerField(null = True, blank = True, verbose_name = 'GMKH')
    _gmrh = models.IntegerField(null = True, blank = True, verbose_name = 'GMRH')
    _scgh = models.IntegerField(null = True, blank = True, verbose_name = 'SCGH')
    _sckh = models.IntegerField(null = True, blank = True, verbose_name = 'SCKH')
    _scrh = models.IntegerField(null = True, blank = True, verbose_name = 'SCRH')
    _stgh = models.IntegerField(null = True, blank = True, verbose_name = 'STGH')
    _stkh = models.IntegerField(null = True, blank = True, verbose_name = 'STKH')
    _strh = models.IntegerField(null = True, blank = True, verbose_name = 'STRH')
    _agl = models.IntegerField(null = True, blank = True, verbose_name = 'AGL')
    _cap = models.IntegerField(null = True, blank = True, verbose_name = 'CAP')
    _d = models.IntegerField(null = True, blank = True, verbose_name = 'D')
    _dk = models.IntegerField(null = True, blank = True, verbose_name = 'DK')
    _jk = models.IntegerField(null = True, blank = True, verbose_name = 'JK')
    _ncc = models.IntegerField(null = True, blank = True, verbose_name = 'NCC')
    _sg = models.IntegerField(null = True, blank = True, verbose_name = 'SG')
    _spo = models.IntegerField(null = True, blank = True, verbose_name = 'SPO')
    _xcp = models.IntegerField(null = True, blank = True, verbose_name = 'XCP')
    _xd = models.IntegerField(null = True, blank = True, verbose_name = 'XD')
    _ph = models.IntegerField(null = True, blank = True, verbose_name = 'PH')
    _snq = models.IntegerField(null = True, blank = True, verbose_name = 'SNQ')
    _nri = models.IntegerField(null = True, blank = True, verbose_name = 'NRI')
    _anglo_indian = models.IntegerField(null = True, blank = True, verbose_name = 'Anglo Indian')
    _gmp = models.IntegerField(null = True, blank = True, verbose_name = 'GMP')
    _gmph = models.IntegerField(null = True, blank = True, verbose_name = 'GMPH')
    _ma = models.IntegerField(null = True, blank = True, verbose_name = 'MA')
    _mc = models.IntegerField(null = True, blank = True, verbose_name = 'MC')
    _me = models.IntegerField(null = True, blank = True, verbose_name = 'ME')
    _meh = models.IntegerField(null = True, blank = True, verbose_name = 'MEH')
    _mk = models.IntegerField(null = True, blank = True, verbose_name = 'MK')
    _mm = models.IntegerField(null = True, blank = True, verbose_name = 'MM')
    _mmh = models.IntegerField(null = True, blank = True, verbose_name = 'MMH')
    _mu = models.IntegerField(null = True, blank = True, verbose_name = 'MU')
    _opn = models.IntegerField(null = True, blank = True, verbose_name = 'OPN')
    _rc2 = models.IntegerField(null = True, blank = True, verbose_name = 'RC2')
    _rc3 = models.IntegerField(null = True, blank = True, verbose_name = 'RC3')
    _rc4 = models.IntegerField(null = True, blank = True, verbose_name = 'RC4')
    _rc5 = models.IntegerField(null = True, blank = True, verbose_name = 'RC5')
    _rc6 = models.IntegerField(null = True, blank = True, verbose_name = 'RC6')
    _rc7 = models.IntegerField(null = True, blank = True, verbose_name = 'RC7')
    _rc8 = models.IntegerField(null = True, blank = True, verbose_name = 'RC8')
    _oth = models.IntegerField(null = True, blank = True, verbose_name = 'OTH')
    _total_approved_intake = models.IntegerField(null = True, blank = True, verbose_name = 'Total Approved Intake')
    _total_reserved_seats = models.IntegerField(null = True, blank = True, verbose_name = 'Total Reserved Seats')
    _management = models.IntegerField(null = True, blank = True, verbose_name = 'Management')  

    def __str__(self):
        return f"[{self._course_type}] {self._college_name} - {self._course_name}"

class JEEORCR(models.Model):

    YEAR = (
        ("2022", "2022"),
        ("2021", "2021"),
        ("2020", "2020"),
        ("2019", "2019"),
        ("2018", "2018"),
        ("2017", "2017"),
        ("2016", "2016"),
    )
    
    INSTITUTE_TYPE = (
        ("IIT's - Indian Institute of Technology", "IIT's - Indian Institute of Technology"),
        ("NIT's - National Institute of Technology", "NIT's - National Institute of Technology"),
        ("GFTI's - Government Funded Technical Institution", "GFTI's - Government Funded Technical Institution"),
        ("II-IT's - Indian Institute of Information Technology", "II-IT's - Indian Institute of Information Technology")
    )

    GENDER = (
        ('Gender-Neutral', 'Gender-Neutral'),
        ('Female-only (including Supernumerary)', 'Female-only (including Supernumerary)')
    )

    SEAT_TYPE = (
        ("OPEN", "OPEN"),
        ("OPEN (PwD)", "OPEN (PwD)"),
        ("EWS", "EWS"),
        ("EWS (PwD)", "EWS (PwD)"),
        ("OBC-NCL", "OBC-NCL"),
        ("OBC-NCL (PwD)", "OBC-NCL (PwD)"),
        ("SC", "SC"),
        ("SC (PwD)", "SC (PwD)"),
        ("ST", "ST"),
        ("ST (PwD)", "ST (PwD)")
    )

    QUOTA = (
        ("AI", "AI"),
        ("HS", "HS"),
        ("OS", "OS"),
        ("GO", "GO"),
        ("AP", "AP"),
        ("JK", "JK"),
        ("LA", "LA"),
    )

    ROUND = (
        ("Round 1", "Round 1"),
        ("Round 2", "Round 2"),
        ("Round 3", "Round 3"),
        ("Round 4", "Round 4"),
        ("Round 5", "Round 5"),
        ("Round 6", "Round 6"),
        ("Round 7", "Round 7")
    )
    year = models.CharField(max_length=1000, choices=YEAR)
    institute_type = models.CharField(max_length=1000, verbose_name="Institute Type", choices = INSTITUTE_TYPE)
    round = models.CharField(max_length=1000, verbose_name= "Round", choices=ROUND)
    institute = models.CharField(max_length=1000, verbose_name="Institute name")
    course  = models.CharField(max_length= 1000, verbose_name="Academic program name")
    quota = models.CharField(max_length=1000, verbose_name="Quota", choices=QUOTA)
    seat_type = models.CharField(max_length=1000, verbose_name="Seat Type", choices=SEAT_TYPE)
    gender = models.CharField(max_length=1000, verbose_name="Gender Type", choices=GENDER)
    opening_rank = models.CharField(max_length=1000, verbose_name="Opening rank")
    closing_rank = models.CharField(max_length=1000, verbose_name="Closing rank")

    def __str__(self) -> str:
        return "{} - {}".format(self.institute, self.course)
    

class NEETSeatMatrix(models.Model):
    INSTITUTE_TYPE = ('AIIMS', 'Except Central University', 'Central University', 'Deemed University', 'ESI Scheme', 'Jamia', 'JIPMER')
    STATES = ('Punjab', 'Himachal Pradesh', 'Assam', 'Jammu & Kashmir', 'Gujarat', 'Odissa', 'Telangana', 'Uttar Pradesh', 'Rajasthan', 'Tamil Nadu', 'Maharastra', 'Delhi', 'Bihar', 'Chattisgarh', 'Madhya Pradesh', 'Jharkhand', 'West Bengal', 'Goa', 'Andhra Pradesh', 'Kerala', 'Karnataka', 'Manipur', 'Meghalaya', 'Andaman & Nicobar')
    PROGRAM = ('MBBS', 'BDS')
    QUOTA = ('Open Seat Quota', 'Foreign Country Quota', 'All India', 'Aligarh Muslim University (AMU) Quota', 'Non-Resident\nIndian(AMU)Quota', 'IP University Quota', 'Delhi University Quota', 'Delhi NCR Children/Widows of Personnel of the Armed Forces (CW) Quota', 'Non-Resident Indian', 'Deemed/Paid Seats Quota', 'Jain Minority Quota', 'Muslim Minority Quota', 'Employees State Insurance Scheme(ESI)', 'Employees State Insurance\nScheme(ESI)', 'Jamia Internal Quota', 'Muslim OBC Quota', 'Muslim ST Quota', 'Muslim Quota', 'Muslim Women Quota', 'Internal -Puducherry UT\nDomicile')
    institute_type = models.CharField(max_length = 30, null=True, blank = True, choices=pair(INSTITUTE_TYPE))
    owned_by = models.CharField(max_length=100, null=True, blank=True)
    city = models.CharField(max_length=30, null=True, blank=True)
    state = models.CharField(max_length = 20, null=True, blank = True, choices=pair(STATES))
    institute = models.CharField(max_length = 150, null=True, blank = True)
    college_code = models.IntegerField(null=True, blank = True)
    program = models.CharField(max_length = 5, null=True, blank = True, choices=pair(PROGRAM))
    affiliation = models.CharField(max_length = 150, null=True, blank = True)
    gender = models.CharField(max_length=100, null=True, blank=True)
    quota = models.CharField(max_length = 80, null=True, blank = True, choices=pair(QUOTA))
    open = models.IntegerField(null=True, blank = True)
    open_pwd = models.IntegerField(null=True, blank = True)
    general_ews = models.IntegerField(null=True, blank = True)
    general_ews_pwd = models.IntegerField(null=True, blank = True)
    obc = models.IntegerField(null=True, blank = True)
    obc_pwd = models.IntegerField(null=True, blank = True)
    sc = models.IntegerField(null=True, blank = True)
    sc_pwd = models.IntegerField(null=True, blank = True)
    st = models.IntegerField(null=True, blank = True)
    st_pwd = models.IntegerField(null=True, blank = True)
    total_seats = models.IntegerField(null=True, blank = True)


#05S@=ym^AO~e
# class Admission(models.Model):
