class AssetCollectionViewModelOfInformationAssetIdentityViewModel:
    _count = 0
    def __init__(self):
        _count +=1
        self.Assets = []  # Collection of InformationAssetIdentityViewModel  INfoAssetIVM
        self.HasMoreAfterLast = False
        self.HasMoreBeforeFirst = False


