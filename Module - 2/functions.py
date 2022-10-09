def all_types_parameterFn(firstArg,secondArg,*simpleArgs,**keyArgs):
    print(firstArg,secondArg)
    print(simpleArgs)
    print(keyArgs)


all_types_parameterFn('Monir','Baiti','kolkata','west bengal',country='india',region='south asia')

