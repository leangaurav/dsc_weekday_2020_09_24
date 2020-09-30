from datetime import datetime   # here module and class under module names are same i.e- datetime
print(datetime.now())   # calling function now() through datetime class
 
# from datetime.datetime import now   # this won't work since datetime under module is not module,it is a class, so it will through error that datetime is not module, it is a package
# print(now()) 

# import datetime.datetime as dt  # this won't work since datetime under module is not module,it is a class, so it will through error that datetime is not module, it is a package
# print(dt.now()) 

import datetime        # import "datetime" module
print(dir(datetime))   # show all classes, functions, variables under module "datetime"
print(datetime.datetime.now())  # calling function under class which is under module  --"module.class name under module.function name under class"
 
    