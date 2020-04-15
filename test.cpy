      ****************************************************************
           COPY COPYRITE.
      ****************************************************************
      * Copybook layout for the aux journ 2 file 
      ****************************************************************
Rel.Vr* Rel.Date  Request  Programmer   Notes 
      * -------- -------- ------------- -------------------------------
19.00r* 04/15/20  OSDC-3258 McCloskey   Add NCOA Rtn Cd               *
19.003* 04/15/20  OSDC-3260 McCloskey   Add Certified Tracking Number *
19.002* 01/08/20  OUTFTR-483 Mark Ludlow New fields Insurance companies
19.001* 01/08/20  SR-175156 Mark Ludlow New fields Paperless Export   *
18.004* 01/09/19  OSDC-2250 Bartlett    Add Bus-Resi-Ind              *
15.004* 11/14/15  OUTFTR-17 McCloskey   Spanish Braille and Large     *
15.004*                                 Print Statements.             *
15.003* 08/08/15  D15B130R Ed Pluta     new fields for Google         *
15.002* 05/16/15  D14J595E  McCloskey      Integration with GOOGLE    *
15.002*                                    Digital Mailbox            *
15.002*                                    chge date format YYYYMMDD  *
15.002*                                    chge time format HHMMSSSS  *
14.001* 10/25/14 D14C258W B Jensen      eCare 2.0 stmt notification
13.002* 04/06/13 D12H321U Ed Pluta      zumbox phase 2
13.001* 04/06/13 D11A264A Ed Pluta      Doxo support
01.001* 11/10/12 D12D863P Ed Pluta      Zumbox support
01.000* 11/10/12 D11K476N Ed Pluta      New copybook
      ****************************************************************

        05 'XXX'-ACCT-NUM                PIC X(25)     VALUE SPACES.
        05 FILLER                        PIC X(1)      VALUE '|'.
        05 'XXX'-STMT-DATE.
            10 'XXX'-STMT-DT-YYYY        PIC X(4)      VALUE '0000'.
            10 'XXX'-STMT-DT-MM          PIC X(2)      VALUE '00'.
	        10 'XXX'-STMT-DT-DD          PIC X(2)      VALUE '00'.
 	    05 FILLER                        PIC X(1)      VALUE '|'.
 	    05 'XXX'-PMT-DUE-DT.
            10 'XXX'-PMT-DUE-DT-YYYY     PIC X(4)      VALUE '0000'.
            10 'XXX'-PMT-DUE-DT-MM       PIC X(2)      VALUE '00'.
            10 'XXX'-PMT-DUE-DT-DD       PIC X(2)      VALUE '00'.
	    05 FILLER                        PIC X(1)      VALUE '|'.
        05 'XXX'-BILL-OPEN-DATE.
            10 'XXX'-BILL-OPEN-YYYY      PIC X(4)      VALUE '0000'.
            10 'XXX'-BILL-OPEN-MM        PIC X(2)      VALUE '00'.
            10 'XXX'-BILL-OPEN-DD        PIC X(2)      VALUE '00'.
        05 FILLER                        PIC X(1)      VALUE '|'.
        05 'XXX'-BILL-CLOSE-DATE.
            10 'XXX'-BILL-CLOSE-YYYY     PIC X(4)      VALUE '0000'.
            10 'XXX'-BILL-CLOSE-MM       PIC X(2)      VALUE '00'.
            10 'XXX'-BILL-CLOSE-DD       PIC X(2)      VALUE '00'.
        05 FILLER                        PIC X(1)      VALUE '|'.
        05 'XXX'-AMT-DUE                 PIC -9(11)v99 VALUE ZEROS.
        05 FILLER                        PIC X(1)      VALUE '|'.
15.003  05 'XXX'-GOOGLE-FLAG             PIC X(1)      VALUE SPACE.
	    05 FILLER                        PIC X(1)      VALUE '|'.
13.001  05 'XXX'-DOXO-FLAG               PIC X(1)      VALUE SPACE.
13.001  05 FILLER                        PIC X(1)      VALUE '|'.
15.003* Date format YYYYMMDD
15.002  05 'XXX'-HCPY-CHNG-DATE          PIC 9(08).
15.003* Time format HHMMSSms
15.002  05 'XXX'-HCPY-CHNG-TIME          PIC 9(08).
        05 FILLER                        PIC X(1)      VALUE '|'.
