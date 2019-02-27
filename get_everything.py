
# looking at http://discovery.nationalarchives.gov.uk/API/help
# under Records - 6th item down is the one we can use to access the children of records
#
#GET records/children/{parentId}?direction={direction}&includeCursor={includeCursor}&batchStartRecordId={batchStartRecordId}&batchStartMark={batchStartMark}&limit={limit}
###Request Information
##URI Parameters
#Name	Description	Type	   Additional information
#parentId           string     Required
#direction          Direction  Default value is NEXT
#includeCursor      boolean    Default value is True
#batchStartRecordId string     Default value is
#batchStartMark     string     Default value is
#limit              #integer   Default value is 30

###Body Parameters    None.
##Response Information
#Resource Description
