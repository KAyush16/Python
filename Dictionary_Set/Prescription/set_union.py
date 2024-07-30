from prescription_data import adverse_interactions

meds_to_watch =set()

'''
# without using for loop 
meds_to_watch.update(*adverse_interactions)
'''
for interaction in adverse_interactions:
    #meds_to_watch=meds_to_watch.union(interaction)
    #meds_to_watch = meds_to_watch | interaction
    meds_to_watch.update(interaction)
print(sorted(meds_to_watch))