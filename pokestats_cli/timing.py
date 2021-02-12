# importing the required module
import timeit

# code snippet to be executed only once
mysetup = """
import pkgutil
import pandas as pd
from io import BytesIO
"""

# code snippet whose execution time is to be measured
mycode = """
data = pkgutil.get_data(__name__, "data/pokemon.csv")
df = pd.read_csv(BytesIO(data))
"""

# timeit statement
print(timeit.timeit(setup=mysetup,
                    stmt=mycode,
                    number=10000))
