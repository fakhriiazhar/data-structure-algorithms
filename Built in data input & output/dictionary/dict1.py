#dictionary
capitals = {'kaltim':'samarinda', 'bali':'denpasar'}
print(capitals['kaltim'])
capitals['jatim']='surabaya'
print(capitals)
capitals['kalsel']='banjarmasin'
print(len(capitals))
for k in capitals:
    print(capitals[k], "adalah ibukota dari", k)
