import furl

API_BASE_URL = furl.furl(r"http://discovery.nationalarchives.gov.uk/API/")
API_VERSION = "v1"


class AssetCollectionViewModelOfInformationAssetIdentityViewModel:
    _count = 0
    def __init__(self):
        _count +=1
        self.Assets = []  # Collection of InformationAssetIdentityViewModel  INfoAssetIVM
        self.HasMoreAfterLast = False
        self.HasMoreBeforeFirst = False


class CollectionOfAssetIVM:
    _count = 0
    def __init__(self):
        _count += 1


class ScopeContentViewModel:
    _count = 0
    def __init__(self, json):
    _count +=1
    self.PlaceNames = [] # Collection of strings
    self.Description: str = ""
    self.Ephemera: str = ""
    self.Schema: str = ""


class InformationAssetIdentityViewModel:
"""  class represents and manipulates a Discovery API subtype """
    _count=0 
    def __init__(self, name):
        _count += 1
        self.name: str = name
        self.AccessConditions: str = ""
        self.CatalogueId: int  = 0
        self.CitableReference: str = ""
        self.ClosureCode: str = ""
        self.ClosureStatus: str = ""
        self.ClosureType: str = ""
        self.CoveringDates: str = ""
        self.CoveringFromDate: int = 0
        self.CoveringToDate: int = 0
        self.ScopeContent: ScopeContentViewModel = None
        self.Digitised: boolean = False
        self.HeldBy=[] # List (Collection)of XReferenceViewModel
        self.Id: str = ""
        self.IsParent: boolean = False
        self.CatalogueLevel: int = 0
        self.ParentId: str = ""
        self.RecordOpeningDate: str = ""
        self.ReferencePart: str = ""
        self.ReferenceParentId: str = ""
        self.SortKey: str = ""
        self.Source: str = ""
        self.Title: str = ""

    def initfromJSON(jsonstr):

        for i in jsonstr["assets"]
            

        jsonstr.

        self.

