from urllib.parse import urlparse

s = urlparse("/charge?network=visa&amount=100&merchant_id=m001&charge_id=c001")
currentQuery = s.query
findNetwork = currentQuery.find('amount', currentQuery.find('&'))
# newQuery = currentQuery.replace('&', ' ')
newQuery = currentQuery.split('&')
print(newQuery)