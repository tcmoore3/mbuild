angles = [
'ring1-chead-ring2',
'chead-ring1-ring2', 
'chead-ring1-ring3', 
'chead-ring1-ring4', 
'ring2-ring1-ring3', 
'ring2-ring1-ring4', 
'ring3-ring2-ring4',   # this is the odd one, needs to be renamed in params file
'chead-ring2-ring1', 
'chead-ring2-ring3', 
'chead-ring2-chme',
'ring1-ring2-ring3', 
'ring1-ring2-chme',
'ring3-ring2-chme',
'ring1-ring3-ring2', 
'ring1-ring3-ring4', 
'ring1-ring3-chme',
'ring2-ring3-ring4', 
'ring2-ring3-chme',
'ring4-ring3-chme',
'ring1-ring4-ring3', 
'ring1-ring4-ctail', 
'ring3-ring4-ctail', 
'ring4-ctail-cterm']

# <Angle class1="tail" class2="tail" class3="head" angle="11" k="11"/>

for i, angle in enumerate(angles):
    print('<Angle class1="{0}" class2="{1}" class3="{2}" angle="{3}" k="{4}"/>'.format(
        *angle.split('-'), i+12, i+12))

