from utils import load_data
import kmodel

# load data
X_train, y_train = load_data()

# create model structure
my_model = kmodel.create_model()

# edit structure
kmodel.compile_model(my_model)

# save model
kmodel.save_model(my_model, 'my_model')