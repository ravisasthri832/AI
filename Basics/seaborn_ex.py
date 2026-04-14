import seaborn as abc
# import matplotlib.pyplot as plt
from matplotlib import pyplot as plt
df = abc.load_dataset("taxis")
abc.lineplot(x="pickup",y="passengers",data=df)
plt.show()

# lineplot()
# barplot()
# histplot()
# boxplot()
# violinplot()
# scatterplot()
# heatmap()

# import matplotlib.pyplot as plt
# import seaborn as sns
# import numpy as np
# import pandas as pd
# df = pd.read_excel("students.xlsx")
# sns.barplot(x="Name",y="Maths",data=df)
# plt.show()



# import numpy as np
# import matplotlib.pyplot as plt
# import seaborn as sns
# data = np.random.rand(5,5)
# sns.heatmap(data,annot=True)
# sns.set_style("whitegrid")
# plt.show()




# import matplotlib.pyplot as plt
# import seaborn as sns
# df = sns.load_dataset("tips")
# sns.boxplot(x="day",y="total_bill",data=df)
# sns.violinplot(x="day",y="total_bill",data=df)
# sns.scatterplot(x="total_bill",y="tip",data=df)
# plt.show()


# import matplotlib.pyplot as plt
# import seaborn as sns
# df = sns.load_dataset("tips")
# sns.histplot(df["total_bill"],bins=10)
# plt.title("Histo Plot")
# plt.show()





# import matplotlib.pyplot as plt
# import seaborn as sns
# df = sns.load_dataset("tips")
# sns.barplot(x="day",y="total_bill",data=df)
# plt.title("Restaurant Bar Chart")
# plt.show()



# import seaborn as sns
# import matplotlib.pyplot as plt
# df = sns.load_dataset("fmri")
# sns.lineplot(x="timepoint",y="signal",data=df)
# plt.title("LinePlot with Seaborn")
# plt.show()





# df = sns.load_dataset("tips")
# df = sns.load_dataset("fmri")
# print(df)