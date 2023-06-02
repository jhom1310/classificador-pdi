from pdi import *

pdi_train = False
pdi_test = False
pdi_validation = False

if pdi_train:
    pp_save(path_train, path_train_p)
if pdi_test:
    pp_save(path_test, path_test_p)
if pdi_validation:
    pp_save(path_validation, path_validation_p)