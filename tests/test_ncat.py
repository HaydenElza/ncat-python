from ncat import ncat

def test_llc():
    response = ncat.llh(39.2240867222, -98.5421515000, 'nad83(1986)', 'nad83(2011)') 
    assert response['destLat'] == '39.2240846022'
    assert response['destLon'] == '-98.5421511291'

def test_spc():
    response = ncat.spc(173099.419, 503626.812, 'nad83(2011)', 'nad83(NSRS2007)', 2402) 
    assert response['destLat'] == '37.3933000245'
    assert response['destLon'] == '-92.4590401909'

def test_utm():
    response = ncat.utm(4138641.144, 547883.655, 'nad83(2011)', 'nad83(NSRS2007)', 15) 
    assert response['destLat'] == '37.3933000021'
    assert response['destLon'] == '-92.4590399996'

def test_xyz():
    response = ncat.xyz(-217687.279, -5069012.406, 3852223.048, 'nad83(2011)', 'nad83(NSRS2007)') 
    assert response['destLat'] == '37.3933000008'
    assert response['destLon'] == '-92.4590400039'

def test_usng():
    response = ncat.usng('15SWB4788338641', 'nad83(2011)', 'nad83(NSRS2007)') 
    assert response['destLat'] == '37.3932987380'
    assert response['destLon'] == '-92.4590474084'