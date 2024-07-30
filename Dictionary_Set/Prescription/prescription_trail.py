from prescription_data import *

trail_patients =["Denise","Eddie","Frank","Georgia"]

# remove Warfarin and add Edocaban 
for pateint in trail_patients:
    prescription = patients[pateint]
    if warfarin in prescription:    
        prescription.remove(warfarin)
        prescription.add(edoxaban)
    else:
        print(f"Patient {pateint} is not taking Warfarin.")
        print(f"Please remove {pateint} from Examination")
    
    '''
    or 
        try:   
            prescription.remove(warfarin)
            prescription.add(edoxaban)
        except KeyError:
            print(f"Patient {pateint} is not taking Warfarin.")
            print(f"Please remove {pateint} from Examination")
    '''
    print(pateint,prescription)