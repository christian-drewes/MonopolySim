import matplotlib.pyplot as plt
import numpy as np

class Graph():
        def __init__(self, labels, sizes):
                self.labels = labels
                self.sizes = sizes
        
        def barChart(self):
                yPos = np.arange(len(self.labels))

                fig1, ax = plt.subplots(num=None, figsize=(18, 12), dpi=80, facecolor='w', edgecolor='k')

                plt.bar(yPos, self.sizes, align='center', alpha=0.5)
                plt.xticks(yPos, self.labels)
                plt.ylabel('Landed (%)')
                plt.title('Number of times landed on')

                plt.setp(ax.get_xticklabels(), rotation=30, horizontalalignment='right', fontsize='x-small')

                plt.show()