# mendal's first law

demo, hetero, reco = 28, 23, 29

total = demo + hetero + reco

ReRe = (reco/total)*((reco-1)/(total-1))
ReHet = (reco/total)*(hetero/(total-1))*2*1/2
HetHet = (hetero/total)*(hetero-1)/(total-1)*1/4

print(1-(ReRe+ReHet+HetHet))