15.003  05 'XXX'-HCPY-TIME-OFFSET        PIC X(6)      VALUE SPACES.
15.003  05 FILLER                        PIC X(1)      VALUE '|'.
13.002  05 'XXX'-CUS-PRODUCT-CD          PIC X(1)      VALUE SPACE.
13.002  05 FILLER                        PIC X(1)      VALUE '|'.
14.001  05 'XXX'-CUS-CONSOLIDATOR-IND    PIC X(1)      VALUE SPACE.
14.001  05 FILLER                        PIC X(1)      VALUE '|'.
15.003  05 'XXX'-PAY-FLAG                PIC X(1)      VALUE '0'.
15.003      88 'XXX'-MAN-PAY                           VALUE '0'.
15.003      88 'XXX'-AUTO-PAY                          VALUE '1'.
15.003  05 FILLER                        PIC X(1)      VALUE '|'.
15.003  05 'XXX'-END-BALANCE             PIC -9(11)V99.
15.003  05 FILLER                        PIC X(1)      VALUE '|'.
15.003  05 'XXX'-EXPIRATION-DATE         PIC X(8)      VALUE SPACES.
15.003  05  FILLER                       PIC X(1)      VALUE '|'.
15.003  05 'XXX'-GOOGLE-SENDER-ID        PIC X(15)     VALUE SPACES.
15.003  05 FILLER                        PIC X(1)      VALUE '|'.
19.001  05 'XXX'-CUSTOMER-ID             PIC X(13)     VALUE SPACES.
19.001  05 FILLER                        PIC X(1)      VALUE '|'.
19.001  05 'XXX'-EMAIL-ADDRESS           PIC X(65)     VALUE SPACES.
19.001  05 FILLER                        PIC X(1)      VALUE '|'.
19.001  05 'XXX'-LANG-IND                PIC X(1)      VALUE SPACES.
19.001  05 FILLER                        PIC X(1)      VALUE '|'.
19.001  05 'XXX'-EBILL-INDICATOR         PIC X(1)      VALUE SPACES.
19.001  05 FILLER                        PIC X(1)      VALUE '|'.
19.001  05 'XXX'-ORIG-PYMT-METHOD        PIC X(1)      VALUE SPACES.
19.001  05 FILLER                        PIC X(1)      VALUE '|'.
19.001  05 'XXX'-ORIG-PYMT-STATUS        PIC X(1)      VALUE SPACES.
19.001  05 FILLER                        PIC X(1)      VALUE '|'.
19.001  05 'XXX'-DEBIT-DATE.
19.001      10 'XXX'-DEBIT-DATE-YYYY     PIC X(4)      VALUE '0000'.
19.001      10 'XXX'-DEBIT-DATE-MM       PIC X(2)      VALUE '00'.
19.001      10 'XXX'-DEBIT-DATE-DD       PIC X(2)      VALUE '00'.
19.001  05 FILLER                        PIC X(1)      VALUE '|'.
19.001  05 'XXX'-EXTERNAL-STATUS         PIC X(1)      VALUE SPACES.
19.001  05 FILLER                        PIC X(1)      VALUE '|'.
19.001  05 'XXX'-AH-HIERARCHY-ID         PIC X(8)      VALUE SPACES.
19.001  05 FILLER                        PIC X(1)      VALUE '|'.

19.001  05 'XXX'-AH-GROUP-ID             PIC X(8)      VALUE SPACES.
19.001  05 FILLER                        PIC X(1)      VALUE '|'.
19.001  05 'XXX'-STMT-ID                 PIC X(8)      VALUE SPACES.
19.001  05 FILLER                        PIC X(1)      VALUE '|'.
19.002  05 'XXX'-COMPOSITION-CITY-CD     PIC X(2)      VALUE SPACES.
19.002  05 FILLER                        PIC X(1)      VALUE '|'.
19.002  05 'XXX'-INS-LOB                 PIC X(4)      VALUE SPACES.
19.002  05 FILLER                        PIC X(1)      VALUE '|'.
19.001  05 'XXX'-USEABLE-FILLER1         PIC X(99)     VALUE SPACES.
19.002  05 FILLER                        PIC X(1)      VALUE '|'.
19.001  05 'XXX'-USEABLE-FILLER2         PIC X(99)     VALUE SPACES.
19.002  05 FILLER                        PIC X(1)      VALUE '|'.
19.001  05 'XXX'-USEABLE-FILLER3         PIC X(99)     VALUE SPACES.
19.002  05 FILLER                        PIC X(1)      VALUE '|'.
19.001  05 'XXX'-USEABLE-FILLER4         PIC X(99)     VALUE SPACES.
19.002  05 FILLER                        PIC X(1)      VALUE '|'.
19.001  05 'XXX'-USEABLE-FILLER5         PIC X(99)     VALUE SPACES.
19.002  05 FILLER                        PIC X(1)      VALUE '|'.
19.001  05 'XXX'-USEABLE-FILLER6         PIC X(99)     VALUE SPACES.
19.002  05 FILLER                        PIC X(1)      VALUE '|'.
19.001  05 'XXX'-USEABLE-FILLER7         PIC X(99)     VALUE SPACES.
19.002  05 FILLER                        PIC X(1)      VALUE '|'.
19.001  05 'XXX'-USEABLE-FILLER8         PIC X(75)     VALUE SPACES.
19.002  05 FILLER                        PIC X(1)      VALUE '|'.
15.004  05 'XXX'-STMT-HOLD               PIC X(1)      VALUE SPACES.
15.004  05 FILLER                        PIC X(1)      VALUE '|'.
18.004  05 'XXX'-BUS-RESI-IND            PIC X(1)      VALUE SPACES.
18.004  05 FILLER                        PIC X(1)      VALUE '|'.
19.003  05 'XXX'-CERT-TRACK-NUM          PIC X(26)     VALUE SPACES.
19.003  05 FILLER                        PIC X(1)      VALUE '|'.
