import json
import
_count=0
Class InformationAssetIdentityViewModel:
"""  class represents and manipulates a Discovery API subtype """
    def __init__(self):
        _count += 1
        self.AccessConditions: str = ""
        self.CatalogueId: int  = 0
        self.CitableReference: str = ""
        self.ClosureCode: str = ""
        self.ClosureStatus: str = ""
        self.ClosureType: str = ""
        self.CoveringDates: str = ""
        self.CoveringFromDate: int = 0
        self.CoveringToDate: int = 0
        self.ScopeContent: ScopeContentViewModel = nil
        self.Digitised: boolean = False
        self.HeldBy=[] # Collection of XReferenceViewModel
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

    def fromJSON(jsonstr):
        #jsonstr.

